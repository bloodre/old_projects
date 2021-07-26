# -*- coding: utf-8 -*-
#
# Script qui sert a creer un build du jeu.

from cx_Freeze import setup, Executable

#On appelle la fonction setup pour creer notre executable.
setup(name = "Simple shoot SFML",
	version = "0.0001",
	description = "Un simple jeu de shoot.",
	executables = [Executable("shooter.py")])
