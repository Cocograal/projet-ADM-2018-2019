# -*- coding: utf-8 -*-
"""
création de la balle, des mouvements et des
options que le joueur 2 peut faire
"""
import time
import munition as m
import canon_pour_direction as c


class Player_2():
    def __init__(self, window, canvas):
        # Pour savoir la position que doit avoir le canon
        self.index = 1
        # faire un dictionnaire vide pour pouvoir cliquer sur plusieurs
        # touches en même temps après
        self.continue_movement = {}
        self.color = "magenta"
        # Créer le plateau où il y aura les objets dessus
        self.canvas = canvas
        # La ball2e qui bougera et sa position initiale
        self.ball2 = self.canvas.create_rectangle(491, 291, 509, 309
                                                  , fill=self.color,
                                                  outline=self.color)
        self.ball2_coords = self.canvas.coords(self.ball2)
        # Le canon
        self.cannon = c.gun(self.canvas, self.ball2, self.color)
        # On connecte les touches (keyboard, function)
        self.canvas.bind_all("<Left>",
                             lambda event: self.key_press(window, event))
        self.canvas.bind_all("<KeyRelease-Left>",
                             lambda event: self.key_release(window, event))
        
        self.canvas.bind_all("<Up>",
                             lambda event: self.key_press(window, event))
        self.canvas.bind_all("<KeyRelease-Up>",
                             lambda event: self.key_release(window, event))
        
        self.canvas.bind_all("<Right>",
                             lambda event: self.key_press(window, event))
        self.canvas.bind_all("<KeyRelease-Right>",
                             lambda event: self.key_release(window, event))
        
        self.canvas.bind_all("<Down>",
                             lambda event: self.key_press(window, event))
        self.canvas.bind_all("<KeyRelease - Down>",
                             lambda event: self.key_release(window, event))
        
        self.canvas.bind_all("<p>",
                             lambda event: self.key_press(window, event))
        self.canvas.bind_all("<KeyRelease-p>",
                             lambda event: self.key_release(window, event))

        self.canvas.bind_all("<l>",
                             lambda event: self.key_press(window, event))
        self.canvas.bind_all("<KeyRelease-l>",
                             lambda event: self.key_release(window, event))
        self.canvas.pack()

    def move(self, window, event):
        """
        Fonction qui fais les mouvements
        """
        if event.keysym == "Left":
            if self.ball2_coords[0] > 5:
                self.canvas.move(self.ball2, -5, 0)
                self.canvas.move(self.cannon, -5, 0)
                self.ball_coords()

        elif event.keysym == "Up":
            if self.ball2_coords[1] > 5:
                self.canvas.move(self.ball2, 0, -5)
                self.canvas.move(self.cannon, 0, -5)
                self.ball_coords()

        elif event.keysym == "Right":
            if self.ball2_coords[2] < 597:
                self.canvas.move(self.ball2, 5, 0)
                self.canvas.move(self.cannon, 5, 0)
                self.ball_coords()

        elif event.keysym == "Down":
            if self.ball2_coords[3] < 597:
                self.canvas.move(self.ball2, 0, 5)
                self.canvas.move(self.cannon, 0, 5)
                self.ball_coords()
        self.canvas.update()
        # Le mouvement continu tant que key_release() ne l'arrête pas
        self.continue_movement[event.keysym] = window.after(100, lambda:
                                                    self.move(window, event))

    def key_press(self, window, event):
        """
        Savoir si une touche a été appuyée
        """
        if (event.keysym in ("Left", "Right", "Up", "Down") and
            self.continue_movement.get(event.keysym) is None):
            self.move(window, event)
        elif (event.keysym in ("<p>") and
            self.continue_movement.get(event.keysym) is None):
            # On met un temps pour qu'on ne puisse tirer en permanence
            self.clock_fin = time.clock()
            # Si c'est la première fois que le joueur tire
            # On fait le tire
            try:
                self.clock_final = self.clock_fin - self.clock_depart
            except AttributeError:
                self.clock_final = 0.5
                self.shoot(window, event)
            else:
                # Si le joueur a tiré il y a + d'1 sec
                # il peut retirer
                if self.clock_final >= 0.5:
                    self.shoot(window, event)
        elif event.keysym in ("l"):
            self.cannon = c.rotation(self.canvas, self.ball2, self.cannon,
                                     self.index, self.color)
            self.index += 1

    def key_release(self, window, event):
        """
        Pour savoir si une touche appuyée a été relachée
        """
        # Si une touche a été relachée on annule ce qu'elle faisait,
        # donc on annule la direction vers laquelle elle allait
        if (event.keysym in ("Left", "Right", "Up", "Down") and
            self.continue_movement.get(event.keysym) is not None):
            window.after_cancel(self.continue_movement[event.keysym])
            self.continue_movement[event.keysym] = None
        elif (event.keysym in ("<p>") and
              self.continue_movement.get(event.keysym) is not None):
            window.after_cancel(self.continue_movement[event.keysym])
            self.continue_movement[event.keysym] = None
            # Si le tire s'est passé, on met un temps avant de pouvoir retirer
            if self.clock_final >= 0.5:
                self.clock_depart = time.clock()

    def shoot(self, window, event):
        """
        Quand on tire un missile
        """
        m.Missile(self.canvas, self.ball2, window, self.cannon)
        # Si le joueur maintient la touche pour tirer, il y a un temps
        # entre les deux tires
        self.continue_movement[event.keysym] = window.after(500, lambda:
                                                            self.shoot(window,
                                                                       event))

    def ball_coords(self):
        self.ball2_coords = self.canvas.coords(self.ball2)
