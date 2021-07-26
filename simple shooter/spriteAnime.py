# -*- coding: utf-8 -*-
"""Module comprenant la classe SpriteAnime qui permet de créer des sprites animés facilement."""

import sfml

CLOCK = sfml.Clock()

class SpriteAnime(sfml.Sprite):

    def __init__(self, animations, vitesse=0.1):
        """Initialise l'objet. Animations doit être une liste contenant des listes représentant une animation chacune. Ces animations sont
        des suites de textures.
        L'attribut num_anim représente l'indexe de l'animation à jouer."""

        self.animations = animations
        self.num_img = 0
        self.num_anim = 0
        self.timestamp_anim = sfml.Time.as_seconds(CLOCK.elapsed_time)
        self.vitesse_anim = vitesse
        sfml.Sprite.__init__(self, self.animations[0][0])

    def set_anim(self, anim):
        """Pour changer d'animation sans risque de relever une exception "Index out of range" à cause de l'attribut num_img qui ne change pas."""

        if self.num_anim != anim:
            self.num_img = 0
            self.num_anim = anim

    def animation(self):
        """Méthode pour animer l'entité"""

        elapsed_time = sfml.Time.as_seconds(CLOCK.elapsed_time)

        if self.timestamp_anim + self.vitesse_anim < elapsed_time:
            self.set_texture(self.animations[self.num_anim][self.num_img])
            self.num_img += 1
            self.timestamp_anim = elapsed_time
            if self.num_img == len(self.animations[self.num_anim]):
                self.num_img = 0