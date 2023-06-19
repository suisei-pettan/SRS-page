import requests
import subprocess
import time

# 填写推流地址和密钥
push_url = input("请输入推流地址: ")
push_key = input("请输入秘钥: ")

# 发送 GET 请求获取直播信息
def get_live_info(channel_id):
    url = "https://holodex.net/api/v2/live"
    headers = {
        "X-APIKEY": "在此填入你的holodex apikey"
    }
    params = {
        "channel_id": channel_id,
        "status": "live",
        "type": "stream"
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    return data

# 在 data 中搜索具有 'live_tl_count' 键的对象
def find_live_object(data):
    for obj in data:
        if 'live_tl_count' in obj:
            return obj
    return None

# 获取直播源链接
def get_live_source(video_id):
    command = f"ytdl-patched -g 'https://www.youtube.com/watch?v={video_id}'"
    output = subprocess.check_output(command, shell=True).decode().strip()
    return output

# 执行 ffmpeg 命令进行推流
def start_pushing(live_source):
    ffmpeg_command = f"ffmpeg -loglevel quiet -i {live_source} -c:v copy -strict -2 -f flv '{push_url}/{push_key}'"
    print("ffmpeg", ffmpeg_command)
    process = subprocess.Popen(ffmpeg_command, shell=True)
    return process

# 主程序
if __name__ == '__main__':
    channel_id = input("请输入 channel_id: ")
    process = None  # 初始化 ffmpeg 进程

    while True:
        data = get_live_info(channel_id)
        live_object = find_live_object(data)

        if live_object:
            video_id = live_object['id']
            live_source = get_live_source(video_id)
            print("直播源:", live_source)
            if process is None or process.poll() is not None:  # 如果 ffmpeg 进程未运行或已停止运行
                process = start_pushing(live_source)
            else:
                print("ffmpeg 进程正在运行，等待 1 分钟后重试...")
                time.sleep(60)
        else:
            print("没有找到具有 'live_tl_count' 键的直播信息，等待 5 分钟后重试...")
            time.sleep(300)

        if process and process.poll() is not None:  # 如果 ffmpeg 进程退出
            print("ffmpeg 进程已退出，执行特定命令...")
            special_command = "ffmpeg -re -stream_loop 8 -i https://github.com/suisei-pettan/SRS-page/raw/main/pause.mp4 -c:v copy -strict -2 -f flv '{push_url}/{push_key}'"
            subprocess.run(special_command, shell=True)
            process = None  # 重置 ffmpeg 进程

    print("程序结束。")
