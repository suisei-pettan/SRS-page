# 一个简单的视频流应用

这是一个使用socket.io，ytdl-patched和python的简单的视频流应用，可以从YouTube下载视频并通过SRS服务器进行流式传输。

## 安装依赖

要运行这个应用，你需要安装以下依赖：

- socket.io: 一个实时通信库，用于在客户端和服务器之间传输数据。
- ytdl-patched: 一个YouTube下载器，可以从YouTube获取视频信息和格式，并下载视频文件。
- python: 一个通用编程语言，用于编写服务器端的逻辑。

你可以使用以下命令来安装这些依赖：

```bash
npm install socket.io
npm install ytdl-patched
pip install python
```

## 启动Docker

要启动SRS服务器，你需要使用Docker来运行一个容器。你可以使用以下命令来启动Docker：

```bash
docker run -p 1935:1935 -p 1985:1985 -p 8081:8080 ossrs/srs:6 ./objs/srs -c conf/docker.conf
```

这个命令会将容器的1935端口映射到主机的1935端口，用于RTMP协议；将容器的1985端口映射到主机的1985端口，用于HTTP API；将容器的8080端口映射到主机的8081端口，用于HTTP FLV协议。