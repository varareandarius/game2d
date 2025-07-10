import pygame

#display a message on the screen

def display_message(screen, message, position, color=(255, 255, 255), font_size=30):
    font = pygame.font.Font(None, font_size)
    text = font.render(message, True, color)
    text_rect = text.get_rect(center=position)
    # Desenează un dreptunghi negru sub text
    background_rect = text_rect.inflate(20, 10)  # puțin padding
    pygame.draw.rect(screen, (0, 0, 0), background_rect)
    screen.blit(text, text_rect)
    