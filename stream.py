import subprocess
import sys

def main():
    # 获取启动参数
    youtube_url = sys.argv[1]
    channel_number = sys.argv[2]

    # 执行 ytdl-patched -g youtube视频链接 获取其输出的链接存入 源直播 变量
    ytdl_patched_output = subprocess.check_output(f"yt-dlp -g {youtube_url}", shell=True)
    source_live = ytdl_patched_output.decode().strip()
    # 执行 ffmpeg -loglevel quiet -i 源直播 -c:v copy -strict -2 -f flv rtmp://127.0.0.1/live/homo频道号.flv
    ffmpeg_command = f"ffmpeg -loglevel quiet -i {source_live} -c:v copy -strict -2 -f flv rtmp://127.0.0.1/live/homo{channel_number}.flv"
    subprocess.run(ffmpeg_command, shell=True)

if __name__ == "__main__":
    main()
