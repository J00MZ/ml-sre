#!/usr/bin/env python

import sys

fb = int(sys.argv[1]) + 1

for fizzbuzz in range(1,fb):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz (SreRacha!)")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz (sre)")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz (racha)")
        continue
    print(fizzbuzz)