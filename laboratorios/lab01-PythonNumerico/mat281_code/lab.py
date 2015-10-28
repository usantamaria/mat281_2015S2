#!/usr/bin/env python
# -*- coding: utf-8 -*-

def greetings(st_1, st_2):
    template = "<b>Alumno</b>: {0:30} <b>rol</b>: {1:10}<br>"
    hi  = ""
    hi += template.format(*st_1)
    hi += template.format(*st_2)
    warning = "</br>Lea el notebook y comente con su compañero de laboratorio."
    warning = "</br>Este es un laboratorio práctico y de aprendizaje:"
    warning+= "</br>Tome apuntes, intente lo sugerido y pruebe otros cambios."
    ending = "</br></br><b>¡Buena suerte!</b>"
    return hi + warning + ending
