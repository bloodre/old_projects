# -*- coding: utf-8 -*-

import sfml
from math import cos, radians, sin
from spriteAnime import SpriteAnime

class Tir(SpriteAnime):
    def __init__(self, x, y, rotation, vitesse, type_tir, camp, vitesse_anim=0.1):
        """Méthode qui initialise l'objet Tir."""

        self.camp = camp
        # On associera camp = 0 aux tirs du joueur et camp = 1 à ceux des enemis
        self.type_tir = type_tir
        if self.type_tir == "laser":
            image = "images/laser.png"
        elif self.type_tir == "tir_ennemi_ligne0" :
            image = "images/tir_ennemi_ligne0.png"
        elif self.type_tir == "missile":
            pass # Image du missile

        SpriteAnime.__init__(self, [[sfml.Texture.load_from_file(image)]], vitesse_anim)
        self.x, self.y = x, y
        self.rotation = rotation
        self.vitesse = vitesse
        self.taille = 0
        self.delete = False

    def manage(self, liste_ennemis, liste_joueurs, game):
        """Méthode qui gère l'objet Tir."""

        if self.type_tir == "laser" or self.type_tir == "tir_ennemi_ligne0":
            vecteur = (cos(radians(self.rotation)) * self.vitesse, sin(radians(self.rotation)) * self.vitesse)
            self.move(vecteur[0], vecteur[1])
            self.taille = 5

        if self.camp == 0:
            for ennemi in liste_ennemis:
                if self.delete is False and abs(self.x - ennemi.x) + abs(self.y - ennemi.y) < 20:
                    ennemi.get_damage(1)
                    game.point += 1000
                    game.explosions.append(SpriteAnime([[game.texture_explosion_05,
                                                    game.texture_explosion_06]]))
                    game.explosions[-1].x = self.x + self.texture.width / 2 - game.explosions[-1].texture.width / 2
                    game.explosions[-1].y = self.y + self.texture.height / 2 - game.explosions[-1].texture.height / 2
                    self.delete = True

