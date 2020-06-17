#!/usr/bin/env python

import random
import os

LIMIT = 25
FILES = os.listdir(".")

def generate_link(files):
    filenames = random.choices(files, k=random.randrange(0,LIMIT))
    s = "";
    for filename in filenames:
        link = f"[[file:{filename}]]\n"
        s += link
    return s

for file in FILES:
    f = open(os.path.join(".", file), "a")
    f.write(generate_link(FILES))
    f.close()
