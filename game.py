import pygame
from player_obj import Player
#from Objects import Ground
from Levels import Level1

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

def playerhandler(player, map):
    keys = pygame.key.get_pressed()
    player.vel_x = 0

    #collide_left = map.horizontal_collision(player, -Player_vel * 3)
    #collide_right = map.horizontal_collision(player, Player_vel * 3)

    if keys[pygame.K_LEFT]:
        player.move_left(Player_vel)

    if keys[pygame.K_RIGHT]:
        player.move_right(Player_vel)

    vertical_collide = map.vertical_collision(player, player.vel_y)

def draw_onboard(win, player, map, offset_x):
    map.draw(win, offset_x)

    player.draw(win, offset_x)
    pygame.display.update()

def main(win):
    clock = pygame.time.Clock()
    run = True
    floor_size = 64

    player = Player(20, screen_height - floor_size + 2)
    level_map = Level1()
    level_map.ground_blocks(floor_size)

    offset_x = 0
    scroll_area_width = 200

    while run:
        clock.tick(FPS)
        win.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()


        player.loop(FPS)
        playerhandler(player, level_map)
        draw_onboard(win, player, level_map, offset_x)

        #if ((player.rect.right - offset_x >= screen_width - scroll_area_width) and player.vel_x > 0) or (
        #        (player.rect.right - offset_x <= scroll_area_width) and player.vel_x <= 0):
        #    offset_x += player.vel_x