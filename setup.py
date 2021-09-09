# Made with python3
# (C) @FayasNoushad
# Copyright permission under MIT License
# All rights reserved by FayasNoushad
# License -> https://github.com/FayasNoushad/Youtube-Video-Thumbnail/blob/main/LICENSE

import pathlib
from setuptools import setup, find_packages


file = pathlib.Path(__file__).parent

README = (file / "README.md").read_text()

setup = (
    name="YTThumb",
    version="1.1.1",
    author="FayasNoushad",
    long_description=README,
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
    install_requires=[],
    python_requires=">=3.6"
)
