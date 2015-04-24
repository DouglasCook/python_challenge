# -*- coding: utf-8 -*-
"""
URL = http://www.pythonchallenge.com/pc/def/channel.html
"""

import os

next_one = 90052
id_list = []
fdir = './data/channel/{}.txt'
fpath = fdir.format(next_one)

while True:
    # read from next file
    with open(fpath) as f:
        text = f.read()
        #print(text)
        next_one = text.split()[-1]

        fpath = fdir.format(next_one)
        # if there is no such file then break out of loop
        if not os.path.isfile(fpath):
            break

        # add to list to play around with
        id_list.append(next_one)

print(len(id_list))
print(id_list)
