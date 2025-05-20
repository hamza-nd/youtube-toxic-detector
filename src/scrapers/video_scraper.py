import requests
import json
import time
import re
from urllib.parse import urlparse, parse_qs
import os

def extract_channel_id_from_url(url):
    """
    Extract channel ID from different types of YouTube channel URLs
    
    Args:
        url (str): YouTube channel URL
        
    Returns:
        str: Channel ID or None if not found
    """
    # Handle channel ID format
    if '/channel/' in url:
        return url.split('/channel/')[1].split('/')[0]
    
    # Handle custom URL format
    if '/c/' in url:
        return url.split('/c/')[1].split('/')[0]
    
    # Handle @username format
    if '/@' in url:
        return url.split('/@')[1].split('/')[0]
    
    # Handle user format
    if '/user/' in url:
        return url.split('/user/')[1].split('/')[0]
    
    return None

def fetch_channel_videos(channel_url, max_videos=50):
    """
    Fetch videos from a YouTube channel using web scraping
    
    Args:
        channel_url (str): YouTube channel URL
        max_videos (int): Maximum number of videos to fetch
        
    Returns:
        list: List of video information dictionaries
    """
    url = "https://www.youtube.com/youtubei/v1/browse?prettyPrint=false"
    
    # Extract channel ID from URL
    channel_id = extract_channel_id_from_url(channel_url)
    if not channel_id:
        raise ValueError("Invalid YouTube channel URL")
    
    # Initial payload for the first page
    payload = json.dumps({
        "context": {
            "client": {
                "hl": "en-GB",
                "gl": "LB",
                "remoteHost": "82.146.184.22",
                "deviceMake": "",
                "deviceModel": "",
                "visitorData": "CgtmNFV2QkVtNHQ1ayj82aPBBjIKCgJMQhIEGgAgZw%3D%3D",
                "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36,gzip(gfe)",
                "clientName": "WEB",
                "clientVersion": "2.20250516.01.00",
                "osName": "Windows",
                "osVersion": "10.0",
                "originalUrl": f"https://www.youtube.com/channel/{channel_id}/videos",
                "screenPixelDensity": 2,
                "platform": "DESKTOP",
                "clientFormFactor": "UNKNOWN_FORM_FACTOR",
                "screenDensityFloat": 2.0000000596046448,
                "userInterfaceTheme": "USER_INTERFACE_THEME_LIGHT",
                "timeZone": "Asia/Beirut",
                "browserName": "Chrome",
                "browserVersion": "136.0.0.0",
                "screenWidthPoints": 868,
                "screenHeightPoints": 787,
                "utcOffsetMinutes": 180,
                "mainAppWebInfo": {
                    "graftUrl": f"/channel/{channel_id}/videos",
                    "webDisplayMode": "WEB_DISPLAY_MODE_BROWSER",
                    "isWebNativeShareAvailable": True
                }
            },
            "user": {
                "lockedSafetyMode": False
            },
            "request": {
                "useSsl": True,
                "internalExperimentFlags": [],
                "consistencyTokenJars": []
            }
        },
        "browseId": channel_id,
        "params": "EgZ2aWRlb3PyBgQKAjoA"
    })
    
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://www.youtube.com',
        'referer': f'https://www.youtube.com/channel/{channel_id}/videos',
        'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'same-origin',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
        'x-youtube-client-name': '1',
        'x-youtube-client-version': '2.20250516.01.00'
    }
    
    results = []
    id_counter = 0
    continuation_token = None
    
    try:
        # First request to get initial videos
        data = requests.request("POST", url, headers=headers, data=payload).json()
        
        # Process the videos and add to results
        tabs = data.get("contents", {}).get("twoColumnBrowseResultsRenderer", {}).get("tabs", [])
        
        # Find the videos tab
        for tab in tabs:
            tab_renderer = tab.get("tabRenderer", {})
            if tab_renderer.get("title", "").lower() == "videos":
                contents = tab_renderer.get("content", {}).get("richGridRenderer", {}).get("contents", [])
                
                # Process videos from the first page
                id_counter, results, continuation_token = process_videos(contents, id_counter, results, max_videos)
                break
        
        # Follow continuation tokens to get more videos
        while continuation_token and len(results) < max_videos:
            print(f"Fetching next page of videos... (Currently have {len(results)} videos)")
            
            # Prepare the continuation request payload
            continuation_payload = json.dumps({
                "context": {
                    "client": {
                        "hl": "en-GB",
                        "gl": "LB",
                        "remoteHost": "82.146.184.22",
                        "deviceMake": "",
                        "deviceModel": "",
                        "visitorData": "CgtmNFV2QkVtNHQ1ayj82aPBBjIKCgJMQhIEGgAgZw%3D%3D",
                        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36,gzip(gfe)",
                        "clientName": "WEB",
                        "clientVersion": "2.20250516.01.00",
                        "osName": "Windows",
                        "osVersion": "10.0",
                        "screenPixelDensity": 2,
                        "platform": "DESKTOP",
                        "clientFormFactor": "UNKNOWN_FORM_FACTOR",
                        "screenDensityFloat": 2.0000000596046448,
                        "userInterfaceTheme": "USER_INTERFACE_THEME_LIGHT",
                        "timeZone": "Asia/Beirut",
                        "browserName": "Chrome",
                        "browserVersion": "136.0.0.0",
                        "screenWidthPoints": 868,
                        "screenHeightPoints": 787,
                        "utcOffsetMinutes": 180
                    },
                    "user": {
                        "lockedSafetyMode": False
                    },
                    "request": {
                        "useSsl": True,
                        "internalExperimentFlags": [],
                        "consistencyTokenJars": []
                    }
                },
                "continuation": continuation_token
            })
            
            # Request the next page
            cont_data = requests.request("POST", url, headers=headers, data=continuation_payload).json()
            
            # Process continuation data
            if "onResponseReceivedActions" in cont_data:
                actions = cont_data.get("onResponseReceivedActions", [])
                for action in actions:
                    if "appendContinuationItemsAction" in action:
                        items = action["appendContinuationItemsAction"].get("continuationItems", [])
                        id_counter, results, continuation_token = process_videos(items, id_counter, results, max_videos)
                        break
            
            # Add a small delay to avoid rate limiting
            time.sleep(0.5)
        
        print(f"Total videos collected: {len(results)}")
        
        # Create data directory if it doesn't exist
        os.makedirs('data', exist_ok=True)
        
        # Save results to JSON file
        output_file = os.path.join('data', 'videos.json')
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=4)
            
        return results
        
    except Exception as e:
        print(f"Error: {e}")
        # If we have partial results, save them anyway
        if results:
            os.makedirs('data', exist_ok=True)
            output_file = os.path.join('data', 'videos.json')
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(results, f, ensure_ascii=False, indent=4)
        raise Exception(f"Error extracting videos: {e}")

def process_videos(contents, id_counter, results, max_videos):
    """
    Process video items and extract relevant information
    
    Args:
        contents (list): List of content items from YouTube response
        id_counter (int): Current ID counter
        results (list): Current results list
        max_videos (int): Maximum number of videos to collect
        
    Returns:
        tuple: Updated id_counter, results list, and continuation token (if any)
    """
    continuation_token = None
    
    for item in contents:
        # Check if this is a continuation item
        if "continuationItemRenderer" in item:
            continuation_data = item.get("continuationItemRenderer", {}).get("continuationEndpoint", {}).get("continuationCommand", {})
            continuation_token = continuation_data.get("token")
            continue
            
        # Process video item
        rich_item = item.get("richItemRenderer", {}).get("content", {})
        video = rich_item.get("videoRenderer")

        if video:
            video_id = video.get("videoId")
            title = video.get("title", {}).get("runs", [{}])[0].get("text", "No title")
            thumbnails = video.get("thumbnail", {}).get("thumbnails", [])
            first_thumbnail = thumbnails[-1]["url"] if thumbnails else None

            length_text = video.get("lengthText", {}).get("simpleText", "Unknown")
            view_count = video.get("viewCountText", {}).get("simpleText", "Unknown")
            publish_time = video.get("publishedTimeText", {}).get("simpleText", "Unknown")

            results.append({
                "videoId": video_id,
                "title": title,
                "thumbnail": first_thumbnail,
                "length": length_text,
                "views": view_count,
                "published": publish_time,
                "url": f"https://www.youtube.com/watch?v={video_id}",
                "id": id_counter
            })
            id_counter += 1

            if len(results) >= max_videos:
                break
    
    return id_counter, results, continuation_token

if __name__ == "__main__":
    # Example usage with different channel URL formats
    channel_urls = [
        "https://www.youtube.com/c/ChannelName",
        "https://www.youtube.com/channel/UC_x5XG1OV2P6uZZ5FSM9Ttw",
        "https://www.youtube.com/@ChannelName",
        "https://www.youtube.com/user/ChannelName"
    ]
    
    # Test with the first URL
    channel_url = channel_urls[1]  # Using Google Developers channel as example
    print(f"Fetching videos from: {channel_url}")
    videos = fetch_channel_videos(channel_url, max_videos=50)
    print(f"Retrieved {len(videos)} videos from {channel_url}")
    print(f"Results saved to data/videos.json")