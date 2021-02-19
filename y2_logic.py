from pytube import YouTube
import subprocess
import os


def func0(url, file_name):
    yt = YouTube(str(url))
    yt.streams.filter(res="1080p").first().download(output_path="C:/Users/Diego Gutiérrez/Documents/VideoDownloads/" ,filename=file_name + "video")
    yt.streams.filter(type="audio").first().download(output_path="C:/Users/Diego Gutiérrez/Documents/VideoDownloads/" ,filename=(file_name + "audio"))

    video_file = file_name + "video.mp4"
    audio_file = file_name + "audio.mp4"
    output = file_name + ".mp4"

    os.chdir('C:/Users/Diego Gutiérrez/Documents/VideoDownloads/')
    subprocess.run(f"ffmpeg -i {video_file} -i {audio_file} -c copy {output}")

    os.remove(file_name + "video.mp4")
    os.remove(file_name + "audio.mp4")

def func1(url, file_name):
    yt = YouTube(str(url))
    yt.streams.first().download(output_path="C:/Users/Diego Gutiérrez/Documents/VideoDownloads/" ,filename=file_name)

def func2(url, file_name):
    yt = YouTube(str(url))
    yt.streams.filter(type="audio").first().download(output_path="C:/Users/Diego Gutiérrez/Documents/VideoDownloads/" ,filename=(file_name))


def getResList(url):
    yt = YouTube(str(url))
    video_list = []

    for video in yt.streams:
        video_list.append(video.resolution)

    video_list = list(dict.fromkeys(video_list))
    video_list.remove(None)
    video_list.append("Audio Only")

    return video_list