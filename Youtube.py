from pytube import YouTube

# Link of the YouTube video you want to download
video_url = input("Enter the YouTube video URL: ")

try:
    yt = YouTube(video_url)
    print(f"Title: {yt.title}")
    print("Downloading...")

    # Download the highest resolution stream available
    stream = yt.streams.get_highest_resolution()
    stream.download()  # You can specify the output path in download('path/to/directory')

    print("Download completed!")
except Exception as e:
    print(f"An error occurred: {e}")

