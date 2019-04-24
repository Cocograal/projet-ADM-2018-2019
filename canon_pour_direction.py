"""
Canon pour la direction des balles
"""


def gun(canvas, ball, color):
    """
    le canon
    """
    ball_third = canvas.coords(ball)[0] + 6
    ball_two_third = canvas.coords(ball)[0] + 12
    ball_minus_third = canvas.coords(ball)[3] - 6
    ball_thirdy = canvas.coords(ball)[1] - 6
    cannon = canvas.create_rectangle(ball_third,
                                    ball_minus_third,
                                    ball_two_third,
                                    ball_thirdy,
                                    fill=color,
                                    outline=color)
    return cannon


def rotation(canvas, ball, cannon, index, color):
    """
    La rotation du canon quand on appuie sur la touche q ou l
    """
    # Le tier de la balle
    ball_thirdx = canvas.coords(ball)[0] + 6
    ball_thirdy = canvas.coords(ball)[1] + 6

    # Les deux tiers de la balle
    ball_two_thirdx = canvas.coords(ball)[0] + 12
    ball_two_thirdy = canvas.coords(ball)[1] + 12

    # Le bout du canon qui dépasse de la balle
    right_cannon = canvas.coords(ball)[0] + 24
    down_cannon = canvas.coords(ball)[1] + 24

    # Le bout du canon qui dépasse de la balle
    left_cannon = canvas.coords(ball)[0] - 6
    up_cannon = canvas.coords(ball)[1] - 6
    # On détruit l'ancien canon
    canvas.delete(cannon)
    # On divise l'index par 4 et on regarde le reste pour savoir
    # la position que doit avoir le canon
    if index % 4 == 3:
        # Vers la droite
        cannon = canvas.create_rectangle(ball_thirdx,
                                        ball_thirdy,
                                        right_cannon,
                                        ball_two_thirdy,
                                        fill=color,
                                        outline=color)
    elif index % 4 == 2:
        # Vers le bas
        cannon = canvas.create_rectangle(ball_thirdx,
                                        ball_thirdy,
                                        ball_two_thirdx,
                                        down_cannon,
                                        fill=color,
                                        outline=color)
    elif index % 4 == 1:
        # Vers la gauche
        cannon = canvas.create_rectangle(left_cannon,
                                        ball_thirdy,
                                        ball_two_thirdx,
                                        ball_two_thirdy,
                                        fill=color,
                                        outline=color)
    else:
        # Vers le haut
        cannon = canvas.create_rectangle(ball_thirdx,
                                        up_cannon,
                                        ball_two_thirdx,
                                        ball_two_thirdy,
                                        fill=color,
                                        outline=color)

    return cannon
