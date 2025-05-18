import requests
import json
from urllib.parse import urlencode
import re
from bs4 import BeautifulSoup

def get_channel_id_from_username(username):
    """
    Convert a YouTube username to a channel ID by trying different URL formats
    and parsing the response.

    Args:
        username (str): YouTube username (without the @ symbol)

    Returns:
        str: YouTube channel ID if successful, None otherwise
    """
    # Try different URL formats
    urls_to_try = [
        f"https://www.youtube.com/@{username}",
        f"https://www.youtube.com/c/{username}",
        f"https://www.youtube.com/user/{username}"
    ]
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    }

    for url in urls_to_try:
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                # Parse channel ID from the HTML
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Find meta tag with channel ID
                meta_tag = soup.find('meta', {'itemprop': 'identifier'})
                if meta_tag and 'content' in meta_tag.attrs:
                    return meta_tag['content']
                    
                # Try alternate method - search for channel ID in the HTML
                channel_id_match = re.search(r'"channelId":"([^"]+)"', response.text)
                if channel_id_match:
                    return channel_id_match.group(1)
                    
                # Another alternate method - search for externalId
                external_id_match = re.search(r'"externalId":"([^"]+)"', response.text)
                if external_id_match:
                    return external_id_match.group(1)
                    
        except Exception as e:
            print(f"Error trying URL {url}: {e}")
            continue
    
    

    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200 and response.text:
            return response.text.strip()
    except Exception as e:
        pass
    
    print(f"Could not find channel ID for username: {username}")
    return None

def get_channel_videos(username, max_videos=20):
    """
    Fetch videos from a YouTube channel using a username.

    Args:
        username (str): YouTube handle (e.g., 'GoogleDevelopers')
        max_videos (int): Maximum number of videos to retrieve

    Returns:
        list: List of dictionaries containing video information
    """
    channel_id = get_channel_id_from_username(username)
    if not channel_id:
        print(f"Could not resolve channel ID for username: {username}")
        return []

    url = "https://www.youtube.com/youtubei/v1/browse?prettyPrint=false"
    original_url = f"https://www.youtube.com/channel/{channel_id}/videos"

    payload = {
        "context": {
            "client": {
                "hl": "en-GB",
                "gl": "US",
                "clientName": "WEB",
                "clientVersion": "2.20250516.01.00",
                "originalUrl": original_url,
                "platform": "DESKTOP"
            },
            "user": {
                "lockedSafetyMode": False
            },
            "request": {
                "useSsl": True
            }
        },
        "browseId": channel_id,
        "params": "EgZ2aWRlb3PyBgQKAjoA"
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://www.youtube.com',
        'referer': original_url,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload)).json()
        return extract_channel_videos(response, max_videos)
    except Exception as e:
        print(f"Error fetching channel videos: {e}")
        return []

def extract_channel_videos(data, max_videos=20):
    """
    Extract video information from YouTube API response.

    Args:
        data (dict): YouTube API response
        max_videos (int): Maximum number of videos to extract

    Returns:
        list: List of dictionaries containing video information
    """
    try:
        tabs = data.get("contents", {}).get("twoColumnBrowseResultsRenderer", {}).get("tabs", [])
        contents = None
        for tab in tabs:
            tab_renderer = tab.get("tabRenderer", {})
            if tab_renderer.get("title", "").lower() == "videos":
                contents = tab_renderer.get("content", {}).get("richGridRenderer", {}).get("contents", [])
                break

        if not contents:
            print("No videos tab found or no videos available")
            return []

        results = []
        for item in contents:
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
                    "url": f"https://www.youtube.com/watch?v={video_id}"
                })

                if len(results) >= max_videos:
                    break

        return results

    except Exception as e:
        print(f"Error extracting videos: {e}")
        return []

if __name__ == "__main__":
    print("\nFetching videos for the channels")
    try:
        channels = ["GoogleDevelopers", "pixegami", "Autostrad"]
        for channel in channels:
            print(f"\nFetching for: {channel}")
            videos = get_channel_videos(channel, max_videos=5)
            if videos:
                print(json.dumps(videos, indent=2))
            else:
                print(f"No videos found for channel: {channel}")
            print("----------------------------------------")
    except Exception as e:
        print(f"Error: {e}")


