import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((124, 124, 124))  
    pygame.display.flip()  # Update the display

    clock.tick(60)  # Limit to 60 frames per second

pygame.quit()
exit(0)