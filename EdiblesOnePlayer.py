from Scene import *
from Entity import *
import random
from PAdLib import rrect
from pygame import gfxdraw

# This class represents the standard One Player Mode of Snake. The player starts off with two tail segments and must
# move around the grid, trying to eat more apples so that it can gain more segments. If it collides with the edge of the
# window, its Game Over. If the snake's head collides with it's own body, it's also Game Over.

class EdiblesOnePlayer(Scene):
    # Initializes the Edibles One Player Object
    def __init__(self, director):
        Scene.__init__(self, director)
        # The change in the x position of the snake
        self.dx = 10 * director.scale
        # The change in the y position of the snake
        self.dy = 0
        # Creates a surface with the specified text printed on it using the font specified, in this case "font"
        self.text = director.font.render("Game Over...", True, (255, 255, 255))
        # This is a rectangle object with the size being the same as the size of the game window size
        self.screen_rect = director.screen.get_rect()
        # These variables hold the width and height of the game window, respectively
        self.w, self.h = pygame.display.get_surface().get_size()
        # The Entity object representing the head of the snake
        self.head = Entity(0 + 1 * director.scale, 1 * director.scale, 9 * director.scale, 9 * director.scale, director.p1color) #added to 0 to show that their is an initial position
        # The Entity object representing the apple
        self.apple = Entity(0 + 11 * director.scale, 11 * director.scale, 9 * director.scale, 9 * director.scale, (255, 44, 44))
        # A list holding the tail segments of the snake
        self.tail = []
        # The boolean value telling whether or not a "Game Over" state has been triggered
        self.gameOver = False
        # The font and size for the GUI and "Game Over" text
        self.plyr = pygame.font.Font("fonts\Condition.ttf", 20 * director.scale)
        # The text object is being changed to print the text "ctrl"
        self.txt = self.plyr.render("ctrl", True, (255, 255, 255))

        # This starts off the snake with two tail segments
        for i in range(1, 3):
            self.tail.append(Entity(self.head.x - 10 * i * director.scale, self.head.y * director.scale, 9 * director.scale, 9 * director.scale, self.director.p1color))

    def on_event(self, event):
        # This conditional statement that if either the W or Up key is pressed down and if the snake is not moving on
        # the y-axis then have it start moving up on the y axis cease movement on the x axis
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_w or event.key == pygame.K_UP) and self.dy == 0:
            self.dy = -10 * self.director.scale
            self.dx = 0
        # This conditional statement that if either the S or Down key is pressed down and if the snake is not moving on
        # the y-axis then have it start moving down on the y axis cease movement on the x axis
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_s or event.key == pygame.K_DOWN) and self.dy == 0:
            self.dy = 10 * self.director.scale
            self.dx = 0
        # This conditional statement that if either the A or Left key is pressed down and if the snake is not moving on
        # the x-axis then have it start moving left on the x axis cease movement on the y axis
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_a or event.key == pygame.K_LEFT) and self.dx == 0:
            self.dx = -10 * self.director.scale
            self.dy = 0
        # This conditional statement that if either the D or Right key is pressed down and if the snake is not moving on
        # the x-axis then have it start moving right on the x axis cease movement on the y axis
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and self.dx == 0:
            self.dx = 10 * self.director.scale
            self.dy = 0
        # This conditional statement checks if the R key is pressed down and if so then it will restart the scene by
        # changing the current scene to a new instance of the EdiblesOnePlayer object
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            # Causes the currently playing song to stop playing
            pygame.mixer.music.stop()
            self.director.change_scene(EdiblesOnePlayer(self.director))
            # Loads the song
            pygame.mixer.music.load("music\snakesong.wav")
            # Plays the loaded song indefinitely
            pygame.mixer.music.play(-1)
        # This conditional statement checks if either of the control buttons are pressed down and if so then it will
        # change the scene to the first scene in the scenes array, the Title Screen. It then resets the One Player
        # Mode by replacing the One Player Mode with a new instance
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL):
            self.director.change_scene(self.director.scenes[0])
            # Causes the currently playing song to stop playing
            pygame.mixer.music.stop()
            self.director.scenes[1] = EdiblesOnePlayer(self.director)

    def on_update(self):
        # The fps (frames per second) is set to 15
        self.director.fps = 15

        # Calling of the is_collide function
        self.is_collide()

        # The code in this conditional statement executes if a gameOver has not been achieved
        if not self.gameOver:

            # Calling of the did_eat function
            self.did_eat()

            # update position of self.tail elements
            for i in range(len(self.tail) - 1, 0, -1):
                self.tail[i].x = self.tail[i - 1].x
                self.tail[i].y = self.tail[i - 1].y
            self.tail[0].x, self.tail[0].y = (self.head.x, self.head.y)
            # The following two lines update the x and y position of the snake's head
            self.head.x += self.dx
            self.head.y += self.dy
            # The following three lines ensure that the head and tail of the snake are the proper color as the color
            # can change if the player picks a new color on the configuration screen
            self.head.color = self.director.p1color
            for i in self.tail:
                i.color = self.director.p1color

    def on_draw(self, screen):
        # Changes every pixel in the window to black. This is done to wipe the screen and set it up for drawing a new
        # frame
        self.director.screen.fill((0, 0, 0))
        # Calls the draw_grid function
        self.draw_grid(screen)
        # Calls the apple Entity's draw function
        self.apple.draw(screen)
        # Calls the head Entity's draw function
        self.head.draw(screen)
        # Calls the print_tail function
        self.print_tail(screen)
        # This conditional statement is executed if the gameOver boolean has been set to true
        if self.gameOver:
            # The text "Game Over" is printed to the middle of the screen
            screen.blit(self.text, self.text.get_rect(center=self.screen_rect.center))
            # draws a round rectangle to the top left corner of the screen
            rrect(screen, (255, 255, 255), pygame.Rect(0 * self.director.scale, 0 * self.director.scale, 63 * self.director.scale, 30 * self.director.scale), 9 * self.director.scale, 3 * self.director.scale)
            # Prints the text to the screen at the specified coordinates
            screen.blit(self.txt, (25 * self.director.scale, 7 * self.director.scale))
            #Draws a filled triangle to the screen with the points being at the specified coordinates
            gfxdraw.filled_trigon(screen, 5 * self.director.scale, 15 * self.director.scale, 20 * self.director.scale, 22 * self.director.scale, 20 * self.director.scale, 8 * self.director.scale, (255, 150, 44))
            #Draws an anti-aliased triangle outline with the points being at the specified coordinates
            gfxdraw.aatrigon(screen, 5 * self.director.scale, 15 * self.director.scale, 20 * self.director.scale, 22 * self.director.scale, 20 * self.director.scale, 8 * self.director.scale, (255, 150, 44))

    def print_tail(self, screen):
            # This draws each of the snake's tail segments to the screen
            for i in range(len(self.tail)):
                pygame.draw.rect(screen, self.tail[i].color, self.tail[i].rect())

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
        # This conditional statement checks if the snake's head and the apple occupy the same spot
        if self.head.x == self.apple.x and self.head.y == self.apple.y:
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
            for i in self.tail:
                if currX == i.x and currY == i.y:
                    spaceEmpty = False
                    while not spaceEmpty and prevX != currX and prevY != currY:
                        currX = myround(random.randint(0, self.w / 10 - 10 * self.director.scale), 10 * self.director.scale) * 10 + 1 * self.director.scale
                        currY = myround(random.randint(0, self.h / 10 - 10 * self.director.scale), 10 * self.director.scale) * 10 + 1 * self.director.scale
                        for j in self.tail:
                            if currX == j.x and currY == j.y:
                                spaceEmpty = False
                                break
                            spaceEmpty = True
            # Once all has been said and done the apple's x and y values are changed to currX and currY
            self.apple.x = currX
            self.apple.y = currY

            # A new segment is added to the end of the snake
            self.tail.append(Entity(self.tail[len(self.tail) - 1].x * self.director.scale, self.tail[len(self.tail) - 1 * self.director.scale].y, 9 * self.director.scale, 9 * self.director.scale, self.director.p1color))

    # Checks to see if a collision has occured
    def is_collide(self):

        # Checks if the snake's head is outside the boundaries of the game window. If so, it stops the movement of the
        # snake in the x and y axis, halting it, and then sets the gameOver boolean to true
        if self.head.x < 0 or self.head.x > self.w or self.head.y < 0 or self.head.y > self.h:
            self.dx = 0
            self.dy = 0
            self.gameOver = True
            pygame.mixer.music.stop()


        # This loop goes through each tail in the snake and checks if the snake's head has collided with it. If so,
        # it stops the movement of the snake in the x and y axis, halting it, and then sets the gameOver boolean to true
        for i in self.tail:
            if self.head.x == i.x and self.head.y == i.y:
                self.dx = 0
                self.dy = 0
                self.gameOver = True
                pygame.mixer.music.stop()

    # Function for rounding numbers to multiples of a specified number, that number being the "base" value
    def myround(self, x, base=5):
        return int(base * round(float(x) / base))
