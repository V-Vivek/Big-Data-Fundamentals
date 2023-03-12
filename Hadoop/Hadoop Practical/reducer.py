#!/usr/bin/env python

import sys

current_word = None
current_count = 0

# Input: Word and its count
for line in sys.stdin:
    # Strip whitespace and split by tab delimiter
    word, count = line.strip().split('\t')

    # Convert count to int
    count = int(count)

    # If the word is the same as the previous word, increment count
    if word == current_word:
        current_count += count
    else:
        # If the word is different, emit the previous word and its count
        if current_word:
            print("%s\t%s" % (current_word, current_count))
        current_word = word
        current_count = count

# Emit the last word and its count
if current_word:
    print("%s\t%s" % (current_word, current_count))
