 
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.auth_service import AuthService
from app.services.db_service import DatabaseService
from fastapi import Header

router = APIRouter(prefix="/api/v1/analytics", tags=["analytics"])

def get_current_user(authorization: str = Header(None), db: Session = Depends(get_db)):
    """
    Dependency to get current user from token
    """
    if not authorization:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated"
        )
    
    # Extract token from "Bearer <token>"
    try:
        scheme, token = authorization.split()
        if scheme.lower() != "bearer":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication scheme"
            )
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token format"
        )
    
    # Decode token to get username
    username = AuthService.decode_token(token)
    if not username:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )
    
    # Get user from database
    user = DatabaseService.get_user_by_username(db, username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    return user

@router.get("/user")
def get_user_analytics(
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Get user's personal analytics
    """
    try:
        analytics = DatabaseService.get_user_analytics(db, current_user.id)
        
        # Add search history
        search_history = DatabaseService.get_user_search_history(db, current_user.id)
        
        analytics["search_history"] = [
            {
                "keywords": sh.keywords,
                "industry": sh.industry,
                "num_ideas": sh.num_ideas,
                "created_at": sh.created_at
            }
            for sh in search_history[:10]  # Last 10 searches
        ]
        
        return analytics
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error fetching analytics: {str(e)}"
        )

@router.get("/platform")
def get_platform_analytics(
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Get platform-wide analytics (available to all authenticated users)
    """
    try:
        analytics = DatabaseService.get_platform_analytics(db)
        return analytics
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error fetching platform analytics: {str(e)}"
        )

@router.get("/user/industries")
def get_user_industry_stats(
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Get user's ideas breakdown by industry
    """
    try:
        from sqlalchemy import func
        from app.models.models import Idea
        
        industry_stats = db.query(
            Idea.industry,
            func.count(Idea.id).label('count')
        ).filter(
            Idea.user_id == current_user.id
        ).group_by(Idea.industry).all()
        
        return {
            "industries": [
                {
                    "industry": industry,
                    "count": count
                }
                for industry, count in industry_stats
            ]
        }
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error fetching industry statistics: {str(e)}"
        )

@router.get("/user/favorites")
def get_user_favorite_ideas(
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Get count and list of user's favorite ideas
    """
    try:
        from app.models.models import Idea
        
        favorite_ideas = db.query(Idea).filter(
            Idea.user_id == current_user.id,
            Idea.is_favorite == True
        ).all()
        
        return {
            "favorite_count": len(favorite_ideas),
            "favorites": [
                {
                    "id": idea.id,
                    "title": idea.title,
                    "industry": idea.industry,
                    "created_at": idea.created_at
                }
                for idea in favorite_ideas
            ]
        }
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error fetching favorite ideas: {str(e)}"
        )

@router.get("/user/trends")
def get_user_search_trends(
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Get user's search trends (most used keywords and industries)
    """
    try:
        from sqlalchemy import func
        from app.models.models import SearchHistory
        
        # Most used keywords
        keyword_trends = db.query(
            SearchHistory.keywords,
            func.count(SearchHistory.id).label('count')
        ).filter(
            SearchHistory.user_id == current_user.id
        ).group_by(SearchHistory.keywords).order_by(
            func.count(SearchHistory.id).desc()
        ).limit(5).all()
        
        # Most used industries
        industry_trends = db.query(
            SearchHistory.industry,
            func.count(SearchHistory.id).label('count')
        ).filter(
            SearchHistory.user_id == current_user.id
        ).group_by(SearchHistory.industry).order_by(
            func.count(SearchHistory.id).desc()
        ).limit(5).all()
        
        return {
            "popular_keywords": [
                {"keyword": kw, "count": count}
                for kw, count in keyword_trends
            ],
            "popular_industries": [
                {"industry": ind, "count": count}
                for ind, count in industry_trends
            ]
        }
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error fetching search trends: {str(e)}"
        )