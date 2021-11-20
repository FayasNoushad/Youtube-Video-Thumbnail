import os
import setuptools


def requirements(file="requirements.txt"):
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


setuptools.setup(
    name="YTThumb",
    version="1.3.7",
    description="YouTube video thumbnail download",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/FayasNoushad/Youtube-Video-Thumbnail",
    license="MIT",
    author="Fayas Noushad",
    author_email="contact@fayas.me",
    packages=setuptools.find_packages(),
    install_requires=requirements(),
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License"
    ]
)
