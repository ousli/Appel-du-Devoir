from ursina import *
import ennemy
from random import randint
from ursina.shaders import basic_lighting_shader
import labyrinthe


class Level:
    def __init__(self, player):
        self._entree = None
        self._sortie = None
        self._porte = None
        self._walls = []
        self._enemies = []
        self._player = player
        self._player_spawn = None
        self._level = 1
        self._score = 0
        self.generate_labyrinthe()

    def generate_labyrinthe(self):
        map = labyrinthe.Labyrinthe(30, 30)
        for i in range(len(map.get_map())):
            for j in range(len(map.get_map()[i])):
                if map.get_map()[i][j] == 1:
                    self._walls.append(
                        Entity(model='cube', origin_y=-.5, scale=2, texture='brick', texture_scale=(1, 2),
                               x=i*2,
                               z=j*2,
                               collider='box',
                               scale_y=4,
                               color=color.hsv(0, 0, random.uniform(.9, 1)), shader=basic_lighting_shader
                               ))
                if map.get_map()[i][j] == 0:
                    la_proba_quil_y_est_un_ennemis = randint(0, 10)
                    if la_proba_quil_y_est_un_ennemis == 3:
                        self._enemies.append(ennemy.Enemy(
                            player=self._player, difficulty=self._level, x=i*2, z=j*2))
                if map.get_map()[i][j] == 3:
                    self._player_spawn = (i*2-0.5, j*2-0.5)
                    # self._entree = Entity(model='sphere', x=i+1*2, y=-
                    #                       0.37, z=j*2, collider='box', color=color.rgba(255, 255, 255, 50))
                    self._porte = Entity(model='cube', origin_y=-.5, scale=2, texture='brick', texture_scale=(1, 2),
                                         x=i*2-2,
                                         z=j*2,
                                         collider='box',
                                         scale_y=3,
                                         color=color.hsv(0, 0, random.uniform(.9, 1)), shader=basic_lighting_shader)
                    self._walls.append(self._porte)
                if map.get_map()[i][j] == 4:
                    self._sortie = Entity(model='sphere', x=i*2, y=-
                                          0.37, z=j*2, collider='box', color=color.rgba(255, 255, 255, 50))

    def get_sortie(self):
        return self._sortie

    def get_entree(self):
        return self._entree

    def get_porte(self):
        return self._porte

    def get_walls(self):
        return self._walls

    def get_enemies(self):
        return self._enemies

    def clear_walls(self):
        self._walls.clear()

    def clear_enemies(self):
        self._enemies.clear()

    def get_player_spawn(self):
        return self._player_spawn

    def get_level(self):
        return self._level

    def set_level(self, level):
        self._level = level

    def get_score(self):
        return self._score

    def set_score(self, score):
        self._score = score
