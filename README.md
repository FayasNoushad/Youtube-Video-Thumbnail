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
print(thumbnail)
# => https://img.youtube.com/vi/rokGy0huYEA/sddedault.jpg

# Available Qualities
print(ytthumb.qualities())
# => ["sd", "mq", "hq", "maxres"]

# Download Thumbnail
ytthumb.download_thumbnail(
    video,
    name='thumbnail.jpg'
)
# => Download thumbnail in 'thumbnail.jpg'
```

---

## Credits

- [Fayas Noushad](https://github.com/FayasNoushad)

---
