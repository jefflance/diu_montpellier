#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

dict1 = {'a': 'y', 'e': 'z'}
dict2 = {}

for key in dict1:
    dict2[key] = dict1[key]
    dict2[dict1[key]] = key

string1 = input("Chaine à traduire : ")
string2 = ""

for char in string1:
    if char in dict2.keys():
       string2 += dict2[char] 
    else:
        string2 += char

print(string2)