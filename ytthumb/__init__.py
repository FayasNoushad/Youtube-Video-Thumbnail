def thumbnail(video, quality='sd'):
    """
    video:
      id - video id
      link - video link
    quality:
      sd - Standard Quality
      mq - Medium Quality 
      hq - High Quality
      maxres - Maximum Resolution 
    """
    qualities = ["sd", "mq", "hq", "maxres"]
    if ("youtube.com" in video) and ("/" in video) and ("=" in video):
        id = video.split("=")[-1]
    elif ("youtu.be" in video) and ("/" in video):
        id = video.split("/")[-1]
    else:
        id = video
    if quality not in qualities:
        quality = 'sd'
    thumbnail = "https://img.youtube.com/vi/" + id + f"/{quality}default.jpg"
    return thumbnail

