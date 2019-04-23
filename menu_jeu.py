# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 17:55:53 2019

@author: willi
"""

import tkinter as tk
import Jeu_et_collision as jeu


class Home():
    def __init__(self, img, root):
        self.menu_canvas = tk.Canvas(root, width=500, height=500)
        self.menu_canvas.pack()
        self.menu_canvas.create_image(250, 250, image=img)
        self.button = tk.Button(root, text="Démarrer le jeu", command= lambda: self.lancerJeu(root))
        self.button_window = self.menu_canvas.create_window(10, 100, anchor='nw', window=self.button) 

    def lancerJeu(self, root):
        self.menu_canvas.destroy()
        jeu.SameCanvas(root)

def lancer_menu():
    root = tk.Tk()
    img = tk.PhotoImage(file='tank_combat.gif')
    Home(img, root)
    root.mainloop()


if __name__ == "__main__":
    lancer_menu()
