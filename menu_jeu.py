# -*- coding: utf-8 -*-
"""
Lancer le jeu pour arriver sur le menu
"""

import tkinter as tk
import Jeu_et_collision as jeu
import tank_combat_rules as tcr


class Home():
    def __init__(self, img, root):
        self.menu_canvas = tk.Canvas(root, width=500, height=500)
        self.menu_canvas.pack()
        self.menu_canvas.create_image(250, 250, image=img)
        # Bouton pour demarrer le jeu
        self.buttonStart = tk.Button(root, text="Démarrer le jeu",
                                     command= lambda: self.startGame(root))
        self.startWindow = self.menu_canvas.create_window(10, 100, anchor='nw',
                                                          window=self.buttonStart)
        # Bouton pour arreter le jeu
        self.buttonClose = tk.Button(root, text="Fermer le jeu", command=root.destroy)
        self.closeWindow = self.menu_canvas.create_window(250, 400, window=self.buttonClose)
        # Bouton pour savoir les règles du jeu 
        self.buttonRules = tk.Button(root, text="informations pour jouer",
                                     command=lambda: self.gameRules(root))
        self.rulesWindow = self.menu_canvas.create_window(490, 100, anchor="ne",
                                                          window=self.buttonRules)
    def startGame(self, root):
        """Fonction qui lance le jeu"""
        self.menu_canvas.destroy()
        jeu.SameCanvas(root)

    def gameRules(self, root):
        """Fonction qui ouvre la fenetre des règles"""
        self.menu_canvas.destroy()
        tcr.Rules(root)

def startMenu():
    """Fonction pour lancer le programme"""
    root = tk.Tk()
    root.title("Tank Combat")
    img = tk.PhotoImage(file='tank_combat.gif')
    Home(img, root)
    root.mainloop()


if __name__ == "__main__":
    startMenu()
