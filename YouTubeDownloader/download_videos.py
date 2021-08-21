from __future__ import unicode_literals
import YouTubeDownloader.search_videos as search_videos
import youtube_dl
import os
videos_links = []
def write_videos(query):
    try:
        try:
            os.mkdir("output")
            os.mkdir("output\\{}".format(query))
        except:
            pass
        write_links = open("output\\{}\\search_videos.txt".format(query),"a",encoding="utf-8")
        global videos_links
        videos_links = search_videos.videos_search(query)

        for video_link in videos_links:
            write_links.write(video_link+"\n")
    except:
        pass


def download_videos(query,number_videos):
    try:
        write_videos(query)
        for video in videos_links:
            if number_videos > 0:
                ydl_opts = {
                    'outtmpl': os.path.join("output\\{}".format(query), '%(title)s-%(id)s.%(ext)s'),
                }
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([video])
                number_videos-=1
    except:
        pass