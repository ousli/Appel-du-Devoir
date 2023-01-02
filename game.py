from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.health_bar import HealthBar

import level

app = Ursina()

# window.borderless = True
# window.editor_ui.enabled = True
# window.fullscreen = True
window.title = "Appel du Devoir"
# window.fps_counter.enabled = False


# Entity.default_shader = noise_fog_shader

ground = Entity(model='plane', collider='box', scale=120,
                texture='grass', texture_scale=(10, 10))


player = FirstPersonController(
    model='cube', color=color.rgba(255, 255, 255, 0), origin_y=-.5, speed=8, hp=100,
    health_bar=HealthBar(bar_color=color.lime.tint(-.25),
                         roundness=.5, value=100, show_text=False, show_lines=False))

player.collider = BoxCollider(player, Vec3(0, 1, 0), Vec3(1, 2, 1))
current_level = level.Level(player)
player.x, player.z = current_level.get_player_spawn()
player.look_at(player, axis='left')

gun = Entity(model='models/Gun.obj', parent=camera, position=(.5, -.25, .5),
             rotation=(0, -100, 0), texture="textures/gun.png", on_cooldown=False, nb_balle=8)


num_level = Text("Niveau : " + str(current_level.get_level()),
                 scale_override=1.5, origin=(0, 0), x=-0.75, y=-0.45)


nb_balle_text = Text(str(gun.nb_balle) + "/8", '', '',
                     True, origin=(14.7, -17.3), scale_override=1.5)


score_text = Text("Score : " + str(current_level.get_score()),
                  scale_override=1, origin=(0, 0), x=0.75, y=0.45)


# titre = Text('Niveau ' + str(current_level.get_level())8
#              '', '', True, scale_override=10)


def input(key):
    if key == 'left mouse down':
        shoot()
    if key == 'r' and gun.nb_balle < 8:
        Audio("sounds/SFB-recharge_bullet_02.mp3", True, False)
        invoke(setattr, gun, 'nb_balle', 8, delay=3)


def update():
    nb_balle_text.text = str(gun.nb_balle) + "/8"
    num_level.text = "Niveau : " + str(current_level.get_level())
    score_text.text = "Score : " + str(current_level.get_score())

    if player.hp <= 0:
        print('Game Over')

    if player.intersects(current_level.get_sortie()).hit:

        current_level.get_sortie().enabled = False

        for e in current_level.get_walls():
            destroy(e)
        for e in current_level.get_enemies():
            destroy(e)
        current_level.clear_walls()
        current_level.clear_enemies()

        current_level.set_level(current_level.get_level() + 1)

        destroy(Text("Niveau Suivant !", scale_override=2, origin=(0, 0)),
                delay=2)

        current_level.generate_labyrinthe()
        player.hp = 100
        player.health_bar.value = player.hp
        current_level.set_score(current_level.get_score()+1000)
        player.x, player.z = current_level.get_player_spawn()
        player.look_at(player, axis='left')


def shoot():
    if not gun.on_cooldown and gun.nb_balle > 0:
        gun.on_cooldown = True
        Audio("sounds/gun.mp3", True, False)
        invoke(setattr, gun, 'on_cooldown', False, delay=.5)
        gun.nb_balle -= 1
        if mouse.hovered_entity and hasattr(mouse.hovered_entity, 'hp'):
            if mouse.hovered_entity.hp - 20 == 0:
                current_level.set_score(current_level.get_score()+100)
            mouse.hovered_entity.hp -= 20
            mouse.hovered_entity.blink(color.red)


sun = DirectionalLight()
sun.look_at(Vec3(1, -1, -1))
# scene.fog_density = .1
# scene.fog_color = color.black
Sky()
app.run()
