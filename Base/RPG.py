import arcade
import random
import os

#Created Classes
import Overlay

CHARACTER_SCALING = 1.0
TILE_SCALING = 1.25
COIN_SCALING = 0.25
SPRITE_PIXEL_SIZE = 128
GRID_PIXEL_SIZE = (SPRITE_PIXEL_SIZE * TILE_SCALING)
MOVEMENT_SPEED = 15
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
LEFT_VIEWPORT_MARGIN = 250
RIGHT_VIEWPORT_MARGIN = 250
BOTTOM_VIEWPORT_MARGIN = 100
TOP_VIEWPORT_MARGIN = 100

class RPG(arcade.Window):

    def __init__(self, width, height, title):
        #Initialize the game
        super().__init__(width, height, title, resizable=False)
        #variables that will hold sprite lists:
        self.player_list = None

        #player info:
        self.player_sprite = None

        self.coin_list = None
        self.wall_list = None
        self.background_list = None
        self.physics_engine = None

        self.view_bottom = 0
        self.view_left = 0

        #Overlay Usage
        self.overlay_dialogue_string = "Testing"
        self.speaker = "Karen"

        #Set background color and center window
        arcade.set_background_color(arcade.csscolor.BURLYWOOD)

    def setup(self):
        # Create your sprites and sprite lists here
        #sprite list:
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.background_list = arcade.SpriteList()

        #player setup:
        self.player_sprite = arcade.Sprite("Images/PlayerSprites/RachelRight.png", CHARACTER_SCALING)
        self.player_sprite.center_x = 384
        self.player_sprite.center_y = 5500
        self.player_list.append(self.player_sprite)

        # Set up overlay class
        self.overlay = Overlay.Overlay()
        self.overlay.load_media()

        #setup map:
        map_name = "maps/overworld.tmx"
        platforms_layer_name = 'walls'
        my_map = arcade.tilemap.read_tmx(map_name)

        #set up walls
        self.wall_list = arcade.tilemap.process_layer(map_object = my_map,
                                              layer_name = platforms_layer_name,
                                              scaling = TILE_SCALING)

        #set up background objects:
        self.background_list = arcade.tilemap.process_layer(my_map, "Background", TILE_SCALING)

        #setup background:
        if my_map.background_color:
            arcade.set_background_color(my_map.background_color)
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)
        self.view_bottom = 0
        self.view_left = 0

    def on_draw(self):
        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()
        self.background_list.draw()
        self.wall_list.draw()
        self.player_list.draw()

        # Overlay
        # self.overlay.draw_dialogue_box_template(self.overlay_dialogue_string, self.view_bottom, self.view_left)
        self.overlay.draw_dialogue_box(self.overlay_dialogue_string, self.speaker, self.view_bottom, self.view_left)
        #User Hitpoints and Energy (Top left)
        self.overlay.draw_player_info(100, 100, self.view_bottom, self.view_left)

    def on_update(self, delta_time):
        #movement logic and game logic goes here:

        self.physics_engine.update()

        # --- Manage Scrolling ---

        # Keep track of if we changed the boundary. We don't want to call the
        # set_viewport command if we didn't change the view port.
        changed = False
        #left:
        left_boundary = self.view_left + LEFT_VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True
        #right:
        right_boundary = self.view_left + SCREEN_WIDTH - RIGHT_VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True
        #up:
        top_boundary = self.view_bottom + SCREEN_HEIGHT - TOP_VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True
        #down:
        bottom_boundary = self.view_bottom + BOTTOM_VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        if changed:
            self.view_bottom = int(self.view_bottom)
            self.view_left = int(self.view_left)
            arcade.set_viewport(self.view_left, SCREEN_WIDTH + self.view_left,
                                self.view_bottom, SCREEN_HEIGHT + self.view_bottom)

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
        #Hiding and showing the dialogue box currently
        elif key == arcade.key.KEY_1:
            self.overlay.showDialogueBox = False
        elif key == arcade.key.KEY_2:
            self.overlay.showDialogueBox = True
            self.overlay_dialogue_string = "New string to show"
        elif key == arcade.key.KEY_3:
            self.overlay.showUI = False
        elif key == arcade.key.KEY_4:
            self.overlay.showUI = True
            self.overlay_dialogue_string = "Brought back the UI"

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
