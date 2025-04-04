import pygame
from classes.stocks import Stock
from classes.window import Window

if __name__ == "__main__":
    pygame.init()

    apple_obj = Stock("AAPL", "2025-01-01", "2025-02-01")
    window_obj = Window(801, 800, "Stonky Wid It")

    # print(apple_obj.stock_data)
    # print(apple_obj.max_y_val)
    # print(apple_obj.min_y_val)

    print(len(apple_obj.dates))
    print(len(apple_obj.opens))
    candles_drawn: int = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            window_obj.screen.fill("black")
            window_obj.draw_axes(
                apple_obj.min_y_val, apple_obj.max_y_val, apple_obj.dates
            )
            window_obj.draw_increment(
                apple_obj.dates,
                apple_obj.opens,
                apple_obj.highs,
                apple_obj.lows,
                apple_obj.closes,
                apple_obj.min_y_val,
            )

            candles_drawn += 1

            pygame.display.flip()  # Update the full display Surface to the screen
            window_obj.clock.tick(60)  # Caps fps to 60

    pygame.quit()
