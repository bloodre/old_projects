# -*- coding: utf-8 -*-

import sfml
import re # Nécessaire pour cx_freeze
from random import *
from spriteAnime import SpriteAnime
from joueur import Joueur
from ennemi import Ennemi
from pattern_manager import PatternManager
from bonus import Bonus

class Game:
    """Classe qui permet de créer l'instance du jeu où tout va se passer."""

    # La police de caractères
    font = sfml.Font.load_from_file("8bitlim.ttf")
    font_score = sfml.Font.load_from_file("times.ttf")
    clock = sfml.Clock()

    def __init__(self):
        """Méthode qui sert à initialiser l'objet."""

        # Création de la fenêtre.
        self.window = sfml.RenderWindow(sfml.VideoMode(650, 500), 'Shooter', sfml.Style.CLOSE)
        self.window.mouse_cursor_visible = False
        self.window.framerate_limit = 60

        self.running = True

        # Définition des textures.
        self.texture_fond = sfml.Texture.load_from_file("images/fond.png")

        self.texture_vaisseau_01 = sfml.Texture.load_from_file("images/vaisseau_01.png")
        self.texture_vaisseau_02 = sfml.Texture.load_from_file("images/vaisseau_02.png")

        self.texture_vaisseau_alien_01 = sfml.Texture.load_from_file("images/vaisseau_alien_01.png")
        self.texture_vaisseau_alien_02 = sfml.Texture.load_from_file("images/vaisseau_alien_02.png")
        self.texture_vaisseau_alien_03 = sfml.Texture.load_from_file("images/vaisseau_alien_03.png")
        self.texture_vaisseau_alien_04 = sfml.Texture.load_from_file("images/vaisseau_03.png")

        self.texture_explosion_01 = sfml.Texture.load_from_file("images/explosion1.png")
        self.texture_explosion_02 = sfml.Texture.load_from_file("images/explosion2.png")
        self.texture_explosion_03 = sfml.Texture.load_from_file("images/explosion3.png")
        self.texture_explosion_04 = sfml.Texture.load_from_file("images/explosion4.png")
        self.texture_explosion_05 = sfml.Texture.load_from_file("images/explosion5.png")
        self.texture_explosion_06 = sfml.Texture.load_from_file("images/explosion6.png")

        self.texture_bonus_puissance = sfml.Texture.load_from_file("images/puissance.png")
        self.texture_bonus_points = sfml.Texture.load_from_file("images/point.png")

        # Image de l'HUD :
        self.hud = sfml.Sprite(sfml.Texture.load_from_file("images/HUD.png"))
        self.hud.x = 500

        # Le score
        self.point = 0
        self.score = sfml.Text()
        self.score.font, self.score.character_size, self.score.style, self.score.color, self.score.string = Game.font_score, 16, sfml.Text.REGULAR, sfml.Color(255, 255, 255), str(self.point)
        self.score.x, self.score.y = 570, 8

        # Les différents personnages du jeu.
        self.joueurs = []

		# La liste contenant la liste d'ennemis.
        self.ennemis = []

        # la liste contenant la liste des explosions.
        self.explosions = []

        # La liste des bonus.
        self.bonus = []

        # Le sprite de fond.
        self.fonds = [sfml.Sprite(self.texture_fond), sfml.Sprite(self.texture_fond)]

        # La musique
        self.musique = sfml.Music.open_from_file("son/debut.ogg")
        self.stage = sfml.Music.open_from_file("son/stageloop.ogg")
        self.mort_ennemi = sfml.Sound(sfml.SoundBuffer.load_from_file("son/seEnemyExplode01.wav"))
        self.mort_ennemi.volume = 50
        self.get_point = sfml.Sound(sfml.SoundBuffer.load_from_file("son/seGraze.wav"))
        self.get_point.volume = 70

        self.q = 0
        self.b = 0

    def play(self):
        """Méthode qui lance le jeu."""

        # Les actions a effectuer avant de lancer le jeu.
        self.debut_jeu = False
        self.fonds[0].y = -250
        self.fonds[1].y = 250

        self.tirs = []

        self.pattern_manager = PatternManager(self)

        while self.running:
            for event in self.window.iter_events():
                if event.type == sfml.Event.CLOSED:
                    self.running = False
                    self.stop()

            self.manage()
            self.update()

    def start_debut_jeu(self):
        """Démarre la partie."""

        self.debut_jeu = True
        self.text_intro = False
        self.text_intro_2 = False

        self.joueurs = [Joueur(3, 240, 430, [[self.texture_vaisseau_01, self.texture_vaisseau_02]], 0.2)]
        #self.joueurs.append(Joueur(3, 240, 430, [[self.texture_vaisseau_01, self.texture_vaisseau_02]], 0.2))

        self.musique.play()

        self.pattern_manager.reset()


    def manage(self):
        """Méthode qui gère le jeu."""

        # On passe à la musique à looper dès que la musique d'intro est finie (et que le jeu est lancé).
        if self.debut_jeu is True and self.musique.status == 0 and self.stage.status == 0:
            self.stage.play()
            self.stage.loop = True


        # Le clignotemment du texte d'intro.
        if self.debut_jeu is False:
            if int(sfml.Time.as_seconds(Game.clock.elapsed_time) * 2) % 2 == 0:
                self.text_intro = sfml.Text()
                self.text_intro.font, self.text_intro.character_size, self.text_intro.style, self.text_intro.string, self.text_intro.color = Game.font, 40, sfml.Text.REGULAR, "Les aliens arrivent !", sfml.Color(255, 255, 255)
                self.text_intro.x, self.text_intro.y = 65, 220
                self.text_intro_2 = sfml.Text()
                self.text_intro_2.font, self.text_intro_2.character_size, self.text_intro_2.style, self.text_intro_2.string, self.text_intro_2.color = Game.font, 25, sfml.Text.REGULAR, "Appuie sur espace", sfml.Color(255, 255, 255)
                self.text_intro_2.x, self.text_intro_2.y = 150, 360

            else:
                self.text_intro = False
                self.text_intro_2 = False

        # Les commandes
        if self.debut_jeu is False:
            if sfml.Keyboard.is_key_pressed(sfml.Keyboard.SPACE):
                self.start_debut_jeu()

        if self.debut_jeu:
            self.pattern_manager.manage()



        # Déplacement du vaisseau
        if sfml.Keyboard.is_key_pressed(sfml.Keyboard.LEFT):
                self.joueurs[0].move(0)
        if sfml.Keyboard.is_key_pressed(sfml.Keyboard.RIGHT):
                self.joueurs[0].move(1)
        if sfml.Keyboard.is_key_pressed(sfml.Keyboard.DOWN):
                self.joueurs[0].move(2)
        if sfml.Keyboard.is_key_pressed(sfml.Keyboard.UP):
            self.joueurs[0].move(3)

        # Tir du vaisseau
        if sfml.Keyboard.is_key_pressed(sfml.Keyboard.W):
                self.joueurs[0].shoot(self.tirs, "laser")

        # Mode concentré pour le vaisseau.
        if sfml.Keyboard.is_key_pressed(sfml.Keyboard.L_SHIFT):
                self.joueurs[0].focus = 3
        else:
                self.joueurs[0].focus = 1

        if len(self.joueurs) > 1:
        # Déplacement du vaisseau 2
         if sfml.Keyboard.is_key_pressed(sfml.Keyboard.Q):
            self.joueurs[1].move(0)
        if sfml.Keyboard.is_key_pressed(sfml.Keyboard.D):
                    self.joueurs[1].move(1)
        if sfml.Keyboard.is_key_pressed(sfml.Keyboard.S):
                    self.joueurs[1].move(2)
        if sfml.Keyboard.is_key_pressed(sfml.Keyboard.Z):
                    self.joueurs[1].move(3)

        # Tir du vaisseau 2
        if sfml.Keyboard.is_key_pressed(sfml.Keyboard.SPACE):
            self.joueurs[1].shoot(self.tirs, "laser")

        # Mode concentré pour le vaisseau 2.
        if sfml.Keyboard.is_key_pressed(sfml.Keyboard.L_SHIFT):
            self.joueurs[1].focus = 3
        else:
            self.joueurs[1].focus = 1

        # La gestion individuelle des tirs.
        i = 0
        for tir in self.tirs:
            tir.manage(self.ennemis,self.joueurs, game)
            if tir.y < 0 or tir.y > 600 or tir.x < -10 or tir.x > 600 or tir.delete:
                del self.tirs[i]
                i -= 1
            if ((self.joueurs[0].x - tir.x)**2 +(self.joueurs[0].y - tir.y)**2)**0.5 < tir.taille:
                del self.tir[i]
                i -= 1
            i += 1

        # La gestion des bonus lachés lorsque les ennemis sont tués:
        i = 0
        for bonus in self.bonus:
            bonus.manage(self.joueurs, self)
            if self.bonus[i].delete == True:
                self.get_point.play()
                del self.bonus[i]
                i -= 1
            i += 1


        # Le déplacement du fond.
        for fond in self.fonds:
            fond.y += 5

            if fond.y >= 500:
                fond.y = -500

        # Les joueurs :
        for joueur in self.joueurs:
            joueur.manage()

		# Les ennemis :
        i = 0
        random = 0
        rotation = 0
        for ennemi in self.ennemis:
            ennemi.manage()
            if ennemi.creve == 1:
                del self.ennemis[i]
                i -= 1
            if ennemi.vies <= 0:
                self.explosions.append(SpriteAnime([[self.texture_explosion_01,
                                                self.texture_explosion_02,
                                                self.texture_explosion_03,
                                                self.texture_explosion_04,
                                                self.texture_explosion_05,
                                                self.texture_explosion_06]]))
                self.explosions[-1].x = ennemi.x + ennemi.texture.width / 2 - self.explosions[-1].texture.width / 2
                self.explosions[-1].y = ennemi.y + ennemi.texture.height / 2 - self.explosions[-1].texture.height / 2

                self.point += ennemi.point
                random = randint(0,3)
                if random == 0:
                    self.bonus.append(Bonus(ennemi.x, ennemi.y, "puissance", 1, sfml.Time.as_seconds(game.clock.elapsed_time), self.texture_bonus_puissance))
                if random != 0:
                    self.bonus.append(Bonus(ennemi.x, ennemi.y, "point", 50000, sfml.Time.as_seconds(game.clock.elapsed_time), self.texture_bonus_points))

                self.mort_ennemi.play()

                del self.ennemis[i]
                i -= 1


            if ennemi.x > 0 and ennemi.x < 600 and ennemi.y > 0 and ennemi.y < 500:
                self.ennemis[i].shoot(self.tirs, self.joueurs)



            i +=1


        # On anime les explosions :
        i = 0
        for explosion in self.explosions:
            if explosion.num_img == len(explosion.animations[explosion.num_anim]) - 1:
                del self.explosions[i]
                i -= 1
            else:
                explosion.animation()
            i += 1



    def update(self):
        """Méthode qui met à jour l'écran."""

        # On efface tout avec un fond noir dans notre cas.
        self.window.clear(sfml.Color.BLACK)

        # On affiche les sprites
        for fond in self.fonds:
            self.window.draw(fond)

        # On affiche le texte de l'intro (si il ne veut pas False)
        if self.text_intro:
            self.window.draw(self.text_intro)
        if self.text_intro_2:
            self.window.draw(self.text_intro_2)

        # On affiche les vaisseaux :
        for joueur in self.joueurs:
            self.window.draw(joueur)

        # On affiche les ennemis :
        for ennemi in self.ennemis:
            self.window.draw(ennemi)

        # On affiche les bonus:
        for bonus in self.bonus:
            self.window.draw(bonus)

        # On affiche les tirs.
        for tir  in self.tirs:
            self.window.draw(tir)

        for explosion in self.explosions:
            self.window.draw(explosion)

        # On affiche le HUD
        self.window.draw(self.hud)

        # On affiche le score
        if self.debut_jeu:
            self.point += (5/3)
        self.score.string = str(int(self.point))
        self.window.draw(self.score)

        # On rafraichi l'écran.
        self.window.display()

    def stop(self):
        """Méthode qui met fin au jeu."""

        pass

if __name__ == "__main__":
    game = Game()
    game.play()

    exit()
