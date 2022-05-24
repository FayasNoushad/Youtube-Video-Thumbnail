import requests



def extract_id(video):
    
    # extract the id
    if ("youtube.com" in video) and ("/" in video) and ("=" in video):
        id = video.split("=")[-1]
    elif ("youtu.be" in video) and ("/" in video):
        id = video.split("/")[-1]
    else:
        id = video
    return id


def qualities(json=True):
    '''
    json:
      True - for return qualities and full form as json (default)
      False - for return only qualities as list
    '''
    # qualities of thumbnail
    json_qualities = {
        "sd": "Standard Quality",
        "mq": "Medium Quality",
        "hq": "High Quality",
        "maxres": "Maximum Resolution"
    }
    if not json:
        qualities = []
        for i in json_qualities:
            qualities.append(i)
    else:
        qualities = json_qualities
    return qualities


def thumbnail(video, quality='sd'):
    '''
    video:
      id - video id
      link - video link
    quality:
      sd - Standard Quality
      mq - Medium Quality 
      hq - High Quality
      maxres - Maximum Resolution 
    '''
    
    # extract the id
    video_id = extract_id(video)
    
    # check the qualities
    if quality not in qualities():
        quality = 'sd'
    
    # thumbnail link
    thumbnail = f"https://img.youtube.com/vi/{video_id}/{quality}default.jpg"
    return thumbnail


def download_thumbnail(video, name='thumbnail.jpg', quality='sd'):
    '''
    video:
      id - video id
      link - video link
    name:
      thumbnail name
    quality:
      sd - Standard Quality
      mq - Medium Quality 
      hq - High Quality
      maxres - Maximum Resolution 
    '''
    
    # thumbnail link
    thumbnail = requests.get(thumbnail(video, quality)).content
    
    # save thumbnail
    with open(name, "wb") as file:
        file.write(thumbnail)
    
    # return name
    return name
