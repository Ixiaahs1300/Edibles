# Imports of all the accompanying python files
from Director import *
from EdiblesOnePlayer import *
from EdiblesTwoPlayer import *
from TitleScreen import *
from Config import *

# This is the "main" method of the game
def main():
    # Array of scenes that shall be passed to the director
    scenes = []
    # The "Director" of the game. It takes in the array of scenes and holds most of the "background" data for the game
    dire = Director(scenes)
    # The Scenes of the game. They all take the director object as an argument
    titlescr = TitleScreen(dire)
    onep = EdiblesOnePlayer(dire)
    twop = EdiblesTwoPlayer(dire)
    config = Config(dire)
    # Here the scenes are being appended to the end of the array
    scenes.append(titlescr)
    scenes.append(onep)
    scenes.append(twop)
    scenes.append((config))

    # Changes/Sets the first scene of the game to be the Title Screen.
    dire.change_scene(titlescr)
    # Starts the game loop
    dire.loop()


# This line executes as if it is a main method from most other OOP languages
if __name__ == '__main__':
    # This line initializes all of the python modules
    pygame.init()
    # Calling of the "main" method defined up above
    main()
