import requests
import os

# Replace with your actual access token
access_token = 'your-access-token'

# Directory where processed TikTok videos are stored
tiktoks_folder = 'newtiktoks'

# Get a list of video files in the folder
video_files = [f for f in os.listdir(tiktoks_folder) if f.endswith('.mp4')]

if video_files:
    # Select the first video file
    video_file_path = os.path.join(tiktoks_folder, video_files[0])

    # Initialize the upload
    init_url = "https://open.tiktokapis.com/v2/post/publish/inbox/video/init/"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json; charset=utf-8'
    }
    data = {
        "source_info": {
            "source": "FILE_UPLOAD",
            "video_size": os.path.getsize(video_file_path),
            "chunk_size": os.path.getsize(video_file_path),
            "total_chunk_count": 1
        }
    }
    response = requests.post(init_url, headers=headers, json=data)

    # Check that the request was successful
    if response.status_code == 200:
        upload_url = response.json()["data"]["upload_url"]

        # Upload the video
        upload_headers = {
            'Content-Range': f"bytes 0-{os.path.getsize(video_file_path) - 1}/{os.path.getsize(video_file_path)}",
            'Content-Type': 'video/mp4'
        }
        with open(video_file_path, 'rb') as f:
            upload_response = requests.put(upload_url, headers=upload_headers, data=f)

            # Check that the upload was successful
            if upload_response.status_code == 200:
                print("Video uploaded successfully!")
            else:
                print("Video upload failed.")
    else:
        print("Initialization failed.")
else:
    print("No video files found in the 'newtiktoks' folder.")
