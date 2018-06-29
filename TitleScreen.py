from Scene import *
from roundrects import *
from PAdLib import *
from Config import *
#blue - (49, 167, 255)
#red - (255, 44, 44)
#button red - (255, 65, 34)


# This class represents a Title Screen and inherits from the Scene class. From the title screen you can select different
# game modes and scenes. The other scenes which can be accessed from this scene are the One Player Mode, Two Player Mode
# , as well as the Configuration / Controls screen. Different scenes can be selected using both the mouse as well as the
# arrow keys


class TitleScreen(Scene):
    # Initializes the Title Screen object
    def __init__(self, director):
        # Calls the constructor of the Scene class
        Scene.__init__(self, director)
        #The font and size of the titlefont, the "edibles" text on the title screen
        self.titlefont = pygame.font.Font("fonts\Condition.ttf", 65 * director.scale)
        # The font and size of text used for the buttons
        self.btnfont = pygame.font.Font("fonts\Condition.ttf", 22 * director.scale)
        # The font and size of the text used to write my name is the upper right corner
        self.subfont = pygame.font.Font("fonts\Condition.ttf", 21 * director.scale)
        # Creates a surface on which the specified text is printed using the font specified in this case "titlefont"
        self.text = self.titlefont.render("Edibles", True, (49, 167, 255))
        # This is a rectangle object with the size being the same as the size of the game window size
        self.screen_rect = director.screen.get_rect()
        # The integer representing the currently selected button, "1" being 1P Mode, "2" being 2P Mode, and "3" being
        # the Config / Controls screen
        self.btnnum = 1
        # The rectangle representing the One Player Button
        self.oneplyrbtn = pygame.Rect(self.text.get_rect().centerx, self.text.get_rect().y, 221 * self.director.scale, 45 * self.director.scale)
        # This changes the center of the rectangle
        self.oneplyrbtn.center = (self.screen_rect.centerx, self.screen_rect.centery / 2 + 70 * self.director.scale)
        # The rectangle representing the Two Player Button
        self.twoplyrbtn = pygame.Rect(self.text.get_rect().centerx, self.text.get_rect().y, 221 * self.director.scale, 45 * self.director.scale)
        # This changes the center of the Two Player Button's rectangle
        self.twoplyrbtn.center = (self.screen_rect.centerx, self.screen_rect.centery / 2 + 140 * self.director.scale)
        # This rectangle represents the Configuration / Controls Button
        self.configbtn = pygame.Rect(self.text.get_rect().centerx, self.text.get_rect().y, 221 * self.director.scale, 45 * self.director.scale)
        # This changes the center of the Configuration / Control Button's rectangle
        self.configbtn.center = (self.screen_rect.centerx, self.screen_rect.centery / 2 + 210 * self.director.scale)

        #This creates an Emitter object
        self.emitter = particles.Emitter()
        #This sets the average number of particles being emitted per second
        self.emitter.set_density(100)
        #This sets the angle at which the particles are being emitted as well as the angle of spread of the particles
        self.emitter.set_angle(90, 10.0)
        #This sets the range of speeds that the particles being emitted can have
        self.emitter.set_speed([400.0, 500.0])
        #This sets the range of life (how long the particle can will last on screen before disappearing) in seconds
        self.emitter.set_life([0.3, 0.9])
        # Sets the color of the particles being emitted in rgb format
        self.emitter.set_colors([(255, 255, 0)])
        # This creates a particle system object
        self.particle_system = particles.ParticleSystem()
        # This sets the general acceleration of particles within the particle system
        self.particle_system.set_particle_acceleration([0.0, 500.0])
        # This adds an emitter to the particle system
        self.particle_system.add_emitter(self.emitter, "emitter")

    def on_update(self):
        # The particle system's update method
        self.particle_system.update(1.0 / 60.0)
        # This sets the fps(frames per second) of the game
        self.director.fps = 30

    def on_event(self, event):
        # Grabs the X and Y position of the mouse cursor, respectively
        mx, my = pygame.mouse.get_pos()

        # This conditional statement checks if the Down or S Key have been pressed down. If the selected button's index
        # is 3 it will change the selected button index to 1 so that it will have the appearance of looping over.
        # Otherwise it will simply increment btnnum
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_DOWN or event.key == pygame.K_s):
            if self.btnnum == 3:
                self.btnnum = 1
            else:
                self.btnnum += 1
        # Checks if either the Up or W key have been pressed down.  If the btnnum is 1 it will change btnnum to 3 so
        # it has the appearance in game of looping over. Otherwise, it will decrement btnnum.
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_UP or event.key == pygame.K_w):
            if self.btnnum == 1:
                self.btnnum = 3
            else:
                self.btnnum -= 1
        # Checks is the Enter key has been pressed down and if the highlighted button index is 1, and if so it will
        # change the scene to the second scene in the director's scenes array, the One Player Mode
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_RETURN or event.key == pygame.K_SPACE) and self.btnnum == 1:
            # Loads the song
            pygame.mixer.music.load("music\snakesong.wav")
            # Plays the loaded song indefinitely
            pygame.mixer.music.play(-1)
            self.director.change_scene(self.director.scenes[1])
        # Checks is the Enter key has been pressed down and if the highlighted button index is 2, and if so it will
        # change the scene to the third scene in the director's scenes array, the Two Player Mode
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_RETURN or event.key == pygame.K_SPACE) and self.btnnum == 2:
            # Loads the song
            pygame.mixer.music.load("music\snakesong.wav")
            # Plays the loaded song indefinitely
            pygame.mixer.music.play(-1)
            self.director.change_scene(self.director.scenes[2])
        # Checks is the Enter key has been pressed down and if the highlighted button index is 3, and if so it will
        # change the scene to the fourth scene in the director's scenes array, the Configuration / Controls scene
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_RETURN or event.key == pygame.K_SPACE) and self.btnnum == 3:
            self.director.change_scene(self.director.scenes[3])

        # This checks if the mouse is within the boundaries of the One Player Button's rectangle and if it is it then
        # changes the highlighted button index to 1. If the player clicks the button it will change the scene to the
        # second scene in the director's scene array, the One Player Mode
        if mx > self.oneplyrbtn.left and mx < self.oneplyrbtn.right and my < self.oneplyrbtn.bottom and my > self.oneplyrbtn.top:
            self.btnnum = 1
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                # Loads the song
                pygame.mixer.music.load("music\snakesong.wav")
                # Plays the loaded song indefinitely
                pygame.mixer.music.play(-1)
                self.director.change_scene(self.director.scenes[1])
        # This checks if the mouse is within the boundaries of the Two Player Button's rectangle and if it is it then
        # changes the highlighted button index to 2. If the player clicks the button it will change the scene to the
        # third scene in the director's scene array, the Two Player Mode
        if mx > self.twoplyrbtn.left and mx < self.twoplyrbtn.right and my < self.twoplyrbtn.bottom and my > self.twoplyrbtn.top:
            self.btnnum = 2
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                self.director.change_scene(self.director.scenes[2])
                # Loads the song
                pygame.mixer.music.load("music\snakesong.wav")
                # Plays the loaded song indefinitely
                pygame.mixer.music.play(-1)
        # This checks if the mouse is within the boundaries of the Configuration / Control Button's rectangle and if it is it then
        # changes the highlighted button index to 3. If the player clicks the button it will change the scene to the
        # fourth scene in the director's scene array, the Configuration / Controls scene
        if mx > self.configbtn.left and mx < self.configbtn.right and my < self.configbtn.bottom and my > self.configbtn.top:
            self.btnnum = 3
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                self.director.change_scene(self.director.scenes[3])
        # This sets the position of the emitter to be near the tip of the mouse cursor
        self.emitter.set_position([mx, my - 10])

    def on_draw(self, screen):
        #Fills the screen with black in order to erase all that was printed in the previous frame
        screen.fill((0, 0, 0))

        # A surface with the text "By: Isaiah Poole" is created using the subfont font, the color being set to a red shade
        self.text = self.subfont.render("By: Isaiah Poole", True, (255, 44, 44))
        # The text is printed to the screen with the specified coordinates
        screen.blit(self.text, self.text.get_rect(right=self.screen_rect.right - 6 * self.director.scale, bottom=self.screen_rect.top + 24 * self.director.scale))

        # A surface with the text "By: Isaiah Poole" is created using the subfont font, the color being set to a blue shade
        self.text = self.subfont.render("By: Isaiah Poole", True, (49, 167, 255))
        # The text is printed to the screen with the specified coordinates
        screen.blit(self.text, self.text.get_rect(right=self.screen_rect.right - 7))

        # A surface with the text "By: Isaiah Poole" is created using the titlefont, the color being set to a red shade
        self.text = self.titlefont.render("Edibles", True, (255, 44, 44))
        # The text is printed to the screen with the specified coordinates
        screen.blit(self.text, self.text.get_rect(centerx=self.screen_rect.centerx + 4 * self.director.scale,centery=self.screen_rect.centery / 2 + 4 * self.director.scale))

        # A surface with the text "By: Isaiah Poole" is created using the titlefont, the color being set to a blue shade
        self.text = self.titlefont.render("Edibles", True, (49, 167, 255))
        # The text is printed to the screen with the specified coordinates
        screen.blit(self.text, self.text.get_rect(centerx=self.screen_rect.centerx, centery=self.screen_rect.centery / 2))

        # RedOnePlayerButton
        # This rectangle object stores of the properties of the rectangle and will be used to make a round rectangle
        op = pygame.Rect(self.text.get_rect().centerx, self.text.get_rect().y, 221 * self.director.scale, 45 * self.director.scale)
        # The center of rectangle "op" is changed
        op.center = (self.screen_rect.centerx + 3 * self.director.scale, self.screen_rect.centery / 2 + 73 * self.director.scale)
        # a red rounded rectangle is created using the pre-made rectangle. It is created with a corner radius of 9 and
        # a border width of 5
        round_rect(screen, op, (255, 64, 34), 9, 5)
        # a surface is created and the specified text is drawn onto it using the btn font
        self.text = self.btnfont.render("start one player", True, (255, 44, 44))
        # The text is drawn onto the screen at the specified coordinates
        screen.blit(self.text, self.text.get_rect(centerx=self.screen_rect.centerx, centery=self.screen_rect.centery / 2 + 73 * self.director.scale))

        # BlueOnePlayerButton
        # This rectangle object stores of the properties of the rectangle and will be used to make a round rectangle
        op = pygame.Rect(self.text.get_rect().centerx, self.text.get_rect().y, 221 * self.director.scale, 45 * self.director.scale)
        # The center of rectangle "op" is changed
        op.center = (self.screen_rect.centerx, self.screen_rect.centery / 2 + 70 * self.director.scale)
        # This conditional statement says that if the highlighted button index is 1 then add an extra rgb parameter for
        # the inside color. Otherwise the rounded rectangle will be drawn with a transparent inside
        if self.btnnum == 1:
            round_rect(screen, op, (49, 167, 255), 9, 5, (255, 64, 34, 255))
        else:
            round_rect(screen, op, (49, 167, 255), 9, 5)
        # a surface is created and the specified text is drawn onto it using the btn font
        self.text = self.btnfont.render("start one player", True, (49, 167, 255))
        # The text is drawn onto the screen at the specified coordinates
        screen.blit(self.text, self.text.get_rect(centerx=self.screen_rect.centerx, centery=self.screen_rect.centery / 2 + 70 * self.director.scale))

        # RedTwoPlayerButton
        # This rectangle object stores of the properties of the rectangle and will be used to make a round rectangle
        op = pygame.Rect(self.text.get_rect().centerx, self.text.get_rect().y, 221 * self.director.scale, 45 * self.director.scale)
        # The center of rectangle "op" is changed
        op.center = (self.screen_rect.centerx + 3 * self.director.scale, self.screen_rect.centery / 2 + 143 * self.director.scale)
        # a red rounded rectangle is created using the pre-made rectangle. It is created with a corner radius of 9 and
        # a border width of 5
        round_rect(screen, op, (255, 64, 34), 9, 5)
        # a surface is created and the specified text is drawn onto it using the btn font
        self.text = self.btnfont.render("start two player", True, (255, 44, 44))
        # The text is drawn onto the screen at the specified coordinates
        screen.blit(self.text, self.text.get_rect(centerx=self.screen_rect.centerx, centery=self.screen_rect.centery / 2 + 143 * self.director.scale))

        # BlueTwoPlayerButton
        # This rectangle object stores of the properties of the rectangle and will be used to make a round rectangle
        op = pygame.Rect(self.text.get_rect().centerx, self.text.get_rect().y, 221 * self.director.scale, 45 * self.director.scale)
        # The center of rectangle "op" is changed
        op.center = (self.screen_rect.centerx, self.screen_rect.centery / 2 + 140 * self.director.scale)
        # This conditional statement says that if the highlighted button index is 2 then add an extra rgb parameter for
        # the inside color. Otherwise the rounded rectangle will be drawn with a transparent inside
        if self.btnnum == 2:
            round_rect(screen, op, (49, 167, 255), 9, 5, (255, 64, 34, 255))
        else:
            round_rect(screen, op, (49, 167, 255), 9, 5)
        # a surface is created and the specified text is drawn onto it using the btn font
        self.text = self.btnfont.render("start two player", True, (49, 167, 255))
        # The text is drawn onto the screen at the specified coordinates
        screen.blit(self.text, self.text.get_rect(centerx=self.screen_rect.centerx, centery=self.screen_rect.centery / 2 + 140 * self.director.scale))

        # RedControls
        # This rectangle object stores of the properties of the rectangle and will be used to make a round rectangle
        op = pygame.Rect(self.text.get_rect().centerx, self.text.get_rect().y, 221 * self.director.scale, 45 * self.director.scale)
        # The center of rectangle "op" is changed
        op.center = (self.screen_rect.centerx + 3 * self.director.scale, self.screen_rect.centery / 2 + 213 * self.director.scale)
        # a red rounded rectangle is created using the pre-made rectangle. It is created with a corner radius of 9 and
        # a border width of 5
        round_rect(screen, op, (255, 64, 34), 9, 5)
        # a surface is created and the specified text is drawn onto it using the btn font
        self.text = self.btnfont.render("controls n config", True, (255, 44, 44))
        # The text is drawn onto the screen at the specified coordinates
        screen.blit(self.text, self.text.get_rect(centerx=self.screen_rect.centerx, centery=self.screen_rect.centery / 2 + 213 * self.director.scale))

        # BlueControls
        # This rectangle object stores of the properties of the rectangle and will be used to make a round rectangle
        op = pygame.Rect(self.text.get_rect().centerx, self.text.get_rect().y, 221 * self.director.scale, 45 * self.director.scale)
        # The center of rectangle "op" is changed
        op.center = (self.screen_rect.centerx, self.screen_rect.centery / 2 + 210 * self.director.scale)
        # This conditional statement says that if the highlighted button index is 3 then add an extra rgb parameter for
        # the inside color. Otherwise the rounded rectangle will be drawn with a transparent inside
        if self.btnnum == 3:
            round_rect(screen, op, (49, 167, 255), 9, 5, (255, 64, 34, 255))
        else:
            round_rect(screen, op, (49, 167, 255), 9, 5)
        # a surface is created and the specified text is drawn onto it using the btn font
        self.text = self.btnfont.render("controls n config", True, (49, 167, 255))
        # The text is drawn onto the screen at the specified coordinates
        screen.blit(self.text, self.text.get_rect(centerx=self.screen_rect.centerx, centery=self.screen_rect.centery / 2 + 210 * self.director.scale))

        #Particles stuff
        self.particle_system.draw(screen)
