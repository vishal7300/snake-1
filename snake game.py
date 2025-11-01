import pygame
import random
pygame.init()

screen_width =800
screen_height =600
clock=pygame.time.Clock()
screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("pygame basics 😌")
width = 1000
height = 600
block_size = 20
clock = pygame.time.Clock()
bgcolor = ("black")
running = True

snake = [(100,100)]
direction = (block_size,0)
x_val = (random.randint(0,width // block_size) * block_size)
y_val = (random.randint(0,height // block_size) * block_size)
food = (x_val,y_val)


def display_grid():
    for x in range(0,width,block_size):
        pygame.draw.line(screen,"white",(x,0),(x,height),1)

    for y in range(0,height,block_size):
        pygame.draw.line(screen,"white",(0,y),(width,y),1)





while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False


        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = (-block_size,0)
            elif event.key == pygame.K_RIGHT:
                direction = (block_size, 0)
            elif event.key == pygame.K_UP:
                direction = (0,-block_size)
            elif event.key == pygame.K_DOWN:
                direction = (0,block_size)




    screen.fill(bgcolor)

    display_grid()
    new_pose = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    if ( new_pose in snake or
            (new_pose[0] < 0 or new_pose[0] >= width) or
            (new_pose[1] < 0 or new_pose[0] >= height)
    ):
        running = False



    snake.insert(0,new_pose)
    if new_pose == food:
        x_val = random.randint(0, width // block_size-2) * block_size
        y_val = random.randint(0, height // block_size-2) * block_size
        food = (x_val, y_val)
        pygame.draw.rect(screen, "red", (food[0], food[1], block_size, block_size))
    else:
        snake.pop()


    for block in snake:
        pygame.draw.rect(screen,"green",(block[0],block[1],block_size,block_size))


    # snake[0] = new_pose
    # pygame.draw.rect(screen, 'green', (snake[0][0], snake[0][1], block_size, block_size))
    pygame.draw.rect(screen,"red",(food[0],food[1],block_size,block_size))
    pygame.display.flip()
    clock.tick(5)
