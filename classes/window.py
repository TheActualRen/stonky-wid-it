import pygame


class Window:
    PADDING = 50

    def __init__(self, WIDTH: int, HEIGHT: int, CAPTION: str):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.CAPTION = CAPTION

        self.screen: pygame.Surface = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock: pygame.time.Clock = pygame.time.Clock()

        self.pan_offset_x: int = 0

        self.origin_x: int = self.pan_offset_x + Window.PADDING
        self.origin_y: int = self.HEIGHT - Window.PADDING

        self.y_axis_length = self.origin_y - Window.PADDING
        self.x_axis_length = (self.WIDTH - Window.PADDING) - self.origin_x

    def draw_axes(self, min_y_val, max_y_val, dates):
        # This will allow for the range to be dynamically updated based on the max, min values
        scale_y: float = self.y_axis_length / (max_y_val - min_y_val + 1)
        scale_x: float = self.x_axis_length / (len(dates) + 2)

        # How much we increment between each label of the scale
        step: int = 1

        # Draw Y-axis
        pygame.draw.line(
            self.screen,
            "white",
            (self.origin_x, Window.PADDING), # bottom of the y-axis
            (self.origin_x, Window.PADDING + self.y_axis_length), # top of the y-axis
            2, # thickness
        )

        # Label Y-Axis
        for i in range(int(min_y_val) - 1, int(max_y_val) + 2, step):
            curr_y_pos = (self.HEIGHT - Window.PADDING + self.pan_offset_x) - (
                i - min_y_val + 1
            ) * scale_y

            # draw the tick lines on the y-axis
            pygame.draw.line(
                self.screen,
                "white",
                (self.origin_x - 5, int(curr_y_pos)),
                (self.origin_x + 5, int(curr_y_pos)),
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
            (self.pan_offset_x + Window.PADDING, self.origin_y), # start of the x-axis

            # end of the x-axis
            (
                self.WIDTH + self.pan_offset_x - Window.PADDING,
                self.origin_y,
            ),
        )

        # Label X-Axis
        for i in range(0, len(dates), 2):
            curr_x_pos = (self.pan_offset_x + Window.PADDING) + (i + 1) * scale_x

            # draw the tick lines on the x-axis
            pygame.draw.line(
                self.screen,
                "white",
                (int(curr_x_pos), self.origin_y - 5),
                (int(curr_x_pos), self.origin_y + 5),
                2,
            )

            date_label = dates[i].strftime("%m %d")

            font = pygame.font.SysFont("JetBrainsMono", 15)
            label = font.render(date_label, True, "white")
            self.screen.blit(
                label, (int(curr_x_pos) - 20, self.HEIGHT - Window.PADDING + 10)
            )
