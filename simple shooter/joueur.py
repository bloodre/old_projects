# -*- coding: utf-8 -*-

import sfml
from spriteAnime import SpriteAnime
from tir import Tir

clock = sfml.Clock()

class Joueur(SpriteAnime):
    """Classe qui permet de créer un joueur."""
    def __init__(self, vies, x, y, animations, vitesse=0.1):
        """Initialisation de l'objet."""

        SpriteAnime.__init__(self, animations, vitesse)
        self.x, self.y = x, y
        self.vies = 3
        self.focus = 1
        self.puissance = 0
        self.temps_dernier_tir = 0

    def manage(self):
        """Méthode qui gère l'objet personnage."""
        self.animation()

        if self.y > 480:
            self.y = 480
        elif self.y < 0:
            self.y = 0

        if self.x > 490:
            self.x = 490
        elif self.x < 0:
            self.x = 0

    def move(self, direction):
        """Méthode qui gère les déplacements du joueur."""
        if direction == 0:
            self.x -= 5 / self.focus
        if direction == 1:
            self.x += 5 / self.focus
        if direction == 2:
            self.y += 5 / self.focus
        if direction == 3:
            self.y -= 5 / self.focus

    def shoot(self, liste_tirs, type_tir):
        """Méthode qui fait tirer le vaisseau."""
        if sfml.Time.as_seconds(clock.elapsed_time) - self.temps_dernier_tir > 0.1:
            # On ajoute le tir à la liste (liste_tirs qui correspond à self.tirs). On indique la position de l'objet Personnage qui tire pour faire partir le tir du vaisseau.
            # On décale cependant la position x de 5 pixels sur la droite pour qu'il soit créé au milieu de la largeur du vaisseau.
            liste_tirs.append(Tir(self.x + 5, self.y, -90, 15, type_tir,0))
            #Timestamp pour la cadence de tire
            self.temps_dernier_tir = sfml.Time.as_seconds(clock.elapsed_time)
