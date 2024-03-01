import pygame
class Object:
    def __init__(self, x, y, width, height, color, name=None):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.name = name
        self.color = color
        self.rect = pygame.Rect(x, y, self.width, self.height)

    def draw(self, win):
        #win.blit(self.image, (self.rect.x, self.rect.y))
        pygame.draw.rect(win, self.color, self.rect)

class Ground(Object):
    def __init__(self, x, y, size = 64):
        super().__init__(x, y, size, size, (0, 255, 0))