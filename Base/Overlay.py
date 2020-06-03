import arcade

class Overlay():
    #Info to set-up overlay
    def __init__(self):
        self.showDialogueBox = True
        self.showUI = True

    def load_media(self):
        #Separating the loading of images and logic for this class
        #Dialogue Panel (not used yet)
        # self.dialoguePanel = arcade.Sprite("Images/UI/DialogueBox.png", 1.0)

        #Profile Images for Dialogue Box
        self.profile_karen = arcade.Sprite("Images/UI/Profile_Karen.jpg", scale= 1.47) #A larger image would looker better (140 x 140 for Profile Images)
        # print(self.profile_karen.height, self.profile_karen.width)

        #User Image for player info box
        self.profile_rachel = arcade.Sprite("Images/UI/Profile_Rachel.png", scale = 2) #Need larger image for less bluriness

    def draw_dialogue_box_template(self, text, view_bottom, view_left):
        if self.showDialogueBox and self.showUI:
            # Border Panel
            arcade.draw_rectangle_filled(view_left + 640, view_bottom + 90, 1020, 180, arcade.color.RASPBERRY)
            # Text Panel Background
            arcade.draw_rectangle_filled(view_left + 640, view_bottom + 90, 1000, 160, arcade.color.WHITE_SMOKE)
            #Profile Image (arcade draws things from the center of the shape)
            #Math: 640 - 425 = (215) edqe of rectangle, add 5 margin to keep a square
            arcade.draw_rectangle_filled(view_left + 220, view_bottom + 90, 150, 150, arcade.color.GRAPE)
            # Speaker Name
            #Math: 220 + 150 + 5 =  new x location
            arcade.draw_rectangle_filled(view_left + 375, view_bottom + 145, 150, 40, arcade.color.PRUSSIAN_BLUE)
            #Text to Render
            #Needs to anchored left/top so the amount of text does not change the formatting of input text
            #Text Box Limit
            # arcade.draw_text("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n"
            #                  "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n"
            #                  "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n"
            #                  "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n"
            #                  , view_left + 300, view_bottom + 120, arcade.color.BLACK, 20, anchor_x="left", anchor_y="top")
            arcade.draw_text(text, view_left + 300, view_bottom + 120, arcade.color.BLACK, 20, anchor_x="left", anchor_y="top")

    def draw_dialogue_box(self, text, speaker, view_bottom, view_left):
        if self.showDialogueBox and self.showUI:
            #Border Panel
            arcade.draw_rectangle_filled(view_left + 640, view_bottom + 90, 1020, 180, arcade.color.BLACK)
            # Text Panel Background
            arcade.draw_rectangle_filled(view_left + 640, view_bottom + 90, 1000, 160, arcade.color.WHITE_SMOKE)
            # Speaker Name
            arcade.draw_text(speaker, view_left + 300, view_bottom + 160, arcade.color.RED, 30, anchor_x="left", anchor_y="top")
            # Profile Image (arcade draws things from the center of the shape)
            if speaker == "Karen":
                #Profile Image Border
                arcade.draw_rectangle_filled(view_left + 220, view_bottom + 90, 150, 150, arcade.color.RED)
                #Profile Image Used
                self.profile_karen.set_position(view_left + 220, view_bottom + 90)
                self.profile_karen.draw()
            # Text to Render
            arcade.draw_text(text, view_left + 300, view_bottom + 120, arcade.color.BLACK, 20, anchor_x="left", anchor_y="top")

    def draw_player_info(self, hit_points, energy_points, view_bottom, view_left):
        if self.showUI:
            # Player Info Background
            arcade.draw_rectangle_filled(view_left + 125, view_bottom + 675, 250, 100, arcade.color.BLACK)
            # Player Info Border
            arcade.draw_rectangle_outline(view_left + 125, view_bottom + 675, 250, 100, arcade.color.WHITE_SMOKE)
            #Player Image Box
            arcade.draw_rectangle_filled(view_left + 50, view_bottom + 675, 75, 75, arcade.color.HAN_BLUE)
            self.profile_rachel.set_position(view_left + 50, view_bottom + 675)
            self.profile_rachel.draw()
            #HP Info
            arcade.draw_text(str(hit_points) + " / 100 HP", view_left + 95, view_bottom + 700, arcade.color.RED, 20, anchor_x="left", anchor_y="top")
            # EP Info
            arcade.draw_text(str(energy_points) + " / 100 EP", view_left + 95, view_bottom + 670, arcade.color.GOLD, 20, anchor_x="left", anchor_y="top")

    def draw_menu_bar(self, view_bottom, view_left):
        if self.showUI:
            #Menu Bar Background
            arcade.draw_rectangle_filled(view_left + 1179, view_bottom + 707, 200, 27, arcade.color.BLACK)
            #Options
            arcade.draw_rectangle_filled(view_left + 1245, view_bottom + 707, 64, 23, arcade.color.RAZZLE_DAZZLE_ROSE)
            arcade.draw_text("Options", view_left + 1220, view_bottom + 697, arcade.color.BLACK)
            #Map
            arcade.draw_rectangle_filled(view_left + 1179, view_bottom + 707, 64, 23, arcade.color.TEA_GREEN)
            arcade.draw_text("Map", view_left + 1165, view_bottom + 697, arcade.color.BLACK)
            #Inventory
            arcade.draw_rectangle_filled(view_left + 1113, view_bottom + 707, 64, 23, arcade.color.BEAU_BLUE)
            arcade.draw_text("Inventory", view_left + 1084, view_bottom + 697, arcade.color.BLACK)