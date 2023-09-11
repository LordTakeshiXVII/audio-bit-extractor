# Extract Audio from MP4 Script

This script allows users to extract audio segments from an MP4 video file and save them as separate MP3 files. Each audio segment's duration can be specified by the user.

## Prerequisites

- Python 3.x
- `moviepy` library. You can install it using pip:
  ```
  pip install moviepy
  ```

## How to Use

1. **Clone the Repository**:
   If you haven't already, clone this repository to your local machine.

2. **Navigate to the Directory**:
   Use the terminal or command prompt to navigate to the directory containing the script.

3. **Run the Script**:
   Execute the script using:
   ```
   python app.py
   ```

4. **Provide Inputs**:
   - **MP4 File Path**: Enter the full path to the MP4 file you want to extract audio from.
   - **Clip Duration**: Specify the duration (in seconds) for each audio segment. For example, if you enter `10`, the script will extract audio in 10-second intervals.
   - **Output Directory**: Enter the directory where you want the extracted audio files to be saved. If you press Enter without specifying a directory, the script will save the files in the current directory by default.

5. **Check the Output**:
   The script will display messages as it processes each segment and saves it to the specified output directory. Once completed, you can navigate to the output directory to access the extracted audio files.

## Features

- **Segmented Extraction**: Instead of extracting the entire audio as one file, this script allows you to break the audio into smaller segments based on a specified duration.
  
- **Customizable Output Directory**: Choose where you want the extracted audio files to be saved.

- **Resource Management**: The script ensures that video and audio objects are closed after processing to free up resources.

## Notes

- The extracted audio segments are saved in the MP3 format.
  
- If the total duration of the video is not a multiple of the specified clip duration, the last segment might be shorter than the specified duration.

## Contributing

Feel free to fork this repository, make changes, and submit pull requests. If you find any bugs or have suggestions for improvements, please open an issue.

## License

This script is provided under the MIT License. See the LICENSE file for details.