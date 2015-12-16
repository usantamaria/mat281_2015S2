#!/usr/bin/env python
# -*- coding: utf-8 -*-

def greetings(st_1, st_2, st_3=None, st_4=None):
    template = "<b>Alumno</b>: {0:30} <b>rol</b>: {1:10}<br>"
    hi  = ""
    hi += template.format(*st_1)
    hi += template.format(*st_2)
    if st_3:
        hi += template.format(*st_3)
    if st_4:
        hi += template.format(*st_4)
    ending = "Good luck!"
    return hi + ending
