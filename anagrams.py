#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" anagrams
    Command line interface that accepts a word file and returns a dictionary of
    anagrams for that file.

    Module provides a function find_anagrams which can be used to do the same
    for an arbitrary list of strings.
    My machine is a potato. With a hamster running the cpu
    Put it in comments for submisssion PR
"""
__author__ = "Bryan is fixing this code"

import sys
from collections import defaultdict


def alphabetize(string):

    return "".join(sorted(string))


def find_anagrams(words):
    anagrams = defaultdict(list)

    for word in words:
        alpha_word = alphabetize(word)
        anagrams[alpha_word].append(word)

    return anagrams


if __name__ == "__main__":
    # run find anagrams of first argument
    if len(sys.argv) < 2:
        print("Please specify a word file!")
        sys.exit(1)
    else:
        with open(sys.argv[1], 'r') as handle:
            words = handle.read().split()
            find_anagrams(words)
