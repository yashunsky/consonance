#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk

from threading import Thread
from time import sleep

from player import Player


KEYS = {
    'a': 'C4',
    'w': 'Cs4',
    's': 'D4',
    'e': 'Ds4',
    'd': 'E4',
    'f': 'F4',
    't': 'Fs4',
    'g': 'G4',
    'y': 'Gs4',
    'h': 'A4',
    'u': 'As4',
    'j': 'B4',
    'k': 'C5',
    'o': 'Cs5',
    'l': 'D5',
    'p': 'Ds5',
    ';': 'E5'
}


class Display(object):
    def __init__(self):
        super(Display, self).__init__()

        self.window = tk.Tk()
        self.window.bind("<Key>", self.on_key)
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.player = Player()
        self.music = Thread(target=self.music_thread)

        self.music.start()

    def on_closing(self):
        self.player.stop()
        sleep(0.1)
        self.window.destroy()

    def music_thread(self):
        self.player.play()

    def on_key(self, event):
        tone = KEYS.get(event.char)
        print(tone)
        if tone is not None:
            self.player.enqueue(('left', tone))

if __name__ == '__main__':
    display = Display()
    tk.mainloop()
