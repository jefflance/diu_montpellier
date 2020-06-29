#!/usr/bin/env python3
# -*- coding: utf8 -*-

def suite(n):
    if n == 0:
        return 4
    if n == 1:
        return 4.25
    else:
        return 108-(815/suite(n-1))+(1500/(suite(n-1)*suite(n-2)))

L=[]

for i in range(30):
    L.append(suite(i))

print(L)
