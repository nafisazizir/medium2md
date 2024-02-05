# Medium to Markdown Converter

Convert your Medium articles to Markdown format easily, not just the text, but including all the images!

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Converting medium articles to markdown, so you can use it in another environment, could be very stressfull. There are plenty of converter out there, but I found that most of them are quite unreliable and buggy.

I found a trick to convert medium to markdown document simply by using Notion! However, if your articles contain images, you have to download the images one by one. This repo will guide you to convert medium article with Notion, and automate download the images using the script.

## Features

- Convert Medium articles to Markdown format
- Simple and easy-to-use

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/nafisazizir/medium2md.git
   ```
2. Navigate to the project directory
   ```bash
   cd medium2md
   ```

## **Usage**

1. Assume that you already have Notion account. Open your Notion app.
2. Open your medium article, and copy all the content that you'd like to convert.
3. Paste it in the Notion. Voila! Notion will preserved the formatting and styling of your article.
4. As for next step, downloading the images. From Notion, select all content and copy again.
5. Paste the content in the ```input.md``` in the root project directory.
6. To download the images and include the images in the markdown, run the following command
   ```bash
   python script.py
   ```
7. The output of your markdown file and the images are in the output directory that'll be automatically created by the script.

## **Contributing**

If you have any suggestions and found some issues/bugs, feel free to open issues and pull requests.

## **License**

This project is licensed under the MIT License.
