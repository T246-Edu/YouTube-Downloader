import YouTubeDownloader.download_playlists as p
import YouTubeDownloader.download_videos as v
def all_function(query,num_v,number_playlists,videosin_eachplaylist):
    v.download_videos(query,num_v)
    p.download_playlists(query,number_playlists,videosin_eachplaylist)