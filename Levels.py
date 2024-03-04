from Objects import Ground

class Map:
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.map = []

    def draw(self, win, offset_x):
        for i, row in enumerate(self.map):
            for j, col in enumerate(row):
                if col != 0:
                    col.draw(win, offset_x)

    def ground_blocks(self, floor_size):
        for i, row in enumerate(self.map):
            for j, col in enumerate(row):
                if col == 1:
                    self.map[i][j] = Ground(((j-1) * floor_size), (i * floor_size), floor_size)

        return self.map

    def vertical_collision(self, player, dy):
        collided_obj = []

        for i, row in enumerate(self.map):
            for j, obj in enumerate(row):
                if obj != 0:
                    if player.rect.colliderect(obj.rect):

                        if player.rect.bottom >= obj.rect.top and dy > 0:
                            player.rect.bottom = obj.rect.top
                            player.landed()
                        elif player.rect.top <= obj.rect.bottom and dy < 0:
                            player.rect.top = obj.rect.bottom
                            player.hit_head()

                collided_obj.append(obj)

        return collided_obj

    def horizontal_collision(self, player, dx):
        player.move(dx, 0)
        # player.update()
        collided_obj = None
        didcolide = False

        for i, row in enumerate(self.map):
            if not didcolide:
                for j, obj in enumerate(row):
                    if not didcolide:
                        if obj != 0:
                            if player.rect.colliderect(obj.rect):
                                collided_obj = obj
                                didcolide = True

        player.move(-dx, 0)
        # player.update()
        return collided_obj


class Level1(Map):

    def __init__(self, name= "level1"):
        super().__init__(name)
        self.map = [
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
        ]


class Level2(Map):

    def __init__(self):
        super().__init__()
        self.map = [
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]