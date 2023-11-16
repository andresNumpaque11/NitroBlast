import pygame
import random

from bomb import Bomb
from node import Node


class Enemy:
    
    dire = [[1,0,1], [0,1,0], [-1,0,3],[0,-1,2]]
    
    TILE_SIZE = 4
    
    def __init__(self, x, y):
        self.life = True
        self.path = []
        self.move_path = []
        self.pos_x = x * Enemy.TILE_SIZE
        self.pos_y = y * Enemy.TILE_SIZE
        self.direction = 0
        self.frame = 0
        self.animation = []
        self.range = 3
        self.bomb_limit = 1
        self.plant = False
    
    def make_move(self, map, bombs, explosions, enemy):
        if not self.life:
            return

        # Realiza una caminata aleatoria
        random.shuffle(self.dire)
        chosen_direction = self.dire[0][2]

        # Intenta moverse en la dirección aleatoria
        if chosen_direction == 0:
            self.pos_y -= 1
        elif chosen_direction == 1:
            self.pos_x += 1
        elif chosen_direction == 2:
            self.pos_y += 1
        elif chosen_direction == 3:
            self.pos_x -= 1

        if 0 <= self.pos_x < len(map) * Enemy.TILE_SIZE and 0 <= self.pos_y < len(map[0]) * Enemy.TILE_SIZE:
            pass
        if not self.life:
            return
        if len(self.move_path) == 0:
            if self.plant:
                bombs.append(self.plant_bomb(map))
                self.plant = False
                map[int(self.pos_x / Enemy.TILE_SIZE)][int(self.pos_y / Enemy.TILE_SIZE)] = 3
            
        else:
            self.direction = self.move_path[0]
            self.make_move(map, bombs, explosions, enemy)

    def plant_bomb(self, map):
        b = Bomb(self.range, round(self.pos_x / Enemy.TILE_SIZE), round(self.pos_y / Enemy.TILE_SIZE), map, self)
        self.bomb_limit -= 1
        return b

    def check_death(self, exp):

        for e in exp:
            for s in e.sectors:
                if int(self.pos_x / Enemy.TILE_SIZE) == s[0] and int(self.pos_y / Enemy.TILE_SIZE) == s[1]:
                    self.life = False
                    return
    def create_grid(self, map, bombs, explosions, enemys):
        grid = [[0] * len(map) for r in range(len(map))]

        # 0 - safe
        # 1 - unsafe
        # 2 - destryable
        # 3 - unreachable

        for b in bombs:
            b.get_range(map)
            for x in b.sectors:
                grid[x[0]][x[1]] = 1
            grid[b.pos_x][b.pos_y] = 3

        for e in explosions:
            for s in e.sectors:
                grid[s[0]][s[1]] = 3

        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == 1:
                    grid[i][j] = 3
                elif map[i][j] == 2:
                    grid[i][j] = 2

        for x in enemys:
            if x == self:
                continue
            elif not x.life:
                continue
            else:
                grid[int(x.pos_x / Enemy.TILE_SIZE)][int(x.pos_y / Enemy.TILE_SIZE)] = 2

        return grid
    def load_animations(self, en, scale):
        front = []
        back = []
        left = []
        right = []
        resize_width = scale
        resize_height = scale

        image_path = 'images/enemy/e'
        if en == '':
            image_path = 'images/hero/p'

        f1 = pygame.image.load(image_path + en + 'f0.png')
        f2 = pygame.image.load(image_path + en + 'f1.png')
        f3 = pygame.image.load(image_path + en + 'f2.png')

        f1 = pygame.transform.scale(f1, (resize_width, resize_height))
        f2 = pygame.transform.scale(f2, (resize_width, resize_height))
        f3 = pygame.transform.scale(f3, (resize_width, resize_height))

        front.append(f1)
        front.append(f2)
        front.append(f3)

        r1 = pygame.image.load(image_path + en + 'r0.png')
        r2 = pygame.image.load(image_path + en + 'r1.png')
        r3 = pygame.image.load(image_path + en + 'r2.png')

        r1 = pygame.transform.scale(r1, (resize_width, resize_height))
        r2 = pygame.transform.scale(r2, (resize_width, resize_height))
        r3 = pygame.transform.scale(r3, (resize_width, resize_height))

        right.append(r1)
        right.append(r2)
        right.append(r3)

        b1 = pygame.image.load(image_path + en + 'b0.png')
        b2 = pygame.image.load(image_path + en + 'b1.png')
        b3 = pygame.image.load(image_path + en + 'b2.png')

        b1 = pygame.transform.scale(b1, (resize_width, resize_height))
        b2 = pygame.transform.scale(b2, (resize_width, resize_height))
        b3 = pygame.transform.scale(b3, (resize_width, resize_height))

        back.append(b1)
        back.append(b2)
        back.append(b3)

        l1 = pygame.image.load(image_path + en + 'l0.png')
        l2 = pygame.image.load(image_path + en + 'l1.png')
        l3 = pygame.image.load(image_path + en + 'l2.png')

        l1 = pygame.transform.scale(l1, (resize_width, resize_height))
        l2 = pygame.transform.scale(l2, (resize_width, resize_height))
        l3 = pygame.transform.scale(l3, (resize_width, resize_height))

        left.append(l1)
        left.append(l2)
        left.append(l3)

        self.animation.append(front)
        self.animation.append(right)
        self.animation.append(back)
        self.animation.append(left)
        
        