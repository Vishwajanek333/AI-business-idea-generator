 
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.models import User, Idea, SearchHistory
from app.schemas.schemas import IdeaCreate, UserCreate
from app.services.auth_service import AuthService
from typing import List, Optional

class DatabaseService:
    
    # ===== USER OPERATIONS =====
    
    @staticmethod
    def create_user(db: Session, user_data: UserCreate) -> User:
        """Create a new user"""
        hashed_password = AuthService.hash_password(user_data.password)
        db_user = User(
            username=user_data.username,
            email=user_data.email,
            hashed_password=hashed_password
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    
    @staticmethod
    def get_user_by_username(db: Session, username: str) -> Optional[User]:
        """Get user by username"""
        return db.query(User).filter(User.username == username).first()
    
    @staticmethod
    def get_user_by_id(db: Session, user_id: int) -> Optional[User]:
        """Get user by ID"""
        return db.query(User).filter(User.id == user_id).first()
    
    # ===== IDEA OPERATIONS =====
    
    @staticmethod
    def create_idea(db: Session, user_id: int, idea_data: IdeaCreate) -> Idea:
        """Create a new idea"""
        db_idea = Idea(
            user_id=user_id,
            title=idea_data.title,
            description=idea_data.description,
            business_model=idea_data.business_model,
            target_audience=idea_data.target_audience,
            swot_analysis=idea_data.swot_analysis,
            market_potential=idea_data.market_potential,
            industry=idea_data.industry,
            keywords=idea_data.keywords
        )
        db.add(db_idea)
        db.commit()
        db.refresh(db_idea)
        return db_idea
    
    @staticmethod
    def get_user_ideas(db: Session, user_id: int, skip: int = 0, limit: int = 10) -> List[Idea]:
        """Get all ideas for a user"""
        return db.query(Idea).filter(Idea.user_id == user_id).offset(skip).limit(limit).all()
    
    @staticmethod
    def get_idea_by_id(db: Session, idea_id: int, user_id: int) -> Optional[Idea]:
        """Get a specific idea"""
        return db.query(Idea).filter(
            Idea.id == idea_id,
            Idea.user_id == user_id
        ).first()
    
    @staticmethod
    def update_idea(db: Session, idea_id: int, user_id: int, update_data: dict) -> Optional[Idea]:
        """Update an idea"""
        db_idea = db.query(Idea).filter(
            Idea.id == idea_id,
            Idea.user_id == user_id
        ).first()
        
        if db_idea:
            for key, value in update_data.items():
                if hasattr(db_idea, key) and value is not None:
                    setattr(db_idea, key, value)
            db.commit()
            db.refresh(db_idea)
        
        return db_idea
    
    @staticmethod
    def delete_idea(db: Session, idea_id: int, user_id: int) -> bool:
        """Delete an idea"""
        db_idea = db.query(Idea).filter(
            Idea.id == idea_id,
            Idea.user_id == user_id
        ).first()
        
        if db_idea:
            db.delete(db_idea)
            db.commit()
            return True
        return False
    
    @staticmethod
    def toggle_favorite(db: Session, idea_id: int, user_id: int) -> Optional[Idea]:
        """Toggle favorite status of an idea"""
        db_idea = db.query(Idea).filter(
            Idea.id == idea_id,
            Idea.user_id == user_id
        ).first()
        
        if db_idea:
            db_idea.is_favorite = not db_idea.is_favorite
            db.commit()
            db.refresh(db_idea)
        
        return db_idea
    
    # ===== SEARCH HISTORY OPERATIONS =====
    
    @staticmethod
    def create_search_history(db: Session, user_id: int, keywords: str, industry: str, num_ideas: int):
        """Log search history"""
        search = SearchHistory(
            user_id=user_id,
            keywords=keywords,
            industry=industry,
            num_ideas=num_ideas
        )
        db.add(search)
        db.commit()
        return search
    
    @staticmethod
    def get_user_search_history(db: Session, user_id: int) -> List[SearchHistory]:
        """Get user's search history"""
        return db.query(SearchHistory).filter(
            SearchHistory.user_id == user_id
        ).order_by(SearchHistory.created_at.desc()).all()
    
    # ===== ANALYTICS OPERATIONS =====
    
    @staticmethod
    def get_user_analytics(db: Session, user_id: int) -> dict:
        """Get user analytics"""
        total_ideas = db.query(func.count(Idea.id)).filter(Idea.user_id == user_id).scalar()
        favorite_ideas = db.query(func.count(Idea.id)).filter(
            Idea.user_id == user_id,
            Idea.is_favorite == True
        ).scalar()
        
        return {
            "total_ideas": total_ideas,
            "favorite_ideas": favorite_ideas,
            "user_id": user_id
        }
    
    @staticmethod
    def get_platform_analytics(db: Session) -> dict:
        """Get platform-wide analytics"""
        total_users = db.query(func.count(User.id)).scalar()
        total_ideas = db.query(func.count(Idea.id)).scalar()
        
        # Most popular industries
        popular_industries = db.query(
            Idea.industry,
            func.count(Idea.id).label('count')
        ).group_by(Idea.industry).order_by(func.count(Idea.id).desc()).limit(5).all()
        
        return {
            "total_users": total_users,
            "total_ideas": total_ideas,
            "popular_industries": [
                {"industry": ind[0], "count": ind[1]} for ind in popular_industries
            ]
        }