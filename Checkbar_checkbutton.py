# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 14:57:29 2019

@author: user
"""

from tkinter import *
import os
from PIL import Image
from PIL import ImageTk

class Checkbar:
    def __init__(self, container, image = None, command = None, i=0, check = False):
        self.i = i
        self.check = check
        self.currentPath = os.getcwd()
        self.image = Image.open(self.currentPath + '\\2.png')
        self.image = ImageTk.PhotoImage(self.image)
        self.bt = Button(container, image = self.image, command = self.ChangeStatus)
        self.bt.pack()
        
    def ChangeStatus(self):
        if self.check:
            self.currentPath = os.getcwd()
            self.image = Image.open(self.currentPath + '\\2.png')
            self.image = ImageTk.PhotoImage(self.image)
            self.bt.configure(image = self.image)
            self.check = False
            lst.remove(self.i)
            
        else:
            self.currentPath = os.getcwd()
            self.image = Image.open(self.currentPath + '\\1.png')
            self.image = ImageTk.PhotoImage(self.image)
            self.bt.configure(image = self.image)
            self.check = True
            lst.append(self.i)