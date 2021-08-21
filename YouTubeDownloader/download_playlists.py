from __future__ import unicode_literals
from pytube import Playlist
import YouTubeDownloader.search_playlists as search_playlist
import youtube_dl
import os
playlists_links = []
def write_playlist(query):
    try:
        os.mkdir("output")
        os.mkdir("output\\{}".format(query))
    except:
        pass
        
    write_links = open("output\\{}\\search_playlists.txt".format(query),"a",encoding="utf-8")
    global playlists_links
    playlists_links = search_playlist.playlists_search(query)
    for video_link in playlists_links:
        write_links.write(video_link+"\n")

def download_playlists(query,number_playlists,videosin_eachplaylist):
    write_playlist(query)
    for playlist in playlists_links:
        if number_playlists > 0:
            play = Playlist(str(playlist))
        for video in play.video_urls:
            if videosin_eachplaylist > 0:
                ydl_opts = {
                    'outtmpl': os.path.join("output\\{}".format(query), '%(title)s-%(id)s.%(ext)s'),
                }
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([video])
                videosin_eachplaylist-=1
        number_playlists-=1