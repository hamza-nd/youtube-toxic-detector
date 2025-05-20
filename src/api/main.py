from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from typing import Optional, List
import hashlib
import os
from src.utils.db_handler import create_connection, insert_user, get_user_by_username, insert_scraped_data
from src.scrapers.video_scraper import fetch_channel_videos  # Import the actual video scraper

# Create FastAPI app
app = FastAPI(title="YouTube Toxic Detector API")

# Enable CORS with specific origins
origins = [
    "http://localhost:3000",
    "https://your-frontend-domain.vercel.app",  # Add your frontend Vercel domain here
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models for request validation
class UserCreate(BaseModel):
    name: str
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    username: str
    email: str
    isadmin: bool

class ScrapeRequest(BaseModel):
    channelUrl: str
    videoCount: int
    userId: int

class VideoData(BaseModel):
    videoid: str
    title: str
    thumbnail: str
    length: str
    views: int
    published: str
    url: str

class ScrapeResponse(BaseModel):
    videos: List[VideoData]
    totalViews: int
    averageDuration: str

def hash_password(password: str) -> str:
    """Hash password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

@app.post("/api/signup", response_model=UserResponse)
async def signup(user: UserCreate):
    try:
        # Hash the password
        hashed_password = hash_password(user.password)
        
        # Insert user into database
        user_id = insert_user(
            name=user.name,
            username=user.username,
            email=user.email,
            password=hashed_password,
            isadmin=False
        )
        
        if not user_id:
            raise HTTPException(status_code=400, detail="Username or email already exists")
        
        # Return user data (excluding password)
        return {
            "id": user_id,
            "name": user.name,
            "username": user.username,
            "email": user.email,
            "isadmin": False
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/login")
async def login(user: UserLogin):
    try:
        # Get user from database
        db_user = get_user_by_username(user.username)
        
        if not db_user:
            raise HTTPException(status_code=401, detail="Invalid username or password")
        
        # Verify password
        hashed_password = hash_password(user.password)
        if hashed_password != db_user["password"]:
            raise HTTPException(status_code=401, detail="Invalid username or password")
        
        # Return user data (excluding password)
        return {
            "id": db_user["id"],
            "name": db_user["name"],
            "username": db_user["username"],
            "email": db_user["email"],
            "isadmin": db_user["isadmin"]
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/scrape", response_model=ScrapeResponse)
async def scrape_videos(request: ScrapeRequest):
    try:
        # Use the actual video scraper to get real data
        scraped_data = fetch_channel_videos(request.channelUrl, request.videoCount)
        
        if not scraped_data:
            raise HTTPException(status_code=400, detail="Failed to scrape videos from the channel")
        
        # Calculate statistics
        total_views = sum(video['views'] for video in scraped_data)
        average_duration = calculate_average_duration(scraped_data)
        
        # Save to database
        for video in scraped_data:
            insert_scraped_data(
                videoid=video['videoid'],
                title=video['title'],
                thumbnail=video['thumbnail'],
                length=video['length'],
                views=video['views'],
                published=video['published'],
                url=video['url'],
                scraped_by=request.userId
            )
        
        return {
            "videos": scraped_data,
            "totalViews": total_views,
            "averageDuration": average_duration
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def calculate_average_duration(videos):
    total_seconds = 0
    for video in videos:
        try:
            # Split duration into parts
            parts = video['length'].split(':')
            
            if len(parts) == 3:
                # Format: HH:MM:SS
                hours, minutes, seconds = map(int, parts)
                total_seconds += hours * 3600 + minutes * 60 + seconds
            elif len(parts) == 2:
                # Format: MM:SS
                minutes, seconds = map(int, parts)
                total_seconds += minutes * 60 + seconds
            elif len(parts) == 1:
                # Format: SS
                seconds = int(parts[0])
                total_seconds += seconds
            else:
                print(f"Invalid duration format: {video['length']}")
                continue
        except (ValueError, TypeError) as e:
            print(f"Error parsing duration {video['length']}: {str(e)}")
            continue
    
    if not videos:
        return "00:00"
    
    avg_seconds = total_seconds // len(videos)
    minutes = avg_seconds // 60
    seconds = avg_seconds % 60
    return f"{minutes:02d}:{seconds:02d}"

# Add a root endpoint for testing
@app.get("/")
async def root():
    return {"message": "YouTube Toxic Detector API is running"}

# Add a test endpoint for the scrape functionality
@app.get("/api/test")
async def test():
    return {"message": "API endpoints are working"} 