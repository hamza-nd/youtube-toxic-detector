# YouTube Toxic Comment Detector

A tool for analyzing YouTube comments to detect toxicity and generate insights using BERT and Gemini AI.

## Features

- Scrape comments from YouTube videos
- Detect toxic comments using BERT
- Generate insights and recommendations using Gemini AI
- Store and analyze data in MongoDB
- Support for analyzing multiple videos from a channel

## Project Structure

```
youtube-toxic-detector/
├── config/
│   └── config.py           # Configuration and API keys
├── src/
│   ├── scrapers/
│   │   ├── video_scraper.py    # YouTube video scraper
│   │   └── comment_scraper.py  # YouTube comment scraper
│   ├── analysis/
│   │   ├── toxicity_detector.py # BERT-based toxicity detection
│   │   └── gemini_analyzer.py   # Gemini AI analysis
│   └── utils/
│       └── db_handler.py        # Database operations
├── requirements.txt
└── README.md
```

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/youtube-toxic-detector.git
cd youtube-toxic-detector
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory with your API keys:
```
YOUTUBE_API_KEY=your_youtube_api_key_here
MONGODB_URI=mongodb://localhost:27017
GEMINI_API_KEY=your_gemini_api_key_here
```

## Usage

1. Scrape videos from a channel:
```python
from src.scrapers.video_scraper import fetch_channel_videos

videos = fetch_channel_videos(channel_id="YOUR_CHANNEL_ID", max_videos=50)
```

2. Scrape comments from videos:
```python
from src.scrapers.comment_scraper import CommentScraper

scraper = CommentScraper()
comments = scraper.get_comments_for_videos(video_ids)
```

3. Analyze comments for toxicity:
```python
from src.analysis.toxicity_detector import ToxicityDetector

detector = ToxicityDetector()
toxic_comments = detector.get_toxic_comments()
```

4. Generate insights using Gemini:
```python
from src.analysis.gemini_analyzer import GeminiAnalyzer

analyzer = GeminiAnalyzer()
analysis = analyzer.generate_insights(toxic_comments)
```

## Requirements

- Python 3.8+
- MongoDB
- YouTube Data API key
- Gemini API key

## License

MIT License
