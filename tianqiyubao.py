# -*- coding: utf-8 -*-
import pyttsx3

engine = pyttsx3.init()
for line in open("av.txt", 'r'):
    print(line, end = '')
    engine.say(line)
engine.runAndWait()
