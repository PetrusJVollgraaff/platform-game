import pygame
from player_obj import Player
from Objects import Ground

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

def handle_vertical_collision(player, objects, dy):
    collided_obj = []

    for obj in objects:
        #if pygame.sprite.collide_mask(player, obj):
        if dy > 0:
           player.rect.bottom = obj.rect.top
           player.landed()
        elif dy < 0:
            player.rect.top = obj.rect.bottom
            player.hit_head()

        collided_obj.append(obj)
    return collided_obj

def handle_horizontal_collision(player, objects, dx):
    player.move(dx, 0)
    player.update()
    collided_obj = None

    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            collided_obj = obj
            break


    player.move(-dx, 0)
    player.update()
    return collided_obj


def draw_text(win, text, color, top, left, font ):
    label = font.render(text, 1, color)

    win.blit(label, (top - (label.get_width() / 2), left - (label.get_height() / 2)))

def playerhandler(player, objects):
    keys = pygame.key.get_pressed()
    player.vel_x = 0

    if keys[pygame.K_LEFT]:
        player.move_left(Player_vel)

    if keys[pygame.K_RIGHT]:
        player.move_right(Player_vel)

    handle_vertical_collision(player, objects, player.vel_y)

def draw_onboard(win, player, objects, offset_x):
    for block in objects:
        block.draw(win, offset_x)

    player.draw(win, offset_x)
    pygame.display.update()

def main(win):
    clock = pygame.time.Clock()
    run = True
    floor_size = 64
    floor = [Ground(i * floor_size, screen_height - floor_size, floor_size)
             for i in range(-screen_width // floor_size, (screen_width * 2) // floor_size)]

    wall = [Ground(500, screen_height - (floor_size * 2), floor_size), Ground(550, screen_height - (floor_size * 3), floor_size)]
    player = Player(20, screen_height - floor_size + 2)
    #ground = Ground(150, 150, )
    objects = [*floor]
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
        playerhandler(player, objects)
        draw_onboard(win, player, objects, offset_x)

        #if ((player.rect.right - offset_x >= screen_width - scroll_area_width) and player.vel_x > 0) or (
        #        (player.rect.right - offset_x <= scroll_area_width) and player.vel_x < 0):
        #    offset_x += player.vel_x