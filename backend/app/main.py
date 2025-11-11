from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.db.database import engine, Base
from app.models.models import User, Idea, SearchHistory
from app.api import auth, ideas, pdf, analytics

# Create all database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI application
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="AI-powered Business Idea Generator SaaS Application"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(auth.router)
app.include_router(ideas.router)
app.include_router(pdf.router)
app.include_router(analytics.router)

# Health check endpoint
@app.get("/health")
def health_check():
    """
    Health check endpoint
    """
    return {
        "status": "healthy",
        "application": settings.PROJECT_NAME,
        "version": settings.VERSION
    }

# Root endpoint
@app.get("/")
def read_root():
    """
    Root endpoint with API information
    """
    return {
        "message": f"Welcome to {settings.PROJECT_NAME}",
        "version": settings.VERSION,
        "docs": "/docs",
        "api_v1": "/api/v1"
    }

# API v1 info
@app.get("/api/v1")
def api_v1_info():
    """
    API v1 information
    """
    return {
        "version": "1.0.0",
        "endpoints": {
            "auth": "/api/v1/auth",
            "ideas": "/api/v1/ideas",
            "pdf": "/api/v1/pdf",
            "analytics": "/api/v1/analytics"
        },
        "documentation": "/docs"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )