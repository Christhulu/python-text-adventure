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

#Death is just a scene, that's pretty funny
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

class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
            The Gothons of Planet Percal #25 have invaded your ship and
            destroyed your entire crew. You are the last surviving
            member and your last mission is to get the neutron destruct
            bomb from the Weapons Armory, put it in the bridge, and
            blow the ship up after getting into an escape pod.

            You're running down the central corridor to the Weapons
            Armory when a gothon jumps out, red scaly skin, dark grimy
            teeth, and an evil clown costume flowing around his hate
            filled body. He's blocking the door to the Armory and
            about to pull a weapon to blast you.
        """))

        action = input("> ")

        if action == "shoot!":
            print(dedent("""
                  Quick on the draw, you yank out your blaster and fire
                  it at the Gothon. His clown costume is flowing and
                  moving around his body, which throws off your aim.
                  Your laser hits his costume but misses him entirely.
                  This completely ruins his brand new costume his mother
                  bought him, which makes him fly into an insane rage.
                  'Why would you do that? This was handmade. Who raised you?'
                  You have been shamed to death.
                  """))
            return 'death'

        elif action == "dodge!":
            print(dedent("""
                  Like a world class boxer, you dodge, weave, slip, and
                  slide right as the Gothon's blaster cranks a laser
                  past your head. In the middle of your artful dodge
                  your foot slips and you bang your head on the metal wall
                  and pass out. You wake up shortly after to the Gothon
                  nursing you back to health. 'I made you some food'.
                  He then offers you a plate with a mysterious looking dish
                  You taste it...and your throat begins to close up.
                  It has cilantro, and you have that one gene where it
                  tastes like soap and you don't like it. You die of
                  tasting a food that you don't like.
                  """))
            return 'death'

        elif action == "tell a joke":
            print(dedent("""
                  Lucky for you, they made you learn Gothon insults in
                  the academy. You tell the one Gothon joke you know:
                  Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr,
                  fur fvgf nebhaq gur ubhfr. The Gothon stops, tries
                  not to laugh, then bursts out laughing and can't move.
                  While he's laughing, he barely manages to speak
                  'That was a good one, man I hadn't heard that one since
                  I was a little nebhaq. What do you need, bud?'
                  He then lets you into the Weapon Armory, and you listen
                  while he explains what they have on store.
            """))
            return 'laser_weapon_armory'

        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'
