from googleapiclient.discovery import build
import os

api_key = os.environ.get('YOUTUBE_API_KEY')
playlist_id = 'RD1TO48Cnl66w'

youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.playlistItems().list(
    part='snippet',
    playlistId=playlist_id,
    maxResults=50
)

response = request.execute()

for item in response['items']:
    title = item['snippet']['title']
    video_id = item['snippet']['resourceId']['videoId']
    print(f"{title} (https://www.youtube.com/watch?v={video_id})")
