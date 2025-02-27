import pygame
from classes.stocks import Stock
from classes.window import Window

if __name__ == "__main__":
    pygame.init()

    apple_obj = Stock("AAPL", "2025-01-01", "2025-02-01")
    window_obj = Window(800, 800, "Stonky Wid It")

    # print(apple_obj.stock_data)
    print(apple_obj.max_y_val)
    print(apple_obj.min_y_val)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            window_obj.screen.fill("black")
            window_obj.draw_axes(apple_obj.min_y_val, apple_obj.max_y_val)

            pygame.display.flip()  # Update the full display Surface to the screen
            window_obj.clock.tick(60)  # Caps fps to 60

    pygame.quit()
