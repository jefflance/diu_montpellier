#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

n = int(sys.argv[1])

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

print(fact(n))