import pygame

class Player:
    color   = (255, 255, 255)
    size    = (20, 30)
    gravity = 1.5


    def __init__(self, x, y):
        self.vel_x = 0
        self.vel_y = 0
        self.x = x
        self.y = y
        self.dir = "left"
        self.isHit = False
        self.fall_count = 0
        self.jump_count = 0
        self.isDead = False

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.size[0], self.size[1]))

    def jump(self):
        pass

    def hit(self):
        pass

    def stop(self):
        self.vel_x = 0
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_left(self, vel):
        self.vel_x = -vel
        if self.dir != "left":
            self.dir = "left"

    def move_right(self, vel):
        self.vel_x = vel
        if self.dir != "right":
            self.dir = "right"

    def loop(self, fps):
        self.vel_y += min(1, (self.fall_count / fps) * self.gravity)
        self.move( self.vel_x, self.vel_y )

        #self.fall_count += 1