import pygame

class Window:
    def __init__(self, WIDTH: int, HEIGHT: int, CAPTION: str):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.CAPTION = CAPTION

        self.screen: pygame.Surface = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock: pygame.time.Clock = pygame.time.Clock()


