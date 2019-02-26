# -*- coding: utf-8 -*-
"""
Dossier qui contient les collisions
pour le jeu
"""

import tkinter as tk
import joueur_1 as j1
import joueur_2 as j2


class SameCanvas():
    def __init__(self):
        self.canvas = tk.Canvas(window, height=600, width=600,
                                background="DeepSkyBlue2")
        self.player1 = j1.Player_1(window, self.canvas)
        self.player2 = j2.Player_2(window, self.canvas)
        self.canvas.pack()
        # Un bouton pour quitter l'interface
        self.button = tk.Button(window, text="Quitter", command=window.destroy)
        self.button.pack()
        self.impact()
        
    def impact(self):
        """
        Voir s'il y a un impacte entre les objets
        """
        self.length_overlapping = len(self.canvas.
                                  find_overlapping(self.player2.ball2_coords[0],
                                                   self.player2.ball2_coords[1],
                                                   self.player2.ball2_coords[2],
                                                   self.player2.ball2_coords[3]))
        self.ball1_coords = self.player1.ball1_coords
        self.ball2_coords = self.player2.ball2_coords
        for coordinate in self.ball1_coords:
            print(coordinate)
            if coordinate in self.ball2_coords:

                print("""Vous êtes entrez les deux en collision et de ce fait,
                      \rvous avez tout les deux perdu.""")
        self.try_impact = window.after(10, self.impact)
    def fin(self):
        """
        Le jeu se termine
        """
        self.canvas.destroy()
        #self.win = tk.Label(window, text="Le joueur {} a gagné".format(self.player1))
window = tk.Tk()
SameCanvas()
window.mainloop()