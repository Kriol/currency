#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re

RE = re.compile(
    r'''
        <[tT][dD]>
            (\d?\d)\.(\d?\d)\.((?:\d\d)?\d\d)
        </[tT][dD]><[tT][dD]>
            (\d+)
        </[tT][dD]><[tT][dD]>
            (\d+)[,\.](\d\d\d\d)
        </[tT][dD]>
    ''',
    flags=re.VERBOSE)

with open('data.html', 'rt', encoding='utf-8') as src:
    for line in src:
        M = RE.search(line)
        if M:
            day, mon, yea, count, rou, kop = M.groups()
            Date = None
            Count = int(count)
            Course = None
            print(Date, Count, Course)
