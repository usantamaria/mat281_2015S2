#!/usr/bin/env python
# -*- coding: utf-8 -*-

def greetings(st_1, st_2=None, st_3=None, st_4=None, st_5=None):
    template = "<b>Alumno</b>: {0:30} <b>rol</b>: {1:10}<br>"
    hi  = ""
    hi += template.format(*st_1)
    for st in [st_2, st_3, st_4, st_5]:
        if st is not None and len(st)==2:
            hi += template.format(*st_2)
    ending = "Good luck!"
    return hi + ending
