#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def bubbleSort(list):
    """
    Tri bulle.

    :param list:
        liste à trier
    :type list:
        list

    :return:
        liste triée
    :rtype:
        list
    """
    l = len(list)
    nouveauCycle = True

    while nouveauCycle:
        nouveauCycle = False
        i = 0

        while i < l-1:
            if list[i] > list[i+1]:
                tmp = list[i]
                list[i] = list[i+1]
                list[i+1] = tmp
                nouveauCycle = True
            i += 1
    
    return list
