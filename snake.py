```python

import pygame

# COLORS
BLUE = (0,0,255) ; RED = (255,0,0) ; WHITE = (255,255,255)
BLACK = (0,0,0)

# SCREEN SIZE
SCREEN_WIDTH, SCREEN_HEIGHT = 800,600
pygame.init()
dis = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game by kig2929kig")
pygame.display.update()
game_over = False

# FRAME
clock = pygame.time.Clock()

# SNAKE
x1, y1 = 300,300
x1_change, y1_change = 0, 0

while not game_over:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            if event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            if event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10
            if event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10
    
    x1 += x1_change
    y1 += y1_change
    dis.fill(WHITE)            
    pygame.draw.rect(dis, BLUE, [x1,y1,10,10])
    
    pygame.display.update()
    clock.tick(10)
pygame.quit()
quit()

```
