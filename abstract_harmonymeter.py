#!/usr/bin/env python3
# -*- coding: utf-8 -*-


FREQUENCIES = {
    'C4': 261.626,
    'Cs4': 277.183,
    'D4': 293.665,
    'Ds4': 311.127,
    'E4': 329.628,
    'F4': 349.228,
    'Fs4': 369.994,
    'G4': 391.995,
    'Gs4': 415.305,
    'A4': 440.000,
    'As4': 466.164,
    'B4': 493.883,
    'C5': 523.251,
    'Cs5': 554.365,
    'D5': 587.330,
    'Ds5': 622.254,
    'E5': 659.255
}


class AbstractHarmonymeter(object):
    def __init__(self):
        super(AbstractHarmonymeter, self).__init__()

    def get_frequency(self, note):
        return FREQUENCIES.get(note)

    def next_note(self, value):
        return self.next_frequency(FREQUENCIES.get(value))

    def next_frequency(self, value):
        return None
