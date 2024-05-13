from googleapiclient.discovery import build

# Kullanıcıdan YouTube Data API için API anahtarını alın.
YOUTUBE_API_KEY = input("Lütfen YouTube Data API anahtarınızı girin: ")

def get_my_youtube_channel_info():
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    request = youtube.channels().list(
        part='snippet,contentDetails,statistics',
        mine=True
    )
    response = request.execute()

    if response['items']:
        channel_info = response['items'][0]
        return {
            'title': channel_info['snippet']['title'],
            'description': channel_info['snippet']['description'],
            'profile_image': channel_info['snippet']['thumbnails']['high']['url'],
            'view_count': channel_info['statistics']['viewCount'],
            'subscriber_count': channel_info['statistics']['subscriberCount'],
            'video_count': channel_info['statistics']['videoCount']
        }
    else:
        return {'error': 'No channel information found.'}

# Kanal bilgilerini al
my_channel_info = get_my_youtube_channel_info()

if 'error' not in my_channel_info:
    print(f"Channel Title: {my_channel_info['title']}")
    print(f"Description: {my_channel_info['description']}")
    print(f"Profile Image URL: {my_channel_info['profile_image']}")
    print(f"View Count: {my_channel_info['view_count']}")
    print(f"Subscriber Count: {my_channel_info['subscriber_count']}")
    print(f"Video Count: {my_channel_info['video_count']}")
else:
    print(my_channel_info['error'])
