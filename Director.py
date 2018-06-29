import pygame

# This is the main object of the game
# This keeps the game on, updates stuff, and draws to the screen as well


class Director:
    def __init__(self, scenes):
        # Initializes a window for the display with a resolution of 400 by 400. Game can be played at 400x400, 800x800,
        # 1600x1600, etc.
        self.screen = pygame.display.set_mode((800, 800))
        # The scale value of the game. It is obtained by taking the width(could also be height since the window is a
        # square) and and dividing it by 400
        self.scale = int(pygame.display.get_surface().get_width() / 400)
        # Sets the string that will be displayed on the title bar of the window a.k.a. the Game Name
        pygame.display.set_caption("Edibles")
        # Sets the icon that will be displayed on the title bar
        pygame.display.set_icon(pygame.image.load("images\ed.png"))
        # Sets the default font and size of the font
        self.font = pygame.font.Font("fonts\Condition.ttf", 45 * self.scale)
        # Takes the array of scenes given by the scenes parameter and sets it as the scenes the director will use
        self.scenes = scenes
        # The current scene of the game
        self.scene = None
        # The frames per second the game is set at
        self.fps = 15
        # The boolean value determining whether or not the game will end
        self.quit_flag = False
        # The color of the first player's snake
        self.p1color = (41, 237, 41)
        # The color of the second player's snake
        self.p2color = (255, 150, 44)
        # The index of the color in the first player's color array
        self.index_one = 0
        # The index of the color in the second player's color array
        self.index_two = 1
        # An object that keeps track of time
        self.clock = pygame.time.Clock()

    # The Game Loop
    def loop(self):

        while not self.quit_flag:
            time = self.clock.tick(self.fps)

            # Loops through all of the events that have been queued up by the user
            for event in pygame.event.get():
                # Checks to see if the red X button on the title bar was clicked. If so, the quit() method is executed.
                if event.type == pygame.QUIT:
                    self.quit()
                # Checks to see if a key is pressed down and if said key is the escape button. If this is the case then
                # the quit() method is executed
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.quit()

                #Detects the events defined in the current scene and executes the specified code if the parameters are met
                self.scene.on_event(event)

            #Updates the scene by executing the code specified in the current scene's update function
            self.scene.on_update()

            #Draws to the screen whatever was specified in the current scene's draw function
            self.scene.on_draw(self.screen)
            pygame.display.flip()

    # Changes the scene to another one within the scenes array. Takes in a scene from the array as a parameter
    def change_scene(self, scene):
        self.scene = scene

    # Sets the boolean flag signalling the end of the game to be true
    def quit(self):
        self.quit_flag = True
