from ursina import *
from random import randint
from ursina.shaders import basic_lighting_shader
import labyrinthe
import ennemy


class Level:
    def __init__(self, player):
        """
        La fonction __init__ est un constructeur qui initialise les attributs de la classe Labyrinthe

        :param player: L'objet joueur
        """
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
        """
        Il génère un labyrinthe, puis il place des ennemis et des murs dans le labyrinthe
        """
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
                    if self._level < 20:
                        la_proba_quil_y_est_un_ennemis = randint(0, 10)
                    elif self._level < 40:
                        la_proba_quil_y_est_un_ennemis = randint(0, 5)
                    else:
                        la_proba_quil_y_est_un_ennemis = randint(0, 2)
                    if la_proba_quil_y_est_un_ennemis == 2:
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
        """
        La fonction get_sortie() renvoie la valeur de l'attribut _sortie
        :return: La valeur de l'attribut _sortie
        """
        return self._sortie

    def get_entree(self):
        """
        La fonction get_entree() renvoie la valeur de la variable privée _entree
        :return: L'entrée
        """
        return self._entree

    def get_porte(self):
        """
        Il renvoie la valeur de l'attribut _porte.
        :return: La porte du chien.
        """
        return self._porte

    def get_walls(self):
        """
        Cette fonction renvoie les murs du labyrinthe
        :return: Les murs du labyrinthe.
        """
        return self._walls

    def get_enemies(self):
        """
        Il renvoie les ennemis du joueur
        :return: La liste des ennemis.
        """
        return self._enemies

    def clear_walls(self):
        """
        Il efface les murs du labyrinthe
        """
        self._walls.clear()

    def clear_enemies(self):
        """
        Il efface la liste des ennemis
        """
        self._enemies.clear()

    def get_player_spawn(self):
        """
        Il renvoie le point d'apparition du joueur
        :return: Le point d'apparition du joueur.
        """
        return self._player_spawn

    def get_level(self):
        """
        Il renvoie le niveau du nœud.
        :return: Le niveau du personnage.
        """
        return self._level

    def set_level(self, level):
        """
        La fonction set_level() prend un paramètre appelé level et définit la valeur de l'attribut
        _level sur la valeur du paramètre level

        :param level: Le niveau de l'enregistreur
        """
        self._level = level

    def get_score(self):
        """
        Il renvoie le score de l'étudiant.
        :return: Le score de l'élève.
        """
        return self._score

    def set_score(self, score):
        """
        La fonction set_score() prend deux paramètres, self et score.

        La fonction définit la valeur de l'attribut _score sur la valeur du paramètre score

        :param score: Le score du joueur
        """
        self._score = score
