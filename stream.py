import time
import subprocess
import sys

def main():
    # 获取启动参数
    youtube_url = sys.argv[1]
    channel_number = sys.argv[2]

    # 执行 ytdl-patched -g youtube视频链接 获取其输出的链接存入 源直播 变量
    ytdl_patched_output = subprocess.check_output(f"ytdl-patched -g {youtube_url}", shell=True)
    source_live = ytdl_patched_output.decode().strip()
    # 执行 ffmpeg -loglevel quiet -i 源直播 -c:v copy -strict -2 -f flv rtmp://127.0.0.1/live/homo频道号.flv
    ffmpeg_command = f"ffmpeg -loglevel quiet -i {source_live} -c:v copy -strict -2 -f flv rtmp://127.0.0.1/live/homo{channel_number}.flv"

    # 启动ffmpeg进程
    ffmpeg_process = subprocess.Popen(ffmpeg_command, shell=True)

    # 等待两分钟
    time.sleep(120)

    # 检查ffmpeg进程是否仍在运行
    if ffmpeg_process.poll() is None:
        # 如果ffmpeg进程仍在运行，则不停止SuperVisord进程
        print("FFmpeg is still running. SuperVisord process will not be stopped.")
    else:
        # 如果ffmpeg进程已退出，则停止与其channel_number相同名称的SuperVisord进程
        supervisor_process_name = f"SuperVisord_{channel_number}"
        stop_supervisor_command = f"supervisorctl stop {supervisor_process_name}"
        subprocess.run(stop_supervisor_command, shell=True)

if __name__ == "__main__":
    main()
