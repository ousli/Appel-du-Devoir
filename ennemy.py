from ursina import *
from ursina.shaders import colored_lights_shader

shootables_parent = Entity()
mouse.traverse_target = shootables_parent


class Enemy(Entity):

    def __init__(self, **kwargs):
        """
        La fonction crée une nouvelle entité, qui est une sous-classe de la classe Entity, et définit le
        parent de l'entité sur l'entité shootables_parent, qui est une sous-classe de la classe Entity
        """
        super().__init__(parent=shootables_parent, model='models/r2-d2.obj', scale=.010,
                         origin_y=0, texture="textures/R2D2_Diffuse.jpg", collider='box', shader=colored_lights_shader, **kwargs)
        self.health_bar = Entity(
            parent=self, y=175, model='cube', color=color.red, world_scale=(1.5, .1, .1))
        self.max_hp = 100
        self.hp = self.max_hp

    def update(self):
        """
        Si le joueur est à moins de 100 unités de l'ennemi, l'ennemi regardera le joueur et si le joueur
        est à moins de 30 unités de l'ennemi, l'ennemi se déplacera vers le joueur. Si le joueur est à
        moins de 2 unités de l'ennemi, l'ennemi infligera 10 dégâts au joueur
        :return: La valeur de retour est le résultat de la dernière expression dans le corps de la
        fonction.
        """
        dist = distance_xz(self.player.position, self.position)
        if dist > 100:
            return

        self.health_bar.alpha = max(0, self.health_bar.alpha - time.dt)

        self.look_at_2d(self.player.position, 'y')
        player_info = raycast(self.world_position + Vec3(0, 1, 0),
                              self.forward, 30, ignore=(self,), traverse_target=self.player)
        if player_info.hit:
            hit_info = raycast(self.world_position + Vec3(0, 1, 0),
                               self.forward, 30, ignore=(self,))
            if hit_info.entity == self.player:
                if dist > 2:
                    self.position += self.forward * \
                        time.dt * (50 + self.difficulty)
                else:
                    invoke(setattr, self.player, 'hp',
                           self.player.hp-10, delay=.8)
                    self.player.health_bar.value = self.player.hp

    @property
    def hp(self):
        """
        La fonction hp() retourne la valeur de la variable _hp
        :return: La valeur de l'attribut hp.
        """
        return self._hp

    @hp.setter
    def hp(self, value):
        """
        Il définit la valeur de la variable _hp sur la valeur de la variable value, et si la valeur de
        la variable value est inférieure ou égale à 0, il détruit l'objet et renvoie

        :param value: La valeur du ch
        :return: La valeur de l'attribut hp.
        """
        self._hp = value
        if value <= 0:
            destroy(self)
            return

        self.health_bar.world_scale_x = self.hp / self.max_hp * 1.5
        self.health_bar.alpha = 1
