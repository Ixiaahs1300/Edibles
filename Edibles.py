from Entity import *
import random


"""
This is how you do multi-line
comments bro
"""



#Initialization
pygame.init()
pygame.display.set_caption("Edibles")
pygame.display.set_icon(pygame.image.load("images\ed.png"))
done = False
fps = 15
font = pygame.font.Font("fonts\Condition.ttf", 45)
#scale = current res / 400 used to scale stuff
text = font.render("Game Over...", True, (255, 255, 255))
clock = pygame.time.Clock()
screen = pygame.display.set_mode((400, 400))
screen_rect = screen.get_rect()
w, h = pygame.display.get_surface().get_size()
dx = 10
dy = 0

head = Entity(1, 1, (w / 40) - 1, (w / 40) - 1, (41, 237, 41))
apple = Entity(11, 11, (w / 40) - 1, (w / 40) - 1, (255, 44, 44))
tail_1 = []

gameOver = False
#GameState Variables #Snake1 Variables #Snake2 Variables


def did_eat():
    if head.x == apple.x and head.y == apple.y:
        # set position of apple
        apple.x = random.randint(0, w / 10 - 1) * 10 + 1
        apple.y = random.randint(0, h / 10 - 1) * 10 + 1
        tail_1.append(Entity(tail_1[len(tail_1) - 1].x, tail_1[len(tail_1) - 1].y, w / 40 - 1, w / 40 - 1, (41, 237, 41)))

def draw_grid():
    for i in range(40):  # draw vertical grid lines
        pygame.draw.line(screen, (56, 56, 56), (i * (w / 40), 0), (i * (w / 40), h))

    for i in range(40):  # draw horizontal grid lines
        pygame.draw.line(screen, (56, 56, 56), (0, i * (h / 40)), (w, i * (h / 40)))


for i in range(1, 3):
    tail_1.append(Entity(head.x - (w / 40) * i, head.y, (w / 40) - 1, (w / 40) - 1, (41, 237, 41)))


#print the tail
def print_tail():
    for i in range(len(tail_1)):
        pygame.draw.rect(screen, tail_1[i].color, tail_1[i].rect())


while not done:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w and dy == 0:
            dy = -(w / 40)
            dx = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s and dy == 0:
            dy = (w / 40)
            dx = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a and dx == 0:
            dx = -(w / 40)
            dy = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d and dx == 0:
            dx = (w / 40)
            dy = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            pygame.transform.scale(screen, (800, 800))

    # isCollide
    for i in tail_1:
        if head.x == i.x and head.y == i.y or head.x < 0 or head.x > w or head.y < 0 or head.y > h:
            dx = 0
            dy = 0
            gameOver = True
            screen.blit(text, text.get_rect(center=screen_rect.center))

    if not gameOver:
        screen.fill((0, 0, 0))

        draw_grid()

        did_eat()

        #update position of tail elements
        for i in range(len(tail_1) - 1, 0, -1):
            tail_1[i].x = tail_1[i - 1].x
            tail_1[i].y = tail_1[i - 1].y
        tail_1[0].x, tail_1[0].y = (head.x, head.y)

        head.x += dx
        head.y += dy
        apple.draw(screen)
        head.draw(screen)
        print_tail()
    pygame.display.flip()
    clock.tick(fps)
