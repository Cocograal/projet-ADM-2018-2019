# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 17:55:53 2019

@author: willi
"""

import tkinter as tk
import Jeu_et_collision as jeu


class Home():
    def __init__(self, img):
        self.menu_canvas = tk.Canvas(root, width=500, height=500)
        self.menu_canvas.pack()
        self.menu_canvas.create_image(250, 250, image=img)
        self.button = tk.Button(root, text="Cliquez ici", command=self.lancerJeu)
        self.button.pack()
    
    def lancerJeu(self):
        window = tk.Tk()
        jeu.SameCanvas(window)
        window.mainloop()
    
root = tk.Tk()
img = tk.PhotoImage(file='tank_combat.gif')
Home(img)
root.mainloop()
