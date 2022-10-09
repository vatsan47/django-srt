import pysrt
from .db import *
import re

def add_subtitles(name):
    name1 = name+".srt"
    subs = pysrt.open(name1)
    for sub in subs:
        start = str(sub.start)
        end = str(sub.end)
        text = sub.text
        put_item(start, end, text, name)
        print("Done")