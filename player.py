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

        pathes = [FILE_TEMPLATE.format(instrument=instrument,
                                       note=note,
                                       length=length,
                                       volume=volume)
                  for note in notes]

        instance = vlc.Instance('--play-and-pause')
        media_list = instance.media_list_new([instance.media_new_path(path)
                                              for path in pathes])

        self.vlc_player = instance.media_list_player_new()
        self.vlc_player.set_media_list(media_list)

        self.tracks = {note: track_id for (track_id, note) in enumerate(notes)}

    def play(self, note):
        track_id = self.tracks.get(note)
        if track_id is not None:
            self.vlc_player.play_item_at_index(track_id)

    def stop(self):
        self.vlc_player.stop()

    def pause(self):
        self.vlc_player.pause()
