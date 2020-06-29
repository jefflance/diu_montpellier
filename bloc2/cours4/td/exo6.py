#!/usr/bin/env python3
# -*- coding: utf8 -*-

def hanoi1(n, A, B, C):
    if n == 1:
        print(A, " -> ", B)
    else:
        hanoi1(n-1, A, C, B)
        print(A, " -> ", B)
        hanoi1(n-1, C, B, A)


def hanoi2(n, A, B, C):
    if n == 1:
        move_to(A, B)
    else:
        hanoi2(n-1, A, C, B)
        move_to(A, B)
        hanoi2(n-1, C, B, A)


def move_to(X, Y):
    pass


hanoi1(4, 'A', 'C', 'B')
hanoi2(4, 'A', 'C', 'B')
