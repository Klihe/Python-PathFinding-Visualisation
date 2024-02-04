# node.py

import math
import pygame

from modules.color import Color
from modules.config import Config

class Node:
    def __init__(self, x, y, node_start, node_end, color=Color.WHITE) -> None:
        self.x = x
        self.y = y 
        self.point = (x, y)
        self.color = color

        self.rect = pygame.Rect(x*Config.NODE_SIZE, y*Config.NODE_SIZE, Config.NODE_SIZE, Config.NODE_SIZE)

        self.node_start = node_start
        self.node_end = node_end

        self.g = 0

    def update_values(self, calc_point, calc_g=0) -> None:
        self.g = round(calc_g + math.sqrt((calc_point[0] - self.point[0])**2 + (calc_point[1] - self.point[1])**2) * 10)
        self.h = round(math.sqrt((self.node_end[0] - self.x)**2 + (self.node_end[1] - self.y)**2) * 10)
        self.f = self.g + self.h

    def draw(self, surface, font) -> None:
        pygame.draw.rect(surface, self.color, self.rect)

        if self.color == Color.GREEN or self.color == Color.RED:
            text_g = font.render(f"{round(self.g)}", None, Color.BLACK)
            text_h = font.render(f"{round(self.h)}", None, Color.BLACK)
            text_f = font.render(f"{round(self.f)}", None, Color.BLACK)
            surface.blit(text_g, (self.rect.x + Config.NODE_SIZE/20, self.rect.y + Config.NODE_SIZE/20))
            surface.blit(text_h, (self.rect.x + Config.NODE_SIZE/2, self.rect.y + Config.NODE_SIZE/20))
            surface.blit(text_f, (self.rect.x + Config.NODE_SIZE/3, self.rect.y + Config.NODE_SIZE/2))