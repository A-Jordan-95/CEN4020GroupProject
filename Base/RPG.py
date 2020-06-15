import arcade
from numpy import random
import os
import time

#Created Classes
import Overlay
import Encounter
import Animation
import Inventory



CHARACTER_SCALING = 1.0
TILE_SCALING = 1.25
COIN_SCALING = 0.25
SPRITE_PIXEL_SIZE = 128
GRID_PIXEL_SIZE = (SPRITE_PIXEL_SIZE * TILE_SCALING)
MOVEMENT_SPEED = 5
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
        self.rand_tile_list = None
        self.wall_list = None
        self.building_list = None
        self.door_list = None
        self.background_list = None
        self.physics_engine = None

        #map info:
        self.map = "overworld"

        self.view_bottom = 0
        self.view_left = 0

        #Overlay Usage
        self.overlay = None
        self.overlay_dialogue_string = "Testing"
        self.speaker = "Karen"

        #Inventory Usage
        self.inventory = None
        self.active_inventory = False
        self.first_draw_of_inventory = True

        #encounters:
        self.encounter = None
        self.rand_range = None

        #animation:
        self.player = None

    def setup(self, x = None, y = None):

        #sprite list:
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.background_list = arcade.SpriteList()
        #self.player_list.append(self.player_sprite)



        #player setup:
        #self.player_sprite = arcade.Sprite("Images/PlayerSprites/RachelRight.png", CHARACTER_SCALING)
        self.player = Animation.PlayerCharacter()

        #setup map:
        map_name = f"maps/{self.map}.tmx"
        platforms_layer_name = 'walls'
        my_map = arcade.tilemap.read_tmx(map_name)

        #setup encounters:
        self.encounter = Encounter.Encounter()
        self.encounter.setup(self.view_bottom, self.view_left)


        if self.map == "overworld":
            self.building_list = arcade.SpriteList()
            self.rand_range = 20
            if x and y:
                self.player.center_x = x
                self.player.center_y = y
            else:
                self.player.center_x = 512
                self.player.center_y = 5000
            self.building_list = arcade.tilemap.process_layer(my_map, "buildings", TILE_SCALING)
            arcade.set_background_color(arcade.csscolor.BURLYWOOD)
        else:
            self.rand_range = 10
            self.door_list = arcade.SpriteList()
            self.player.center_x = 256
            self.player.center_y = 2960
            self.door_list = arcade.tilemap.process_layer(my_map, "doors", TILE_SCALING)
            arcade.set_background_color(arcade.csscolor.WHITE_SMOKE)

        self.player_list.append(self.player)


        # Set up overlay class
        self.overlay = Overlay.Overlay()
        self.overlay.load_media()

        #Set up Inventory Class
        self.inventory = Inventory.Inventory()

        #set up walls
        self.wall_list = arcade.tilemap.process_layer(map_object = my_map,
                                              layer_name = platforms_layer_name,
                                              scaling = TILE_SCALING)
        #set up background objects:
        self.background_list = arcade.tilemap.process_layer(my_map, "Background", TILE_SCALING)
        #setup background:
        if my_map.background_color:
            arcade.set_background_color(my_map.background_color)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player, self.wall_list)
        self.view_bottom = 0
        self.view_left = 0

    def on_draw(self):
        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()
        self.background_list.draw()
        self.wall_list.draw()
        if self.map == "overworld":
            self.building_list.draw()
        else:
            self.door_list.draw()
        self.player_list.draw()
        ## Overlay
        self.overlay.draw_dialogue_box(self.overlay_dialogue_string, self.speaker, self.view_bottom, self.view_left)
        #User Hitpoints and Energy (Top left)
        self.overlay.draw_player_info(100, 100, self.view_bottom, self.view_left)
        #User Menu Bar
        self.overlay.draw_menu_bar(self.view_bottom, self.view_left)
        #User Encounter
        if self.encounter.active_encounter:
            if self.encounter.first_draw_of_encounter:
                self.encounter.setup(self.view_bottom, self.view_left)
                self.encounter.first_draw_of_encounter = False
            self.encounter.draw_encounter()
        #User Inventory
        if self.active_inventory:
            if self.first_draw_of_inventory:
                self.inventory.setup(self.view_bottom, self.view_left)
                self.first_draw_of_inventory = False
            self.inventory.draw_inventory()

    def on_update(self, delta_time):


        #movement logic and game logic goes here:
        if self.encounter.active_encounter:
            if self.encounter.handle_selection:
                self.overlay_dialogue_string = f"you chose to {self.encounter.handle_selection()}, good luck"
                #self.encounter.handle_the_selection = False
                if self.encounter.end_encounter_on_update:
                    self.encounter.active_encounter = False
                    self.encounter.first_draw_of_encounter = True
                    self.encounter.end_encounter_on_update = False
            else:
                self.overlay_dialogue_string = "Move the selector with the arrow keys and use enter to select."
        #Using the inventory
        elif self.active_inventory:
            self.overlay.showUI = False
        else:
            self.overlay_dialogue_string = "New string to show"
            self.physics_engine.update()

            # player animation
            self.player_list.update()
            self.player_list.update_animation()

        if self.map == "overworld":
            self.rand_range = 20
            #check if building has been touched:
            building_hit_list = arcade.check_for_collision_with_list(self.player, self.building_list)
            if building_hit_list:
                player_x = self.player.center_x
                player_y = self.player.center_y
                #overworld map grid size = 5760x4480
                if player_y < 2880:
                    if player_x < 2240:
                        print("Changed map to malmart\n")
                        self.map = "MalMart"
                    else:
                        self.map = "TheSchool"
                        print("Changed map to school\n")
                else:
                    self.map = "DollarStore"
                    print("Changed map to dollar store\n")
                self.setup()
        else:
            self.rand_range = 10
            door_hit_list = arcade.check_for_collision_with_list(self.player, self.door_list)
            if door_hit_list:
                if self.map == "DollarStore":
                    x = 6600
                    y = 5050
                elif self.map == "MalMart":
                    x = 512
                    y = 128
                elif self.map == "TheSchool":
                    x = 6600
                    y = 128
                self.map = "overworld"
                self.setup(x,y)

        # --- Manage Scrolling ---

        # Keep track of if we changed the boundary. We don't want to call the
        # set_viewport command if we didn't change the view port.
        changed = False
        #left:
        left_boundary = self.view_left + LEFT_VIEWPORT_MARGIN
        if self.player.left < left_boundary:
            self.view_left -= left_boundary - self.player.left
            changed = True
        #right:
        right_boundary = self.view_left + SCREEN_WIDTH - RIGHT_VIEWPORT_MARGIN
        if self.player.right > right_boundary:
            self.view_left += self.player.right - right_boundary
            changed = True
        #up:
        top_boundary = self.view_bottom + SCREEN_HEIGHT - TOP_VIEWPORT_MARGIN
        if self.player.top > top_boundary:
            self.view_bottom += self.player.top - top_boundary
            changed = True
        #down:
        bottom_boundary = self.view_bottom + BOTTOM_VIEWPORT_MARGIN
        if self.player.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player.bottom
            changed = True

        if changed:
            self.view_bottom = int(self.view_bottom)
            self.view_left = int(self.view_left)
            arcade.set_viewport(self.view_left, SCREEN_WIDTH + self.view_left,
                                self.view_bottom, SCREEN_HEIGHT + self.view_bottom)

    def on_key_press(self, key, modifiers):
        #Called whenever a key is pressed
        if self.encounter.active_encounter:
            if key == arcade.key.ENTER:
                self.encounter.handle_the_selection = True
                return_string = self.encounter.handle_selection()
                if return_string == "Run" or return_string == "Hide":
                    self.encounter.end_encounter_on_update = True
            else:
                self.encounter.handle_the_selection = False
                self.encounter.change_arrow_pos(key, self.view_left, self.view_bottom)
        else:
            if key == arcade.key.UP:
                self.player.change_y = MOVEMENT_SPEED
            elif key == arcade.key.DOWN:
                self.player.change_y = -MOVEMENT_SPEED
            elif key == arcade.key.LEFT:
                self.player.change_x = -MOVEMENT_SPEED
            elif key == arcade.key.RIGHT:
                self.player.change_x = MOVEMENT_SPEED
        #Hiding and showing the dialogue box currently
        if key == arcade.key.KEY_1:
            self.overlay.showDialogueBox = False
        elif key == arcade.key.KEY_2:
            self.overlay.showDialogueBox = True
            self.overlay_dialogue_string = "New string to show"
        elif key == arcade.key.KEY_3:
            self.overlay.showUI = False
        elif key == arcade.key.KEY_4:
            self.overlay.showUI = True
            self.overlay_dialogue_string = "Brought back the UI"
        # Using the inventory, prevent the player from accessing inventory in battle
        if key == arcade.key.I and not self.encounter.active_encounter:
            # If we are already inside our inventory
            if self.active_inventory:
                self.active_inventory = False
                self.first_draw_of_inventory = True
                self.overlay.showUI = True
            # We are opening up the inventory
            else:
                self.active_inventory = True

    def on_key_release(self, key, modifiers):
        #Called when the user releases a key
        x = random.randint(self.rand_range)
        if key == arcade.key.UP or key == arcade.key.DOWN:

            self.player.change_y = 0
            # Dont want encounters when using the menu
            if not self.encounter.active_encounter and not self.active_inventory:
                if x == 1:
                    self.encounter.active_encounter  = True
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0
            # Dont want encounters when using the menu
            if not self.encounter.active_encounter and not self.active_inventory:
                if x == 1:
                    self.encounter.active_encounter  = True

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
