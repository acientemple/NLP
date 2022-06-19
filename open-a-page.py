# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import urllib.request
import re
page=urllib.request.urlopen("https://www.scientificamerican.com/article/presidential-debates-have-shockingly-little-effect-on-election-outcomes/")
text=page.read().decode("utf8")
print(text)






