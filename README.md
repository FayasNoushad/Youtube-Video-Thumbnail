# YouTube Video Thumbnail

A simple youtube video thumbnail downloader with more qualities via youtube video link or id.

## Installation

```
pip install YTThumb
```

## Usage

### Get Thumbnail

```py
import ytthumb

video = 'https://youtu.be/rokGy0huYEA'  # link/id

# Basic Usage
print(ytthumb.thumbnail(video))
# => returns thumbnail link

# Advanced Usage
thumbnail = ytthumb.thumbnail(
    video=video,
    quality="sd"  # Not required
)
print(thumbnail)
# returns thumbnail link
```

### Get Qualities

```py
import ytthumb

print(ytthumb.qualities())
# returns list of qualities
```

### Download Thumbnail

```py
import ytthumb

ytthumb.download_thumbnail(
    video='https://youtu.be/rokGy0huYEA',
    name='thumbnail.jpg',  # Not required
    quality='sd'  # Not required
)
# Download thumbnail in 'thumbnail.jpg'
```
