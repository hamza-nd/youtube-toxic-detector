// API URL configuration
const API_URL = process.env.NODE_ENV === 'production' 
    ? 'https://youtube-toxic-detector.vercel.app/api'
    : 'http://localhost:8000/api';

// Check if user is logged in
document.addEventListener('DOMContentLoaded', () => {
    const user = JSON.parse(localStorage.getItem('user'));
    if (!user) {
        window.location.href = './index.html';
        return;
    }

    // Set user name
    document.getElementById('userName').textContent = user.name;

    // Initialize charts
    initializeCharts();

    // Add event listeners
    document.getElementById('scrapeForm').addEventListener('submit', handleScrape);
    document.getElementById('logoutBtn').addEventListener('click', handleLogout);

    // Sidebar toggle functionality
    const menuToggle = document.getElementById('menuToggle');
    const sidebar = document.querySelector('.sidebar');
    const mainContent = document.querySelector('.main-content');
    const closeSidebar = document.querySelector('.close-sidebar');

    menuToggle.addEventListener('click', () => {
        sidebar.classList.add('active');
        mainContent.classList.add('sidebar-active');
    });

    closeSidebar.addEventListener('click', () => {
        sidebar.classList.remove('active');
        mainContent.classList.remove('sidebar-active');
    });

    // Close sidebar when clicking outside
    document.addEventListener('click', (e) => {
        if (!sidebar.contains(e.target) && !menuToggle.contains(e.target) && sidebar.classList.contains('active')) {
            sidebar.classList.remove('active');
            mainContent.classList.remove('sidebar-active');
        }
    });
});

// Handle logout
function handleLogout(e) {
    e.preventDefault();
    localStorage.removeItem('user');
    window.location.href = './index.html';
}

// Handle video scraping
async function handleScrape(e) {
    e.preventDefault();
    
    const form = e.target;
    const formData = new FormData(form);
    const user = JSON.parse(localStorage.getItem('user'));
    
    try {
        const response = await fetch(`${API_URL}/scrape`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify({
                channelUrl: formData.get('channelUrl'),
                videoCount: parseInt(formData.get('videoCount')),
                userId: user.id
            })
        });
        
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.detail || 'Failed to scrape videos');
        }
        
        const data = await response.json();
        updateDashboard(data);
    } catch (error) {
        console.error('Error:', error);
        alert(error.message || 'An error occurred. Please try again.');
    }
}

// Update dashboard with scraped data
function updateDashboard(data) {
    // Update statistics
    document.getElementById('totalVideos').textContent = data.videos.length;
    document.getElementById('totalViews').textContent = formatNumber(data.totalViews);
    document.getElementById('avgDuration').textContent = formatDuration(data.averageDuration);

    // Update charts
    updateViewsChart(data.videos);
    updateDurationChart(data.videos);

    // Update video grid
    updateVideoGrid(data.videos);
}

// Initialize charts
function initializeCharts() {
    // Views chart
    const viewsCtx = document.getElementById('viewsChart').getContext('2d');
    window.viewsChart = new Chart(viewsCtx, {
        type: 'bar',
        data: {
            labels: [],
            datasets: [{
                label: 'Views',
                data: [],
                backgroundColor: '#667eea',
                borderColor: '#764ba2',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    // Duration chart
    const durationCtx = document.getElementById('durationChart').getContext('2d');
    window.durationChart = new Chart(durationCtx, {
        type: 'line',
        data: {
            labels: [],
            datasets: [{
                label: 'Duration (minutes)',
                data: [],
                borderColor: '#667eea',
                tension: 0.4,
                fill: false
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

// Update views chart
function updateViewsChart(videos) {
    const sortedVideos = [...videos].sort((a, b) => b.views - a.views).slice(0, 10);
    
    window.viewsChart.data.labels = sortedVideos.map(v => v.title.substring(0, 20) + '...');
    window.viewsChart.data.datasets[0].data = sortedVideos.map(v => v.views);
    window.viewsChart.update();
}

// Update duration chart
function updateDurationChart(videos) {
    try {
        const sortedVideos = [...videos].sort((a, b) => {
            const durationA = parseDuration(a.length);
            const durationB = parseDuration(b.length);
            return durationA - durationB;
        });
        
        window.durationChart.data.labels = sortedVideos.map(v => v.title.substring(0, 20) + '...');
        window.durationChart.data.datasets[0].data = sortedVideos.map(v => parseDuration(v.length));
        window.durationChart.update();
    } catch (error) {
        console.error('Error updating duration chart:', error);
        console.log('Videos data:', videos);
    }
}

// Update video grid
function updateVideoGrid(videos) {
    const grid = document.getElementById('videosGrid');
    grid.innerHTML = '';

    videos.forEach(video => {
        const card = document.createElement('div');
        card.className = 'video-card';
        card.innerHTML = `
            <img src="${video.thumbnail}" alt="${video.title}" class="video-thumbnail">
            <div class="video-info">
                <h3 class="video-title">${video.title}</h3>
                <div class="video-meta">
                    <span>${formatNumber(video.views)} views</span>
                    <span>${video.length}</span>
                </div>
            </div>
        `;
        grid.appendChild(card);
    });
}

// Utility functions
function formatNumber(num) {
    return new Intl.NumberFormat().format(num);
}

function formatDuration(duration) {
    return duration; // Assuming duration is already in the correct format
}

function parseDuration(duration) {
    // Log the duration for debugging
    console.log('Parsing duration:', duration);
    
    // Handle null or undefined
    if (!duration) {
        console.warn('Duration is null or undefined');
        return 0;
    }

    // Handle string format
    if (typeof duration === 'string') {
        // Remove any non-numeric characters except colons
        duration = duration.replace(/[^0-9:]/g, '');
        
        // Split by colon and convert to numbers
        const parts = duration.split(':').map(part => {
            const num = parseInt(part, 10);
            return isNaN(num) ? 0 : num;
        });

        console.log('Duration parts:', parts);

        if (parts.length === 3) {
            // Format: HH:MM:SS
            return parts[0] * 60 + parts[1] + parts[2] / 60;
        } else if (parts.length === 2) {
            // Format: MM:SS
            return parts[0] + parts[1] / 60;
        } else if (parts.length === 1) {
            // Format: SS
            return parts[0] / 60;
        }
    }

    // If we get here, something went wrong
    console.warn('Invalid duration format:', duration);
    return 0;
} 