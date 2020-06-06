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
    def __init__(self, harmonymeter):
        super(Display, self).__init__()

        self.window = tk.Tk()
        self.window.bind("<Key>", self.on_key)
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.title('Harmonymeter')
        self.window.geometry('400x100')

        self.harmonymeter = harmonymeter

        self.harmony_value = tk.StringVar()
        self.harmony_lable = tk.Label(self.window,
                                      textvariable=self.harmony_value,
                                      font=('Arial', 100))
        self.harmony_lable.pack()

        self.player = Player()
        self.music = Thread(target=self.music_thread)

        self.music.start()

        self.harmony_value.set('?')

    def on_closing(self):
        self.player.stop()
        sleep(0.1)
        self.window.destroy()

    def music_thread(self):
        self.player.play()

    def on_key(self, event):
        note = KEYS.get(event.char)
        if note is not None:
            self.player.enqueue(('left', note))
            self.harmony_value.set(self.harmonymeter.next_note(note))

if __name__ == '__main__':
    from mock_harmonymeter import MockHarmonymeter
    harmonymeter = MockHarmonymeter()

    display = Display(harmonymeter)
    tk.mainloop()
