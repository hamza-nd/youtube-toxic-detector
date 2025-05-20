# YouTube Video Analyzer

A web application that allows users to analyze YouTube videos from a channel, providing insights into video statistics and trends.

## Features

- User authentication (signup/login)
- YouTube channel video scraping
- Video statistics dashboard
- Interactive charts for views and duration analysis
- Responsive design with dark mode support

## Tech Stack

### Backend
- FastAPI (Python)
- MySQL Database
- YouTube Data API

### Frontend
- HTML5
- CSS3
- JavaScript
- Chart.js for data visualization

## Project Structure

```
youtube-toxic-detector/
├── Frontend/
│   ├── index.html
│   ├── dashboard.html
│   ├── styles.css
│   └── js/
│       ├── auth.js
│       └── dashboard.js
├── src/
│   ├── api/
│   │   └── main.py
│   ├── scrapers/
│   │   └── video_scraper.py
│   └── utils/
│       └── db_handler.py
├── requirements.txt
├── vercel.json
└── README.md
```

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/youtube-toxic-detector.git
cd youtube-toxic-detector
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file in the root directory with the following variables:
```
DB_HOST=your_database_host
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_NAME=your_database_name
YOUTUBE_API_KEY=your_youtube_api_key
```

4. Deploy to Vercel:
```bash
vercel
```

## Usage

1. Open the application in your browser
2. Sign up for a new account or log in
3. Enter a YouTube channel URL and the number of videos to analyze
4. View the dashboard with video statistics and charts

## API Endpoints

- `POST /api/signup` - Create a new user account
- `POST /api/login` - Authenticate user
- `POST /api/scrape` - Scrape videos from a YouTube channel

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
