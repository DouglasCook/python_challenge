# -*- coding: utf-8 -*-
"""
URL = http://www.pythonchallenge.com/pc/def/channel.html
"""

import os
import zipfile

next_one = 90052
comments = []
fdir = './data/channel/{}.txt'
fpath = fdir.format(next_one)

# open the zip file to access comments
with zipfile.ZipFile('./data/channel.zip', 'r') as zf:

    while True:
        # collect comment for this file
        comments.append(zf.getinfo('{}.txt'.format(next_one)).comment)

        # read from next file
        with open(fpath) as f:
            text = f.read()
            next_one = text.split()[-1]

            fpath = fdir.format(next_one)
            # if there is no such file then break out of loop
            if not os.path.isfile(fpath):
                break

print(''.join(comments))
