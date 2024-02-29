
class Object:
    def __init__(self, x, y, width, height, name=None):
        super().__init__()
        self.width = width
        self.height = height
        self.name = name

    def draw(self, win):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Ground(Object):
    def __init__(self):
        super().__init__()