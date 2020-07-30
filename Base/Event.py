import Entity
import arcade

class Event:

    def __init__(self):
        self.dialogue_events_overworld = None
        self.dialogue_events_dollarstore = None
        self.dialogue_events_malmart = None
        self.dialogue_events_school = None
        self.need_to_add_item = True
        self.event_num_lines = 0

    # Handle Dialogue Events in the world
    def handle_dialogue_event(self, event_ID, overlay, current_dialogue_line, map_name, player_items, view_left, view_bottom):
        if map_name == "overworld":
            # Intro Event
            if event_ID == "1":
                if current_dialogue_line == 1:
                    # When creating an event make sure to list the number of lines in the first dialogue check (match lowest line)
                    self.event_num_lines = 3
                    overlay.draw_dialogue_box("(Welcome to Korona Kingdom! To cycle through dialogue press [Enter]!)", "Main Character", view_bottom, view_left)
                elif current_dialogue_line == 2:
                    overlay.draw_dialogue_box("(The goal of the game is to find a roll of toilet paper.)", "Main Character", view_bottom, view_left)
                elif current_dialogue_line == 3:
                    overlay.draw_dialogue_box("(You’ve heard that the Dollar Store east of here may be selling some.)", "Main Character", view_bottom, view_left)
            # Dollar Tree Intro Event
            elif event_ID == "2":
                if current_dialogue_line == 1:
                    # When creating an event make sure to list the number of lines in the first dialogue check (match lowest line)
                    self.event_num_lines = 1
                    overlay.draw_dialogue_box("(This is the Dollar Store, maybe I should check in here)", "Main Character", view_bottom, view_left)
            # School Intro Event
            elif event_ID == "3":
                if current_dialogue_line == 1:
                    # When creating an event make sure to list the number of lines in the first dialogue check (match lowest line)
                    self.event_num_lines = 1
                    overlay.draw_dialogue_box("(This is the School, maybe I should check in here)", "Main Character", view_bottom, view_left)
            # Malmart Intro Event
            elif event_ID == "4":
                if current_dialogue_line == 1:
                    # When creating an event make sure to list the number of lines in the first dialogue check (match lowest line)
                    self.event_num_lines = 1
                    overlay.draw_dialogue_box("(This is Malmart, maybe I should check in here)", "Main Character", view_bottom, view_left)
            # Angry Man Boss Fight Dialogue (Created by event_ID #X in Dollar Store)
            elif event_ID == "5":
                if current_dialogue_line == 1:
                    # When creating an event make sure to list the number of lines in the first dialogue check (match lowest line)
                    self.event_num_lines = 3
                    overlay.draw_dialogue_box("(The man who stole your toilet paper is still in front of the store)", "Main Character", view_bottom, view_left)
                elif current_dialogue_line == 2:
                    overlay.draw_dialogue_box("(You approach the man angrily)", "Main Character", view_bottom, view_left)
                elif current_dialogue_line == 3:
                    overlay.draw_dialogue_box("(Looks like a boss event is going to begin)", "Main Character", view_bottom, view_left)
            # Angry Man Aftermath
            elif event_ID == "6":
                if current_dialogue_line == 1:
                    # When creating an event make sure to list the number of lines in the first dialogue check (match lowest line)
                    self.event_num_lines = 4
                    overlay.draw_dialogue_box("(It’s one of those fights that you won, but somehow lost)", "Main Character", view_bottom, view_left)
                elif current_dialogue_line == 2:
                    overlay.draw_dialogue_box("Thanks for the roll!", "Man", view_bottom, view_left)
                elif current_dialogue_line == 3:
                    overlay.draw_dialogue_box("I bet those plague carriers at the school have some stockpiled!", "Man", view_bottom, view_left)
                elif current_dialogue_line == 4:
                    overlay.draw_dialogue_box("(Maybe I should look there next?)", "Main Character", view_bottom, view_left)
            # Found Item events
            # Revolver
            elif event_ID == "50":
                if current_dialogue_line == 1:
                    # When creating an event make sure to list the number of lines in the first dialogue check (match lowest line)
                    self.event_num_lines = 1
                    overlay.draw_dialogue_box("(You found a REVOLVER)", "Main Character", view_bottom, view_left)
                    # For items we need this check or else we'll continuously create objects while drawing when
                    # we only want 1
                    if self.need_to_add_item:
                        # Insert into Weapons Array
                        player_items[1].append(Entity.Revolver())
                        # No longer need to add item to the array
                        self.need_to_add_item = False
        elif map_name == "DollarStore":
            # Entered Dollar Store Event
            if event_ID == "1":
                if current_dialogue_line == 1:
                    # When creating an event make sure to list the number of lines in the first dialogue check (match lowest line)
                    self.event_num_lines = 1
                    overlay.draw_dialogue_box("(There has to be some toilet paper in here somewhere right?)", "Main Character", view_bottom, view_left)
            # Leaving Dollar Store Event
            elif event_ID == "2":
                if current_dialogue_line == 1:
                    # When creating an event make sure to list the number of lines in the first dialogue check (match lowest line)
                    self.event_num_lines = 3
                    overlay.draw_dialogue_box("(As you are about to exit, an angry man walks up to you)", "Main Character", view_bottom, view_left)
                elif current_dialogue_line == 2:
                    overlay.draw_dialogue_box("Gimme that last roll, I know you found it!", "Man", view_bottom, view_left)
                elif current_dialogue_line == 3:
                    overlay.draw_dialogue_box("(The man swipes the toilet from your hand and runs out the door)", "Man", view_bottom, view_left)
                # Chaining to event 5 outside dollar store
                if self.need_to_add_item:
                    # Create Event outside
                    self.testSprite = arcade.Sprite("maps/Man_Tile.png", scale=1.25)
                    # Subtract 160 (V), use center_x and center_y as reference (or just test on Tiled)
                    self.testSprite.set_position(6960, 5040)
                    # Give Event an ID tag so we know which ID to reference
                    self.testSprite.properties.__setitem__("ID", "5")
                    # Add event to appropriate list (overworld event)
                    self.dialogue_events_overworld.append(self.testSprite)
                    # Remove the player's toilet paper
                    player_items[7].clear()
                    # No longer need to add item to the array
                    self.need_to_add_item = False
            # Found Item events
            # Toilet paper
            elif event_ID == "51":
                if current_dialogue_line == 1:
                    # When creating an event make sure to list the number of lines in the first dialogue check (match lowest line)
                    self.event_num_lines = 1
                    overlay.draw_dialogue_box("(You found Toilet Paper)", "Main Character", view_bottom, view_left)
                    # For items we need this check or else we'll continuously create objects while drawing when
                    # we only want 1
                    if self.need_to_add_item:
                        # Insert into TBD Array
                        player_items[7].append(Entity.ToiletPaper())
                        # Chanining to event #2
                        self.testSprite = arcade.Sprite("maps/dialogue_event_3.png", scale=1.25)
                        # Subtract 160 (V), use center_x and center_y as reference (or just test on Tiled)
                        self.testSprite.set_position(240, 2960)
                        # Give Event an ID tag so we know which ID to reference
                        self.testSprite.properties.__setitem__("ID", "2")
                        # Add event to appropriate list (overworld event)
                        self.dialogue_events_dollarstore.append(self.testSprite)
                        # No longer need to add item to the array
                        self.need_to_add_item = False
            elif event_ID == "52":
                if current_dialogue_line == 1:
                    # When creating an event make sure to list the number of lines in the first dialogue check (match lowest line)
                    self.event_num_lines = 1
                    overlay.draw_dialogue_box("(You found some hydroxychloroquine)", "Main Character", view_bottom, view_left)
                    if self.need_to_add_item:
                        # Insert into Consumables List
                        player_items[6].append(Entity.H0CQ())
                        # No longer need to add item to the array
                        self.need_to_add_item = False
        elif map_name == "MalMart":
            # Entered MalMart Event
            if event_ID == "1":
                if current_dialogue_line == 1:
                    # When creating an event make sure to list the number of lines in the first dialogue check (match lowest line)
                    self.event_num_lines = 1
                    overlay.draw_dialogue_box("(I wonder what I can find here)", "Main Character", view_bottom, view_left)
        elif map_name == "TheSchool":
            # Entered School Event
            if event_ID == "1":
                if current_dialogue_line == 1:
                    # When creating an event make sure to list the number of lines in the first dialogue check (match lowest line)
                    self.event_num_lines = 1
                    overlay.draw_dialogue_box("(nyyyaAAGhrrrAaaa!)", "Covid Mantis", view_bottom, view_left)
            if event_ID == "2":
                if current_dialogue_line == 1:
                    # When creating an event make sure to list the number of lines in the first dialogue check (match lowest line)
                    self.event_num_lines = 1
                    overlay.draw_dialogue_box("(nNNRrrrghhHAHAHA)", "Covid Mantis", view_bottom, view_left)
            if event_ID == "6":
                if current_dialogue_line == 1:
                    # When creating an event make sure to list the number of lines in the first dialogue check (match lowest line)
                    self.event_num_lines = 1
                    overlay.draw_dialogue_box("(huuuuNNNGGRRRAGAAHAHAH)", "Covid Mantis", view_bottom, view_left)
                    if self.need_to_add_item:
                        self.need_to_add_item = False
                        self.testSprite = arcade.Sprite("maps/floor.png", scale=1.25)
                        self.testSprite.set_position(240, 2960)
                        self.testSprite.properties.__setitem__("ID", "7")
                        self.dialogue_events_school.append(self.testSprite)
            if event_ID == "7":
                if current_dialogue_line == 1:
                    self.event_num_lines = 3
                    overlay.draw_dialogue_box("Boy that escalated quickly, things really got out of hand.", "Main Character", view_bottom, view_left)
                if current_dialogue_line == 2:
                    overlay.draw_dialogue_box("All this toilet paper is gooey...", "Main Character", view_bottom, view_left)
                if current_dialogue_line == 3:
                    overlay.draw_dialogue_box("I guess I have no other choice but to go where only Karens dare,\ninto the maw of Malmart I go...", "Main Character", view_bottom, view_left)

    # Create an encounter after dialogue event is over (pressed [Enter] on last dialogue string)
    def handle_add_encounter_after_event(self, event_id, map_name, encounter, view_bottom, view_left):
        if map_name == "overworld":
            # Create Hobo Boss Event at the end of Event #5
            if event_id == "5":
                encounter.active_encounter = True
                encounter.setup_kombat("hobo", view_left, view_bottom)
        elif map_name == "TheSchool":
            if event_id == "6":
                encounter.active_encounter = True
                encounter.setup_kombat("covid_mantis", view_left, view_bottom)

    # Create an event after a boss encounter is over
    def handle_add_event_after_encounter(self, return_string, map_name):
        #Defeated the Dollar Store Boss
        if "Homeless Man" in return_string and map_name == "overworld":
            self.dollar_store_boss_aftermath = arcade.Sprite("maps/Man_Tile.png", scale=1.25)
            # Coords of events
            self.dollar_store_boss_aftermath.set_position(6960, 5040)
            # Give Event an ID tag so we know which ID to reference
            self.dollar_store_boss_aftermath.properties.__setitem__("ID", "6")
            # Add event to appropriate list (overworld event)
            self.dialogue_events_overworld.append(self.dollar_store_boss_aftermath)