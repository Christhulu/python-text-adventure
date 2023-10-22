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
        print(Death.quips[randint(0, len(self.quips)-1)])
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
            about to pull a weapon to blast you. What do you do?
            >shoot!
            >dodge!
            >tell a joke
        """))

        action = input("> ")

        if "shoot" in action:
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

        elif "dodge" in action:
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

        elif "joke" in action:
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


class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
        Laser Weapon Armory Scene:
        The door locked behind you. You've been tricked.
        'Uh, I don't know why you thought I'd just give you free weapons'
        The turrets are armed.
        'If you can guess the code, you can get out, but I'm going on break.
        Sick of this job. I didn't even want to invade planets, I just wanted a spaceship.
        My recruiter lied to me!'
        You know the code is a 3 digit code, because you can see it on the screen.
        What is the code?
        """))
        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 9:
            print("BZZZZED! Incorrect Password.")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""You guessed the correct password
                        Now you can head to the bridge."""))
            return 'the_bridge'
        else:
            print(dedent("""The turrets activated...You didn't make it."""))
            return 'death'

class TheBridge(Scene):

    def enter(self):
        print(dedent("""
        Bridge Scene:
        Will you blow up the bridge so that you are not followed?
        What is your choice?
        >throw the bomb
        >slowly place the bomb
        >something else
        """))

        action = input("> ")

        if "throw" in action:

            print(dedent("""It didn't work!"""))

            return 'death'
        elif "slowly" in action:
            print(dedent("""It worked!"""))

            return 'escape_pod'
        else:
            print("DOES NOT COMPUTE!")
            return "the_bridge"

class EscapePod(Scene):

    def enter(self):
        print(dedent("""
        Escape Pod Scene:
        You have discovered a dark, metallic roam.
        It is cold and damp.
        You notice 5 pods, numbered 1-5.
        Some of them look old, and in various states
        of disrepair. Which do you attempt to take?"""))

        good_pod = randint(1,5)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(dedent(f"""
                  You jump into pod {guess} and hit the eject button.
                  The pod escapes out into the void of space, then
                  implodes as the hull ruptures, crushing you instantly
                  """))
            return 'death'
        else:
            print(dedent(f"""
                  You jump into pod {guess} and hit the eject button.
                  The pod easily slides out into space heading to the
                  planet below. As it flies to the planet, you look
                  back and see your ship implode then explode like a
                  bright star. You won!
                  """))

            return 'finished'

class Finished(Scene):

    def enter(self):
        print("You won! Good job.")
        return 'finished'

class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


#Setup and launch game
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
