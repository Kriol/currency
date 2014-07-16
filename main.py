#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re

RE = re.compile(r'<[tT][dD]>\d?\d.\d?\d.(\d\d)?\d\d.')

with open('data.html', 'rt', encoding='utf-8') as src:
    for line in src:
        print(line)
