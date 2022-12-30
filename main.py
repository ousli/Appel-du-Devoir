from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.health_bar import HealthBar

import level

app = Ursina()

# window.borderless = True
# window.editor_ui.enabled = True
# window.fullscreen = True


# Entity.default_shader = noise_fog_shader

ground = Entity(model='plane', collider='box', scale=120,
                texture='grass', texture_scale=(10, 10))


# editor_camera = EditorCamera(enabled=False, ignore_paused=True)
player = FirstPersonController(
    model='cube', color=color.orange, origin_y=-.5, speed=8, hp=100,
    health_bar=HealthBar(bar_color=color.lime.tint(-.25),
                         roundness=.5, value=100, show_text=False, show_lines=False))

player.collider = BoxCollider(player, Vec3(0, 1, 0), Vec3(1, 2, 1))
current_level = level.Level(player)
player.x, player.z = current_level.get_player_spawn()
player.look_at(player, axis='left')

gun = Entity(model='models/Gun.obj', parent=camera, position=(.5, -.25, .5),
             rotation=(0, -100, 0), texture="textures/gun.png", on_cooldown=False, nb_balle=8)


# gun.muzzle_flash = Entity(parent=gun, z=1, world_scale=.5,
#                           model='quad', color=color.yellow, enabled=False)

# def loading_screen():
#     screen = Entity(model='quad', color=color.black)

# retry = Button('Retry', on_click=loading_screen, scale=.25)
num_level = Text("Niveau " + str(current_level.get_level()), '', '',
                 True, origin=(5, 17.3), scale_override=1.5)

nb_balle_text = Text(str(gun.nb_balle) + "/8", '', '',
                     True, origin=(14.7, -17.3), scale_override=1.5)


# titre = Text('Niveau ' + str(current_level.get_level())8
#              '', '', True, scale_override=10)


def input(key):
    if key == 'left mouse down':
        shoot()
    if key == 'r' and gun.nb_balle < 8:
        Audio("sounds/SFB-recharge_bullet_02.mp3", True, False)
        invoke(setattr, gun, 'nb_balle', 8, delay=3)
    # if key == 'b':
    #     # EditorCamera()
    #     for e in current_level.get_walls():
    #         destroy(e)
    #     for e in current_level.get_enemies():
    #         destroy(e)
    #     current_level.clear_walls()
    #     current_level.clear_enemies()
    #     current_level.generate_labyrinthe()


def update():
    nb_balle_text.text = str(gun.nb_balle) + "/8"
    num_level.text = "Niveau " + str(current_level.get_level())

    if player.hp <= 0:
        print('Game Over')
        # game_over()
    if player.intersects(current_level.get_entree()).hit:
        current_level.get_porte().enabled = True
        current_level.get_entree().enabled = False
    if player.intersects(current_level.get_sortie()).hit:

        current_level.get_sortie().enabled = False

        for e in current_level.get_walls():
            destroy(e)
        for e in current_level.get_enemies():
            destroy(e)
        current_level.clear_walls()
        current_level.clear_enemies()

        current_level.set_level(current_level.get_level() + 1)

        destroy(Text("Niveau Suivant !", scale_override=1.5), delay=2)

        current_level.generate_labyrinthe()
        player.x, player.z = current_level.get_player_spawn()
        player.look_at(player, axis='left')


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


# pause_handler = Entity(ignore_paused=True, input=pause_input)


sun = DirectionalLight()
sun.look_at(Vec3(1, -1, -1))
# scene.fog_density = .1
# scene.fog_color = color.black
Sky()
app.run()
