import pygame
import random
pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Arial', 20)
screen = pygame.display.set_mode((500, 500))
head = (25, 25)
body = [(24, 25)]
food = (random.randint(0, 50), random.randint(0, 50))
direction = (1, 0)
white = pygame.Surface((10, 10))
red = pygame.Surface((10, 10))
white.fill((255, 255, 255))
red.fill((255, 0, 0))
step = False
run = True
clock = pygame.time.Clock()
gameover = False
while not gameover:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP and not direction == (0, 1):
                direction = (0, -1)
            if event.key == pygame.K_DOWN and not direction == (0, -1):
                direction = (0, 1)
            if event.key == pygame.K_RIGHT and not direction == (-1, 0):
                direction = (1, 0)
            if event.key == pygame.K_LEFT and not direction == (1, 0):
                direction = (-1, 0)
            if event.key == pygame.K_SPACE:
                run = not run
            if event.key == pygame.K_f:
                step = True
            if event.key == pygame.K_r:
                head = (25, 25)
                body = [(24, 25)]
                food = (random.randint(0, 50), random.randint(0, 50))
                direction = (1, 0)
            if event.key == pygame.K_a:
                body.append(body[-1])
            if event.key == pygame.K_d:
                body.pop(-1)
    if step or run:
        body.append(head)
        body.pop(0)
        head = (head[0]+direction[0], head[1]+direction[1])
        if head in body:
            gameover = True
        for i in range(len(body)):
            if body[i][0] > 49:
                body[i] = (0, body[i][1])
            if body[i][0] < 0:
                body[i] = (49, body[i][1])
            if body[i][1] > 49:
                body[i] = (body[i][0], 0)
            if body[i][1] < 0:
                body[i] = (body[i][0], 49)
        if head[0] > 49:
            head = (0, head[1])
        if head[0] < 0:
            head = (49, head[1])
        if head[1] > 49:
            head = (head[0], 0)
        if head[1] < 0:
            head = (head[0], 49)
        if step:
            step = False
    if head == food:
        food = (random.randint(0, 50), random.randint(0, 50))
        body.append(body[-1])
    screen.fill((0, 0, 0))
    b = font.render(str(body), True, (255, 255, 255))
    if b.get_width() > 500:
        b = font.render(str(len(body)), True, (255, 255, 255))
    screen.blit(b, (0, 0))
    screen.blit(a := font.render(f"{head}, {direction}",
                True, (255, 255, 255)), (0, 20))
    screen.blit(font.render(f", {food}", True,
                (255, 0, 0)), (a.get_width(), 20))
    screen.blit(white, (head[0]*10, head[1]*10))
    for i in body:
        screen.blit(white, (i[0]*10, i[1]*10))
    screen.blit(red, (food[0]*10, food[1]*10))
    clock.tick(10)
    pygame.display.update()
