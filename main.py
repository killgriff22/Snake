import pygame
import random
pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Arial', 20)
screen = pygame.display.set_mode((500, 500))
#set up an arbitrary position for the snake, with the head to the left of the body
head = (25, 25)
body = [(24, 25)]
#spawn in some food somewhere
food = (random.randint(0, 50), random.randint(0, 50))
#define our direction, to the left.
direction = (1, 0)
#define some constant colors to use later
white = pygame.Surface((10, 10))
red = pygame.Surface((10, 10))
white.fill((255, 255, 255))
red.fill((255, 0, 0))
#debug stuff, pausing and stepping the "simulation" (game)
step = False
run = True
#clock for drawing the fps
clock = pygame.time.Clock()
#flag for if we need to stop the game
gameover = False
#game loop
while not gameover:
    #key logic https://www.pygame.org/docs/ref/key.html
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYUP: #listen for key release events
            # and not direction == (n, n) is to make it so you cant double back on yourself
            if event.key == pygame.K_UP and not direction == (0, 1):
                direction = (0, -1)
            elif event.key == pygame.K_DOWN and not direction == (0, -1):
                direction = (0, 1)
            elif event.key == pygame.K_RIGHT and not direction == (-1, 0):
                direction = (1, 0)
            elif event.key == pygame.K_LEFT and not direction == (1, 0):
                direction = (-1, 0)
            #"simualtion" key listenmers
            if event.key == pygame.K_SPACE: # pause/unpause
                run = not run
            elif event.key == pygame.K_f: # step forward
                step = True
            elif event.key == pygame.K_r: # reset the game, same code as before for starting, just redefining the vars from before
                head = (25, 25)
                body = [(24, 25)]
                food = (random.randint(0, 50), random.randint(0, 50))
                direction = (1, 0)
            elif event.key == pygame.K_a: # add a segment
                body.append(body[-1])
            elif event.key == pygame.K_d: # remove a segment
                body.pop(-1)
    if step or run: # if either of the debug flags are true, run a frame of simulation.
        body.append(head) # add the head to the end of the body, kind of hacky, but its not noticeable
        body.pop(0) # make the body one segment shorter, because we just added the head as a segment
        head = (head[0]+direction[0], head[1]+direction[1]) # make the new head into the first item in the list, the head goes to the back of the list so this will be the segment just before the body
        if head in body:
            gameover = True #reads plainly, this is a reason why i like python :3
        for i in range(len(body)): # peform a check on all the body segments to see if they are all in bounds, if not, wrap them around.
            if body[i][0] > 49:
                body[i] = (0, body[i][1])
            if body[i][0] < 0:
                body[i] = (49, body[i][1])
            if body[i][1] > 49:
                body[i] = (body[i][0], 0)
            if body[i][1] < 0:
                body[i] = (body[i][0], 49)
        # do that same check on the head.
        if head[0] > 49:
            head = (0, head[1])
        if head[0] < 0:
            head = (49, head[1])
        if head[1] > 49:
            head = (head[0], 0)
        if head[1] < 0:
            head = (head[0], 49)
        # end of the frame, if the step flag is what got us here, set it to false to complete the frame.
        if step:
            step = False
    # check if we have eaten the food
    if head == food:
        food = (random.randint(0, 50), random.randint(0, 50))
        body.append(body[-1])
    #rendering.
    screen.fill((0, 0, 0)) # fill the screen black
    #--debug code--
    #b = font.render(str(body), True, (255, 255, 255)) # render the body list to print to the screen
    #if b.get_width() > 500: # if the length of the text we just made is bigger than the screen size 
    #    b = font.render(str(len(body)), True, (255, 255, 255)) # overwrite that with just the length of the list.
    #screen.blit(b, (0, 0)) # blit that to the screem
    #a = font.render(f"{head}, {direction}, ", True, (255, 255, 255)) # render the head's pos and your direction as a tuple (n, n)
    #screen.blit(a, (0, 20)) # blit that to the screen
    #screen.blit(font.render(f" {food}", True, (255, 0, 0)), (a.get_width(), 20)) # render the food's pos in red and blit it next to the head and direction
    screen.blit(white, (head[0]*10, head[1]*10)) # blit the head to the screen
    for i in body:
        screen.blit(white, (i[0]*10, i[1]*10)) #blit the body to the screen
    screen.blit(red, (food[0]*10, food[1]*10)) # blit the food to the screen
    clock.tick(10) # speed is linked to fps, so we use this to lock the fps to 10.
    pygame.display.update() # tell the pygame renderer that we want to update the screen.
