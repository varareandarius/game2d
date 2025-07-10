import pygame
from player import player_body, player_body_color, player_speed
from screenmessage import display_message
from prime import checkPrime
from palindrome import checkPalindrome
from denominator import highest_denominator

pygame.init()
screen = pygame.display.set_mode((1600, 800))
clock = pygame.time.Clock()
running = True

isThisPrime = 31
myString = "racecar"
first_number = 15
second_number = -12

player_speed = 10  # Speed of the player



x = 300
y = 300
width = 100
height = 100

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((124, 124, 124))  
    left_wall = pygame.draw.rect(screen, (0,0,0), (1,0,2,800), 0)
    right_wall = pygame.draw.rect(screen, (0,0,0), (1599,0,2,800), 0)
    top_wall = pygame.draw.rect(screen, (0,0,0), (0,1,1600,2), 0)
    bottom_wall = pygame.draw.rect(screen, (0,0,0), (0,798,1600,2), 0)

    character = pygame.draw.rect(screen, player_body_color, player_body, 0, 50)


    prime_scene = pygame.draw.rect(screen, (0,0,0), (50, 50, 100, 100), 0)

    if character.colliderect(prime_scene):
        display_message(screen, "Number is " + str(isThisPrime) + " having the prime status: " + str(checkPrime(isThisPrime)) , (800, 400), color=(255, 255, 255), font_size=30)

    palindrome_scene = pygame.draw.rect(screen, (0,0,0), (200, 50, 100, 100), 0)

    if character.colliderect(palindrome_scene):
        display_message(screen, "String is " + myString + " having the palindrome status: " + str(checkPalindrome(myString)), (800, 400), color=(255, 255, 255), font_size=30)
    
    denominator_scene = pygame.draw.rect(screen, (0,0,0), (350, 50, 100, 100), 0)

    if( first_number == 0 or second_number == 0):
        denominator_string = highest_denominator(first_number, second_number)
    else:
        denominator_string = "For " + str(first_number) + " and " + str(second_number) + " the highest common denominator is " + str(highest_denominator(first_number, second_number))

    if character.colliderect(denominator_scene):
        display_message(screen, denominator_string, (800, 400), color=(255, 255, 255), font_size=30)

    position_scene = pygame.draw.rect(screen, (0,0,0), (500, 50, 100, 100), 0)

    word_scene = pygame.draw.rect(screen, (0,0,0), (650, 50, 100, 100), 0)

    bubble_scene = pygame.draw.rect(screen, (0,0,0), (800, 50, 100, 100), 0)

    merge_scene = pygame.draw.rect(screen, (0,0,0), (950, 50, 100, 100), 0)

    fibonacci_scene = pygame.draw.rect(screen, (0,0,0), (1100, 50, 100, 100), 0)

    nth_prime_scene = pygame.draw.rect(screen, (0,0,0), (1250, 50, 100, 100), 0)

    factorial_scene = pygame.draw.rect(screen, (0,0,0), (1400, 50, 100, 100), 0)

    frequency_scene = pygame.draw.rect(screen, (0,0,0), (50, 450, 100, 100), 0)

    power_scene = pygame.draw.rect(screen, (0,0,0), (200, 450, 100, 100), 0)

    triee_scene = pygame.draw.rect(screen, (0,0,0), (350, 450, 100, 100), 0)

    #display the player body
    

    pygame.display.flip()  # Update the display

    keys = pygame.key.get_pressed()
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and character.colliderect(left_wall) == False:
        player_body.x -= player_speed
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and character.colliderect(right_wall) == False:
        player_body.x += player_speed
    if keys[pygame.K_UP] or keys[pygame.K_w] and character.colliderect(top_wall) == False:
        player_body.y -= player_speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s] and character.colliderect(bottom_wall) == False:
        player_body.y += player_speed

    clock.tick(60)  # Limit to 60 frames per second

pygame.quit()
exit(0)