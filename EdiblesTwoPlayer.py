from Scene import *
from Entity import *
import random
from pygame import gfxdraw
from PAdLib import rrect

class EdiblesTwoPlayer(Scene):
    def __init__(self, director):
        Scene.__init__(self, director)
        # Boolean value that tells whether or not player one has won
        self.plyronewins = False
        # Boolean value that tells whether or not player two has won
        self.plyrtwowins = False
        # Boolean value that tells whether or not there has been a "draw"
        self.plyrdraw = False
        # A surface with the text "Draw..." printed on it using the font named "font"
        self.draw_txt = director.font.render("Draw...", True, (255, 255, 255))
        # A surface with the text "Player One Wins" printed on it using the font named "font"
        self.plyronewins_txt = director.font.render("Player One Wins", True, (255, 255, 255))
        # A surface with the text "Player Two Wins" printed on it using the font named "font"
        self.plyrtwowins_txt = director.font.render("Player Two Wins", True, (255, 255, 255))
        # A surface with the text "Draw" printed on it using the font named "font"
        self.plyrdraw_txt = director.font.render("Draw", True, (255, 255, 255))
        # This is a rectangle object with the size being the same as the size of the game window size
        self.screen_rect = director.screen.get_rect()
        # The font and size of the text that will be used to display text on the screen
        self.plyr = pygame.font.Font("fonts\Condition.ttf", 20 * director.scale)
        # Creates a surface with the text "ctrl" printed on it using the plyr font
        self.txt = self.plyr.render("ctrl", True, (255, 255, 255))

        # These variables hold the width and height of the game window, respectively
        self.w, self.h = pygame.display.get_surface().get_size()
        # The change in x value of the first player's snake
        self.dx1 = 10 * director.scale
        # The change in y value of the first player's snake
        self.dy1 = 0
        # The change in x value of the second player's snake
        self.dx2 = -10 * director.scale
        # The change in y value of the second player's snake
        self.dy2 = 0
        # The Entity object representing the head of the first player's snake
        self.head_1 = Entity(21 * director.scale, 1 * director.scale, 9 * director.scale, 9 * director.scale, director.p1color)
        # The Entity object representing the head of the second player's snake
        self.head_2 = Entity(371 * director.scale, 1 * director.scale, 9 * director.scale, 9 * director.scale, director.p2color)
        # The Entity object representing the apple
        self.apple = Entity(11 * director.scale, 11 * director.scale, 9 * director.scale, 9 * director.scale, (255, 44, 44))
        # A list holding the tail segments of the first player's snake
        self.tail_1 = []
        # A list holding the tail segments of the second player's snake
        self.tail_2 = []

        # This starts off the first player's snake with two tail segments
        for i in range(1, 3):
            self.tail_1.append(Entity(self.head_1.x - 10 * i * director.scale, self.head_1.y * director.scale, 9 * director.scale, 9 * director.scale, self.director.p1color))
        # This starts off the second player's snake with two tail segments
        for i in range(1, 3):
            self.tail_2.append(Entity(self.head_2.x + 10 * i * director.scale, self.head_2.y * director.scale, 9 * director.scale, 9 * director.scale, self.director.p2color))

    def on_event(self, event):
        # This conditional statement that if either the W key is pressed down and if the first player's snake
        # is not moving on the y-axis then have it start moving up on the y axis cease movement on the x axis
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w and self.dy1 == 0:
            self.dy1 = -10 * self.director.scale
            self.dx1 = 0
        # This conditional statement that if either the S key is pressed down and if the first player's snake
        # is not moving on the y-axis then have it start moving down on the y axis cease movement on the x axis
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s and self.dy1 == 0:
            self.dy1 = 10 * self.director.scale
            self.dx1 = 0
        # This conditional statement that if either the A key is pressed down and if the first player's snake
        # is not moving on the x-axis then have it start moving left on the x axis cease movement on the y axis
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a and self.dx1 == 0:
            self.dx1 = -10 * self.director.scale
            self.dy1 = 0
        # This conditional statement that if either the D key is pressed down and if the first player's snake
        # is not moving on the x-axis then have it start moving right on the x axis cease movement on the y axis
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d and self.dx1 == 0:
            self.dx1 = 10 * self.director.scale
            self.dy1 = 0

        # This conditional statement that if either the Up key is pressed down and if the second player's snake
        # is not moving on the y-axis then have it start moving up on the y axis cease movement on the x axis
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP and self.dy2 == 0:
            self.dy2 = -10 * self.director.scale
            self.dx2 = 0
        # This conditional statement that if either the Down key is pressed down and if the second player's snake
        # is not moving on the y-axis then have it start moving down on the y axis cease movement on the x axis
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN and self.dy2 == 0:
            self.dy2 = 10 * self.director.scale
            self.dx2 = 0
        # This conditional statement that if either the A key is pressed down and if the second player's snake
        # is not moving on the x-axis then have it start moving left on the x axis cease movement on the y axis
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and self.dx2 == 0:
            self.dx2 = -10 * self.director.scale
            self.dy2 = 0
        # This conditional statement that if either the D key is pressed down and if the second player's snake
        # is not moving on the x-axis then have it start moving right on the x axis cease movement on the y axis
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and self.dx2 == 0:
            self.dx2 = 10 * self.director.scale
            self.dy2 = 0
        # If the R button is pressed down then the scene is changed to a new instance of the Two Player Mode
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            # Causes the currently playing song to stop playing
            pygame.mixer.music.stop()
            self.director.change_scene(EdiblesTwoPlayer(self.director))
            # Loads the song
            pygame.mixer.music.load("music\snakesong.wav")
            # Plays the loaded song indefinitely
            pygame.mixer.music.play(-1)
        #  If either of the control buttons are pressed then the scene is chagned to the Title Screen and the Two
        # Player Mode is reset by creating a new instance of it
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL):
            self.director.change_scene(self.director.scenes[0])
            # Causes the currently playing song to stop playing
            pygame.mixer.music.stop()
            self.director.scenes[2] = EdiblesTwoPlayer(self.director)

    def on_update(self):
        # The fps (frames per second) is changed to 15
        self.director.fps = 15

        # This conditional statement checks to see if none of the win states have been met, and if so, execute the
        # following code
        if not self.plyronewins and not self.plyrtwowins and not self.plyrdraw:
            # Calling the did_eat function
            self.did_eat()

            # update position of the first tail's elements
            for i in range(len(self.tail_1) - 1, 0, -1):
                self.tail_1[i].x = self.tail_1[i - 1].x
                self.tail_1[i].y = self.tail_1[i - 1].y
            self.tail_1[0].x, self.tail_1[0].y = (self.head_1.x, self.head_1.y)
            # The following two lines update the x and y position of the first snake's head
            self.head_1.x += self.dx1
            self.head_1.y += self.dy1
            # The following three lines ensure that the head and tail of the snake are the proper color as the color
            # can change if the player picks a new color on the configuration screen
            self.head_1.color = self.director.p1color
            for i in self.tail_1:
                i.color = self.director.p1color
            # Calling of the is_collide function
            self.is_collide()
            # Checks if any of the game win / game over states and have been met and if so then the function ceases to
            # execute
            if self.plyrdraw or self.plyronewins or self.plyrtwowins:
                return
            # update position of the second tail's elements
            for i in range(len(self.tail_2) - 1, 0, -1):
                self.tail_2[i].x = self.tail_2[i - 1].x
                self.tail_2[i].y = self.tail_2[i - 1].y
            self.tail_2[0].x, self.tail_2[0].y = (self.head_2.x, self.head_2.y)
            # The following two lines update the x and y position of the first snake's head
            self.head_2.x += self.dx2
            self.head_2.y += self.dy2
            # The following three lines ensure that the head and tail of the snake are the proper color as the color
            # can change if the player picks a new color on the configuration screen
            self.head_2.color = self.director.p2color
            for i in self.tail_2:
                i.color = self.director.p2color
            # Calling of the is_collide function
            self.is_collide()

            # Checks if any of the game win / game over states and have been met and if so then the function ceases to
            # execute
            if self.plyrdraw or self.plyronewins or self.plyrtwowins:
                return

    def on_draw(self, screen):
        # Changes every pixel in the window to black. This is done to wipe the screen and set it up for drawing a new
        # frame
        self.director.screen.fill((0, 0, 0))
        # Calls the draw_grid function
        self.draw_grid(screen)
        # Calls the apple Entity's draw function
        self.apple.draw(screen)
        # Calls the head Entity's draw function
        self.head_1.draw(screen)
        # Calls the head Entity's draw function
        self.head_2.draw(screen)
        # Calls the print_tail function
        self.print_tails(screen)
        # This conditional statement executes if player one has won
        if self.plyronewins:
            # The text "Player One Wins" is printed to the middle of the screen
            screen.blit(self.plyronewins_txt, self.plyronewins_txt.get_rect(center=self.screen_rect.center))
            # Creates a surface with the text "ctrl" print on it using the plyr font
            self.txt = self.plyr.render("ctrl", True, (255, 255, 255))
            # draws a round rectangle to the top left corner of the screen
            rrect(screen, (255, 255, 255), pygame.Rect(0 * self.director.scale, 0 * self.director.scale, 63 * self.director.scale, 30 * self.director.scale), 9 * self.director.scale, 3 * self.director.scale)
            # The text ctrl is printed in the top left corner of the screen
            screen.blit(self.txt, (25 * self.director.scale, 7 * self.director.scale))
            #Draws a filled triangle to the screen with the points being at the specified coordinates
            gfxdraw.filled_trigon(screen, 5 * self.director.scale, 15 * self.director.scale, 20 * self.director.scale, 22 * self.director.scale, 20 * self.director.scale, 8 * self.director.scale, (255, 150, 44))
            #Draws an anti-aliased triangle outline with the points being at the specified coordinates
            gfxdraw.aatrigon(screen, 5 * self.director.scale, 15 * self.director.scale, 20 * self.director.scale, 22 * self.director.scale, 20 * self.director.scale, 8 * self.director.scale, (255, 150, 44))
           #pygame.mixer.music.stop()
        # This conditional statement executes if player two has won
        if self.plyrtwowins:
            # The text "Player Two Wins" is printed to the middle of the screen
            screen.blit(self.plyrtwowins_txt, self.plyronewins_txt.get_rect(center=self.screen_rect.center))
            # Creates a surface with the text "ctrl" print on it using the plyr font
            self.txt = self.plyr.render("ctrl", True, (255, 255, 255))
            # draws a round rectangle to the top left corner of the screen
            rrect(screen, (255, 255, 255), pygame.Rect(0 * self.director.scale, 0 * self.director.scale, 63 * self.director.scale, 30 * self.director.scale), 9 * self.director.scale, 3 * self.director.scale)
            # The text ctrl is printed in the top left corner of the screen
            screen.blit(self.txt, (25 * self.director.scale, 7 * self.director.scale))
            #Draws a filled triangle to the screen with the points being at the specified coordinates
            gfxdraw.filled_trigon(screen, 5 * self.director.scale, 15 * self.director.scale, 20 * self.director.scale, 22 * self.director.scale, 20 * self.director.scale, 8 * self.director.scale, (255, 150, 44))
            #Draws an anti-aliased triangle outline with the points being at the specified coordinates
            gfxdraw.aatrigon(screen, 5 * self.director.scale, 15 * self.director.scale, 20 * self.director.scale, 22 * self.director.scale, 20 * self.director.scale, 8 * self.director.scale, (255, 150, 44))
            #pygame.mixer.music.stop()
        #  This conditional statement executes if there has been a draw
        if self.plyrdraw:
            # Creates a surface with the text "ctrl" print on it using the plyr font
            self.txt = self.plyr.render("ctrl", True, (255, 255, 255))
            # The text "draw" is printed to the middle of the screen
            screen.blit(self.plyrdraw_txt, self.plyrdraw_txt.get_rect(center=self.screen_rect.center))
            # draws a round rectangle to the top left corner of the screen
            rrect(screen, (255, 255, 255), pygame.Rect(0 * self.director.scale, 0 * self.director.scale, 63 * self.director.scale, 30 * self.director.scale), 9 * self.director.scale, 3 * self.director.scale)
            # The text ctrl is printed in the top left corner of the screen
            screen.blit(self.txt, (25 * self.director.scale, 7 * self.director.scale))
            #Draws a filled triangle to the screen with the points being at the specified coordinates
            gfxdraw.filled_trigon(screen, 5 * self.director.scale, 15 * self.director.scale, 20 * self.director.scale, 22 * self.director.scale, 20 * self.director.scale, 8 * self.director.scale, (255, 150, 44))
            #Draws an anti-aliased triangle outline with the points being at the specified coordinates
            gfxdraw.aatrigon(screen, 5 * self.director.scale, 15 * self.director.scale, 20 * self.director.scale, 22 * self.director.scale, 20 * self.director.scale, 8 * self.director.scale, (255, 150, 44))
            #pygame.mixer.music.stop()

    def print_tails(self, screen):
        # This draws each of the first snake's tail segments to the screen
        for i in range(len(self.tail_1)):
            pygame.draw.rect(screen, self.tail_1[i].color, self.tail_1[i].rect())
        # This draws each of the second snake's tail segments to the screen
        for i in range(len(self.tail_2)):
            pygame.draw.rect(screen, self.tail_2[i].color, self.tail_2[i].rect())

    def draw_grid(self, screen):
        #Draws the grid lines to the screen
        for i in range(40):  # draw vertical grid lines
            pygame.draw.line(screen, (56, 56, 56), (i * 10 * self.director.scale, 0), (i * 10 * self.director.scale, self.h))

        for i in range(40):  # draw horizontal grid lines
            pygame.draw.line(screen, (56, 56, 56), (0, i * 10 * self.director.scale), (self.w, i * 10 * self.director.scale))

    # This function decides whether or not an apple has been eaten by the snake and if so it then adds a new segment to
    # the snake and spawns in a new apple
    def did_eat(self):
        # Boolean value representing whether or not a space is empty. This matters as you don't want the apple spawning
        # on the same spot as part of the snake's body
        spaceEmpty = True
        # This conditional statement checks whether or not the apple and head of the first snake occupy the same spot
        if self.head_1.x == self.apple.x and self.head_1.y == self.apple.y:
            # The integer value of what will be the previous X value
            prevX = self.apple.x
            # The integer value of what will be the previous Y value
            prevY = self.apple.y
            # The integer value of what will be the new current X value. It is randomly generated
            currX = myround(random.randint(0, self.w / 10 - 10 * self.director.scale), 10 * self.director.scale) * 10 + 1 * self.director.scale
            # This loop checks if the previous X value and the newly generated X value are the same, if so it will
            # generate a new one until they no longer match. This stops the apple from spawning in place
            while prevX == currX:
                currX = myround(random.randint(0, self.w / 10 - 10 * self.director.scale), 10 * self.director.scale) * 10 + 1 * self.director.scale
            # The integer value of what will be the new current Y value. It is randomly generated
            currY = myround(random.randint(0, self.h / 10 - 10 * self.director.scale), 10 * self.director.scale) * 10 + 1 * self.director.scale
            # This loop checks if the previous Y value and the newly generated Y value are the same, if so it will
            # generate a new one until they no longer match. This stops the apple from spawning in place
            while prevY == currY:
                currY = myround(random.randint(0, self.h / 10 - 10 * self.director.scale), 10 * self.director.scale) * 10 + 1 * self.director.scale
            # The next 11 lines essentially do what the previous lines have except it checks each segements of the tail
            # so that the apple doesn't spawn in one of their spots
            for i in self.tail_1:
                if currX == i.x and currY == i.y:
                    spaceEmpty = False
                    while not spaceEmpty and prevX != currX and prevY != currY:
                        currX = myround(random.randint(0, self.w / 10 - 10 * self.director.scale), 10 * self.director.scale) * 10 + 1 * self.director.scale
                        currY = myround(random.randint(0, self.h / 10 - 10 * self.director.scale), 10 * self.director.scale) * 10 + 1 * self.director.scale
                        for j in self.tail_1:
                            if currX == j.x and currY == j.y:
                                spaceEmpty = False
                                break
                            spaceEmpty = True

            # Once all has been said and done the apple's x and y values are changed to currX and currY
            self.apple.x = currX
            self.apple.y = currY

            # A new segment is added to the end of the first player's snake
            self.tail_1.append(Entity(self.tail_1[len(self.tail_1) - 1].x * self.director.scale, self.tail_1[len(self.tail_1) - 1 * self.director.scale].y, 9 * self.director.scale, 9 * self.director.scale, self.director.p1color))

        # This conditional statement checks whether or not the apple and  head of the second snake occupy the same spot
        if self.head_2.x == self.apple.x and self.head_2.y == self.apple.y:
            # The integer value of what will be the previous X value
            prevX = self.apple.x
            # The integer value of what will be the previous Y value
            prevY = self.apple.y
            # The integer value of what will be the new current X value. It is randomly generated
            currX = myround(random.randint(0, self.w / 10 - 10 * self.director.scale), 10 * self.director.scale) * 10 + 1 * self.director.scale
            # This loop checks if the previous X value and the newly generated X value are the same, if so it will
            # generate a new one until they no longer match. This stops the apple from spawning in place
            while prevX == currX:
                currX = myround(random.randint(0, self.w / 10 - 10 * self.director.scale), 10 * self.director.scale) * 10 + 1 * self.director.scale
            # The integer value of what will be the new current Y value. It is randomly generated
            currY = myround(random.randint(0, self.h / 10 - 10 * self.director.scale), 10 * self.director.scale) * 10 + 1 * self.director.scale
            # This loop checks if the previous Y value and the newly generated Y value are the same, if so it will
            # generate a new one until they no longer match. This stops the apple from spawning in place
            while prevY == currY:
                currY = myround(random.randint(0, self.h / 10 - 10 * self.director.scale), 10 * self.director.scale) * 10 + 1 * self.director.scale
            # The next 11 lines essentially do what the previous lines have except it checks each segements of the tail
            # so that the apple doesn't spawn in one of their spots
            for i in self.tail_2:
                if currX == i.x and currY == i.y:
                    spaceEmpty = False
                    while not spaceEmpty and prevX != currX and prevY != currY:
                        currX = myround(random.randint(0, self.w / 10 - 10 * self.director.scale), 10 * self.director.scale) * 10 + 1 * self.director.scale
                        currY = myround(random.randint(0, self.h / 10 - 10 * self.director.scale), 10 * self.director.scale) * 10 + 1 * self.director.scale
                        for j in self.tail_2:
                            if currX == j.x and currY == j.y:
                                spaceEmpty = False
                                break
                            spaceEmpty = True

            # Once all has been said and done the apple's x and y values are changed to currX and currY
            self.apple.x = currX
            self.apple.y = currY

            # A new segment is added to the end of the first player's snake
            self.tail_2.append(Entity(self.tail_2[len(self.tail_2) - 1].x * self.director.scale, self.tail_2[len(self.tail_2) - 1 * self.director.scale].y, 9 * self.director.scale, 9 * self.director.scale, self.director.p2color))

    def is_collide(self):
        # This conditional statement checks if the head of the two snakes occupy the same space. If so it sets the
        # player draw variable to true and ends the execution of the method
        if self.head_1.x == self.head_2.x and self.head_1.y == self.head_2.y:
            self.plyrdraw = True
            # Causes the currently playing song to stop playing
            pygame.mixer.music.stop()
            return

        # This loop iterates through each tail segment in the first snake's tail
        for i in self.tail_1:
            # This conditional statement checks if the current tail segment and the head of the second snake occupy the
            # same space. If so it sets the player one wins variable to true
            if self.head_2.x == i.x and self.head_2.y == i.y:
                self.plyronewins = True
                # Causes the currently playing song to stop playing
                pygame.mixer.music.stop()
                return
            # This conditional statement checks if the first snake's head has gone out of bounds and if so then it sets
            # the player two wins variable to true
            if self.head_1.x == i.x and self.head_1.y == i.y or self.head_1.x < 0 or self.head_1.x > self.w or self.head_1.y < 0 or self.head_1.y > self.h:
                self.plyrtwowins = True
                # Causes the currently playing song to stop playing
                pygame.mixer.music.stop()
                return

        # This loops iterates through each tail segment in the second snake's tail
        for i in self.tail_2:
            # This conditional statement checks if the current tail segment and the head of the first snake occupy the
            # same space. If so it sets the player two wins variable to true
            if self.head_1.x == i.x and self.head_1.y == i.y:
                self.plyrtwowins = True
                # Causes the currently playing song to stop playing
                pygame.mixer.music.stop()
                return
            # This conditional statement checks if the second snake's head has gone out of bounds and if so then it sets
            # the player one wins variable to true
            if self.head_2.x == i.x and self.head_2.y == i.y or self.head_2.x < 0 or self.head_2.x > self.w or self.head_2.y < 0 or self.head_2.y > self.h:
                self.plyronewins = True
                # Causes the currently playing song to stop playing
                pygame.mixer.music.stop()
                return
