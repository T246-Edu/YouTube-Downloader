from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRoundFlatButton
from kivy.lang import Builder
from pytube import Playlist
import YouTubeDownloader.all_VP as all
import youtube_dl
import threading
import os
Query_YT_DOWN_NEW = '''
MDTextField:
    hint_text: "Enter query to download about: "
    helper_text: "Enter search query to download videos about"
    helper_text_mode: "on_focus"
    pos_hint: {'center_x':0.5,'center_y':0.6}
    required:True
    max_text_length:50
    size_hint_x:None
    width:300
'''
NumberOf_Videos_YTDOWN = '''
MDTextField:
    hint_text: "Enter Number Of Videos: "
    helper_text: "Enter right Number Of Videos here."
    helper_text_mode: "on_focus"
    pos_hint: {'center_x':0.5,'center_y':0.5}
    required:True
    max_text_length:2
    size_hint_x:None
    width:300
'''
Number_PlayLISTSYT = '''
MDTextField:
    hint_text: "Enter Number of playlist: "
    helper_text: "Enter right number of playlists here."
    helper_text_mode: "on_focus"
    pos_hint: {'center_x':0.5,'center_y':0.4}
    required:True
    max_text_length:2
    size_hint_x:None
    width:300
'''
NUMBER_videos_ToDown_Each_Playlist = '''
MDTextField:
    hint_text: "Enter Number videos in each playlist"
    helper_text: "Enter right number here."
    helper_text_mode: "on_focus"
    pos_hint: {'center_x':0.5,'center_y':0.3}
    required:True
    max_text_length:2
    size_hint_x:None
    width:300
'''
YouTube_Videos_Down = '''
MDTextField:
    hint_text: "Enter The Video Link: "
    helper_text: "Enter right video link here."
    helper_text_mode: "on_focus"
    pos_hint: {'center_x':0.5,'center_y':0.5}
    required:True
    max_text_length:150
    size_hint_x:None
    width:300
'''
Plsylists_Videos_Down = '''
MDTextField:
    hint_text: "Enter The Playlist Link: "
    helper_text: "Enter right playlist link here."
    helper_text_mode: "on_focus"
    pos_hint: {'center_x':0.5,'center_y':0.5}
    required:True
    max_text_length:150
    size_hint_x:None
    width:300
'''

class YouTube(MDApp):
    def build(self):
        self.screen = Screen()
        self.data_status = MDLabel(text = "status...",
                                    pos_hint = {'center_x':.97,'center_y':.3})
        self.youtubeVP()
        return self.screen
    def youtubeVP(self):
        self.header = MDLabel(text = "YouTube",
                            pos_hint = {'center_x':.87,'center_y':.9},
                            font_style = "H3")
        self.custom_search = MDRoundFlatButton(text = "custom download playlist or video with link",
                                        pos_hint={'center_x':.7,'center_y':.7},
                                        on_press = self.custom_search_download)
        self.download_search = MDRoundFlatButton(text = "search playlist or video with query",
                                        pos_hint = {'center_x':.2,'center_y':.7},
                                        on_press = self.YouTube_With_Query)
        self.screen.add_widget(self.header)
        self.screen.add_widget(self.custom_search)
        self.screen.add_widget(self.download_search)
    def custom_search_download(self,args):
        self.button_videos = MDRoundFlatButton(text = "download videos",
                                            pos_hint = {'center_x':.5,'center_y':.5},
                                            on_press = self.custom_videos_downloader)
        self.button_playlists = MDRoundFlatButton(text = "download playlists",
                                                pos_hint = {'center_x':.5,'center_y':.35},
                                                on_press = self.custom_playlist_download)
        self.return_back_custon = MDRoundFlatButton(text = "<= return back",
                                        pos_hint = {'center_x':.5,'center_y':.2},
                                        on_press = self.return_back_down)

        self.screen.add_widget(self.button_videos)
        self.screen.add_widget(self.button_playlists)
        self.screen.add_widget(self.return_back_custon)
    def return_back_down(self,*args):
        self.screen.clear_widgets()
        self.custom_search.disabled = False
        self.download_search.disabled = False
        self.screen.add_widget(self.header)
        self.screen.add_widget(self.custom_search)
        self.screen.add_widget(self.download_search)
    def custom_videos_downloader(self,args):
        self.return_back_custon = MDRoundFlatButton(text = "<= return back",
                                        pos_hint = {'center_x':.5,'center_y':.07},
                                        on_press = self.return_back_down)
        self.screen.clear_widgets()
        self.screen.add_widget(self.header)
        self.screen.add_widget(self.custom_search)
        self.screen.add_widget(self.download_search)
        self.input_data = Builder.load_string(YouTube_Videos_Down)
        self.submit_data = MDRoundFlatButton(text = "download now!",
                                                pos_hint = {'center_x':.5,'center_y':.4},
                                                on_press = self.download_videos_with_url)
        
        self.screen.add_widget(self.return_back_custon)
        self.screen.add_widget(self.input_data)
        self.screen.add_widget(self.submit_data)
        self.screen.add_widget(self.data_status)
        self.custom_search.disabled = True
    def custom_playlist_download(self,args):
        self.return_back_custon = MDRoundFlatButton(text = "<= return back",
                                        pos_hint = {'center_x':.5,'center_y':.07},
                                        on_press = self.return_back_down)
        self.screen.clear_widgets()
        self.screen.add_widget(self.header)
        self.screen.add_widget(self.custom_search)
        self.screen.add_widget(self.download_search)
        self.playlists_links_data = Builder.load_string(Plsylists_Videos_Down)
        self.submit_data_playlists = MDRoundFlatButton(text = "download now!",
                                                pos_hint = {'center_x':.5,'center_y':.4},
                                                on_press = self.download_playlist_with_url)
        self.data_status_playlists = MDLabel(text = "status...",
                                    pos_hint = {'center_x':.97,'center_y':.3})
        self.screen.add_widget(self.return_back_custon)
        self.screen.add_widget(self.playlists_links_data)
        self.screen.add_widget(self.submit_data_playlists)
        self.screen.add_widget(self.data_status_playlists)
        self.custom_search.disabled = True
    def download_videos_with_url(self,args):
        def threadung():
            try:
                os.mkdir("output")
            except Exception as error:
                pass
            ydl_opts = {
                        'outtmpl': os.path.join("output\\", '%(title)s-%(id)s.%(ext)s'),
                    }
            video = self.input_data.text
            try:
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    self.data_status.pos_hint = {'center_x':.88,'center_y':.3}
                    self.data_status.text = "Downloading the video."
                    ydl.download([video])
                    self.data_status.text = "Successfully downloaded the video."
            except Exception as error:
                self.data_status.text = "Enter right video link or make sure you are connected."
        threadii = threading.Thread(target=threadung)
        threadii.start()
    def download_playlist_with_url(self,args):
        def startin_threading():
            #https://www.youtube.com/playlist?list=PL9oHIc7p2bTH-HUPV-Yv1mIGRhR5SVwmM playlist_link test
            try:
                os.mkdir("output")
            except Exception as error:
                pass
            ydl_opts = {
                        'outtmpl': os.path.join("output", '%(title)s-%(id)s.%(ext)s'),
                    }
            counter = 1
            try:
                for video in Playlist(self.playlists_links_data.text).video_urls:
                    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        self.data_status_playlists.pos_hint = {'center_x':.88,'center_y':.3}
                        self.data_status_playlists.text = "Downloading the videos in the playlist."
                        ydl.download([video])
                        self.data_status_playlists.text = "Successfully downloaded the {} video.".format(counter)
                        counter+=1
            except Exception as error:
                self.data_status_playlists.text = "Enter right playlist link or make sure you are connected."
        threadii = threading.Thread(target=startin_threading)
        threadii.start()
    
    def return_back_in_video_playlist_new(self):
        self.screen.clear_widgets()
        self.screen.add_widget(self.button_videos)
        self.custom_search.disabled = False
        self.screen.add_widget(self.button_playlists)
        self.screen.add_widget(self.custom_search)
        self.screen.add_widget(self.header)
        self.screen.add_widget(self.download_search)
    def YouTube_With_Query(self,args):
        self.screen.clear_widgets()
        self.screen.add_widget(self.header)
        self.return_back_custon = MDRoundFlatButton(text = "<= return back",
                                        pos_hint = {'center_x':.5,'center_y':.07},
                                        on_press = self.return_back_down)
        self.screen.add_widget(self.custom_search)
        self.screen.add_widget(self.return_back_custon)
        self.label_statsu = MDLabel(text = "status",
                                    pos_hint = {'center_x':.97,'center_y':.23})
        self.screen.add_widget(self.label_statsu)
        self.queryYT_Query = Builder.load_string(Query_YT_DOWN_NEW)
        self.screen.add_widget(self.queryYT_Query)
        self.num_videos_down = Builder.load_string(NumberOf_Videos_YTDOWN)
        self.screen.add_widget(self.num_videos_down)
        self.Number_PLAYLISTS = Builder.load_string(Number_PlayLISTSYT)
        self.screen.add_widget(self.Number_PLAYLISTS)
        self.number_playlists_each = Builder.load_string(NUMBER_videos_ToDown_Each_Playlist)
        self.screen.add_widget(self.number_playlists_each)
        self.screen.add_widget(self.download_search)
        self.button_submit_data_data = MDRoundFlatButton(text = "start Downloading",
                                                            pos_hint = {'center_x':.5,'center_y':.15})
        self.screen.add_widget(self.button_submit_data_data)
        self.custom_search.disabled = True
        self.button_submit_data_data.on_press = self.start_download_YT
        
    def return_query_youtuber_hello(self):
        self.screen.clear_widgets()
        self.screen.add_widget(self.custom_search)
        self.screen.add_widget(self.header)
        self.screen.add_widget(self.download_search)
        self.custom_search.disabled = False
        self.download_search.pos_hint = {'center_x':.2,'center_y':.7}
    def start_download_YT(self):
        try:
            query = self.queryYT_Query.text
            if query != "" and query != "":
                num_videos = int(self.num_videos_down.text)
                num_playlist = int(self.Number_PLAYLISTS.text)
                number_playlists_each_play = int(self.number_playlists_each.text)
                self.label_statsu.text = "starting downloading"
                threadinf_dowmlk = threading.Thread(target=self.run_required_download,args = (query,num_videos,num_playlist,number_playlists_each_play))
                threadinf_dowmlk.start()
                if not threadinf_dowmlk.is_alive:
                    self.label_statsu.text = "successfully, finished downloading."
            else:
                self.label_statsu.text = "Enter Valid Input now."
        except Exception as error:
            self.label_statsu.text = "Enter Valid Input now."
    def run_required_download(self,query,num_v,number_playlists,videosin_eachplaylist):
        all.all_function(query,num_v,number_playlists,videosin_eachplaylist)