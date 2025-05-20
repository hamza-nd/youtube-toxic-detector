import sys
from pathlib import Path

# Add the project root to Python path
project_root = str(Path(__file__).parent.parent)
if project_root not in sys.path:
    sys.path.append(project_root)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.main import app as fastapi_app

# Create a new FastAPI app for Vercel
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include all routes from the main FastAPI app
app.include_router(fastapi_app.router)

# Add a root endpoint for testing
@app.get("/")
async def root():
    return {"message": "YouTube Video Analyzer API is running"} 