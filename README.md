# Youtube-Video-Thumbnail

A youtube video link or id to video thumbnail python package.

---

```
Made with Python3
(C) @FayasNoushad
Copyright permission under MIT License
License -> https://github.com/FayasNoushad/Youtube-Video-Thumbnail/blob/main/LICENSE
```

---

## Installation

```
pip3 install ytthumb
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
```

### Advanced Usage

```python
import ytthumb

thumbnail = ytthumb.thumbnail(
    video="https://youtu.be/rokGy0huYEA",
    quality="sd"
)
print(thumbnail)
```

<details>
  <summary><b>Available Qualities</b></summary>
<br/>

- sd - Standard Quality
- mq - Medium Quality
- hq - High Quality
- maxres - Maximum Resolution

</details>

---

## Help

```python
import ytthumb

help = help(ytthumb.thumbnail)
print(help)
```

---

## Credits

- [Fayas Noushad](https://github.com/FayasNoushad)
- [YouTube Thumbnail API](https://img.youtube.com)
