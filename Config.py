from PAdLib import *
from Scene import *
from PAdLib import rrect
from pygame import gfxdraw
from TitleScreen import *
from EdiblesOnePlayer import *

class Config(Scene):
    def __init__(self, director):
        Scene.__init__(self, director)
        # This is a rectangle object with the size being the same as the size of the game window size
        self.screen_rect = director.screen.get_rect()
        # A list of the names of all the possible colors for the snakes
        self.color_name =["Green", "Orange",  "Purple", "Blue", "Pink", "Yellow", "Rose"]
        # A list of the rgb of all the possible colors for the snakes
        self.color_rgb = [(41, 237, 41), (255, 150, 44), (100, 61, 227), (38, 219, 219), (237, 41, 152), (255, 230, 44), (251, 43, 67)]
        # Points in space for  the occluders
        self.pnts_one = [[103 * self.director.scale, 364 * self.director.scale], [103 * self.director.scale, 370 * self.director.scale], [163 * self.director.scale, 370 * self.director.scale], [163 * self.director.scale, 364 * self.director.scale]]
        self.pnts_two = [[97 * self.director.scale, 304 * self.director.scale], [97 * self.director.scale, 370 * self.director.scale], [104 * self.director.scale, 370 * self.director.scale], [104 * self.director.scale, 304 * self.director.scale]]
        self.pnts_three = [[162 * self.director.scale, 304 * self.director.scale], [162 * self.director.scale, 370 * self.director.scale], [169 * self.director.scale, 370 * self.director.scale], [169 * self.director.scale, 304 * self.director.scale]]
        self.pnts_four = [[231 * self.director.scale, 304 * self.director.scale], [231 * self.director.scale, 370 * self.director.scale], [238 * self.director.scale, 370 * self.director.scale], [238 * self.director.scale, 304 * self.director.scale]]
        self.pnts_five = [[237 * self.director.scale, 364 * self.director.scale], [237 * self.director.scale, 370 * self.director.scale], [297 * self.director.scale, 370 * self.director.scale], [297 * self.director.scale, 364 * self.director.scale]]
        self.pnts_six = [[296 * self.director.scale, 304 * self.director.scale], [296 * self.director.scale, 370 * self.director.scale], [303 * self.director.scale, 370 * self.director.scale], [303 * self.director.scale, 304 * self.director.scale]]
        # Points in space for the lines that will be drawn to represent the occluders
        self.drawpnts_one = [[103 * self.director.scale, 304 * self.director.scale], [103 * self.director.scale, 364 * self.director.scale], [163 * self.director.scale, 364 * self.director.scale], [163 * self.director.scale, 304 * self.director.scale]]
        self.drawpnts_two = [[237 * self.director.scale, 304 * self.director.scale], [237 * self.director.scale, 364 * self.director.scale], [297 * self.director.scale, 364 * self.director.scale], [297 * self.director.scale, 304 * self.director.scale]]
        # The three occluders that make up the colliders for the first snake's particle emitter
        self.occ_one = occluder.Occluder(self.pnts_one)
        self.occ_two = occluder.Occluder(self.pnts_two)
        self.occ_three = occluder.Occluder(self.pnts_three)
        # The three occluders that make up the colliders for the second snake's particle emitter
        self.occ_four = occluder.Occluder(self.pnts_four)
        self.occ_five = occluder.Occluder(self.pnts_five)
        self.occ_six = occluder.Occluder(self.pnts_six)
        # The amount of bounce for each of the occluders
        self.occ_one.set_bounce(0.6)
        self.occ_two.set_bounce(0.6)
        self.occ_three.set_bounce(0.6)

        self.occ_four.set_bounce(0.6)
        self.occ_five.set_bounce(0.6)
        self.occ_six.set_bounce(0.6)

        # The font and size of the text that will be used to display text on the screen
        self.plyr = pygame.font.Font("fonts\Condition.ttf", 20 * director.scale)
        # The font and size of the text that will be used to display text on the screen
        self.colortxt = pygame.font.Font("fonts\Condition.ttf", 18 * director.scale)
        # The font and size of the text that will be used to display text on the screen
        self.ctrl = pygame.font.Font("fonts\Condition.ttf", 30 * director.scale)
        # The font and size of the text that will be used to display text on the screen
        self.p = pygame.font.Font("fonts\Condition.ttf", 24 * director.scale)
        # The font and size of the text that will be used to display text on the screen
        self.txt = director.font.render("Player One Controls", True, (255, 255, 255))

        # The particle system object that will host the two emitters
        self.particle_system = particles.ParticleSystem()
        # The general acceleration for all particles in the emitter
        self.particle_system.set_particle_acceleration([0.0, 500.0])
        # The occluders that the particle system that will use
        self.particle_system.set_particle_occluders([self.occ_one, self.occ_two, self.occ_three, self.occ_four, self.occ_five, self.occ_six])

        # The object that represents the first snake's color Emitter
        self.emitter_one = particles.Emitter()
        #This sets the average number of particles being emitted per second
        self.emitter_one.set_density(500 * self.director.scale)
        #This sets the angle at which the particles are being emitted as well as the angle of spread of the particles
        self.emitter_one.set_angle(90, 120.0)
        #This sets the range of speeds that the particles being emitted can have
        self.emitter_one.set_speed([200.0, 300.0])
        #This sets the range of life (how long the particle can will last on screen before disappearing) in seconds
        self.emitter_one.set_life([0.3, 1.0])
        # Sets the color of the particles being emitted in rgb format
        self.emitter_one.set_colors([self.color_rgb[self.director.index_one]])
        # This sets the general acceleration of particles within the particle system
        self.particle_system.set_particle_acceleration([0.0, 500.0])
        # Adds the emitter to the particle system
        self.particle_system.add_emitter(self.emitter_one, "emitter_one")
        # Sets the position of the emitter in the game window
        self.emitter_one.set_position([133 * self.director.scale, self.screen_rect.bottom - 116 * self.director.scale])

        # The object that represents the first snake's color Emitter
        self.emitter_two = particles.Emitter()
        #This sets the average number of particles being emitted per second
        self.emitter_two.set_density(500 * self.director.scale)
        #This sets the angle at which the particles are being emitted as well as the angle of spread of the particles
        self.emitter_two.set_angle(90, 120.0)
        #This sets the range of speeds that the particles being emitted can have
        self.emitter_two.set_speed([200.0, 300.0])
        #This sets the range of life (how long the particle can will last on screen before disappearing) in seconds
        self.emitter_two.set_life([0.3, 1.0])
        # Sets the color of the particles being emitted in rgb format
        self.emitter_two.set_colors([self.color_rgb[self.director.index_two]])
        # This sets the general acceleration of particles within the particle system
        self.particle_system.set_particle_acceleration([0.0, 500.0])
        # Adds the emitter to the particle system
        self.particle_system.add_emitter(self.emitter_two, "emitter_two")
        # Sets the position of the emitter in the game window
        self.emitter_two.set_position([267 * self.director.scale, self.screen_rect.bottom - 116 * self.director.scale])

        # Boolean variable telling whether or not player one's left arrow is enlarged
        self.p1_hili_l_arrow = False
        # Boolean variable telling whether or not player one's left arrow is enlarged
        self.p1_hili_r_arrow = False
        # Boolean variable telling whether or not player one's left arrow is enlarged
        self.p2_hili_l_arrow = False
        # Boolean variable telling whether or not player one's left arrow is enlarged
        self.p2_hili_r_arrow = False

    def on_update(self):
        # Update method of the particle system
        self.particle_system.update(1.0 / 60.0)
        # Sets the fps (frames per second to 30
        self.director.fps = 30

    def on_event(self, event):
        # This conditional statement checks if a key has been pressed down
        if event.type == pygame.KEYDOWN:
            # This conditional statement checks if the D key has been pressed. If it does and the index of the first
            # player's color is 6 it will change to 0. Otherwise it will increment
            if event.key == pygame.K_d:
                if self.director.index_one == 6:
                    self.director.index_one = 0
                else:
                    self.director.index_one += 1
            # This conditional statement checks if the A key has been pressed. If it does and the index of the first
            # player's color is 0 it will change to the last index. Otherwise it will decrement
            if event.key == pygame.K_a:
                if self.director.index_one == 0:
                    self.director.index_one = len(self.color_rgb) - 1
                else:
                    self.director.index_one -= 1
            # An Emitter object is made
            self.emitter_one = particles.Emitter()
            #This sets the average number of particles being emitted per second
            self.emitter_one.set_density(500 * self.director.scale)
            # This sets the angle at which the particles are being emitted as well as the angle of spread of the particles
            self.emitter_one.set_angle(90, 120.0)
            # This sets the range of speeds that the particles being emitted can have
            self.emitter_one.set_speed([200.0, 300.0])
            # This sets the range of life (how long the particle can will last on screen before disappearing) in seconds
            self.emitter_one.set_life([0.3, 1.0])
            # Sets the color of the particles being emitted in rgb format
            self.emitter_one.set_colors([self.color_rgb[self.director.index_one]])
            # Sets the first player's character to the rgb value of the index_one
            self.director.p1color = self.color_rgb[self.director.index_one]
            # Sets the general acceleration of particle's in the system
            self.particle_system.set_particle_acceleration([0.0, 500.0])
            # Adds the emitter to the particle system
            self.particle_system.add_emitter(self.emitter_one, "emitter_one")
            # Sets the position of the particle emitter in the game window
            self.emitter_one.set_position([133 * self.director.scale, self.screen_rect.bottom - 116 * self.director.scale])

        # Checks if a key has been pressed down
        if event.type == pygame.KEYDOWN:
            # This conditional statement checks if the Right key has been pressed. If the index of the second player's
            # color is 6 then then it will change to 0. Otherwise, it will increment.
            if event.key == pygame.K_RIGHT:
                if self.director.index_two == 6:
                    self.director.index_two = 0
                else:
                    self.director.index_two += 1
            # This conditional statement checks if the Left key has been pressed. If the index of the second player's
            # color is 0 then then it will change to the last index. Otherwise, it will decrement.
            if event.key == pygame.K_LEFT:
                if self.director.index_two == 0:
                    self.director.index_two = len(self.color_rgb) - 1
                else:
                    self.director.index_two -= 1
            # An Emitter object is made
            self.emitter_two = particles.Emitter()
            #This sets the average number of particles being emitted per second
            self.emitter_two.set_density(500 * self.director.scale)
            # This sets the angle at which the particles are being emitted as well as the angle of spread of the particles
            self.emitter_two.set_angle(90, 120.0)
            # This sets the range of speeds that the particles being emitted can have
            self.emitter_two.set_speed([200.0, 300.0])
            # This sets the range of life (how long the particle can will last on screen before disappearing) in seconds
            self.emitter_two.set_life([0.3, 1.0])
            # Sets the color of the particles being emitted in rgb format
            self.emitter_two.set_colors([self.color_rgb[self.director.index_two]])  # need to access dictionary value
            # Sets the second player's character to the rgb value of the index_one
            self.director.p2color = self.color_rgb[self.director.index_two]
            # Sets the general acceleration of particle's in the system
            self.particle_system.set_particle_acceleration([0.0, 500.0])
            # Adds the emitter to the particle system
            self.particle_system.add_emitter(self.emitter_two, "emitter_two")
            # Adds the emitter to the particle system
            self.emitter_two.set_position([267 * self.director.scale, self.screen_rect.bottom - 116 * self.director.scale])

        # Checks if the Right key is pressed down. If so, it will set p2_hili_r_arrow to true, causing the second
        # player's right arrow to enlarge, and its left arrow to shrink
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            self.p2_hili_r_arrow = True
            self.p2_hili_l_arrow = False
        # Checks if the Left key is pressed down. If so, it will set p2_hili_l_arrow to true, causing the second
        # player's left arrow to enlarge, and its right arrow to shrink
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            self.p2_hili_l_arrow = True
            self.p2_hili_r_arrow = False
        # Checks if the A key is pressed down. If so, it will set p1_hili_l_arrow to true, causing the first
        # player's left arrow to enlarge, and its right arrow to shrink
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            self.p1_hili_l_arrow = True
            self.p1_hili_r_arrow = False
        # Checks if the D key is pressed down. If so, it will set p1_hili_r_arrow to true, causing the first
        # player's right arrow to enlarge, and its left arrow to shrink
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            self.p1_hili_r_arrow = True
            self.p1_hili_l_arrow = False

        # Checks if the key if either of the control keys are pressed down, and if so, it will change to the Title
        # Screen, as well as shrink all of the arrows in the scene
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL):
            self.director.change_scene(self.director.scenes[0])
            self.p1_hili_l_arrow = False
            self.p1_hili_r_arrow = False
            self.p2_hili_l_arrow = False
            self.p2_hili_r_arrow = False

    def on_draw(self, screen):
        # Changes every pixel in the window to black. This is done to wipe the screen and set it up for drawing a new
        # frame
        screen.fill((0, 0, 0))

        # Player One Config
        # A surface is created with the text "Player One Controls" printed on it
        self.txt = self.plyr.render("Player One Controls", True, (255, 255, 255))
        # Prints the text to the game window at the specified coordinates
        screen.blit(self.txt, self.txt.get_rect(centerx=self.screen_rect.centerx, centery=19 * self.director.scale))
        # A surface is created with the text "Player Two Controls" printed on it
        self.txt = self.plyr.render("Player Two Controls", True, (255, 255, 255))
        # Prints the text to the game window at the specified coordinates
        screen.blit(self.txt, self.txt.get_rect(centerx=self.screen_rect.centerx, centery=149 * self.director.scale))

        # Creates a rounded rectangle with an rgb color of white at the specified coordinates
        rrect(screen, (255, 255, 255), pygame.Rect(47 * self.director.scale, 34 * self.director.scale, 51 * self.director.scale, 51 * self.director.scale), 12 * self.director.scale, 3 * self.director.scale)
        # Creates a surface with the letter W printed on it
        self.txt = self.ctrl.render("W", True, (255, 255, 255))
        # Prints the text to the game window a the specified coordinates
        screen.blit(self.txt, self.txt.get_rect(centerx=47 * self.director.scale + 25 * self.director.scale, centery=34 * self.director.scale + 25 * self.director.scale))
        # Creates a surface with the word "up" on it
        self.txt = self.plyr.render("up", True, (255, 255, 255))
        # Prints the text to the game window a the specified coordinates
        screen.blit(self.txt, self.txt.get_rect(centerx=47 * self.director.scale + 25 * self.director.scale, centery=34 * self.director.scale + 65 * self.director.scale))

        # Creates a rounded rectangle with an rgb color of white at the specified coordinates
        rrect(screen, (255, 255, 255), pygame.Rect(133 * self.director.scale, 34 * self.director.scale, 51 * self.director.scale, 51 * self.director.scale), 12 * self.director.scale, 3 * self.director.scale)
        # Creates a surface with the letter A printed on it
        self.txt = self.ctrl.render("A", True, (255, 255, 255))
        # Prints the text to the game window a the specified coordinates
        screen.blit(self.txt, self.txt.get_rect(centerx=133 * self.director.scale + 25 * self.director.scale, centery=34 * self.director.scale + 25 * self.director.scale))
        # Creates a surface with the word "left" on it
        self.txt = self.plyr.render("left", True, (255, 255, 255))
        # Prints the text to the game window a the specified coordinates
        screen.blit(self.txt, self.txt.get_rect(centerx=133 * self.director.scale + 25 * self.director.scale, centery=34 * self.director.scale + 65 * self.director.scale))

        # Creates a rounded rectangle with an rgb color of white at the specified coordinates
        rrect(screen, (255, 255, 255), pygame.Rect(219 * self.director.scale, 34 * self.director.scale, 51 * self.director.scale, 51 * self.director.scale), 12 * self.director.scale, 3 * self.director.scale)
        # Creates a surface with the letter S printed on it
        self.txt = self.ctrl.render("S", True, (255, 255, 255))
        # Prints the text to the game window a the specified coordinates
        screen.blit(self.txt, self.txt.get_rect(centerx=219 * self.director.scale + 25 * self.director.scale, centery=34 * self.director.scale + 25 * self.director.scale))
        # Creates a surface with the word "down" on it
        self.txt = self.plyr.render("down", True, (255, 255, 255))
        # Prints the text to the game window a the specified coordinates
        screen.blit(self.txt, self.txt.get_rect(centerx=219 * self.director.scale + 25 * self.director.scale, centery=34 * self.director.scale + 65 * self.director.scale))

        # Creates a rounded rectangle with an rgb color of white at the specified coordinates
        rrect(screen, (255, 255, 255), pygame.Rect(305 * self.director.scale, 34 * self.director.scale, 51 * self.director.scale, 51 * self.director.scale), 12 * self.director.scale, 3 * self.director.scale)
        # Creates a surface with the letter D printed on it
        self.txt = self.ctrl.render("D", True, (255, 255, 255))
        # Prints the text to the game window a the specified coordinates
        screen.blit(self.txt, self.txt.get_rect(centerx=305 * self.director.scale + 25 * self.director.scale, centery=34 * self.director.scale + 25 * self.director.scale))
        # Creates a surface with the word "right" on it
        self.txt = self.plyr.render("right", True, (255, 255, 255))
        # Prints the text to the game window a the specified coordinates
        screen.blit(self.txt, self.txt.get_rect(centerx=305 * self.director.scale + 25 * self.director.scale, centery=34 * self.director.scale + 65 * self.director.scale))

        # Player Two Config
        # Creates a rounded rectangle with an rgb color of white at the specified coordinates
        rrect(screen, (255, 255, 255), pygame.Rect(47 * self.director.scale, 164 * self.director.scale, 51 * self.director.scale, 51 * self.director.scale), 12 * self.director.scale, 3 * self.director.scale)
        # Draws a filled triangle to the screen using the specified points
        gfxdraw.filled_trigon(screen, 72 * self.director.scale, 176 * self.director.scale, 86 * self.director.scale, 204 * self.director.scale, 58 * self.director.scale,204 * self.director.scale, (255, 255, 255))
        # Draws an outline of an anti-aliased triangle using the specified points
        gfxdraw.aatrigon(screen, 72 * self.director.scale, 176 * self.director.scale, 86 * self.director.scale, 204 * self.director.scale, 58 * self.director.scale,204 * self.director.scale, (255, 255, 255))
        # Creates a surface with the word "up" printed on it
        self.txt = self.plyr.render("up", True, (255, 255, 255))
        # Prints the text to the game window a the specified coordinates
        screen.blit(self.txt, self.txt.get_rect(centerx=47 * self.director.scale + 25 * self.director.scale, centery=164 * self.director.scale + 65 * self.director.scale))

        # Creates a rounded rectangle with an rgb color of white at the specified coordinates
        rrect(screen, (255, 255, 255), pygame.Rect(133 * self.director.scale, 164 * self.director.scale, 51 * self.director.scale, 51 * self.director.scale), 12 * self.director.scale, 3 * self.director.scale)
        # Draws a filled triangle to the screen using the specified points
        gfxdraw.filled_trigon(screen, 144 * self.director.scale, 189 * self.director.scale, 172 * self.director.scale, 175 * self.director.scale, 172 * self.director.scale, 203 * self.director.scale, (255, 255, 255))
        # Draws an outline of an anti-aliased triangle using the specified points
        gfxdraw.aatrigon(screen, 144 * self.director.scale, 189 * self.director.scale, 172 * self.director.scale, 175 * self.director.scale, 172 * self.director.scale, 203 * self.director.scale, (255, 255, 255))
        # Creates a surface with the word "left" printed on it
        self.txt = self.plyr.render("left", True, (255, 255, 255))
        # Prints the text to the game window a the specified coordinates
        screen.blit(self.txt, self.txt.get_rect(centerx=133 * self.director.scale + 25 * self.director.scale, centery=164 * self.director.scale + 65 * self.director.scale))

        # Creates a rounded rectangle with an rgb color of white at the specified coordinates
        rrect(screen, (255, 255, 255), pygame.Rect(219 * self.director.scale, 164 * self.director.scale, 51 * self.director.scale, 51 * self.director.scale), 12 * self.director.scale, 3 * self.director.scale)
        # Draws a filled triangle to the screen using the specified points
        gfxdraw.filled_trigon(screen, 244 * self.director.scale, 204 * self.director.scale, 258 * self.director.scale, 176 * self.director.scale, 230 * self.director.scale, 176 * self.director.scale, (255, 255, 255))
        # Draws an outline of an anti-aliased triangle using the specified points
        gfxdraw.aatrigon(screen, 244 * self.director.scale, 204 * self.director.scale, 258 * self.director.scale, 176 * self.director.scale, 230 * self.director.scale, 176 * self.director.scale, (255, 255, 255))
        # Creates a surface with the word "left" printed on it
        self.txt = self.plyr.render("down", True, (255, 255, 255))
        # Prints the text to the game window a the specified coordinates
        screen.blit(self.txt, self.txt.get_rect(centerx=219 * self.director.scale + 25 * self.director.scale, centery=164 * self.director.scale + 65 * self.director.scale))

        # Creates a rounded rectangle with an rgb color of white at the specified coordinates
        rrect(screen, (255, 255, 255), pygame.Rect(305 * self.director.scale, 164 * self.director.scale, 51 * self.director.scale, 51 * self.director.scale), 12 * self.director.scale, 3 * self.director.scale)
        # Draws a filled triangle to the screen using the specified points
        gfxdraw.filled_trigon(screen, 344 * self.director.scale, 189 * self.director.scale, 316 * self.director.scale, 175 * self.director.scale, 316 * self.director.scale, 203 * self.director.scale, (255, 255, 255))
        # Draws an outline of an anti-aliased triangle using the specified points
        gfxdraw.aatrigon(screen, 344 * self.director.scale, 189 * self.director.scale, 316 * self.director.scale, 175 * self.director.scale, 316 * self.director.scale, 203 * self.director.scale, (255, 255, 255))
        # Creates a surface with the word "right" printed on it
        self.txt = self.plyr.render("right", True, (255, 255, 255))
        # Prints the text to the game window a the specified coordinates
        screen.blit(self.txt, self.txt.get_rect(centerx=305 * self.director.scale + 25 * self.director.scale, centery=164 * self.director.scale + 65 * self.director.scale))

        # Creates a surface with the word "p1" printed on it
        self.txt = self.p.render("p1", True, (255, 255, 255))
        # Prints the text to the game window a the specified coordinates
        screen.blit(self.txt, self.txt.get_rect(centerx=self.screen_rect.right / 3, centery=self.screen_rect.bottom - 116 *self.director.scale))

        # Creates a surface with the word "p2" printed on it
        self.txt = self.p.render("p2", True, (255, 255, 255))
        # Prints the text to the game window a the specified coordinates
        screen.blit(self.txt, self.txt.get_rect(centerx=self.screen_rect.right * (2 / 3), centery=self.screen_rect.bottom - 116 * self.director.scale))

        # Draws anti-aliased lines to the screen using the coordinates given by drawpnts_one
        pygame.draw.aalines(screen, (255, 255, 255), False, self.drawpnts_one)
        # Draws anti-aliased lines to the screen using the coordinates given by drawpnts_two
        pygame.draw.aalines(screen, (255, 255, 255), False, self.drawpnts_two)
        # Draws the particle system
        self.particle_system.draw(screen)

        # Creates a surface with the name of the color printed on it using the color associated with that name
        self.txt = self.colortxt.render(self.color_name[self.director.index_one], True, self.color_rgb[self.director.index_one])
        # Prints the text to the game window a the specified coordinates
        screen.blit(self.txt, self.txt.get_rect(centerx=133 * self.director.scale, centery=373 * self.director.scale))

        # Creates a surface with the name of the color printed on it using the color associated with that name
        self.txt = self.colortxt.render(self.color_name[self.director.index_two], True, self.color_rgb[self.director.index_two])
        # Prints the text to the game window a the specified coordinates
        screen.blit(self.txt, self.txt.get_rect(centerx=267 * self.director.scale, centery=373 * self.director.scale))

        # This conditional statement says that if p1_hili_l_arrow is set to true then draw the enlarged version of the
        # triangle. Otherwise, draw the regular version
        if self.p1_hili_l_arrow:
            gfxdraw.filled_trigon(screen, 94 * self.director.scale, 363 * self.director.scale, 94 * self.director.scale, 383 * self.director.scale, 74 * self.director.scale, 373 * self.director.scale, (255, 255, 255))
            gfxdraw.aatrigon(screen, 94 * self.director.scale, 363 * self.director.scale, 94 * self.director.scale, 383 * self.director.scale, 74 * self.director.scale, 373 * self.director.scale, (255, 255, 255))
        else:
            gfxdraw.filled_trigon(screen, 91 * self.director.scale, 366 * self.director.scale, 91 * self.director.scale, 380 * self.director.scale, 77 * self.director.scale, 373 * self.director.scale, (255, 255, 255))
            gfxdraw.aatrigon(screen, 91 * self.director.scale, 366 * self.director.scale, 91 * self.director.scale, 380 * self.director.scale, 77 * self.director.scale, 373 * self.director.scale, (255, 255, 255))

        # This conditional statement says that if p1_hili_l_arrow is set to true then draw the enlarged version of the
        # triangle. Otherwise, draw the regular version
        if self.p1_hili_r_arrow:
            gfxdraw.filled_trigon(screen, 172 * self.director.scale, 363 * self.director.scale, 172 * self.director.scale, 383 * self.director.scale, 192 * self.director.scale, 373 * self.director.scale, (255, 255, 255))
            gfxdraw.aatrigon(screen, 172 * self.director.scale, 363 * self.director.scale, 172 * self.director.scale, 383 * self.director.scale, 192 * self.director.scale, 373 * self.director.scale, (255, 255, 255))
        else:
            gfxdraw.filled_trigon(screen, 175 * self.director.scale, 366 * self.director.scale, 175 * self.director.scale, 380 * self.director.scale, 189 * self.director.scale, 373 * self.director.scale, (255, 255, 255))
            gfxdraw.aatrigon(screen, 175 * self.director.scale, 366 * self.director.scale, 175 * self.director.scale, 380 * self.director.scale, 189 * self.director.scale, 373 * self.director.scale, (255, 255, 255))

        # This conditional statement says that if p2_hili_l_arrow is set to true then draw the enlarged version of the
        # triangle. Otherwise, draw the regular version
        if self.p2_hili_l_arrow:
            gfxdraw.filled_trigon(screen, 228 * self.director.scale, 363 * self.director.scale, 228 * self.director.scale, 383 * self.director.scale, 209 * self.director.scale, 373 * self.director.scale, (255, 255, 255))
            gfxdraw.aatrigon(screen, 228 * self.director.scale, 363 * self.director.scale, 228 * self.director.scale, 383 * self.director.scale, 209 * self.director.scale, 373 * self.director.scale, (255, 255, 255))
        else:
            gfxdraw.filled_trigon(screen, 225 * self.director.scale, 366 * self.director.scale,225 * self.director.scale, 380 * self.director.scale, 211 * self.director.scale, 373 * self.director.scale, (255, 255, 255))
            gfxdraw.aatrigon(screen, 225 * self.director.scale, 366 * self.director.scale, 225 * self.director.scale, 380 * self.director.scale, 211 * self.director.scale, 373 * self.director.scale, (255, 255, 255))

        # This conditional statement says that if p2_hili_r_arrow is set to true then draw the enlarged version of the
        # triangle. Otherwise, draw the regular version
        if self.p2_hili_r_arrow:
            gfxdraw.filled_trigon(screen, 306 * self.director.scale, 363 * self.director.scale, 306 * self.director.scale, 383 * self.director.scale, 326 * self.director.scale, 373 * self.director.scale, (255, 255, 255))
            gfxdraw.aatrigon(screen, 306 * self.director.scale, 363 * self.director.scale, 306 * self.director.scale, 383 * self.director.scale, 326 * self.director.scale, 373 * self.director.scale, (255, 255, 255))
        else:
            gfxdraw.filled_trigon(screen, 309 * self.director.scale, 366 * self.director.scale, 309 * self.director.scale, 380 * self.director.scale, 323 * self.director.scale, 373 * self.director.scale, (255, 255, 255))
            gfxdraw.aatrigon(screen, 309 * self.director.scale, 366 * self.director.scale, 309 * self.director.scale, 380 * self.director.scale, 323 * self.director.scale, 373 * self.director.scale, (255, 255, 255))

        # Creates a rounded rectangle with an rgb color of white at the specified coordinates
        rrect(screen, (255, 255, 255), pygame.Rect(0 * self.director.scale, 0 * self.director.scale, 63 * self.director.scale, 30 * self.director.scale), 9 * self.director.scale, 3 * self.director.scale)
        # Creates a surface with the word "ctrl" printed on it
        self.txt = self.plyr.render("ctrl",True, (255, 255, 255))
        # Prints the text to the game window a the specified coordinates
        screen.blit(self.txt, (25 * self.director.scale, 7 * self.director.scale))
        # Draws a filled triangle to the screen using the specified points
        gfxdraw.filled_trigon(screen, 5 * self.director.scale, 15 * self.director.scale, 20 * self.director.scale, 22 * self.director.scale, 20 * self.director.scale, 8 * self.director.scale, (255, 150, 44))
        # Draws an outline of an anti-aliased triangle using the specified points
        gfxdraw.aatrigon(screen, 5 * self.director.scale, 15 * self.director.scale, 20 * self.director.scale, 22 * self.director.scale, 20 * self.director.scale, 8 * self.director.scale, (255, 150, 44))
