import pygame
import ptext
from player import player_body, player_body_color, player_speed
from screenmessage import display_message
from functions import checkPrime, checkPalindrome, highest_denominator, reorder_words, reverse_each_word, bubble_sort, merge_sort, fibonacci, prime, factorial, frequency, power

isThisPrime = 31
myString = "racecar"
first_number = 15
second_number = -12
order_string = "Here we have a string that will be reordered"
arr = [5, 2, 9, 1, 5, 6, 3, 8, 7, 4, 2]
nth_fibonacci = 10
nth_prime = 27
nth_factorial = 7
base = 24
exponent = 9




screen_width = 1600
screen_height = 800
margin_offset = 1

# https://www.pygame.org/wiki/TextWrap
def drawText(surface, text, color, rect, font, aa=False, bkg=None):
    rect = pygame.Rect(rect)
    y = rect.top
    lineSpacing = -2
    rect = rect.inflate(-20, 0)
    # get the height of the font
    fontHeight = font.size("Tg")[1]

    while text:
        i = 1

        # determine if the row of text will be outside our area
        if y + fontHeight > rect.bottom:
            break

        # determine maximum width of line
        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1

        # if we've wrapped the text, then adjust the wrap to the last word      
        if i < len(text): 
            i = text.rfind(" ", 0, i) + 1

        # render the line and blit it to the surface
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)

        surface.blit(image, (rect.left, y))
        y += fontHeight + lineSpacing

        # remove the text we just blitted
        text = text[i:]

    return text


pygame.init()
screen = pygame.display.set_mode((1600, 800), pygame.NOFRAME)
clock = pygame.time.Clock()
running = True
player_speed = 10  # Speed of the player

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((124, 124, 124))  
    left_wall = pygame.draw.rect(screen, (0,0,0), (0,0,2,screen_height - margin_offset), 0)
    right_wall = pygame.draw.rect(screen, (0,0,0), (screen_width - margin_offset,0,2,screen_height), 0)
    top_wall = pygame.draw.rect(screen, (0,0,0), (0,0,screen_width,2), 0)
    bottom_wall = pygame.draw.rect(screen, (0,0,0), (0,screen_height - margin_offset,screen_width,2), 0)

    character = pygame.draw.rect(screen, player_body_color, player_body, 0, 50)


    prime_scene = pygame.draw.rect(screen, (0,0,0), (50, 50, 100, 100), 0)
    prime_string = "Number is " + str(isThisPrime) + " having the prime status: " + str(checkPrime(isThisPrime))

    if character.colliderect(prime_scene):
        display_message(screen, prime_string, (800, 400), color=(255, 255, 255), font_size=30)

    palindrome_scene = pygame.draw.rect(screen, (0,0,0), (200, 50, 100, 100), 0)
    palindrome_string = "String is \"" + myString + "\" having the palindrome status: " + str(checkPalindrome(myString))

    if character.colliderect(palindrome_scene):
        display_message(screen, palindrome_string, (800, 400), color=(255, 255, 255), font_size=30)
    
    denominator_scene = pygame.draw.rect(screen, (0,0,0), (350, 50, 100, 100), 0)

    if( first_number == 0 or second_number == 0):
        denominator_string = highest_denominator(first_number, second_number)
    else:
        denominator_string = "For " + str(first_number) + " and " + str(second_number) + " the highest common denominator is " + str(highest_denominator(first_number, second_number))

    if character.colliderect(denominator_scene):
        display_message(screen, denominator_string, (800, 400), color=(255, 255, 255), font_size=30)

    position_scene = pygame.draw.rect(screen, (0,0,0), (500, 50, 100, 100), 0)

    position_string = str(reorder_words(order_string))
    if character.colliderect(position_scene):
        display_message(screen, "Reordered string is: \"" + position_string + "\"", (800, 400), color=(255, 255, 255), font_size=30)

    word_scene = pygame.draw.rect(screen, (0,0,0), (650, 50, 100, 100), 0)
    word_string = "After reversing each word, the string is \"" + reverse_each_word(order_string) + "\""
    if character.colliderect(word_scene):
        display_message(screen, word_string, (800, 400), color=(255, 255, 255), font_size=30)

    bubble_scene = pygame.draw.rect(screen, (0,0,0), (800, 50, 100, 100), 0)
    bubble_string = "Initial array is " + str(arr) + " and after bubble sort, the array is " + str(bubble_sort(arr))

    if character.colliderect(bubble_scene):
        display_message(screen, bubble_string, (800, 400), color=(255, 255, 255), font_size=30)

    merge_scene = pygame.draw.rect(screen, (0,0,0), (950, 50, 100, 100), 0)
    merge_string = "Initial array is " + str(arr) + " and after merge sort, the array is " + str(merge_sort(arr))

    if character.colliderect(merge_scene):
        display_message(screen, merge_string, (800, 400), color=(255, 255, 255), font_size=30)

    fibonacci_scene = pygame.draw.rect(screen, (0,0,0), (1100, 50, 100, 100), 0)
    fibonacci_string = "The " + str(nth_fibonacci) + "th Fibonacci number is " + str(fibonacci(nth_fibonacci))

    if character.colliderect(fibonacci_scene):
        display_message(screen, fibonacci_string, (800, 400), color=(255, 255, 255), font_size=30)

    nth_prime_scene = pygame.draw.rect(screen, (0,0,0), (1250, 50, 100, 100), 0)
    nth_prime_string = "The " + str(nth_prime) + "st/nd/rd/th prime number is " + str(prime(nth_prime))

    if character.colliderect(nth_prime_scene):
        display_message(screen, nth_prime_string, (800, 400), color=(255, 255, 255), font_size=30)

    factorial_scene = pygame.draw.rect(screen, (0,0,0), (1400, 50, 100, 100), 0)
    factorial_string = "The factorial of " + str(nth_factorial) + " is " + str(factorial(nth_factorial))

    if character.colliderect(factorial_scene):
        display_message(screen, factorial_string, (800, 400), color=(255, 255, 255), font_size=30)

    


    #create text.in and write something to it
    with open("text.in", "w") as file:
        file.write("This is a sample text file.\n")
        file.write("It contains some sample text for demonstration purposes.\n")
        file.write("You can modify this text as needed.\n")
        file.write("Feel free to add more lines or change the content.\n")
        file.write("This is the last line of the sample text file.\n")
    
    #read all the lines from text.in and keep all text in a variable
    with open("text.in", "r") as file:
        text_content = str(file.readlines())
    
    char_freq, word_freq = frequency(text_content)
    
    frequency_scene = pygame.draw.rect(screen, (0,0,0), (50, 450, 100, 100), 0)

    if character.colliderect(frequency_scene):
        display_message(screen, str(char_freq), (800, 200), color=(255, 255, 255), font_size=30)
        word_freq_rect = pygame.draw.rect(screen, (0,0,0), (800, 400, 600, 200), 0)
        drawText(screen, str(word_freq), (255, 255, 255), word_freq_rect, pygame.font.Font(None, 30), aa=True)


    power_scene = pygame.draw.rect(screen, (0,0,0), (200, 450, 100, 100), 0)
    power_string = "The result of " + str(base) + " raised to the power of " + str(exponent) + " is " + str(power(base, exponent))

    if character.colliderect(power_scene):
        display_message(screen, power_string, (800, 400), color=(255, 255, 255), font_size=30)
    

    # add an X button to the top right corner to close the window
    close_rect = pygame.draw.rect(screen, (255, 0, 0), (screen_width - 50, 10, 40, 40), 0)
    pygame.draw.line(screen, (255, 255, 255), (screen_width - 40, 20), (screen_width - 20, 40), 5)
    pygame.draw.line(screen, (255, 255, 255), (screen_width - 20, 20), (screen_width - 40, 40), 5)
    # Check if the X button is clicked or if the 'player' rectangle collides with it
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        if (screen_width - 50 <= mouse_pos[0] <= screen_width - 10) and (10 <= mouse_pos[1] <= 50):
            running = False
    #if the 'player' rectangle collides with it
    if character.colliderect(close_rect):
        running = False

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

    if keys[pygame.K_ESCAPE]:
        running = False

    clock.tick(60)  # Limit to 60 frames per second

pygame.quit()
exit(0)