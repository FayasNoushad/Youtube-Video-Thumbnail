# Made with python3
# (C) @FayasNoushad
# Copyright permission under MIT License
# All rights reserved by FayasNoushad
# License -> https://github.com/FayasNoushad/Youtube-Video-Thumbnail/blob/main/LICENSE

#sd - Standard Definition
#mq - Medium Quality
#hq - High Quality
#maxres - MAXimum RESolution

def thumbnail(video, quality='sd'):
    if ("youtube.com" in video) and ("/" in video) and ("=" in video):
        id = video.split("=")[-1]
    elif ("youtu.be" in video) and ("/" in video):
        id = video.split("/")[-1]
    else:
        id = video
    if quality not in ['sd','mq','hq','maxres']:
        quality = 'sd'
    thumbnail = "https://img.youtube.com/vi/" + id + f"/{quality}default.jpg"
    return thumbnail

