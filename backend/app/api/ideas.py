from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.schemas import Idea, IdeaCreate, GenerationRequest
from app.services.auth_service import AuthService
from app.services.ai_service import AIService
from app.services.db_service import DatabaseService
from fastapi import Header

router = APIRouter(prefix="/api/v1/ideas", tags=["ideas"])

def get_current_user(authorization: str = Header(None), db: Session = Depends(get_db)):
    if not authorization:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated"
        )
    
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
    
    username = AuthService.decode_token(token)
    if not username:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )
    
    user = DatabaseService.get_user_by_username(db, username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    return user

@router.post("/generate", response_model=List[Idea])
def generate_ideas(
    request: GenerationRequest,
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        print("\n[GENERATE] Starting idea generation")
        print(f"[GENERATE] User: {current_user.username}")
        print(f"[GENERATE] Keywords: {request.keywords}")
        print(f"[GENERATE] Industry: {request.industry}")
        
        ai_service = AIService()
        generated_ideas = ai_service.generate_business_ideas(
            keywords=request.keywords,
            industry=request.industry,
            num_ideas=request.num_ideas
        )
        
        saved_ideas = []
        for idea_data in generated_ideas:
            if "error" not in idea_data:
                idea_create = IdeaCreate(
                    title=idea_data.get("title", "Untitled"),
                    description=idea_data.get("description", ""),
                    business_model=idea_data.get("business_model", ""),
                    target_audience=idea_data.get("target_audience", ""),
                    swot_analysis=idea_data.get("swot_analysis", ""),
                    market_potential=idea_data.get("market_potential", ""),
                    industry=request.industry,
                    keywords=request.keywords
                )
                
                saved_idea = DatabaseService.create_idea(db, current_user.id, idea_create)
                saved_ideas.append(saved_idea)
        
        DatabaseService.create_search_history(
            db,
            current_user.id,
            request.keywords,
            request.industry,
            request.num_ideas
        )
        
        print(f"[GENERATE] SUCCESS! Generated {len(saved_ideas)} ideas\n")
        return saved_ideas
    
    except Exception as e:
        print(f"\n[GENERATE] ERROR: {str(e)}\n")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error generating ideas: {str(e)}"
        )

@router.get("/", response_model=List[Idea])
def get_user_ideas(
    skip: int = 0,
    limit: int = 10,
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    ideas = DatabaseService.get_user_ideas(db, current_user.id, skip, limit)
    return ideas

@router.get("/{idea_id}", response_model=Idea)
def get_idea(
    idea_id: int,
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    idea = DatabaseService.get_idea_by_id(db, idea_id, current_user.id)
    
    if not idea:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Idea not found"
        )
    
    return idea

@router.put("/{idea_id}", response_model=Idea)
def update_idea(
    idea_id: int,
    update_data: dict,
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    idea = DatabaseService.update_idea(db, idea_id, current_user.id, update_data)
    
    if not idea:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Idea not found"
        )
    
    return idea

@router.delete("/{idea_id}")
def delete_idea(
    idea_id: int,
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    success = DatabaseService.delete_idea(db, idea_id, current_user.id)
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Idea not found"
        )
    
    return {"message": "Idea deleted successfully"}

@router.post("/{idea_id}/favorite")
def toggle_favorite(
    idea_id: int,
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    idea = DatabaseService.toggle_favorite(db, idea_id, current_user.id)
    
    if not idea:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Idea not found"
        )
    
    return {"idea": idea, "is_favorite": idea.is_favorite}