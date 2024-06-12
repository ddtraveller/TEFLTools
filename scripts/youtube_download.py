import yt_dlp

if __name__ == '__main__':
    # Prompt the user to enter the video URL
    video_url = input("Enter the URL of the age-restricted YouTube video you want to download: ")
    # Example: "https://www.youtube.com/watch?v=rtAIPn3V23U&t=348s"

    # Configure the YouTube downloader options
    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',  # Output filename template
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',  # Video format and quality
        'noplaylist': True,  # Download only the video, not the playlist
    }

    try:
        # Create a yt-dlp object with the configured options
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Extract video info
            info_dict = ydl.extract_info(video_url, download=False)
            video_title = info_dict.get('title', None)

            # Prompt for authentication if required
            if info_dict.get('age_limit') is not None:
                print("This video is age-restricted. Please provide your YouTube account credentials.")
                username = input("Enter your YouTube username or email: ")
                password = input("Enter your YouTube password: ")
                ydl_opts['username'] = username
                ydl_opts['password'] = password

            # Download the video
            print(f"Downloading video: {video_title}")
            ydl.download([video_url])
            print("Video downloaded successfully!")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
