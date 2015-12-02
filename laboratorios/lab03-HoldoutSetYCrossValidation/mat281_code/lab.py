#!/usr/bin/env python
# -*- coding: utf-8 -*-

def greetings(st_1, st_2):
    template = "<b>Alumno</b>: {0:30} <b>rol</b>: {1:10}<br>"
    hi  = ""
    hi += template.format(*st_1)
    hi += template.format(*st_2)
    ending = "Good luck!"
    return hi + ending
