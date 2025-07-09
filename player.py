import pygame

player_body_width = 40
player_body_height = 40

player_x, player_y = 780, 380
player_body_color = (0, 0, 255)  # Blue color for the player body
player_body = pygame.Rect(player_x, player_y, player_body_width, player_body_height)


player_speed = 4