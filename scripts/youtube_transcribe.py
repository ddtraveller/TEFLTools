import yt_dlp
import os

if __name__ == '__main__':
    # Prompt the user to enter the video URL
    video_url = input("Enter the URL of the YouTube video you want to download and transcribe: ")

    # Configure the YouTube downloader options
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
        'writesubtitles': True,
        'subtitleslangs': ['en'],
        'subtitlesformat': 'vtt',
        'outtmpl': '%(title)s.%(ext)s',
        'noplaylist': True,
        'keepvideo': True,  # Keep the video file after conversion
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

            print(f"Video saved as: {video_title}.mp4")

    except Exception as e:
        print(f"An error occurred: {str(e)}")