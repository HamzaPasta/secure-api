from fastapi import FastAPI
from app.routes.health import router as health_router

#Initialize FastAPI application
app = FastAPI(
    title="Secure API",
    description="A secure Python microservice with automated security scanning",
    version="1.0.0"
)

#Register API endpoints
app.include_router(health_router, prefix="/api/v1")

#Base root endpoint
@app.get("/")
async def root():
    return {"message": "Secure API is running", "status": "healthy"}