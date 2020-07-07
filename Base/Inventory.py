import arcade

class Inventory():

    def __init__(self):
        self.pos_tab = None
        self.inventory_item_tab_selected_posX = None
        self.pos_item = None
        self.inventory_item_selected_posX = None
        self.offset = 0

    def setup(self, view_bottom, view_left, player_equipped, pos_tab=None, pos_item=None):
        #Set-Up Tab Chosen Drawing Logic
        self.inventory_item_tab_selected_posX = [view_left + 653, view_left + 698, view_left + 743, view_left + 788,
        view_left + 833, view_left + 878, view_left + 923, view_left + 968]
        #Drawing when first opened or drawing when player has moved tabs
        if pos_tab:
            self.pos_tab = pos_tab
        else:
            self.pos_tab = 0

        #Set-up Item Chosen Drawing Logic
        self.inventory_item_selected_posX = [view_bottom + 592, view_bottom + 516, view_bottom + 440, view_bottom + 364,
        view_bottom + 288, view_bottom + 212, view_bottom + 136, view_bottom + 60]
        if pos_item:
            self.pos_item = pos_item
        else:
            self.pos_item = 0

        ###############################################################
        # Separating the loading of images and logic for this class
        ###############################################################
        # INVENTORY SPRITE LIST
        self.inventory_gui_spritelist = arcade.SpriteList()

        # Background
        self.inventory_background = arcade.SpriteSolidColor(1260, 700, arcade.color.RED)
        self.inventory_background.set_position(view_left + 640, view_bottom + 360)
        self.inventory_gui_spritelist.append(self.inventory_background)

        ###############################################################
        # Player Info Background
        self.inventory_player_info_background = arcade.SpriteSolidColor(600, 680, arcade.color.BLACK)
        self.inventory_player_info_background.set_position(view_left + 320, view_bottom + 360)
        self.inventory_gui_spritelist.append(self.inventory_player_info_background)

        ###################################
        # Player Level
        self.inventory_player_level = arcade.SpriteSolidColor(180, 40, arcade.color.TEA_GREEN)
        self.inventory_player_level.set_position(view_left + 125, view_bottom + 670)
        self.inventory_gui_spritelist.append(self.inventory_player_level)

        # Player HP
        self.inventory_player_hp = arcade.SpriteSolidColor(180, 40, arcade.color.RED)
        self.inventory_player_hp.set_position(view_left + 320, view_bottom + 670)
        self.inventory_gui_spritelist.append(self.inventory_player_hp)

        # Player Energy
        self.inventory_player_energy = arcade.SpriteSolidColor(180, 40, arcade.color.SAFFRON)
        self.inventory_player_energy.set_position(view_left + 320 + 195, view_bottom + 670)
        self.inventory_gui_spritelist.append(self.inventory_player_energy)

        ###################################
        # Player Helmet Background
        self.inventory_player_helmet = arcade.SpriteSolidColor(80, 80, arcade.color.GOLD)
        self.inventory_player_helmet.set_position(view_left + 320, view_bottom + 595)
        self.inventory_gui_spritelist.append(self.inventory_player_helmet)

        # Helmet to Draw
        if player_equipped[0] is not None:
            self.helmet = arcade.Sprite(f"{player_equipped[0].sprite}", scale=0.5)
            self.helmet.set_position(view_left + 320, view_bottom + 595)
            self.inventory_gui_spritelist.append(self.helmet)

        # Player Weapon Background
        self.inventory_player_weapon = arcade.SpriteSolidColor(80, 80, arcade.color.GOLD)
        self.inventory_player_weapon.set_position(view_left + 230, view_bottom + 505)
        self.inventory_gui_spritelist.append(self.inventory_player_weapon)

        # Weapon to Draw
        if player_equipped[1] is not None:
            self.weapon = arcade.Sprite(f"{player_equipped[1].sprite}", scale=0.5)
            self.weapon.set_position(view_left + 230, view_bottom + 505)
            self.inventory_gui_spritelist.append(self.weapon)

        # Player Shirt Background
        self.inventory_player_shirt = arcade.SpriteSolidColor(80, 80, arcade.color.GOLD)
        self.inventory_player_shirt.set_position(view_left + 320, view_bottom + 505)
        self.inventory_gui_spritelist.append(self.inventory_player_shirt)

        # Shirt/Body to Draw
        if player_equipped[2] is not None:
            self.shirt = arcade.Sprite(f"{player_equipped[2].sprite}", scale=0.5)
            self.shirt.set_position(view_left + 320, view_bottom + 505)
            self.inventory_gui_spritelist.append(self.shirt)

        # Player Gloves Background
        self.inventory_player_gloves = arcade.SpriteSolidColor(80, 80, arcade.color.GOLD)
        self.inventory_player_gloves.set_position(view_left + 410, view_bottom + 505)
        self.inventory_gui_spritelist.append(self.inventory_player_gloves)

        # Gloves to Draw
        if player_equipped[3] is not None:
            self.gloves = arcade.Sprite(f"{player_equipped[3].sprite}", scale=0.5)
            self.gloves.set_position(view_left + 410, view_bottom + 505)
            self.inventory_gui_spritelist.append(self.gloves)

        # Player Pants
        self.inventory_player_pants = arcade.SpriteSolidColor(80, 80, arcade.color.GOLD)
        self.inventory_player_pants.set_position(view_left + 320, view_bottom + 415)
        self.inventory_gui_spritelist.append(self.inventory_player_pants)

        # Pants to Draw
        if player_equipped[4] is not None:
            self.pants = arcade.Sprite(f"{player_equipped[4].sprite}", scale=0.5)
            self.pants.set_position(view_left + 320, view_bottom + 415)
            self.inventory_gui_spritelist.append(self.pants)

        # Player Shoes
        self.inventory_player_shoes = arcade.SpriteSolidColor(80, 80, arcade.color.GOLD)
        self.inventory_player_shoes.set_position(view_left + 320, view_bottom + 325)
        self.inventory_gui_spritelist.append(self.inventory_player_shoes)

        # Shoes to Draw
        if player_equipped[5] is not None:
            self.shoes = arcade.Sprite(f"{player_equipped[5].sprite}", scale=0.5)
            self.shoes.set_position(view_left + 320, view_bottom + 325)
            self.inventory_gui_spritelist.append(self.shoes)

        ###################################
        # Player Info Bottom Panel
        self.inventory_player_info_bottom_panel = arcade.SpriteSolidColor(590, 255, arcade.color.TRACTOR_RED)
        self.inventory_player_info_bottom_panel.set_position(view_left + 320, view_bottom + 360 - 208)
        self.inventory_gui_spritelist.append(self.inventory_player_info_bottom_panel)

        # Player Info Strength
        self.inventory_player_info_strength = arcade.SpriteSolidColor(275, 60, arcade.color.SOAP)
        self.inventory_player_info_strength.set_position(view_left + 320 - 148, view_bottom + 235)
        self.inventory_gui_spritelist.append(self.inventory_player_info_strength)

        # Player Info Intelligence
        self.inventory_player_info_intelligence = arcade.SpriteSolidColor(275, 60, arcade.color.SOAP)
        self.inventory_player_info_intelligence.set_position(view_left + 320 - 148, view_bottom + 150)
        self.inventory_gui_spritelist.append(self.inventory_player_info_intelligence)

        # Player Info Agility
        self.inventory_player_info_agility = arcade.SpriteSolidColor(275, 60, arcade.color.SOAP)
        self.inventory_player_info_agility.set_position(view_left + 320 - 148, view_bottom + 70)
        self.inventory_gui_spritelist.append(self.inventory_player_info_agility)

        # Player Info Defense
        self.inventory_player_info_defense = arcade.SpriteSolidColor(275, 60, arcade.color.SOAP)
        self.inventory_player_info_defense.set_position(view_left + 320 + 148, view_bottom + 235)
        self.inventory_gui_spritelist.append(self.inventory_player_info_defense)

        # Player Info Immunity
        self.inventory_player_info_immunity = arcade.SpriteSolidColor(275, 60, arcade.color.SOAP)
        self.inventory_player_info_immunity.set_position(view_left + 320 + 148, view_bottom + 150)
        self.inventory_gui_spritelist.append(self.inventory_player_info_immunity)

        # Player Info Luck
        self.inventory_player_info_luck = arcade.SpriteSolidColor(275, 60, arcade.color.SOAP)
        self.inventory_player_info_luck.set_position(view_left + 320 + 148, view_bottom + 70)
        self.inventory_gui_spritelist.append(self.inventory_player_info_luck)

        ###############################################################
        # Player Items Background
        self.inventory_player_items_background = arcade.SpriteSolidColor(361, 655, arcade.color.BLACK)
        self.inventory_player_items_background.set_position(view_left + 345 + 320 + 145, view_bottom + 347)
        self.inventory_gui_spritelist.append(self.inventory_player_items_background)

        #Inventory Item Tab Selected (Initial always top-left)
        self.inventory_item_tab_selected = arcade.SpriteSolidColor(45, 45, arcade.color.ZAFFRE)
        self.inventory_item_tab_selected.set_position(self.inventory_item_tab_selected_posX[self.pos_tab], view_bottom + 652)
        self.inventory_gui_spritelist.append(self.inventory_item_tab_selected)

        #Inventory Item Selected
        self.inventory_item_selected = arcade.SpriteSolidColor(361, 78, arcade.color.ZAFFRE)
        self.inventory_item_selected.set_position(view_left + 810, self.inventory_item_selected_posX[self.pos_item])
        self.inventory_gui_spritelist.append(self.inventory_item_selected)

        # Inventory Item Type Grid
        self.inventory_item_type_grid = arcade.Sprite("Images/UI/Item_Type_Grid.png", 1.0)
        self.inventory_item_type_grid.set_position(view_left + 345 + 320 + 145, view_bottom + 347)
        self.inventory_gui_spritelist.append(self.inventory_item_type_grid)

        ###############################################################
        # Item Info Background
        self.inventory_item_background = arcade.SpriteSolidColor(260, 655, arcade.color.BLACK)
        self.inventory_item_background.set_position(view_left + 1130, view_bottom + 347)
        self.inventory_gui_spritelist.append(self.inventory_item_background)

        # Item Info Grid
        self.inventory_item_grid = arcade.Sprite("Images/UI/Item_Grid.png", 1.0)
        self.inventory_item_grid.set_position(view_left + 1130, view_bottom + 347)
        self.inventory_gui_spritelist.append(self.inventory_item_grid)

    def change_arrow_pos(self, key, view_left, view_bottom, player_items, player_equipped):
        #Moving tabs reset list selection (->)
        if key == arcade.key.RIGHT and self.pos_tab < 7:
            self.pos_tab += 1
            self.pos_item = 0
            self.offset = 0
        # Moving tabs reset list selection (<-)
        elif key == arcade.key.LEFT and self.pos_tab > 0:
            self.pos_tab -= 1
            self.pos_item = 0
            self.offset = 0
        # Moving down the list (v)
        elif key == arcade.key.DOWN:
            #Only allow selection on the 8 boxes
            if self.pos_item < 7:
                # Limit selection if item array has less than 8 items
                if self.pos_item < len(player_items[self.pos_tab]) - 1:
                    self.pos_item += 1
            #Allow the user to scroll down if they have more than 8 of that item type
            elif self.pos_item + self.offset < len(player_items[self.pos_tab]) - 1:
                self.offset += 1
            else:
                #Don't let the user do anything
                pass
        # Moving up the list (^)
        elif key == arcade.key.UP and self.pos_item > 0:
            #If we have an offset, we subtract from that first
            if self.offset > 0:
                self.offset -= 1
            #Don't have an offset we change cursored item
            elif self.pos_item > 0:
                self.pos_item -= 1
            else:
                # Don't let the user do anything
                pass
        elif key == arcade.key.ENTER and len(player_items[self.pos_tab]) > 0:
            #We are equipping an item
            if self.pos_tab >= 0 and self.pos_tab <= 5:
                # Move Item to Player Equipped
                player_equipped[self.pos_tab] = player_items[self.pos_tab][self.pos_item + self.offset]
            elif self.pos_tab == 6:
                #We are using a consumable
                print("Consume")
                pass
            else:
                #Do nothing as of now (tab 7)
                print("Don't know yet")
                pass
        elif key == arcade.key.BACKSPACE and len(player_items[self.pos_tab]) > 0:
            # We are removing a equipped item
            if self.pos_tab >= 0 and self.pos_tab <= 5 and player_equipped[self.pos_tab] is not None:
                # Remove item from equipped
                player_equipped[self.pos_tab] = None
            elif self.pos_tab == 6:
                # Something else with consumable?
                print("?")
                pass
            else:
                # Do nothing as of now (tab 7)
                print("Don't know yet")
                pass
        # Redraw everything (probably needs to be optimized)
        self.setup(view_bottom, view_left, player_equipped, self.pos_tab, self.pos_item)

    def draw_inventory(self, view_left, view_bottom, player_items, player_equipped):
        # Draw the UI before drawing the text
        self.inventory_gui_spritelist.draw()

        # Check that the player has an item to fill this spot
        if len(player_items) > self.pos_tab:
            # Draw Item in Box # 1
            if len(player_items[self.pos_tab]) > 0 + self.offset:
                arcade.draw_text(player_items[self.pos_tab][0 + self.offset].name, view_left + 650, view_bottom + 577, arcade.color.WHITE, 20, anchor_x="left")
            else:
                arcade.draw_text("....", view_left + 650, view_bottom + 577, arcade.color.WHITE, 20, anchor_x="left")
            # Draw Item in Box # 2
            if len(player_items[self.pos_tab]) > 1 + self.offset:
                arcade.draw_text(player_items[self.pos_tab][1 + self.offset].name, view_left + 650, view_bottom + 500, arcade.color.WHITE, 20, anchor_x="left")
            else:
                arcade.draw_text("....", view_left + 650, view_bottom + 500, arcade.color.WHITE, 20, anchor_x="left")
            # Draw Item in Box # 3
            if len(player_items[self.pos_tab]) > 2 + self.offset:
                arcade.draw_text(player_items[self.pos_tab][2 + self.offset].name, view_left + 650, view_bottom + 422, arcade.color.WHITE, 20, anchor_x="left")
            else:
                arcade.draw_text("....", view_left + 650, view_bottom + 422, arcade.color.WHITE, 20, anchor_x="left")
            # Draw Item in Box # 4
            if len(player_items[self.pos_tab]) > 3 + self.offset:
                arcade.draw_text(player_items[self.pos_tab][3 + self.offset].name, view_left + 650, view_bottom + 350, arcade.color.WHITE, 20, anchor_x="left")
            else:
                arcade.draw_text("....", view_left + 650, view_bottom + 350, arcade.color.WHITE, 20, anchor_x="left")
            # Draw Item in Box # 5
            if len(player_items[self.pos_tab]) > 4 + self.offset:
                arcade.draw_text(player_items[self.pos_tab][4 + self.offset].name, view_left + 650, view_bottom + 270, arcade.color.WHITE, 20, anchor_x="left")
            else:
                arcade.draw_text("....", view_left + 650, view_bottom + 270, arcade.color.WHITE, 20, anchor_x="left")
            # Draw Item in Box # 6
            if len(player_items[self.pos_tab]) > 5 + self.offset:
                arcade.draw_text(player_items[self.pos_tab][5 + self.offset].name, view_left + 650, view_bottom + 200, arcade.color.WHITE, 20, anchor_x="left")
            else:
                arcade.draw_text("....", view_left + 650, view_bottom + 200, arcade.color.WHITE, 20, anchor_x="left")
            # Draw Item in Box # 7
            if len(player_items[self.pos_tab]) > 6 + self.offset:
                arcade.draw_text(player_items[self.pos_tab][6 + self.offset], view_left + 650, view_bottom + 120, arcade.color.WHITE, 20, anchor_x="left")
            else:
                arcade.draw_text("....", view_left + 650, view_bottom + 120, arcade.color.WHITE, 20, anchor_x="left")
            # Draw Item in Box # 8
            if len(player_items[self.pos_tab]) > 7 + self.offset:
                arcade.draw_text(player_items[self.pos_tab][7 + self.offset].name, view_left + 650, view_bottom + 45, arcade.color.WHITE, 20, anchor_x="left")
            else:
                arcade.draw_text("....", view_left + 650, view_bottom + 45, arcade.color.WHITE, 20, anchor_x="left")

            # Alexander Stuff
            if len(player_items[self.pos_tab]) > 0:
                arcade.draw_text(player_items[self.pos_tab][self.pos_item + self.offset].name, view_left + 1050, view_bottom + 577, arcade.color.WHITE, 20, anchor_x="left")