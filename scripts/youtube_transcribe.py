import yt_dlp
import os

# Specify the URL of the YouTube video you want to transcribe
video_url = "https://www.youtube.com/watch?v=rtAIPn3V23U&t=348s"

# Configure the YouTube downloader options
ydl_opts = {
    'writesubtitles': True,  # Write subtitles to file
    'subtitleslangs': ['en'],  # Download English subtitles
    'subtitlesformat': 'vtt',  # Subtitle format
    'outtmpl': '%(title)s.%(ext)s',  # Output filename template
    'noplaylist': True,  # Download only the video, not the playlist
}

try:
    # Create a yt-dlp object with the configured options
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Extract video info
        info_dict = ydl.extract_info(video_url, download=False)
        video_title = info_dict.get('title', None)

        # Download the video and subtitles
        print(f"Downloading video: {video_title}")
        ydl.download([video_url])

        # Check if subtitles were downloaded
        subtitle_file = f"{video_title}.en.vtt"
        if os.path.isfile(subtitle_file):
            # Read the subtitle file
            with open(subtitle_file, 'r', encoding='utf-8') as file:
                subtitles = file.read()

            # Remove timestamps and format the transcript
            lines = subtitles.split('\n')
            transcript = []
            for line in lines:
                if '-->' not in line and line.strip() != '':
                    transcript.append(line.strip())

            # Save the transcript to a text file named transcript.txt
            transcript_file = "transcript.txt"
            with open(transcript_file, 'w', encoding='utf-8') as file:
                file.write('\n'.join(transcript))

            print(f"Transcript saved to: {transcript_file}")
        else:
            print("No subtitles found for the video. Transcript not generated.")

except Exception as e:
    print(f"An error occurred: {str(e)}")