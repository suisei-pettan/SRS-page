import os
import re
import subprocess

def get_video_url(video_url):
    command = f"ytdl-patched -g {video_url}"
    output = subprocess.check_output(command.split(), universal_newlines=True)
    url = output.strip().replace('%', '%%')
    return url

def get_ffmpeg_command(video_url, ch):
    url = get_video_url(video_url)
    command = f'ffmpeg -loglevel quiet -i {url} -c:v copy -strict -2 -user_agent "Mozilla/5.0 (Linux; Android 13; 21051182C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 EdgA/111.0.1661.59" -f flv rtmp://127.0.0.1/live/homo{ch}.flv'
    return command
    
video_url = input("请输入YouTube视频链接：")
ch = input("请输入要增加的值：")
command = get_ffmpeg_command(video_url, ch)
print(f"处理后的字符串：{command}")
