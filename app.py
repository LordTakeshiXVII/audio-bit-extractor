import os
from moviepy.editor import *

def extract_audio_from_mp4(input_file, clip_duration, output_dir="."):
    # Load the video file
    video = VideoFileClip(input_file)
    
    # Extract audio from the video
    audio = video.audio
    
    # Calculate the number of clips
    num_clips = int(audio.duration // clip_duration)
    
    for i in range(num_clips):
        start_time = i * clip_duration
        end_time = (i + 1) * clip_duration
        
        # Extract the audio segment
        audio_segment = audio.subclip(start_time, end_time)
        
        # Export the audio segment to a file
        output_file = f"output_{i}.mp3"
        output_path = os.path.join(output_dir, output_file)
        audio_segment.write_audiofile(output_path)
        print(f"Saved: {output_path}")

    # Close the audio and video objects to free up resources
    audio.close()
    video.close()

if __name__ == "__main__":
    input_file = input("Enter the path to the MP4 file: ")
    clip_duration = float(input("Enter the duration of each clip (in seconds): "))
    output_dir = input(f"Enter the output directory (default: current directory '{os.getcwd()}'): ") or "."
    extract_audio_from_mp4(input_file, clip_duration, output_dir)