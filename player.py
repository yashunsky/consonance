#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import vlc
import os

FILE_TEMPLATE = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'samples',
    '{instrument}',
    '{instrument}_{note}_{length}_{volume}.mp3')


class Player(object):
    def __init__(self, notes, instrument, length, volume):
        super(Player, self).__init__()

        self.pathes = {note: FILE_TEMPLATE.format(instrument=instrument,
                                                  note=note,
                                                  length=length,
                                                  volume=volume)
                       for note in notes}

    def play(self, note):
        local_player = vlc.MediaPlayer(self.pathes[note])
        local_player.play()

    def stop(self):
        pass

    def pause(self):
        pass
