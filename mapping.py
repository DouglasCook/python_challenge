# -*- coding: utf-8 -*-
"""
URL = http://www.pythonchallenge.com/pc/def/map.html
"""


def char_mapping(s):
    """
    Swap each alphabetic character in string by the one two ahead.
    """
    return ' '.join([''.join([chr((ord(c) - 95) % 26 + 97)
                              for c in w if c.isalpha()])
                     for w in s.split()])


if __name__ == '__main__':
    orig = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

    print(char_mapping(orig))
