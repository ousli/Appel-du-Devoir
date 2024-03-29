from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.health_bar import HealthBar
from ursina.shaders import lit_with_shadows_shader
import level
import subprocess


app = Ursina()

window.title = "Appel du Devoir"


Entity.default_shader = lit_with_shadows_shader
ground = Entity(model='plane', collider='box', scale=120,
                texture='grass', texture_scale=(10, 10))


# Création d'un objet joueur avec une barre de santé et un collisionneur.
player = FirstPersonController(
    model='cube', color=color.rgba(255, 255, 255, 0), origin_y=-.5, speed=8, hp=100, scale_y=1,
    health_bar=HealthBar(bar_color=color.lime.tint(-.25),
                         roundness=.5, value=100, show_text=False, show_lines=False), collider="box")

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


def restart():
    """
    Il ferme l'application en cours puis en ouvre une nouvelle
    """
    application.quit()
    subprocess.call(['python', 'main.py'])


menu_panel = Panel(scale=(2, 2), enabled=False,
                   color=color.rgba(0, 0, 0, 50))

game_over = Text('GAME OVER !', parent=menu_panel,
                 origin=(0, 0), y=0.1, scale_override=2)
retour_au_mennu = Button(
    'Retour au menu', scale=(0.25, 0.055), parent=menu_panel, on_click=restart)

quit = Button(
    'Quitter', scale=(0.25, 0.055), y=-0.1, parent=menu_panel, on_click=application.quit)


def input(key):
    """
    Lorsque le bouton gauche de la souris est enfoncé, la fonction shoot() est appelée

    :param key: la touche qui a été enfoncée
    """
    if key == 'left mouse down':
        shoot()
    if key == 'r' and gun.nb_balle < 8:
        Audio("sounds/SFB-recharge_bullet_02.mp3", True, False)
        invoke(setattr, gun, 'nb_balle', 8, delay=3)


editor_camera = EditorCamera(enabled=False, ignore_paused=True)


def update():
    """
    Il met à jour le texte des éléments de l'interface utilisateur, vérifie si le joueur est mort, et si
    le joueur est mort, il met le jeu en pause et affiche le menu
    """
    nb_balle_text.text = str(gun.nb_balle) + "/8"
    num_level.text = "Niveau : " + str(current_level.get_level())
    score_text.text = "Score : " + str(current_level.get_score())

    if player.hp <= 0:
        editor_camera.enabled = not editor_camera.enabled
        player.visible_self = editor_camera.enabled
        player.cursor.enabled = not editor_camera.enabled
        gun.enabled = not editor_camera.enabled
        mouse.locked = not editor_camera.enabled
        editor_camera.position = player.position
        application.paused = editor_camera.enabled
        menu_panel.enabled = True

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
    """
    Il tire le pistolet s'il n'est pas en recharge et s'il y a encore des balles dedans
    """
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


# Création d'une lumière directionnelle et réglage de la densité et de la couleur du brouillard.
sun = DirectionalLight()
sun.look_at(Vec3(1, -1, -1))
scene.fog_density = .2
scene.fog_color = color.black
Sky(texture='sky_sunset')
app.run()
