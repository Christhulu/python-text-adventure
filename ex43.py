#Imports
from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        #Print out final scene
        current_scene.enter()

class Death(Scene):

    quips = [
        "You died.",
        "That didn't turn out how you wanted.",
        "Game over",
        "Try again?"
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)]
        exit(1)
