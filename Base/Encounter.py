import arcade
from masterMoveDict import mmd
import koronakombat as kk

class Encounter():
    def __init__(self):
        self.enemy_window_sprite = None
        self.command_window_sprite = None
        self.arrow_sprite = None
        self.enemy_sprite = None
        self.windows_sprite_list = None
        self.arrow_sprite_positions = None
        self.arrow_pos = 0 #can be 0-3
        self.menu_sprite_list = None
        self.menu = None #list of strings optionally passed to the setup function.
        self.menu_offset = 0 #keeps track of menu scrolling
        self.menu_positions = None #can be 0-3
        self.active_encounter = False
        self.handle_the_selection = False
        self.first_draw_of_encounter = True
        self.end_encounter_on_update = False
        self.hero_move_list = None
        self.hero = None
        self.kombat = None

    def setup_kombat(self):
        self.hero_move_list = ['Run', 'Hide', 'Smile', 'Attack', 'Chortle', 'Cough on']
        self.hero = kk.Hero(10, 10, 8, 6, 5, 5, self.hero_move_list, "Main character")
        self.kombat = kk.Kombat("Overworld")

    def setup(self, view_bottom, view_left, pos = None, menu = None):
        #setup menu functionality:
        self.menu_sprite_list = arcade.SpriteList()
        self.arrow_sprite_positions = [[view_left + 350, view_bottom + 642],
              [view_left + 650,view_bottom + 642], [view_left + 350, view_bottom + 590],
              [view_left + 650, view_bottom + 590]] #coordinates of arrow pos 0-3
        self.menu_positions = [[view_left + 380, view_bottom + 630],
              [view_left + 680,view_bottom + 630], [view_left + 380, view_bottom + 580],
              [view_left + 680, view_bottom + 580]] #coordinates of menu pos 0-3
        if menu:
            self.menu = self.parse_menu(menu)
        else:
            self.menu = ['Run', 'Hide', 'Smile', 'Attack', 'Chortle', 'Cough on', '', '']
        if pos:
            self.arrow_pos = pos
        else:
            self.arrow_pos = 0
        #setup window_sprite_list:
        self.windows_sprite_list = arcade.SpriteList()
        #setup enemy sprite:
        self.enemy_sprite = arcade.Sprite("Images/EnemySprites/CORONAPILLAR.png", 1.0)
        self.enemy_sprite.center_x = view_left + 640
        self.enemy_sprite.center_y = view_bottom + 330
        #setup encounter ui windows:
        self.enemy_window_sprite = arcade.Sprite("Images/EncounterSprites/enemy_window.png", 1.0)
        self.enemy_window_sprite.center_x = view_left + 640
        self.enemy_window_sprite.center_y = view_bottom + 360
        self.command_window_sprite = arcade.Sprite("Images/EncounterSprites/command_window.png", 1.0)
        self.command_window_sprite.center_x = view_left + 640
        self.command_window_sprite.center_y = view_bottom + 620
        #add windows to sprite list:
        self.windows_sprite_list.append(self.enemy_window_sprite)
        self.windows_sprite_list.append(self.command_window_sprite)
        self.windows_sprite_list.append(self.enemy_sprite)
        #setup encounter ui menu:
        self.arrow_sprite = arcade.Sprite("Images/EncounterSprites/arrow.png", 0.5)
        self.arrow_sprite.center_x = self.arrow_sprite_positions[self.arrow_pos][0]
        self.arrow_sprite.center_y = self.arrow_sprite_positions[self.arrow_pos][1]
        #add arrow to sprite list:
        self.menu_sprite_list.append(self.arrow_sprite)
        

    def change_arrow_pos(self, key, view_left, view_bottom):
        if key == arcade.key.UP:
            if self.arrow_pos == 0:
                #scroll screen up:
                if self.menu_offset > 0:
                    self.menu_offset -= 4
            elif self.arrow_pos == 1:
                #scroll screen up:
                if self.menu_offset > 0:
                    self.menu_offset -= 4
            elif self.arrow_pos == 2:
                self.arrow_pos = 0
            elif self.arrow_pos == 3:
                self.arrow_pos = 1
        elif key == arcade.key.DOWN:
            if self.arrow_pos == 0:
                self.arrow_pos = 2
            elif self.arrow_pos == 1:
                self.arrow_pos = 3
            elif self.arrow_pos == 2:
                #scroll screen down:
                if len(self.menu) > (self.menu_offset + 4):
                    self.menu_offset += 4
            elif self.arrow_pos == 3:
                #scroll screen down:
                if len(self.menu) > (self.menu_offset + 4):
                    self.menu_offset += 4
        elif key == arcade.key.LEFT:
            if self.arrow_pos == 0:
                self.arrow_pos = 1
            elif self.arrow_pos == 1:
                self.arrow_pos = 0
            elif self.arrow_pos == 2:
                self.arrow_pos = 3
            elif self.arrow_pos == 3:
                self.arrow_pos = 2
        elif key == arcade.key.RIGHT:
            if self.arrow_pos == 0:
                self.arrow_pos = 1
            elif self.arrow_pos == 1:
                self.arrow_pos = 0
            elif self.arrow_pos == 2:
                self.arrow_pos = 3
            elif self.arrow_pos == 3:
                self.arrow_pos = 2
        self.setup(view_bottom, view_left, self.arrow_pos)

    def parse_menu(self, menu):
        the_menu = []
        if menu[0]:
            the_menu.append(menu[0])
        if menu[1]:
            the_menu.append(menu[1])
        if menu[2]:
            the_menu.append(menu[2])
        if menu[3]:
            the_menu.append(menu[3])
        return the_menu

    def draw_encounter(self):
        self.windows_sprite_list.draw()
        self.menu_sprite_list.draw()
        for x in range(0,4):
            if len(self.menu) >= (self.menu_offset + x):
                arcade.draw_text(self.menu[x + self.menu_offset],
                self.menu_positions[x][0],
                self.menu_positions[x][1],
                arcade.csscolor.WHITE, 18)

    def handle_selection(self):
        pos = self.arrow_pos + self.menu_offset
        if self.menu[pos] != "Run" and self.menu[pos] != "Hide":
            print("checking for defeat...")
            ret_val = self.kombat.check_for_defeat(self.hero, self.kombat.enem, pos)
        else:
            ret_val = self.menu[pos]

        #if ret_val == "You have defeated the monster! :)" or ret_val == "You are dead as shit":
            #self.end_encounter_on_update = True
            #self.__init__()
        return ret_val
