import os

# Define the path to the folder containing video 1 files
video1_folder = 'video1'

# Define the path to the folder containing video 2 files
video2_folder = 'video2'

# Specify the folder where the output videos will be saved
output_folder = 'newtiktoks'
os.makedirs(output_folder, exist_ok=True)

# TikTok preferred resolution (1080x1920, 9:16 aspect ratio)
tiktok_width = 1080
tiktok_height = 1920

# Get a list of video 1 files (assuming they're all in the video1 folder)
video1_files = os.listdir(video1_folder)
video1_files.sort()  # Ensure files are in the desired order

# Get a list of video 2 files in the video2 folder
video2_files = os.listdir(video2_folder)
video2_files.sort()  # Ensure files are in the desired order

# Loop through up to 50 different videos for video 2 (the bottom third)
for i, video2_filename in enumerate(video2_files[:117]):  # Loop through the first 50 videos
    # Define the paths to video 1 and video 2 files
    video1_file = os.path.join(video1_folder, video1_files[i % len(video1_files)])
    video2_file = os.path.join(video2_folder, video2_filename)

    # Define the output file path
    output_path = os.path.join(output_folder, f'output_{i+1}.mp4')

    # Use FFmpeg to combine video 1 and video 2 with the TikTok dimensions and adjust the top and bottom video sizes
    cmd = (
        f'ffmpeg -i "{video1_file}" -i "{video2_file}" '
        f'-filter_complex "[0:v]scale={tiktok_width}:{int(tiktok_height*2/3)}[top]; '
        f'[1:v]scale={tiktok_width}:{int(tiktok_height*1/3)}[bottom]; [top][bottom]vstack" '
        '-c:v libx264 -crf 32 -preset veryfast -c:a aac -strict experimental '
        f'"{output_path}"'
    )

    os.system(cmd)

    print(f"Video {i+1}/{len(video2_files[:117])} processed. Output saved as '{output_path}'")
