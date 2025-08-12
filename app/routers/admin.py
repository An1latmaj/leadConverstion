from fastapi import APIRouter
from app.services.data_service import data_service

router = APIRouter(prefix="/admin")

@router.get("/leads")
async def get_leads():
    """Admin endpoint to view all leads and analytics"""
    return data_service.get_analytics()

@router.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "career-consultation-api"}
