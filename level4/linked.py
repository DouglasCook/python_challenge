# -*- coding: utf-8 -*-
"""
URL = http://www.pythonchallenge.com/pc/def/linkedlist.php
"""

import urllib.request

base_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}'

nothing = 12345

for i in range(400):
    # create url
    url = base_url.format(nothing)

    # open url and read into string
    f = urllib.request.urlopen(url)
    page = f.read()
    print(page)

    words = page.split()
    # at divide by two message, need to compare to byte string
    if words[1] == b'Divide':
        nothing = nothing/2
        print('DIVIDING BY TWO!')
    else:
        # taking final word is not best way to do it but works
        nothing = int(words[-1])
