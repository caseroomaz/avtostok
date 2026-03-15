import pygame
import random

pygame.init()
ekran = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Topu Tut!")

top_x = random.randint(0, 380)
top_y = 0
top_radius = 20
top_speed = 5

player_x = 200
player_y = 350
player_width = 80
player_height = 10
player_speed = 10

run = True
clock = pygame.time.Clock()

while run:
    clock.tick(30)
    ekran.fill((0,0,0))
    pygame.draw.circle(ekran, (255,0,0), (top_x, top_y), top_radius)
    pygame.draw.rect(ekran, (0,255,0), (player_x, player_y, player_width, player_height))
    
    top_y += top_speed
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < 320:
        player_x += player_speed
    
    if top_y + top_radius > player_y and player_x < top_x < player_x + player_width:
        print("Tutdunuz!")
        top_y = 0
        top_x = random.randint(0, 380)
    
    if top_y > 400:
        print("Qaçırdınız!")
        top_y = 0
        top_x = random.randint(0, 380)
    
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
