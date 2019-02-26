# -*- coding: utf-8 -*-
"""
création de la balle, des mouvements et des
options que le joueur 2 peut faire
"""
import munition as m
import canon_pour_direction as c


class Player_2():
    def __init__(self, window, canvas):
        # Pour savoir la position que doit avoir le canon
        self.index = 1
        # faire un dictionnaire vide pour pouvoir cliquer sur plusieurs
        # touches en même temps après
        self.continue_movement = {}
        # Créer le plateau où il y aura les objets dessus
        self.canvas = canvas
        # La ball2e qui bougera
        self.ball2 = self.canvas.create_rectangle(299, 299, 317, 317, fill="light green", outline = "light green")
        self.ball2_coords = self.canvas.coords(self.ball2)
        # Le canon
        self.cannon = c.gun(self.canvas, self.ball2)
        # On connecte les touches (keyboard, function)
        self.canvas.bind_all("<Left>", lambda event: self.key_press(window, event))
        self.canvas.bind_all("<KeyRelease-Left>", lambda event: self.key_release(window, event))
        
        self.canvas.bind_all("<Up>", lambda event: self.key_press(window, event))
        self.canvas.bind_all("<KeyRelease-Up>", lambda event: self.key_release(window, event))
        
        self.canvas.bind_all("<Right>", lambda event: self.key_press(window, event))
        self.canvas.bind_all("<KeyRelease-Right>", lambda event: self.key_release(window, event))
        
        self.canvas.bind_all("<Down>", lambda event: self.key_press(window, event))
        self.canvas.bind_all("<KeyRelease - Down>", lambda event: self.key_release(window, event))
        
        self.canvas.bind_all("<p>", lambda event: self.key_press(window, event))
        self.canvas.bind_all("<KeyRelease-p>", lambda event: self.key_release(window, event))

        self.canvas.bind_all("<l>", lambda event: self.key_press(window, event))
        self.canvas.bind_all("<KeyRelease-l>", lambda event: self.key_release(window, event))
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
            self.shoot(window, event)
        elif event.keysym in ("l"):
            self.cannon = c.rotation(self.canvas, self.ball2, self.cannon, self.index)
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
        elif (event.keysym in ("<space>") and
              self.continue_movement.get(event.keysym) is not None):
            window.after_cancel(self.continue_movement[event.keysym])
            self.continue_movement[event.keysym] = None

    def shoot(self, window, event):
        """
        Quand on tire un missile
        """
        m.Missile(self.canvas, self.ball2, window, self.cannon)
        # Si le joueur maintient la touche pour tirer, il y a un temps
        # entre les deux tires
        self.continue_movement[event.keysym] = window.after(1000, lambda:
                                                            self.shoot(window, event))
    def ball_coords(self):
        self.ball2_coords = self.canvas.coords(self.ball2)