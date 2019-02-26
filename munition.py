# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 16:16:23 2019

@author: willi
"""

class Missile():
    def __init__(self, canvas, ball, window, cannon):
        self.window = window
        # On attribue le canvas de player_1 pour pouvoir l'utiliser
        # dans cette classe
        self.canvas = canvas
        self.cannon = cannon
        self.right_cannon = canvas.coords(ball)[0] + 24
        self.down_cannon = canvas.coords(ball)[1] + 24
        self.left_cannon = canvas.coords(ball)[0] - 6
        self.up_cannon = canvas.coords(ball)[1] - 6

        # On appelle la fonction self.roquette pour faire les missiles
        self.roquette(ball)
    def roquette(self, ball):
        """
        Création du missile + mouvement
        """
        self.x_coord1 = self.canvas.coords(ball)[0]
        self.y_coord1 = self.canvas.coords(ball)[1]
        self.projectile = self.canvas.create_oval(self.x_coord1 + 6,
                                                   self.y_coord1 + 6,
                                                   self.x_coord1 + 12,
                                                   self.y_coord1 + 12)
        # On appelle la fonction self.missileMovement pour faire le mouvement
        # du missile
        self.positionCannon()

    def positionCannon(self):
        """
        Savoir la position du canon
        """
        if self.canvas.coords(self.cannon)[1] == self.up_cannon:
            self.missileMovementUp()
        elif self.canvas.coords(self.cannon)[0] == self.left_cannon:
            self.missileMovementLeft()
        elif self.canvas.coords(self.cannon)[3] == self.down_cannon:
            self.missileMovementDown()
        elif self.canvas.coords(self.cannon)[2] == self.right_cannon:
            self.missileMovementRight()
    def missileMovementUp(self):
        """
        Mouvement du missile vers le haut
        """
        self.canvas.move(self.projectile, 0, -6)
        self.temps_projectile = self.window.after(70, self.missileMovementUp)
        return self.projectile

    def missileMovementLeft(self):
        """
        Mouvement du missile vers la gauche
        """
        self.canvas.move(self.projectile, -6, 0)
        self.temps_projectile = self.window.after(70, self.missileMovementLeft)
        return self.projectile
    
    def missileMovementDown(self):
        """
        Mouvement du missile vers le bas
        """
        self.canvas.move(self.projectile, 0, 6)
        self.temps_projectile = self.window.after(70, self.missileMovementDown)
        return self.projectile
    
    def missileMovementRight(self):
        """
        Mouvement du missile vers la gauche
        """
        self.canvas.move(self.projectile, 6, 0)
        self.temps_projectile = self.window.after(70, self.missileMovementRight)
        return self.projectile
