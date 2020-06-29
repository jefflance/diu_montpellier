#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if len(sys.argv) != 2:
    print('Ce script prend un unique paramètre')
    exit()

n = int(sys.argv[1])
result = 1

for i in range(1, n+1):
    result = result * i

print(result)
