import arcade

class Inventory():

    def __init__(self):
        pass

    def setup(self, view_bottom, view_left):
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
        # Player Shoes
        self.inventory_player_shoes = arcade.SpriteSolidColor(80, 80, arcade.color.GOLD)
        self.inventory_player_shoes.set_position(view_left + 320, view_bottom + 325)
        self.inventory_gui_spritelist.append(self.inventory_player_shoes)

        # Player Pants
        self.inventory_player_pants = arcade.SpriteSolidColor(80, 80, arcade.color.GOLD)
        self.inventory_player_pants.set_position(view_left + 320, view_bottom + 415)
        self.inventory_gui_spritelist.append(self.inventory_player_pants)

        # Player Shirt
        self.inventory_player_shirt = arcade.SpriteSolidColor(80, 80, arcade.color.GOLD)
        self.inventory_player_shirt.set_position(view_left + 320, view_bottom + 505)
        self.inventory_gui_spritelist.append(self.inventory_player_shirt)

        # Player Helmet
        self.inventory_player_helmet = arcade.SpriteSolidColor(80, 80, arcade.color.GOLD)
        self.inventory_player_helmet.set_position(view_left + 320, view_bottom + 595)
        self.inventory_gui_spritelist.append(self.inventory_player_helmet)

        # Player Weapon
        self.inventory_player_weapon = arcade.SpriteSolidColor(80, 80, arcade.color.GOLD)
        self.inventory_player_weapon.set_position(view_left + 230, view_bottom + 505)
        self.inventory_gui_spritelist.append(self.inventory_player_weapon)

        # Player Gloves
        self.inventory_player_gloves = arcade.SpriteSolidColor(80, 80, arcade.color.GOLD)
        self.inventory_player_gloves.set_position(view_left + 410, view_bottom + 505)
        self.inventory_gui_spritelist.append(self.inventory_player_gloves)

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

        #Inventory Item Tab Selected
        self.inventory_item_tab_selected = arcade.SpriteSolidColor(45, 45, arcade.color.ZAFFRE)
        self.inventory_item_tab_selected.set_position(view_left + 345 + 308, view_bottom + 652)
        self.inventory_gui_spritelist.append(self.inventory_item_tab_selected)

        #Inventory Item Selected
        self.inventory_item_selected = arcade.SpriteSolidColor(361, 78, arcade.color.ZAFFRE)
        self.inventory_item_selected.set_position(view_left + 345 + 320 + 145, view_bottom + 364)
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

    def draw_inventory(self):
        self.inventory_gui_spritelist.draw()