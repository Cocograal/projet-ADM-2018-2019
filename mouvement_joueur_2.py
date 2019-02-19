# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 18:36:38 2019

@author: willi
"""
import tkinter as tk


class Player_2():
    def __init__(self):
        # Créer le plateau où il y aura les objets dessus
        self.canevas = tk.Canvas(window, height=300, width=300,
                                 background="yellow")
        # La balle qui bougera
        self.ball_2 = self.canevas.create_oval(290, 290, 270, 270, fill="red")
        # On connecte les touches (keyboard, function)
        self.canevas.bind_all("<Left>", self.left)
        self.canevas.bind_all("<Up>", self.up)
        self.canevas.bind_all("<Right>", self.right)
        self.canevas.bind_all("<Down>", self.down)
        self.canevas.pack()
        
    def left(self, event):
        """
        pour aller à gauche
        """
        self.canevas.move(self.ball_2, -3, 0)
        self.canevas.update()

    def up(self, event):
        """
        Pour aller en haut
        """
        self.canevas.move(self.ball_2, 0, -3)
        self.canevas.update()

    def right(self, event):
        """
        Pour aller à droite
        """
        self.canevas.move(self.ball_2, 3, 0)
        self.canevas.update()

    def down(self, event):
        """
        pour aller en bas
        """
        self.canevas.move(self.ball_2, 0, 3)
        self.canevas.update()

window = tk.Tk()
Player_2()
window.mainloop()
