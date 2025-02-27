import pygame


class Window:
    PADDING = 50

    def __init__(self, WIDTH: int, HEIGHT: int, CAPTION: str):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.CAPTION = CAPTION

        self.screen: pygame.Surface = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock: pygame.time.Clock = pygame.time.Clock()

        self.pan_offset_x = 0
        self.y_axis_length = self.HEIGHT - (2 * Window.PADDING)


    def draw_axes(self, min_y_val, max_y_val):
        # pygame.draw.line(
        #     self.screen,
        #     "white",
        #     [30, 20],
        #     [30, 780]
        # )

        # This will allow for the range to be dynamically updated based on the max, min values
        scale = self.y_axis_length / (max_y_val - min_y_val) 

        # Draw Y-axis
        pygame.draw.line(
            self.screen,
            "white",
            (self.pan_offset_x + Window.PADDING, Window.PADDING),
            (self.pan_offset_x + Window.PADDING, Window.PADDING + self.y_axis_length),
            2,
        )

        # Label Y-Axis
        for i in range(int(min_y_val), int(max_y_val) + 1, 5):
            curr_y_pos = (self.HEIGHT - Window.PADDING) - (i - min_y_val) * scale
            pygame.draw.line(
                self.screen,
                "white",
                (self.pan_offset_x + Window.PADDING - 5, int(curr_y_pos)),
                (self.pan_offset_x + Window.PADDING + 5, int(curr_y_pos)),
                2,
            )

            font = pygame.font.SysFont("JetBrainsMono", 15)
            label = font.render(str(i), True, "white")
            self.screen.blit(
                label, (self.pan_offset_x + Window.PADDING - 40, int(curr_y_pos) - 10)
            )

        # Draw X-axis
        pygame.draw.line(
            self.screen,
            "white",
            (self.pan_offset_x + Window.PADDING, self.HEIGHT - Window.PADDING),
            (
                self.WIDTH + self.pan_offset_x - Window.PADDING,
                self.HEIGHT - Window.PADDING,
            ),
        )
