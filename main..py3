from pytube import YouTube

# Enter the YouTube video URL
url = "https://www.youtube.com/watch?v=6FJiGC-MXag"

# Create a YouTube object
yt = YouTube(url)

# Get the first stream with the highest resolution
stream = yt.streams.filter(progressive=True).order_by('resolution').desc().first()

# Download the video to the current working directory
stream.download()
