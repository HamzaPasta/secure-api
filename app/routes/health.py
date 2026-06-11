from fastapi import APIRouter

router = APIRouter()

#Health check route for container orchestrators and load balancers
@router.get("/health", tags=["health"])
async def health_check():
    return {
        "status": "healthy",
        "service": "secure-api",
        "version": "1.0.0"
    }