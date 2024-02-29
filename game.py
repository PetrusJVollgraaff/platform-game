import pygame
from player_obj import Player

BG_Color = (255, 255, 255)
screen_width = 800
screen_height = 700
play_width = 300 #meaning 300 // 10 = 30 width per block
play_height = 600 #meaning 600 // 10 = 60 width per block

top_left_x = (screen_width - play_width) // 2
top_left_y = screen_height - play_height

FPS = 60
Player_vel = 5

pygame.font.init()

def draw_text(win, text, color, top, left, font ):
    label = font.render(text, 1, color)

    win.blit(label, (top - (label.get_width() / 2), left - (label.get_height() / 2)))

def playerhandler(player):
    keys = pygame.key.get_pressed()
    player.vel_x = 0

    if keys[pygame.K_LEFT]:
        player.move_left(Player_vel)

    if keys[pygame.K_RIGHT]:
        player.move_right(Player_vel)

def draw_onboard(win, player):
    player.draw(win)
    pygame.display.update()

def main(win):
    clock = pygame.time.Clock()
    run = True
    player = Player(20, 20)
    while run:
        clock.tick(FPS)
        win.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()


        player.loop(FPS)
        playerhandler(player)
        draw_onboard(win, player)