# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 15:17:51 2019

@author: willi
"""
import tkinter as tk
import time

class Player_1():
    def __init__(self):
        # faire un dictionnaire vide pour pouvoir cliquer sur plusieurs
        # touches en même temps après
        self.continuer_mouvement = {}
        # Créer le plateau où il y aura les objets dessus
        self.canevas = tk.Canvas(window, height=600, width=600,
                                 background="DeepSkyBlue2")
        # La balle qui bougera
        self.ball = self.canevas.create_oval(9, 9, 27, 27, fill="lime Green")
        # On connecte les touches (keyboard, function)
        self.canevas.bind_all("<KeyPress>", self.key_press)
        self.canevas.bind_all("<KeyRelease>", self.key_release)

        self.canevas.bind_all("<space>", self.missile)
        self.canevas.pack()

        # Un bouton pour quitter l'interface
        self.button = tk.Button(window, text="Quitter", command=window.destroy)
        self.button.pack()
    
    def move(self, event):
        """
        Fonction qui fais les mouvements
        """
        if event.keysym == "a":
            if self.canevas.coords(self.ball)[0] > 5:
                self.canevas.move(self.ball, -5, 0)
        elif event.keysym == "w":
            if self.canevas.coords(self.ball)[1] > 5:
                self.canevas.move(self.ball, 0, -5)
        elif event.keysym == "d":
            if self.canevas.coords(self.ball)[2] < 597:
                self.canevas.move(self.ball, 5, 0)
        elif event.keysym == "s":
            if self.canevas.coords(self.ball)[3] < 597:
                self.canevas.move(self.ball, 0, 5)
        self.canevas.update()
        # Le mouvement continu tant que key_release() ne l'arrête pas
        self.continuer_mouvement[event.keysym] = window.after(100, lambda: 
                                                              self.move(event))

    def key_press(self, event):
        """
        Savoir si une touche a été appuyée
        """
        if (event.keysym in ("a", "w", "d", "s") and
            self.continuer_mouvement.get(event.keysym) is None):
            self.move(event)

    def key_release(self, event):
        """
        Pour savoir si une touche appuyée a été relachée
        """
        # Si une touche a été relachée on annule ce qu'elle faisait,
        # donc on annule la direction vers laquelle elle allait
        if (event.keysym in ("a", "w", "d", "s") and
        self.continuer_mouvement.get(event.keysym) is not None):
            window.after_cancel(self.continuer_mouvement[event.keysym])
            self.continuer_mouvement[event.keysym] = None

    def missile(self, event):
        """
        Quand on tire un missile
        """

        self.x_coord1 = self.canevas.coords(self.ball)[0]
        self.x_coord2 = self.canevas.coords(self.ball)[2]
        self.y_coord1 = self.canevas.coords(self.ball)[1]
        self.y_coord2 = self.canevas.coords(self.ball)[3]
        self.projectile = self.canevas.create_oval(self.x_coord1,
                                              self.y_coord1,
                                              self.x_coord2,
                                              self.y_coord2)
        self.missileMovement()
        
    def missileMovement(self):
        self.canevas.move(self.projectile, 0, 5)
        self.temps = window.after(70, self.missileMovement)


window = tk.Tk()
Player_1()
window.mainloop()










