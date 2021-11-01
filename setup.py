import os
import pathlib
from setuptools import setup, find_packages


def requirements(file="requirements.txt") -> list:
    if os.path.isfile(file):
        with open(file, encoding="utf-8") as r:
            return [i.strip() for i in r]
    else:
        return []


def readme(file="README.md"):
    if os.path.isfile(file):
        with open(file, encoding="utf8") as r:
            return r.read()
    else:
        return ""


setup(
    name="YTThumb",
    version="1.3.4",
    author="FayasNoushad",
    long_description=readme(),
    long_description_content_type="text/markdown",
    description="A youtube video link or id to video thumbnail python package.",
    license="MIT",
    url="https://github.com/FayasNoushad/Youtube-Video-Thumbnail",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    install_requires=requirements(),
    python_requires=">=3.6"
)
