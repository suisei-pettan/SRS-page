#!/bin/bash

# 安装youtube-dl工具
sudo curl -L https://github.com/ytdl-patched/ytdl-patched/releases/latest/download/ytdl-patched -o /usr/local/bin/ytdl-patched
sudo chmod a+rx /usr/local/bin/ytdl-patched

# 检查是否安装了pip
command -v pip >/dev/null 2>&1 || {
    echo "请确保已安装pip3。"
    exit 1
}

# 安装requests库
pip3 install requests

# 安装ffmpeg工具
apt-get update
apt-get install ffmpeg

echo "所有依赖安装完成。"
