from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from config.settings import APP_CONFIG
from app.routers import pages, quiz, chat, admin

# Create FastAPI app with configuration
app = FastAPI(
    title=APP_CONFIG["title"],
    description=APP_CONFIG["description"],
    version=APP_CONFIG["version"]
)

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Include routers
app.include_router(pages.router, tags=["Pages"])
app.include_router(quiz.router, tags=["Quiz"])
app.include_router(chat.router, tags=["Chat"])
app.include_router(admin.router, tags=["Admin"])

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "Career Consultation API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
