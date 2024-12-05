import time
from typing import Dict

class VideoDownloader:
    def download_video(self, url: str) -> str:
        print(f"Downloading video from {url}...")
        time.sleep(2)  # Simulate time taken to download
        return f"Video content from {url}"

class VideoDownloaderProxy:
    def __init__(self, downloader: VideoDownloader):
        self.downloader = downloader
        self.cache: Dict[str, str] = {} 
    def download_video(self, url: str) -> str:
        if url in self.cache:
            print(f"Fetching video from cache for {url}")
            return self.cache[url]
        
        # If not in cache, download it and store in cache
        print(f"Video not found in cache for {url}. Downloading...")
        video_content = self.downloader.download_video(url)
        self.cache[url] = video_content
        return video_content

if __name__ == "__main__":
    real_downloader = VideoDownloader()
    proxy_downloader = VideoDownloaderProxy(real_downloader)# object creation logic can also reside inside proxyclass, so we wouldn't need to create a real_downloader and than pass it

    # First download (will download from the server)
    video1 = proxy_downloader.download_video("https://example.com/video1")
    print(video1)
    print()

    # Second download of the same video (will fetch from cache)
    video1_cached = proxy_downloader.download_video("https://example.com/video1")
    print(video1_cached)
    print()

    # Download a different video
    video2 = proxy_downloader.download_video("https://example.com/video2")
    print(video2)
    print()

    # Download the first video again (should fetch from cache)
    video1_again = proxy_downloader.download_video("https://example.com/video1")
    print(video1_again)
