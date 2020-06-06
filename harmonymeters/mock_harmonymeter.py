#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .abstract_harmonymeter import AbstractHarmonymeter


class MockHarmonymeter(AbstractHarmonymeter):
    def __init__(self):
        super(MockHarmonymeter, self).__init__()
        self.prev_frequency = None
        self.current_harmony = 0.0

    def next_frequency(self, value):
        if self.prev_frequency is not None and value is not None:
            self.current_harmony += value - self.prev_frequency

        if value is not None:
            self.prev_frequency = value

        return '%.2f' % self.current_harmony
