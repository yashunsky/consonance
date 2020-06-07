#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from bisect import bisect_left
from .abstract_harmonymeter import AbstractHarmonymeter


# based on https://en.wikipedia.org/wiki/Consonance_and_dissonance

# currently not working as expected as
# a cacophony is detected as being harmonic :(

FILENAME = 'harmony.txt'


class EntropyHarmonymeter(AbstractHarmonymeter):
    def __init__(self):
        super(EntropyHarmonymeter, self).__init__()

        path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                            FILENAME)
        with open(path, 'r') as f:
            lines = f.readlines()

        data = [list(map(float, line.split())) for line in lines]

        self.ratio, self.harmony = list(map(list, zip(*data)))

        self.prev_frequency = None
        self.current_harmony = 0.0

    def get_harmony(self, ratio):
        if ratio < self.ratio[0] or ratio > self.ratio[-1]:
            return None

        if ratio > 0.99:
            return None

        index = bisect_left(self.ratio, ratio)
        return self.harmony[index]

    def next_frequency(self, value):
        if self.prev_frequency is not None and value is not None:
            ratio = value / self.prev_frequency
            if ratio > 1:
                ratio = 1 / ratio

            interval_harmony = self.get_harmony(ratio)
            if interval_harmony is not None:
                self.current_harmony += interval_harmony

        if value is not None:
            self.prev_frequency = value

        return '%.2f' % self.current_harmony
