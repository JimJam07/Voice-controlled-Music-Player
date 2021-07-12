import os
from pygame import mixer
import random


class Music:
    """
    a class that deals with all the commands related to music
    """

    def __init__(self):
        self.recog_command = None
        self.playlist = None
        self.currentPlay = None
        self.size = 0

    def get_song_path(self, song):
        if song == "":
            return "/Users/circuit_walker/Desktop/personal_projects/MIC-Filter/song/"
        return "/Users/circuit_walker/Desktop/personal_projects/MIC-Filter/song/" + song

    def play_one_song(self, song_name):
        path = self.get_song_path(song_name)
        if os.path.isfile(path):
            print(True)
            mixer.init()
            mixer.music.load(path)
            mixer.music.play()

    def stop(self):
        mixer.music.pause()

    def resume(self):
        mixer.music.unpause()

    def random_play(self):
        # mixer.music.stop()
        self.recog_command = "random"
        mypath = self.get_song_path("")
        self.playlist = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
        self.currentPlay = 0
        self.size = len(self.playlist)
        random.shuffle(self.playlist)
        for i in range(self.size):
            self.playlist[i] = mypath + self.playlist[i]
        print(self.playlist)
        mixer.init()
        mixer.music.load(self.playlist[0])
        mixer.music.play()
        self.queue()

    def random_next(self):
        if self.recog_command == "random" and self.currentPlay < self.size-1:
            mixer.music.stop()
            self.currentPlay += 1
            mixer.music.load((self.playlist[self.currentPlay]))
            mixer.music.play()

    def random_prev(self):
        if self.recog_command == "random" and self.currentPlay != 0:
            self.currentPlay -= 1
            mixer.music.load(self.playlist[self.currentPlay])
            mixer.music.play()

    def queue(self):
        """
        implementation of queue structure in music player
        :return:
        """
        print(mixer.music.get_pos())

    def volume_controls(self,type, volume):
        """

        :param type: str (i/d)
        :param volume: int
        :return: None
        """
        if type == "i":
            mixer.music.set_volume(mixer.music.get_volume()+0.1)