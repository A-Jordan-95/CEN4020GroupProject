import arcade

RIGHT_FACING = 0
LEFT_FACING = 1
CHARACTER_SCALING = 1
UPDATES_PER_FRAME = 7

def load_texture_pair(filename):
    return [
        arcade.load_texture(filename),
        arcade.load_texture(filename, mirrored=True)
    ]
    #load a texture pair with a mirrored image

class PlayerCharacter(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.character_face_direction = RIGHT_FACING
        #always start facing right
        self.cur_texture = 0
        self.scale = CHARACTER_SCALING
        main_path = "Images/PlayerSprites/RachelRight"

        self.idle_texture_pair = load_texture_pair(f"{main_path}_idle.png")

        self.walk_textures = []
        for i in range(8):
            texture = load_texture_pair(f"{main_path}_walk{i}.png")
            self.walk_textures.append(texture)

    def update_animation(self,delta_time: float = 1/60):
        #Left and Right changes
        if self.change_x < 0 and self.character_face_direction == RIGHT_FACING:
            self.character_face_direction = LEFT_FACING
        if self.change_x > 0 and self.character_face_direction == LEFT_FACING:
            self.character_face_direction = RIGHT_FACING

        #Idle
        if self.change_x == 0 and self.change_y == 0:
            self.texture = self.idle_texture_pair[self.character_face_direction]
            return

        # Walking
        self.cur_texture += 1
        if self.cur_texture > 7 * UPDATES_PER_FRAME:
            self.cur_texture = 0
        self.texture = self.walk_textures[self.cur_texture // UPDATES_PER_FRAME][self.character_face_direction]