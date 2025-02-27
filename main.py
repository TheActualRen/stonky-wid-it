import pygame
from classes.stocks import Stock
from classes.window import Window

if __name__ == "__main__":
    pygame.init()

    apple_obj = Stock("AAPL", "2025-01-01", "2025-02-01")
    window_obj = Window(800, 800, "Stonky Wid It")

    print(apple_obj.stock_data)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            window_obj.screen.fill("black")

            pygame.display.flip()
            window_obj.clock.tick(60)

    pygame.quit()
