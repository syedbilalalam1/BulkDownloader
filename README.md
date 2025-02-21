# Batch URL Downloader

## Overview
Batch URL Downloader is a simple and efficient tool to download multiple files from URLs at once. Built using Python and Tkinter, it provides a user-friendly interface with a progress bar and status updates. 

![Screenshot](https://github.com/user-attachments/assets/cf6227c4-827b-4b41-95e2-7b94218aaab7) *(Replace with an actual screenshot)*

## Features
- **Batch Downloading**: Download multiple files by pasting URLs (one per line).
- **Custom Save Location**: Choose where the downloaded files will be saved.
- **Progress Tracking**: A progress bar updates as files are downloaded.
- **Error Handling**: Alerts for invalid URLs or failed downloads.
- **Lightweight & Easy to Use**: Simple interface with no unnecessary complexities.
- **Themed UI**: Uses `ttkthemes` for a polished look.

## Installation
You can download the latest version of **Batch URL Downloader** from the [Releases](https://github.com/yourusername/yourrepository/releases) section.

### Requirements (For Running from Source)
If you want to run the script from source, ensure you have the following installed:

```sh
pip install requests ttkthemes
```

## Usage
1. **Download the .exe** from the [Releases](https://github.com/yourusername/yourrepository/releases) section and run it.
2. Enter the URLs (one per line) in the text box.
3. Choose the download location or use the default `Downloads` folder.
4. Click **Start Download** to begin.
5. Monitor progress and status updates.

## Building from Source
If you'd like to build the executable yourself, use PyInstaller:

```sh
pyinstaller --onefile --windowed --name "Batch URL Downloader" main.py
```

## Made By
**Syed Bilal Alam**  
Discord: bilalwastaken #9773

## License
This project is licensed under the MIT License.
