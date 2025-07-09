import pygame

#display a message on the screen

def display_message(screen, message, position, color=(255, 255, 255), font_size=30):
    font = pygame.font.Font(None, font_size)
    text = font.render(message, True, color)
    text_rect = text.get_rect(center=position)
    screen.blit(text, text_rect)
    