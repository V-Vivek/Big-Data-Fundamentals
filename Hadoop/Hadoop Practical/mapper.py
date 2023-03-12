#!/usr/bin/env python

import sys

# Input: A line of text from demo.txt
for line in sys.stdin:
    # Split the line into words
    words = line.strip().split()

    # Emit each word with a count of 1
    for word in words:
        print("%s\t%s" % (word, 1))
