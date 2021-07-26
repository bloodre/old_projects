# -*- coding: utf-8 -*-

import sfml
from joueur import Joueur
from spriteAnime import SpriteAnime

class Bonus(SpriteAnime):

    def __init__(self, x, y, type_bonus, valeur_bonus, temps_apparition, texture, vitesse=0.1):
        SpriteAnime.__init__(self, [[texture]], vitesse)

        self.x, self.y = x, y
        self.valeur_bonus = valeur_bonus
        self.type_bonus = type_bonus
        self.delete = False
        self.y_apparition = y
        self.temps_apparition = temps_apparition

    def manage(self, liste_joueurs, game):
        for joueur in liste_joueurs:
            if abs(self.x - joueur.x) + abs(self.y - joueur.y) < 15:
                self.delete = True
                if self.type_bonus == "point":
                    game.point += self.valeur_bonus
                elif self.type_bonus == "puissance":
                    joueur.puissance += self.valeur_bonus

        if self.y > 520:
            self.delete = True

        # mouvement du bonus
        self.y = (30 * ((sfml.Time.as_seconds(game.clock.elapsed_time) - self.temps_apparition) - 1)**2) - 30 + self.y_apparition
