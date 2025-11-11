 
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.auth_service import AuthService
from app.services.pdf_service import PDFService
from app.services.db_service import DatabaseService
from fastapi import Header
import io

router = APIRouter(prefix="/api/v1/pdf", tags=["pdf"])

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

@router.get("/export/{idea_id}")
def export_idea_to_pdf(
    idea_id: int,
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Export a business idea to PDF
    """
    # Get idea from database
    idea = DatabaseService.get_idea_by_id(db, idea_id, current_user.id)
    
    if not idea:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Idea not found"
        )
    
    try:
        # Prepare idea data
        idea_data = {
            "title": idea.title,
            "description": idea.description,
            "business_model": idea.business_model,
            "target_audience": idea.target_audience,
            "swot_analysis": idea.swot_analysis,
            "market_potential": idea.market_potential,
            "industry": idea.industry,
            "keywords": idea.keywords
        }
        
        # Generate PDF
        pdf_bytes = PDFService.generate_business_plan_pdf(idea_data)
        
        # Create filename
        filename = f"business_plan_{idea.id}_{idea.title.replace(' ', '_')}.pdf"
        
        # Return PDF file
        return FileResponse(
            io.BytesIO(pdf_bytes),
            media_type="application/pdf",
            filename=filename
        )
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error generating PDF: {str(e)}"
        )

@router.post("/export-multiple")
def export_multiple_ideas_to_pdf(
    idea_ids: list,
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Export multiple ideas to a single PDF document
    """
    try:
        # Get all ideas
        ideas = []
        for idea_id in idea_ids:
            idea = DatabaseService.get_idea_by_id(db, idea_id, current_user.id)
            if idea:
                ideas.append(idea)
        
        if not ideas:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No ideas found"
            )
        
        # Generate combined PDF for first idea (can be extended for multiple)
        idea_data = {
            "title": f"Business Plans - {len(ideas)} Ideas",
            "description": f"Combined business plan document with {len(ideas)} startup ideas",
            "business_model": "See individual ideas below",
            "target_audience": "See individual ideas below",
            "swot_analysis": "See individual ideas below",
            "market_potential": "See individual ideas below",
            "industry": ", ".join([idea.industry for idea in ideas if idea.industry]),
            "keywords": ", ".join([idea.keywords for idea in ideas if idea.keywords])
        }
        
        # Generate PDF
        pdf_bytes = PDFService.generate_business_plan_pdf(idea_data)
        
        # Create filename
        filename = f"business_plans_combined_{len(ideas)}_ideas.pdf"
        
        # Return PDF file
        return FileResponse(
            io.BytesIO(pdf_bytes),
            media_type="application/pdf",
            filename=filename
        )
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error generating PDF: {str(e)}"
        )