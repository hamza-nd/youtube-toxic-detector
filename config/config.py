import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# YouTube API Configuration
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')

# MongoDB Configuration
MONGODB_URI = os.getenv('MONGODB_URI', 'mongodb://localhost:27017')
DB_NAME = 'youtube_toxic_detector'

# Gemini API Configuration
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Scraping Configuration
MAX_VIDEOS_PER_CHANNEL = 50
MAX_COMMENTS_PER_VIDEO = 1000

# Model Configuration
TOXICITY_THRESHOLD = 0.5  # Threshold for considering a comment toxic
BERT_MODEL_NAME = "unitary/toxic-bert"  # Pre-trained model for toxicity detection

# File Paths
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
RESULTS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'results') 