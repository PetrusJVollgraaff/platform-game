import pygame

class Player:
    color   = (255, 255, 255)
    size    = (20, 30)
    gravity = 1


    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel_x = 0
        self.vel_y = 0
        self.dir = "left"
        self.isHit = False
        self.fall_count = 0
        self.jump_count = 0
        self.isDead = False
        self.rect = pygame.Rect(x, y, self.size[0], self.size[1])

    def draw(self, win, offset_x):
        self.rect.x = self.rect.x - offset_x
        pygame.draw.rect(win, self.color, self.rect)

    def jump(self):
        self.vel_y = -self.gravity * 8
        self.jump_count += 1

        if self.jump_count == 1:
            self.fall_count = 0

    def hit(self):
        pass

    def stop(self):
        self.vel_x = 0

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

        self.x = self.rect.x
        self.y = self.rect.y

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
        self.move(self.vel_x, self.vel_y)

        self.fall_count += 1

    def landed(self):
        self.fall_count = 0
        self.vel_y = 0
        self.jump_count = 0

    def hit_head(self):
        self.count = 0
        self.vel_y *= -1

    def update(self):
        self.rect = self.rect
