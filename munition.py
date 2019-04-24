# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 16:16:23 2019

@author: willi
"""
import time


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
        # et décider la direction vers lequel le missile va aller
        self.roquette()

    def roquette(self):
        """
        Savoir la position du canon + creation du missile
        """
        self.x_coord1 = self.canvas.coords(self.cannon)
        if self.canvas.coords(self.cannon)[1] == self.up_cannon:

            self.projectile = self.canvas.create_oval(self.x_coord1[0],
                                                      self.x_coord1[1],
                                                      self.x_coord1[2],
                                                      self.x_coord1[1] - 6)
            
            self.missileMovementUp()
        elif self.canvas.coords(self.cannon)[0] == self.left_cannon:

            self.projectile = self.canvas.create_oval(self.x_coord1[0],
                                                      self.x_coord1[1],
                                                      self.x_coord1[0] - 6,
                                                      self.x_coord1[3])
            self.missileMovementLeft()
        elif self.canvas.coords(self.cannon)[3] == self.down_cannon:
            self.projectile = self.canvas.create_oval(self.x_coord1[0],
                                                      self.x_coord1[3] + 6,
                                                      self.x_coord1[2],
                                                      self.x_coord1[3])
            self.missileMovementDown()
        elif self.canvas.coords(self.cannon)[2] == self.right_cannon:

            self.projectile = self.canvas.create_oval(self.x_coord1[2],
                                                   self.x_coord1[1],
                                                   self.x_coord1[2] + 6,
                                                   self.x_coord1[3])
            self.missileMovementRight()
    def missileMovementUp(self):
        """
        Mouvement du missile vers le haut
        """
        self.canvas.move(self.projectile, 0, -6)
        self.temps_projectile = self.window.after(70, self.missileMovementUp)
        self.projectile_coords = self.canvas.coords(self.projectile)
        
        # On regarde s'il y a des collisions
        # entre les missiles et certains objets
        self.overlap_missile(0, 0, 0, 1)

        return self.projectile

    def missileMovementLeft(self):
        """
        Mouvement du missile vers la gauche
        """
        self.canvas.move(self.projectile, -6, 0)
        
        self.temps_projectile = self.window.after(70, self.missileMovementLeft)
        # On regarde s'il y a des collisions
        # entre les missiles et certains objets
        self.overlap_missile(1, 0, 0, 0)
        return self.projectile
    
    def missileMovementDown(self):
        """
        Mouvement du missile vers le bas
        """
        self.canvas.move(self.projectile, 0, 6)
        self.temps_projectile = self.window.after(70, self.missileMovementDown)
        # On regarde s'il y a des collisions
        # entre les missiles et certains objets
        self.overlap_missile(0, 1, 0, 0)
        return self.projectile
    
    def missileMovementRight(self):
        """
        Mouvement du missile vers la gauche
        """
        self.canvas.move(self.projectile, 6, 0)
        self.temps_projectile = self.window.after(70, self.missileMovementRight)
        # On regarde s'il y a des collisions
        # entre les missiles et certains objets
        self.overlap_missile(0, 0, 1, 0)
        return self.projectile

    def overlap_missile(self, indexleft, indexdown, indexright, indexup):
        """
        Fonction qui regarde si le missile
        entre en collision avec un autre objet
        """
        self.projectile_coords = self.canvas.coords(self.projectile)
        self.overlap_projectile = len(self.canvas.
                                      find_overlapping
                                      (self.projectile_coords[0] - indexleft,
                                       self.projectile_coords[1] + indexdown,
                                       self.projectile_coords[2] + indexright,
                                       self.projectile_coords[3] - indexup))
        if self.overlap_projectile >= 3:
            self.canvas.delete(self.projectile)
            self.window.after_cancel(self.temps_projectile)
