from ursina import *
from ursina.shaders import colored_lights_shader

shootables_parent = Entity()
mouse.traverse_target = shootables_parent


class Enemy(Entity):

    def __init__(self, **kwargs):
        super().__init__(parent=shootables_parent, model='models/r2-d2.obj', scale=.010,
                         origin_y=0, texture="textures/R2D2_Diffuse.jpg", collider='box', shader=colored_lights_shader, **kwargs)
        self.health_bar = Entity(
            parent=self, y=175, model='cube', color=color.red, world_scale=(1.5, .1, .1))
        self.max_hp = 100
        self.hp = self.max_hp

    def update(self):
        dist = distance_xz(self.player.position, self.position)
        if dist > 100:
            return

        self.health_bar.alpha = max(0, self.health_bar.alpha - time.dt)

        self.look_at_2d(self.player.position, 'y')
        hit_info = raycast(self.world_position + Vec3(0, 1, 0),
                           self.forward, 30, ignore=(self,))
        if hit_info.entity == self.player:
            if dist > 2:
                self.position += self.forward * \
                    time.dt * (50 + self.difficulty/3)
            else:
                # player.hp -= 10

                invoke(setattr, self.player, 'hp', self.player.hp-10, delay=.8)
                self.player.health_bar.value = self.player.hp

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = value
        if value <= 0:
            destroy(self)
            return

        self.health_bar.world_scale_x = self.hp / self.max_hp * 1.5
        self.health_bar.alpha = 1
