import av
import os
from datetime import datetime

def save_frames():
    os.makedirs("frames", exist_ok=True)
    print("Waiting for stream on rtmp://nginx/live/stream...")

    container = av.open("rtmp://nginx/live/stream")

    for frame in container.decode(video=0):
        timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S_%f")
        filename = f"frames/frame_{timestamp}.jpg"
        frame.to_image().save(filename)
        print(f"Saved {filename}")

if __name__ == "__main__":
    print("Monitor Started")
    save_frames()
