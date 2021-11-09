```
Made with Python3
(C) @FayasNoushad
Copyright permission under MIT License
License -> https://github.com/FayasNoushad/Youtube-Video-Thumbnail/blob/main/LICENSE
```

---

## Installation

```
pip install YTThumb
```

---

## Usage

```py
import ytthumb


# Basic Usage
thumbnail = ytthumb.thumbnail('https://youtu.be/rokGy0huYEA')
print(thumbnail)
# => https://img.youtube.com/vi/rokGy0huYEA/sddedault.jpg

# Advanced Usage
thumbnail = ytthumb.thumbnail(
    video="https://youtu.be/rokGy0huYEA",
    quality="sd"
)
'''
Available qualities
  - sd - Standard Quality
  - mq - Medium Quality
  - hq - High Quality
  - maxres - Maximum Resolution
'''
print(thumbnail)
# => https://img.youtube.com/vi/rokGy0huYEA/sddedault.jpg


download_thumbnail(video, name='thumbnail.jpg', quality='sd')
# => For download thumbnail "thumbnail.jpg"
```

---

## Credits

- [Fayas Noushad](https://github.com/FayasNoushad)

---
