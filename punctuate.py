#!/usr/bin/env python3

import fileinput
import random
import time
import sys
import argparse


parser = argparse.ArgumentParser(description="random punctuation and capitalization of words")
parser.add_argument("file", metavar="FILE", help="input file or '-' to use standard input")
parser.add_argument("-o", metavar="FILE", help="optional output file")
parser.add_argument("-c", "--capitalize", metavar="\b", default=10, type=int, help="percent chance to capitalize (default: %(default)d)")
parser.add_argument("-p", "--punctuate", metavar="\b", default=10, type=int, help="percent chance to add ending punctuation (default: %(default)d)")
parser.add_argument("-d", "--double-punct", metavar="\b", default=5, type=int, help="percent chance to add surrounding punctuation (default: %(default)d)")
parser.add_argument("-s", "--seed", required=False, help="random seed")

args = parser.parse_args()

random.seed(float(args.seed) if args.seed is not None else time.time())

handle = open(args.o, 'w') if args.o else sys.stdout

for line in fileinput.input(args.file):
    line = line.rstrip()
    if random.randint(0, 99) < args.capitalize:
        line = line.capitalize()
    punct = random.sample(['.', '!', '/', ',', ';', ':'], 1)[0]
    double_punct = random.sample(['""', "''", '()', '{}', '[]', '||'], 1)[0]
    if random.randint(0, 99) < args.double_punct:
        line = double_punct[0] + line + double_punct[1]
    if random.randint(0, 99) < args.punctuate:
        if random.randint(0, 1) == 0:
            line = line + punct
        else:
            line = punct + line
    print(line, file=handle)

handle.close()
