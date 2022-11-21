import pygame
  
pygame.init()
 
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Drawing Program")
  
x = 200
y = 200

width = 20
height = 20

vel = 10

run = True

while run:
    pygame.time.delay(10)
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False

    keys = pygame.key.get_pressed()
      
    # if A is pressed
    if keys[pygame.K_a] and x>0:
        # decrement in x co-ordinate
        x -= vel
          
    # if D is pressed
    if keys[pygame.K_d] and x<500-width:   
        # increment in x co-ordinate
        x += vel
         
    # if W is pressed   
    if keys[pygame.K_w] and y>0:
        # decrement in y co-ordinate
        y -= vel
          
    # if S is pressed   
    if keys[pygame.K_s] and y<500-height:
        # increment in y co-ordinate
        y += vel

    #win.fill((0,0,0))

    # drawing object on screen which is rectangle here 
    pygame.draw.rect(win, (255, 255, 255), (x, y, width, height))

    pygame.display.update() 

pygame.quit()
