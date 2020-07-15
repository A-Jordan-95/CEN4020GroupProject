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
                    overlay.draw_dialogue_box("(Boss Fight?)", "Main Character", view_bottom, view_left)
                    # We need to add an event after our boss fight.
                    if self.need_to_add_item:
                        # Event Chaining - Add new event to Overworld Map (use grass to hide it later, or just use grass)
                        self.dollar_store_boss_aftermath = arcade.Sprite("maps/dialogue_event_6.png", scale=1.25)
                        # Add 160x2 (>), use center_x and center_y as reference (or just test on Tiled)
                        self.dollar_store_boss_aftermath.set_position(6960, 5040)
                        # Give Event an ID tag so we know which ID to reference
                        self.dollar_store_boss_aftermath.properties.__setitem__("ID", "6")
                        # Add event to appropriate list (overworld event)
                        self.dialogue_events_overworld.append(self.dollar_store_boss_aftermath)
                        # No longer need to add item to the array
                        self.need_to_add_item = False
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
                        player_items[2].append(Entity.Revolver())
                        player_items[2].append(Entity.Revolver())
                        player_items[2].append(Entity.Revolver())
                        player_items[2].append(Entity.Revolver())
                        player_items[2].append(Entity.Fists())
                        player_items[2].append(Entity.Revolver())
                        player_items[2].append(Entity.Fists())
                        player_items[2].append(Entity.Fists())
                        player_items[2].append(Entity.Fists())
                        player_items[2].append(Entity.Revolver())
                        player_items[2].append(Entity.Revolver())
                        player_items[2].append(Entity.Fists())
                        # No longer need to add item to the array
                        self.need_to_add_item = False
                        #Event Chaining - Add new event to Map (testing event 5 for overworld spawn, hidden in grass near front of dollar store)
                        self.testSprite = arcade.Sprite("maps/dialogue_event_5.png", scale=1.25)
                        # Subtract 160 (V), use center_x and center_y as reference (or just test on Tiled)
                        self.testSprite.set_position(6960, 5040)
                        # Give Event an ID tag so we know which ID to reference
                        self.testSprite.properties.__setitem__("ID", "5")
                        # Add event to appropriate list (overworld event)
                        self.dialogue_events_overworld.append(self.testSprite)
                        # Delete Events not used initially
                        for x in self.dialogue_events_overworld:
                            print(x.properties)
                            print(x.center_x)
                            print(x.center_y)
                        print(player_items)
        elif map_name == "DollarStore":
            # Entered Dollar Store Event
            if event_ID == "1":
                if current_dialogue_line == 1:
                    # When creating an event make sure to list the number of lines in the first dialogue check (match lowest line)
                    self.event_num_lines = 1
                    overlay.draw_dialogue_box("(I wonder what I can find here)", "Main Character", view_bottom, view_left)
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
                        print(player_items)
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
                    overlay.draw_dialogue_box("(I wonder what I can find here)", "Main Character", view_bottom, view_left)