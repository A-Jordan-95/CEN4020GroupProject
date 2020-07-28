import arcade

class Overlay():
    # Info to set-up overlay
    def __init__(self):
        self.showDialogueBox = True
        self.showUI = True
        self.current_speaker = None

    def load_media(self):
        ###############################################################
        # Separating the loading of images and logic for this class
        ###############################################################
        # DIALOGUE BOX SPRITE LIST
        self.dialogue_sprite_list = arcade.SpriteList()

        # Border Panel
        self.dialogue_border_background = arcade.SpriteSolidColor(1020, 180, arcade.color.BLACK)
        self.dialogue_sprite_list.append(self.dialogue_border_background)
        # Text Panel
        self.text_panel = arcade.SpriteSolidColor(1000, 160, arcade.color.WHITE_SMOKE)
        self.dialogue_sprite_list.append(self.text_panel)
        # Profile Image Border
        self.profile_border_red = arcade.SpriteSolidColor(150, 150, arcade.color.RED)
        self.dialogue_sprite_list.append(self.profile_border_red)

        ##############################
        # PROFILE IMAGES FOR DIALOGUE BOX (Will be deleted on first run and replaced by current speaker)
        self.profile = arcade.SpriteSolidColor(75, 75, arcade.color.DESIRE)
        self.dialogue_sprite_list.append(self.profile)

        ###############################################################
        # PLAYER INFO BOX SPRITE LIST
        self.player_info_sprite_list = arcade.SpriteList()

        # Border Panel
        self.player_info_border_background = arcade.SpriteSolidColor(252, 102, arcade.color.WHITE_SMOKE)
        self.player_info_sprite_list.append(self.player_info_border_background)
        # Player Info Border
        self.player_info_player_border = arcade.SpriteSolidColor(250, 100, arcade.color.BLACK)
        self.player_info_sprite_list.append(self.player_info_player_border)
        # Player Image Box - NOTE: current image is too small so we put it on top of this
        self.player_info_player_image = arcade.SpriteSolidColor(75, 75, arcade.color.HAN_BLUE)
        self.player_info_sprite_list.append(self.player_info_player_image)

        ###################################
        # User Image for player info box (placeholder)
        self.profile_rachel = arcade.Sprite("Images/UI/Profile_Rachel.png", scale=2)  # Need larger image for less bluriness
        self.player_info_sprite_list.append(self.profile_rachel)

        ###############################################################
        # MENU BAR SPRITE LIST
        self.menu_bar_sprite_list = arcade.SpriteList()
        # Menu Bar Background
        self.menu_bar_background = arcade.SpriteSolidColor(200, 27, arcade.color.BLACK)
        self.menu_bar_sprite_list.append(self.menu_bar_background)
        # Options
        self.menu_bar_option_button = arcade.SpriteSolidColor(64, 23, arcade.color.RAZZLE_DAZZLE_ROSE)
        self.menu_bar_sprite_list.append(self.menu_bar_option_button)
        # Map
        self.menu_bar_map_button = arcade.SpriteSolidColor(64, 23, arcade.color.TEA_GREEN)
        self.menu_bar_sprite_list.append(self.menu_bar_map_button)
        # Inventory
        self.menu_bar_inventory_button = arcade.SpriteSolidColor(64, 23, arcade.color.BEAU_BLUE)
        self.menu_bar_sprite_list.append(self.menu_bar_inventory_button)

################################################################################################################################

    def draw_dialogue_box(self, text, speaker, view_bottom, view_left):
        if self.showDialogueBox and self.showUI:
            # Border Panel
            self.dialogue_border_background.set_position(view_left + 640, view_bottom + 90)
            # Text Panel Background
            self.text_panel.set_position(view_left + 640, view_bottom + 90)
            # Profile Image (arcade draws things from the center of the shape)
            if self.current_speaker != speaker or self.current_speaker is None:
                # Change local data for speaker and remove current speaker from spritelist
                self.current_speaker = speaker
                self.profile.kill()
                # Speakers in the game
                if speaker == "Karen":
                    self.profile = arcade.Sprite("Images/UI/Profile_Karen.jpg", scale=1.47)  # A larger image would looker better (140 x 140 for Profile Images)
                    self.dialogue_sprite_list.append(self.profile)
                else:
                    #Currently the player
                    self.profile = arcade.SpriteSolidColor(100, 100, arcade.color.GOLD)
                    self.dialogue_sprite_list.append((self.profile))
            else:
                # Profile Image Border
                self.profile_border_red.set_position(view_left + 220, view_bottom + 90)
                # Draw the current speaker
                self.profile.set_position(view_left + 220, view_bottom + 90)
            self.dialogue_sprite_list.draw()
            # Have to render text afterwards
            # Speaker Name
            arcade.draw_text(speaker, view_left + 300, view_bottom + 160, arcade.color.RED, 30, anchor_x="left", anchor_y="top")
            # Text to Render
            arcade.draw_text(text, view_left + 300, view_bottom + 120, arcade.color.BLACK, 20, anchor_x="left", anchor_y="top")

    def draw_player_info(self, hit_points, energy_points, view_bottom, view_left):
        if self.showUI:
            # Player Info Background
            self.player_info_border_background.set_position(view_left + 125, view_bottom + 675)
            # Player Info Border
            self.player_info_player_border.set_position(view_left + 125, view_bottom + 675)
            # Player Image Box
            self.player_info_player_image.set_position(view_left + 50, view_bottom + 675)
            # # # # Place holder
            self.profile_rachel.set_position(view_left + 50, view_bottom + 675)
            # Draw sprite list
            self.player_info_sprite_list.draw()
            # Have to render text afterwards
            # HP Info
            arcade.draw_text(str(hit_points), view_left + 95, view_bottom + 700, arcade.color.RED, 20, anchor_x="left", anchor_y="top")
            # EP Info
            arcade.draw_text(str(energy_points), view_left + 95, view_bottom + 670, arcade.color.GOLD, 20, anchor_x="left", anchor_y="top")

    def draw_menu_bar(self, view_bottom, view_left):
        if self.showUI:
            # Menu Bar Background
            self.menu_bar_background.set_position(view_left + 1179, view_bottom + 707)
            # Options
            self.menu_bar_option_button.set_position(view_left + 1245, view_bottom + 707)
            # Map
            self.menu_bar_map_button.set_position(view_left + 1179, view_bottom + 707)
            # Inventory
            self.menu_bar_inventory_button.set_position(view_left + 1113, view_bottom + 707)
            # Draw above items
            self.menu_bar_sprite_list.draw()
            # Have to render text afterwards
            # Draw the text shown on the above items
            arcade.draw_text("Options", view_left + 1220, view_bottom + 697, arcade.color.BLACK)
            arcade.draw_text("Map", view_left + 1165, view_bottom + 697, arcade.color.BLACK)
            arcade.draw_text("Inventory", view_left + 1084, view_bottom + 697, arcade.color.BLACK)

    ################################################################################################################################
    # Unused, for future reference
    ################################################################################################################################

    def draw_dialogue_box_template(self, text, speaker, view_bottom, view_left):
        if self.showDialogueBox and self.showUI:
            # Border Panel
            arcade.draw_rectangle_filled(view_left + 640, view_bottom + 90, 1020, 180, arcade.color.BLACK)
            # Text Panel Background
            arcade.draw_rectangle_filled(view_left + 640, view_bottom + 90, 1000, 160, arcade.color.WHITE_SMOKE)
            # Speaker Name
            arcade.draw_text(speaker, view_left + 300, view_bottom + 160, arcade.color.RED, 30, anchor_x="left", anchor_y="top")
            # Profile Image (arcade draws things from the center of the shape)
            if speaker == "Karen":
                # Profile Image Border
                arcade.draw_rectangle_filled(view_left + 220, view_bottom + 90, 150, 150, arcade.color.RED)
                # Profile Image Used
                self.profile_karen.set_position(view_left + 220, view_bottom + 90)
                self.profile_karen.draw()
            # Text Box Limit
            # arcade.draw_text("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n"
            #                  "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n"
            #                  "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n"
            #                  "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n"
            #                  , view_left + 300, view_bottom + 120, arcade.color.BLACK, 20, anchor_x="left", anchor_y="top")
            arcade.draw_text(text, view_left + 300, view_bottom + 120, arcade.color.BLACK, 20, anchor_x="left", anchor_y="top")

    def draw_player_info_template(self, hit_points, energy_points, view_bottom, view_left):
        if self.showUI:
            # Player Info Background
            arcade.draw_rectangle_filled(view_left + 125, view_bottom + 675, 250, 100, arcade.color.BLACK)
            # Player Info Border
            arcade.draw_rectangle_outline(view_left + 125, view_bottom + 675, 250, 100, arcade.color.WHITE_SMOKE)
            # Player Image Box
            arcade.draw_rectangle_filled(view_left + 50, view_bottom + 675, 75, 75, arcade.color.HAN_BLUE)
            self.profile_rachel.set_position(view_left + 50, view_bottom + 675)
            self.profile_rachel.draw()
            # HP Info
            arcade.draw_text(str(hit_points) + " / 100 HP", view_left + 95, view_bottom + 700, arcade.color.RED, 20, anchor_x="left", anchor_y="top")
            # EP Info
            arcade.draw_text(str(energy_points) + " / 100 EP", view_left + 95, view_bottom + 670, arcade.color.GOLD, 20, anchor_x="left", anchor_y="top")

    def draw_menu_bar_template(self, view_bottom, view_left):
        if self.showUI:
            # Menu Bar Background
            arcade.draw_rectangle_filled(view_left + 1179, view_bottom + 707, 200, 27, arcade.color.BLACK)
            # Options
            arcade.draw_rectangle_filled(view_left + 1245, view_bottom + 707, 64, 23, arcade.color.RAZZLE_DAZZLE_ROSE)
            arcade.draw_text("Options", view_left + 1220, view_bottom + 697, arcade.color.BLACK)
            # Map
            arcade.draw_rectangle_filled(view_left + 1179, view_bottom + 707, 64, 23, arcade.color.TEA_GREEN)
            arcade.draw_text("Map", view_left + 1165, view_bottom + 697, arcade.color.BLACK)
            # Inventory
            arcade.draw_rectangle_filled(view_left + 1113, view_bottom + 707, 64, 23, arcade.color.BEAU_BLUE)
            arcade.draw_text("Inventory", view_left + 1084, view_bottom + 697, arcade.color.BLACK)