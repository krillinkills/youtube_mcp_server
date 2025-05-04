from googleapiclient.discovery import build
import os
from typing import List, Dict

# Replace with your actual API key
YOUTUBE_API_KEY: str = os.getenv("YOUTUBE_API_KEY")
# Initialize the YouTube API client
youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)


def get_top_videos(query: str, max_results: int = 100) -> List[Dict[str, str]]:
    """
    Fetches top videos from YouTube based on the query.

    Args:
        query (str): Search term.
        max_results (int): Number of videos to retrieve.

    Returns:
        List[Dict[str, str]]: List of dictionaries with videoId, title, and viewCount.
    """
    videos: List[Dict[str, str]] = []
    video_ids: List[str] = []
    request = youtube.search().list(
        q=query,
        part="snippet",
        type="video",
        order="viewCount",
        maxResults=50,
    )
    while len(videos) < max_results:
        response = request.execute()
        for item in response["items"]:
            video_id = item["id"]["videoId"]
            title = item["snippet"]["title"]
            videos.append({"videoId": video_id, "title": title})
            video_ids.append(video_id)
            if len(videos) >= max_results:
                break
        if "nextPageToken" in response:
            request = youtube.search().list(
                q=query,
                part="snippet",
                type="video",
                order="viewCount",
                maxResults=50,
                pageToken=response["nextPageToken"],
            )
        else:
            break
    # Fetch statistics for all videos in one batch
    stats_response = (
        youtube.videos().list(part="statistics", id=",".join(video_ids)).execute()
    )
    # Map video IDs to view counts
    stats_map: Dict[str, str] = {}
    for item in stats_response["items"]:
        vid = item["id"]
        view_count = item["statistics"].get("viewCount", "0")
        stats_map[vid] = view_count
    # Add view counts to your videos list
    for video in videos:
        video["viewCount"] = stats_map.get(video["videoId"], "0")
    return videos


# Example usage
search_query: str = "hyaluronic acid"
top_videos: List[Dict[str, str]] = get_top_videos(search_query, 10)
# Print the results with view counts
for idx, video in enumerate(top_videos, 1):
    print(
        f"{idx}. {video['title']} - {video['viewCount']} views (https://www.youtube.com/watch?v={video['videoId']})"
    )
