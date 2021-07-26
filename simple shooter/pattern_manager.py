# -*- coding: utf-8 -*-

import sfml
from joueur import Joueur
from ennemi import Ennemi


class PatternManager:

    """Classe qui gère la création des ennemis."""

    def __init__(self, game):
        """Initialisation de l'objet."""
        self.game = game
        self.reset()

    def reset(self):
        """Reset la clock."""
        self.clock = sfml.Clock()
        self.etape = 0

    def manage(self):
        """Gestion des patterns."""
        temps_ecoule = sfml.Time.as_seconds(self.clock.elapsed_time)

        if self.etape == 0 and temps_ecoule > 3:
            self.etape = 1

            fonc = [["90",1.39, 0, 0], ["x - 160",1.39, 0, 250], ["140",1.39, 0, 300]]
            self.game.ennemis.append(Ennemi(6, -10, fonc, [[self.game.texture_vaisseau_alien_01, self.game.texture_vaisseau_alien_02]], 5000,0.1 ,"tir_ennemi_ligne0"))
            self.game.ennemis.append(Ennemi(6, -30, fonc, [[self.game.texture_vaisseau_alien_01, self.game.texture_vaisseau_alien_02]], 5000,0.1 ,"tir_ennemi_ligne0"))
            self.game.ennemis.append(Ennemi(6, -50, fonc, [[self.game.texture_vaisseau_alien_01, self.game.texture_vaisseau_alien_02]], 5000,0.1 ,"tir_ennemi_ligne0"))

        elif self.etape == 1 and temps_ecoule > 10:
            self.etape = 2

            fonc = [["40",5, 0, 0], ["-x / 2 + 265",5, 1, 450], ["240",5, 0, 50]]
            self.game.ennemis.append(Ennemi(3, -10, fonc, [[self.game.texture_vaisseau_alien_03, self.game.texture_vaisseau_alien_04]], 15000,0.1 ,"tir_ennemi_ligne0"))
            self.game.ennemis.append(Ennemi(3, -30, fonc, [[self.game.texture_vaisseau_alien_03, self.game.texture_vaisseau_alien_04]], 15000,0.1 ,"tir_ennemi_ligne0"))
            self.game.ennemis.append(Ennemi(3, -50, fonc, [[self.game.texture_vaisseau_alien_03, self.game.texture_vaisseau_alien_04]], 15000,0.1 ,"tir_ennemi_ligne0"))

            # La trajectoire sinusoïdale.
            fonc = [["degrees(sin(x / 20)) + 80",3, 0, 0]]
            self.game.ennemis.append(Ennemi(3, -20, fonc, [[self.game.texture_vaisseau_alien_03, self.game.texture_vaisseau_alien_04]], 7000,0.1 ,"tir_ennemi_ligne0"))
            self.game.ennemis.append(Ennemi(3, -40, fonc, [[self.game.texture_vaisseau_alien_03, self.game.texture_vaisseau_alien_04]], 7000,0.1 ,"tir_ennemi_ligne0"))
            self.game.ennemis.append(Ennemi(3, -60,  fonc, [[self.game.texture_vaisseau_alien_03, self.game.texture_vaisseau_alien_04]], 7000,0.1 ,"tir_ennemi_ligne0"))
            self.game.ennemis.append(Ennemi(3, -80,  fonc, [[self.game.texture_vaisseau_alien_03, self.game.texture_vaisseau_alien_04]], 7000,0.1 ,"tir_ennemi_ligne0"))
            self.game.ennemis.append(Ennemi(3, -100,  fonc, [[self.game.texture_vaisseau_alien_03, self.game.texture_vaisseau_alien_04]], 7000,0.1 ,"tir_ennemi_ligne0"))

        elif self.etape == 2 and temps_ecoule > 15:
            self.etape = 3

            # La trajectoire sinusoïdale.
            fonc = [["degrees(sin(x / 30)) + 130",2, 1, 0]]
            self.game.ennemis.append(Ennemi(6, 520,  fonc, [[self.game.texture_vaisseau_alien_01, self.game.texture_vaisseau_alien_02]], 5000,0.1 ,"tir_ennemi_ligne0"))
            self.game.ennemis.append(Ennemi(6, 540,  fonc, [[self.game.texture_vaisseau_alien_01, self.game.texture_vaisseau_alien_02]], 5000,0.1 ,"tir_ennemi_ligne0"))
            self.game.ennemis.append(Ennemi(6, 560,  fonc, [[self.game.texture_vaisseau_alien_01, self.game.texture_vaisseau_alien_02]], 5000,0.1 ,"tir_ennemi_ligne0"))
            self.game.ennemis.append(Ennemi(6, 580,  fonc, [[self.game.texture_vaisseau_alien_01, self.game.texture_vaisseau_alien_02]], 5000,0.1 ,"tir_ennemi_ligne0"))
            self.game.ennemis.append(Ennemi(6, 600,  fonc, [[self.game.texture_vaisseau_alien_01, self.game.texture_vaisseau_alien_02]], 5000,0.1 ,"tir_ennemi_ligne0"))

        elif self.etape == 3 and temps_ecoule > 20:
            self.etape = 4

            fonc = [["degrees(sin(x / 30)) + 130",2, 1, 0]]
            self.game.ennemis.append(Ennemi(6, 520,  fonc, [[self.game.texture_vaisseau_alien_01, self.game.texture_vaisseau_alien_02]], 5000,0.1 ,"tir_ennemi_ligne0"))
            self.game.ennemis.append(Ennemi(6, 540,  fonc, [[self.game.texture_vaisseau_alien_01, self.game.texture_vaisseau_alien_02]], 5000,0.1 ,"tir_ennemi_ligne0"))
            self.game.ennemis.append(Ennemi(6, 560, fonc, [[self.game.texture_vaisseau_alien_01, self.game.texture_vaisseau_alien_02]], 5000,0.1 ,"tir_ennemi_ligne0"))
            self.game.ennemis.append(Ennemi(6, 580,  fonc, [[self.game.texture_vaisseau_alien_01, self.game.texture_vaisseau_alien_02]], 5000,0.1 ,"tir_ennemi_ligne0"))
            self.game.ennemis.append(Ennemi(6, 600,  fonc, [[self.game.texture_vaisseau_alien_01, self.game.texture_vaisseau_alien_02]], 5000,0.1 ,"tir_ennemi_ligne0"))

            fonc = [["degrees(sin(x / 75)) + 80",2, 0, 0]]
            self.game.ennemis.append(Ennemi(6, -20, fonc, [[self.game.texture_vaisseau_alien_01, self.game.texture_vaisseau_alien_02]], 5000,0.1 ,"tir_ennemi_ligne0"))
            self.game.ennemis.append(Ennemi(6, -40,  fonc, [[self.game.texture_vaisseau_alien_01, self.game.texture_vaisseau_alien_02]], 5000,0.1 ,"tir_ennemi_ligne0"))

        elif self.etape == 4 and temps_ecoule > 25:
            self.etape = 5

            # La trajectoire arrondie bas gauche, vers haut droite
            fonc = [["250 - (x**2 / 500)" ,2, 0, 0]]
            self.game.ennemis.append(Ennemi(6, 0,  fonc, [[self.game.texture_vaisseau_alien_01, self.game.texture_vaisseau_alien_02]], 5000,0.1 ,"tir_ennemi_ligne0"))
            self.game.ennemis.append(Ennemi(6, -20, fonc, [[self.game.texture_vaisseau_alien_01, self.game.texture_vaisseau_alien_02]], 5000,0.1 ,"tir_ennemi_ligne0"))

            # La trajectoire arrondie bas droite vers haut gauche.
            fonc = [["x**2 / 700 + 50" ,2, 1, 0]]
            self.game.ennemis.append(Ennemi(6, 550,  fonc, [[self.game.texture_vaisseau_alien_01, self.game.texture_vaisseau_alien_02]], 5000,0.1 ,"tir_ennemi_ligne0"))
            self.game.ennemis.append(Ennemi(6, 570,  fonc, [[self.game.texture_vaisseau_alien_01, self.game.texture_vaisseau_alien_02]], 5000,0.1 ,"tir_ennemi_ligne0"))

            # La trajectoire droite.
            self.game.ennemis.append(Ennemi(6, -40,  [["80" , 2,0, 0]], [[self.game.texture_vaisseau_alien_01, self.game.texture_vaisseau_alien_02]], 5000,0.1 ,"tir_ennemi_ligne0"))
            self.game.ennemis.append(Ennemi(6, -60,  [["85" , 2,0, 0]], [[self.game.texture_vaisseau_alien_01, self.game.texture_vaisseau_alien_02]], 5000,0.1 ,"tir_ennemi_ligne0"))
            self.game.ennemis.append(Ennemi(6, -80,  [["90" , 2,0, 0]], [[self.game.texture_vaisseau_alien_01, self.game.texture_vaisseau_alien_02]], 5000,0.1 ,"tir_ennemi_ligne0"))
            self.game.ennemis.append(Ennemi(6, -100,  [["95" ,2, 0, 0]], [[self.game.texture_vaisseau_alien_01, self.game.texture_vaisseau_alien_02]], 5000,0.1 ,"tir_ennemi_ligne0"))

        elif self.etape == 5 and temps_ecoule > 30:
            self.etape = 6

            fonc = [["degrees(sin(x / 30)) + 100" ,2, 0, 0], ["degrees(sin(-x / 30)) + 165" ,4, 1, 450], ["107 - (x / 8)" ,1, 0, 50]]
            self.game.ennemis.append(Ennemi(6, 0,  fonc, [[self.game.texture_vaisseau_alien_01, self.game.texture_vaisseau_alien_02]], 5000))
            self.game.ennemis.append(Ennemi(6, -20,  fonc, [[self.game.texture_vaisseau_alien_01, self.game.texture_vaisseau_alien_02]], 5000))
            self.game.ennemis.append(Ennemi(6, -40,  fonc, [[self.game.texture_vaisseau_alien_01, self.game.texture_vaisseau_alien_02]], 5000))
            self.game.ennemis.append(Ennemi(6, -60,  fonc, [[self.game.texture_vaisseau_alien_01, self.game.texture_vaisseau_alien_02]], 5000))
            self.game.ennemis.append(Ennemi(6, -80,  fonc, [[self.game.texture_vaisseau_alien_01, self.game.texture_vaisseau_alien_02]], 5000))
            self.game.ennemis.append(Ennemi(6, -100,  fonc, [[self.game.texture_vaisseau_alien_01, self.game.texture_vaisseau_alien_02]], 5000))
            self.game.ennemis.append(Ennemi(6, -120,  fonc, [[self.game.texture_vaisseau_alien_01, self.game.texture_vaisseau_alien_02]], 5000))
            self.game.ennemis.append(Ennemi(6, -140,  fonc, [[self.game.texture_vaisseau_alien_01, self.game.texture_vaisseau_alien_02]], 5000))
            self.game.ennemis.append(Ennemi(6, -160,  fonc, [[self.game.texture_vaisseau_alien_01, self.game.texture_vaisseau_alien_02]], 5000))
            self.game.ennemis.append(Ennemi(6, -180,  fonc, [[self.game.texture_vaisseau_alien_01, self.game.texture_vaisseau_alien_02]], 5000))
            self.game.ennemis.append(Ennemi(6, -200,  fonc, [[self.game.texture_vaisseau_alien_01, self.game.texture_vaisseau_alien_02]], 5000))
