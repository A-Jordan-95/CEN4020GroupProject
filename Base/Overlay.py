import arcade

class Overlay():
    #Info to set-up overlay
    def __init__(self):
        self.showDialogueBox = True

    def load_media(self):
        #Separating the loading of images and logic for this class
        #Dialogue Panel (not used yet)
        # self.dialoguePanel = arcade.Sprite("Images/UI/DialogueBox.png", 1.0)
        pass

    def draw_dialogue_box(self, text, view_bottom, view_left):
        # print("view left:", view_left," view bottom:", view_left)
        if self.showDialogueBox:
            # Border Panel
            arcade.draw_rectangle_filled(view_left + 640, view_bottom + 90, 1020, 180, arcade.color.RASPBERRY)
            # Text Panel Background
            arcade.draw_rectangle_filled(view_left + 640, view_bottom + 90, 1000, 160, arcade.color.WHITE_SMOKE)
            #Profile Image (arcade draws things from the center of the shape)
            #Math: 640 - 425 = (215) edqe of rectangle, add 5 margin to keep a square
            arcade.draw_rectangle_filled(view_left + 220, view_bottom + 90, 150, 150, arcade.color.BLACK)
            # Speaker Image
            #Math: 220 + 150 + 5 =  new x location
            arcade.draw_rectangle_filled(view_left + 375, view_bottom + 145, 150, 40, arcade.color.PRUSSIAN_BLUE)
            #Text to Render
            #Needs to anchored left/top so the amount of text does not change the formatting of input text
            #Text Limit
            # arcade.draw_text("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n"
            #                  "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n"
            #                  "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n"
            #                  "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n"
            #                  , view_left + 300, view_bottom + 120, arcade.color.BLACK, 20, anchor_x="left", anchor_y="top")
            arcade.draw_text(text, view_left + 300, view_bottom + 120, arcade.color.BLACK, 20, anchor_x="left", anchor_y="top")