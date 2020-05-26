import arcade

import os

class RPG(arcade.Window):

    def __init__(self, width, height, title):
        #Initialize the game
        super().__init__(width, height, title, resizable=False)
        #Set background color and center window
        arcade.set_background_color(arcade.color.ARSENIC)

    def setup(self):
        # Create your sprites and sprite lists here
        pass

    def on_draw(self):
        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

def main():
    game = RPG(1280, 720, "Korona Kingdom")
    # Center Window no longer works?
    # https://arcade.academy/arcade.html#arcade.Window
    # game.center_window()
    game.setup()
    arcade.run()

#Run the game with this file
if __name__ == "__main__":
    main()


