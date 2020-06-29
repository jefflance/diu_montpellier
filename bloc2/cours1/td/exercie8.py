#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def triBulle(T):
    for i in range(len(T), 0, -1):
        for j in range(0, i):
            if T[j] > T[j+1]:
                T[j], T[j+1] = T[j+1], T[j]
    return T

test = [7, 3, 9, 1, 2, 6, 12]

print(triBulle(test))
