# YouTube Video Thumbnail

```py
import ytthumb


# Get Thumbnail
thumbnail = ytthumb.thumbnail('https://youtu.be/rokGy0huYEA')
thumbnail = ytthumb.thumbnail(
    video="https://youtu.be/rokGy0huYEA",  # You can alse add id
    quality="sd"  # Not required
)
print(thumbnail)
# => https://img.youtube.com/vi/rokGy0huYEA/sddedault.jpg

# Available Qualities
print(ytthumb.qualities())
# => ["sd", "mq", "hq", "maxres"]

# Download Thumbnail
ytthumb.download_thumbnail(
    video,
    name='thumbnail.jpg',  # Not required
    quality='sd'  # Not required
)
# => Download thumbnail in 'thumbnail.jpg'
```

## Installation

```
pip install YTThumb
```

## Features

- YouTube video link/id to thumbnail
  - Quality select option
- YouTube video link/id to download thumbnail
  - Quality select option
  - Custom name
