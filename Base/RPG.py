import arcade
import random
import os

SPRITE_SCALING = 0.5
MOVEMENT_SPEED = 5
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
VIEWPORT_MARGIN = 40
NUMBER_OF_TREES = 75

class RPG(arcade.Window):

    def __init__(self, width, height, title):
        #Initialize the game
        super().__init__(width, height, title, resizable=False)
        #variables that will hold sprite lists:
        self.all_sprites_list = None

        #player info:
        self.player_sprite = None

        self.coin_list = None
        self.wall_list = None
        self.physics_engine = None

        self.view_bottom = 0
        self.view_left = 0
        #Set background color and center window
        arcade.set_background_color(arcade.color.ARSENIC)

    def setup(self):
        # Create your sprites and sprite lists here
        #sprite list:
        self.all_sprites_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        #player setup:
        self.player_sprite = arcade.Sprite("Images/PlayerSprites/RachelRight.png", 1.0)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 64

         # Create a series of horizontal tree walls
        for y in range(0, 800, 200):
            for x in range(100, 700, 64):
                wall = arcade.Sprite("Images/NPCS/tree.png", 1.0)
                wall.center_x = x
                wall.center_y = y
                self.wall_list.append(wall)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)
        self.view_bottom = 0
        self.view_left = 0

    def on_draw(self):
        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()
        self.wall_list.draw()
        self.player_sprite.draw()

    def on_update(self, delta_time):
        #movement logic and game logic goes here:

        self.physics_engine.update()

        # --- Manage Scrolling ---

        # Keep track of if we changed the boundary. We don't want to call the
        # set_viewport command if we didn't change the view port.
        changed = False

        # Scroll left
        left_boundary = self.view_left + VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        # Scroll right
        right_boundary = self.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        # Scroll up
        top_boundary = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        self.view_left = int(self.view_left)
        self.view_bottom = int(self.view_bottom)

        # If we changed the boundary values, update the view port to match
        if changed:
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)

        # Call update to move the sprite
        #self.player_list.update()

    def on_key_press(self, key, modifiers):
        #Called whenever a key is pressed
        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        #Called when the user releases a key
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

def main():
    game = RPG(SCREEN_WIDTH, SCREEN_HEIGHT, "Korona Kingdom")
    # Center Window no longer works?
    # https://arcade.academy/arcade.html#arcade.Window
    # game.center_window()
    game.setup()
    arcade.run()

#Run the game with this file
if __name__ == "__main__":
    main()
