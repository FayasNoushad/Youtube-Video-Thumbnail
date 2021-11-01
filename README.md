```
Made with Python3
(C) @FayasNoushad
Copyright permission under MIT License
License -> https://github.com/FayasNoushad/Youtube-Video-Thumbnail/blob/main/LICENSE
```

---

## Installation

```
pip install ytthumb
```

---

## Usage

### Basic Usage

```python
import ytthumb

thumbnail = ytthumb.thumbnail(
    video="https://youtu.be/rokGy0huYEA"
)
print(thumbnail)
# => https://img.youtube.com/vi/rokGy0huYEA/sddedault.jpg
```

### Advanced Usage

```python
import ytthumb

thumbnail = ytthumb.thumbnail(
    video="https://youtu.be/rokGy0huYEA",
    quality="sd"
)
"""
Available qualities
  - sd - Standard Quality
  - mq - Medium Quality
  - hq - High Quality
  - maxres - Maximum Resolution
"""

print(thumbnail)
# => https://img.youtube.com/vi/rokGy0huYEA/sddedault.jpg

download_thumbnail(video, name='thumbnail.jpg', quality='sd')
# => For download thumbnail "thumbnail.jpg"
```

---

## Help

```python
import ytthumb

help = help(ytthumb.thumbnail)
print(help)
# => For help
```

---

## Credits

- [Fayas Noushad](https://github.com/FayasNoushad)
- [YouTube Thumbnail API](https://img.youtube.com)

---
