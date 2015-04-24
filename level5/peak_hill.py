# -*- coding: utf-8 -*-
"""
URL = http://www.pythonchallenge.com/pc/def/peak.html
"""

import pickle

banner = pickle.load(open('./data/banner.p', 'rb'))
print(banner)

for row in banner:
    for col in row:
        print(col[0] * col[1], end='')
    print()
