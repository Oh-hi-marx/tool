import ffmpeg
import os
from PIL import Image
import math
from tqdm import tqdm

def get_video_info(video_path):
    probe = ffmpeg.probe(video_path)
    video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
    if video_stream is None:
        raise ValueError("No video stream found")
    
    width = int(video_stream['width'])
    height = int(video_stream['height'])
    
    if 'duration' in video_stream:
        duration = float(video_stream['duration'])
    elif 'duration' in probe['format']:
        duration = float(probe['format']['duration'])
    else:
        nb_frames = int(video_stream.get('nb_frames', 0))
        fps = eval(video_stream.get('avg_frame_rate', '0/0'))
        if nb_frames > 0 and fps > 0:
            duration = nb_frames / fps
        else:
            raise ValueError("Unable to determine video duration")
    
    return width, height, duration

def create_video_preview(video_path, preview_path, frame_count=24):
    try:
        width, height, duration = get_video_info(video_path)
        grid_size = math.ceil(math.sqrt(frame_count))
        
        interval = duration / frame_count
        frames = []
        for i in range(frame_count):
            timestamp = i * interval
            out, _ = (
                ffmpeg
                .input(video_path, ss=timestamp)
                .filter('scale', width, height)
                .output('pipe:', vframes=1, format='rawvideo', pix_fmt='rgb24')
                .run(capture_stdout=True, quiet=True)
            )
            frame = Image.frombytes('RGB', (width, height), out)
            frames.append(frame)

        preview_image = Image.new('RGB', (width * grid_size, height * grid_size))
        for idx, frame in enumerate(frames):
            x = (idx % grid_size) * width
            y = (idx // grid_size) * height
            preview_image.paste(frame, (x, y))

        preview_image.save(preview_path)
        print(f"Preview created for {os.path.basename(video_path)} with {frame_count} frames")
    except Exception as e:
        print(f"Error processing {os.path.basename(video_path)}: {str(e)}")

def process_videos(video_folder, preview_folder, frame_count=16):
    valid_extensions = (".mp4", ".avi", ".mov", ".mkv", ".wmv")
    video_files = []

    # Collect all video files, including those in subdirectories
    for root, _, files in os.walk(video_folder):
        for file in files:
            if file.lower().endswith(valid_extensions):
                video_files.append(os.path.join(root, file))

    print(f"Found {len(video_files)} video files")

    # Process each video file with a progress bar
    for video_path in tqdm(video_files, desc="Processing videos"):
        # Generate the filename for the preview image
        video_filename = os.path.basename(video_path)
        preview_filename = f"{os.path.splitext(video_filename)[0]}_preview_{frame_count}frames.jpg"
        preview_path = os.path.join(preview_folder, preview_filename)
        
        # Check if the preview already exists
        if os.path.exists(preview_path):
            print(f"Preview already exists for {video_filename}, skipping...")
            continue
        
        create_video_preview(video_path, preview_path, frame_count)

# Define the folder paths
video_folder = "./"
preview_folder = "previews"

# Create the preview folder if it doesn't exist
if not os.path.exists(preview_folder):
    os.makedirs(preview_folder)

# Example usage:
process_videos(video_folder, preview_folder, frame_count=25)  # Creates previews with 25 frames
