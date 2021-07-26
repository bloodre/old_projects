# -*- coding: utf-8 -*-

import sfml
from math import *
from spriteAnime import SpriteAnime
from tir import Tir


clock = sfml.Clock()

class Ennemi(SpriteAnime):
    """Classe qui permet de créer un joueur."""

    def __init__(self, vies, x, functions, animations, point, cadence_tir, type_tir, vitesse_anim=0.1):
        """Initialisation de l'objet."""
        SpriteAnime.__init__(self, animations, vitesse_anim)
        self.cadence = cadence_tir
        self.type_tir = type_tir
        self.x, self.y = x, 0
        self.vies = vies
        self.point = point
        self.creve = 0
        self.functions = functions
        self.func_no = 0
        self.delete = False

        self.son_tir_ennemi0 = sfml.Sound(sfml.SoundBuffer.load_from_file("son/seBomb_MarisaA_Star.wav"))
        self.son_tir_ennemi0.volume = 65


        self.temps_dernier_tir = 0

    def manage(self):
        """Méthode qui gère l'objet personnage."""
        self.animation()
        self.move(self.functions[self.func_no][2], self.functions[self.func_no][1])
        self.move_by_function()

        if self.x > 700 or self.x < -200:
            self.creve = 1

        if len(self.functions) - 1 > self.func_no:
            if (self.functions[self.func_no][2] == 0 and self.x > self.functions[self.func_no + 1][3]) \
            or (self.functions[self.func_no][2] == 1 and self.x < self.functions[self.func_no + 1][3]):
                self.func_no += 1

    def move(self, direction, vitesse):
        """Méthode pour déplacer l'ennemi à gauche ou à droite.
        si direction = 0, aller à droite.
        si direction = 1, aller à gauche.

        """
        if direction == 0:
            self.x += vitesse
        elif direction == 1:
            self.x -= vitesse

    def move_by_function(self):
        """Méthode qui gère les déplacements du joueur."""
        try:
            self.y = eval(self.functions[self.func_no][0].replace("x", str(self.x)))
        except ZeroDivisionError or ValueError:
            pass

    def shoot(self, liste_tirs, liste_joueurs):
        """Méthode qui fait tirer le vaisseau."""
        if sfml.Time.as_seconds(clock.elapsed_time) - self.temps_dernier_tir > self.cadence:

            if self.type_tir == "tir_ennemi_ligne0":
                oppose = self.y - liste_joueurs[0].y
                adjacent = self.x - liste_joueurs[0].x

                if self.x < liste_joueurs[0].x:
                    rotation = degrees(atan(oppose/adjacent))
                if self.x > liste_joueurs[0].x:
                    rotation =  degrees(atan(oppose/adjacent)) - 180
                if adjacent == 0:
                    rotation = 270
                liste_tirs.append(Tir(self.x, self.y, rotation, 15, self.type_tir,1))
                self.son_tir_ennemi0.play()

                self.temps_dernier_tir = sfml.Time.as_seconds(clock.elapsed_time)
            else:
                pass

    def get_damage(self, damage):
        self.vies -= damage

