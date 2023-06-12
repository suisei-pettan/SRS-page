#!/bin/bash

# Download and install yt-dlp
sudo curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp
sudo chmod a+rx /usr/local/bin/yt-dlp

# Install python3 and ffmpeg
sudo apt update
sudo apt install -y python3 ffmpeg

# Download stream.py to /root directory
sudo curl -L https://raw.githubusercontent.com/suisei-pettan/SRS-page/main/stream.py -o /root/stream.py

# Execute the install script
sudo wget -O install.sh http://io.bt.sy/install/install-ubuntu_6.0.sh && sudo bash install.sh

# Output instructions
echo -e "\033[38;2;102;204;255m请在 /root 目录下执行 python3 stream.py 加直播页、channel 参数即可启动\033[0m"

