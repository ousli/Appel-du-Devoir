from random import randint
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.health_bar import HealthBar
from ursina.shaders import colored_lights_shader
from ursina.shaders import basic_lighting_shader
import labyrinthe

app = Ursina()

# window.borderless = True
# window.editor_ui.enabled = True
# window.fullscreen = True


# Entity.default_shader = noise_fog_shader

ground = Entity(model='plane', collider='box', scale=200,
                texture='grass', texture_scale=(10, 10))


editor_camera = EditorCamera(enabled=False, ignore_paused=True)
player = FirstPersonController(
    model='cube', z=-10, color=color.orange, origin_y=-.5, speed=8, hp=100,
    health_bar=HealthBar(bar_color=color.lime.tint(-.25),
                         roundness=.5, value=100, show_text=False, show_lines=False))
player.collider = BoxCollider(player, Vec3(0, 1, 0), Vec3(1, 2, 1))


# player.

gun = Entity(model='models/Gun.obj', parent=camera, position=(.5, -.25, .5),
             rotation=(0, -100, 0), texture="textures/gun.png", on_cooldown=False, nb_balle=8)
# gun.shader = colored_lights_shader
# camera.shader = basic_lighting_shader


# gun.muzzle_flash = Entity(parent=gun, z=1, world_scale=.5,
#                           model='quad', color=color.yellow, enabled=False)


shootables_parent = Entity()
mouse.traverse_target = shootables_parent


# def loading_screen():
#     screen = Entity(model='quad', color=color.black)


def game_over():
    editor_camera.enabled = not editor_camera.enabled

    player.visible_self = editor_camera.enabled
    player.cursor.enabled = not editor_camera.enabled
    gun.enabled = not editor_camera.enabled
    mouse.locked = not editor_camera.enabled
    editor_camera.position = player.position

    application.paused = editor_camera.enabled
    scene.clear()

    # retry = Button('Retry', on_click=loading_screen, scale=.25)


def pause_input(key):
    if key == 'tab':    # press tab to toggle edit/play mode
        editor_camera.enabled = not editor_camera.enabled

        player.visible_self = editor_camera.enabled
        player.cursor.enabled = not editor_camera.enabled
        gun.enabled = not editor_camera.enabled
        mouse.locked = not editor_camera.enabled
        editor_camera.position = player.position

        application.paused = editor_camera.enabled


class Enemy(Entity):
    def __init__(self, **kwargs):
        super().__init__(parent=shootables_parent, model='models/r2-d2.obj', scale=.015,
                         origin_y=0, texture="textures/R2D2_Diffuse.jpg", collider='box', shader=colored_lights_shader, **kwargs)
        self.health_bar = Entity(
            parent=self, y=175, model='cube', color=color.red, world_scale=(1.5, .1, .1))
        self.max_hp = 100
        self.hp = self.max_hp

    def update(self):
        dist = distance_xz(player.position, self.position)
        if dist > 100:
            return

        self.health_bar.alpha = max(0, self.health_bar.alpha - time.dt)

        self.look_at_2d(player.position, 'y')
        hit_info = raycast(self.world_position + Vec3(0, 1, 0),
                           self.forward, 30, ignore=(self,))
        if hit_info.entity == player:
            if dist > 2:
                self.position += self.forward * time.dt * 50
            else:
                # player.hp -= 10
                invoke(setattr, player, 'hp', player.hp-10, delay=.5)
                player.health_bar.value = player.hp

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


map = labyrinthe.Labyrinthe(30, 30)
nb_balle_text = Text(str(gun.nb_balle) + "/8", '', '',
                     True, origin=(14.7, -17.3), scale_override=1.5)
# print(map.get_map())
enemies = []
walls = []
entree = None
sortie = None
porte = None


def generate_labyrinthe():
    enemies = []
    walls = []
    for i in range(len(map.get_map())):
        for j in range(len(map.get_map()[i])):
            if map.get_map()[i][j] == 1:
                walls.append(
                    Entity(model='cube', origin_y=-.5, scale=2, texture='brick', texture_scale=(1, 2),
                           x=i*2,
                           z=j*2,
                           collider='box',
                           scale_y=3,
                           color=color.hsv(0, 0, random.uniform(.9, 1)), shader=basic_lighting_shader
                           ))
            if map.get_map()[i][j] == 0:
                jkfne = randint(0, 10)
                if jkfne == 3:
                    enemies.append(Enemy(x=i*2, z=j*2))
            if map.get_map()[i][j] == 3:
                entree = Entity(model='sphere', x=i+1*2, y=-
                                0.3, z=j*2, collider='box', color=color.rgba(255, 255, 255, 0))
                porte = Entity(model='cube', origin_y=-.5, scale=2, texture='brick', texture_scale=(1, 2),
                               x=i*2,
                               z=j*2,
                               collider='box',
                               scale_y=3,
                               color=color.hsv(0, 0, random.uniform(.9, 1)), shader=basic_lighting_shader,
                               enabled=False
                               )
                walls.append(porte)
            if map.get_map()[i][j] == 4:
                sortie = Entity(model='cube', x=i+1*2, y=-
                                0.3, z=j*2, collider='box', color=color.rgba(255, 255, 255, 50))
    return walls, enemies, entree, sortie, porte


# Enemy()
# enemies=[Enemy(x=x*4) for x in range(4)]
enemies, walls, entree, sortie, porte = generate_labyrinthe()


def update():
    nb_balle_text.text = str(gun.nb_balle) + "/8"
    if player.hp <= 0:
        print('Game Over')
        game_over()
    if held_keys['left mouse']:
        shoot()
    if player.intersects(entree).hit:
        porte.enabled = True
    if player.intersects(sortie).hit:
        # EditorCamera()
        for e in walls:
            destroy(e)
        for e in enemies:
            destroy(e)
        walls.clear()
        enemies.clear()
        # destroy(entree)
        # destroy(sortie)

    if held_keys['r'] and gun.nb_balle < 8:
        Audio("sounds/SFB-recharge_bullet_02.mp3", True, False)
        invoke(setattr, gun, 'nb_balle', 8, delay=3)


def shoot():
    if not gun.on_cooldown and gun.nb_balle > 0:
        # print('shoot')
        gun.on_cooldown = True
        # gun.muzzle_flash.enabled = True
        Audio("sounds/gun.mp3", True, False)
        # invoke(gun.muzzle_flash.disable, delay=.05)
        invoke(setattr, gun, 'on_cooldown', False, delay=.5)
        gun.nb_balle -= 1
        if mouse.hovered_entity and hasattr(mouse.hovered_entity, 'hp'):
            mouse.hovered_entity.hp -= 20
            mouse.hovered_entity.blink(color.red)


pause_handler = Entity(ignore_paused=True, input=pause_input)


sun = DirectionalLight()
sun.look_at(Vec3(1, -1, -1))
# scene.fog_density = .1
# scene.fog_color = color.black
Sky()
app.run()
