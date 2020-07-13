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
            # House Event
            if event_ID == "1":
                if current_dialogue_line == 1:
                    # When creating an event make sure to list the number of lines in the first dialogue check (match lowest line)
                    self.event_num_lines = 1
                    overlay.draw_dialogue_box("Why can't I enter my own house?\nPress [Enter] to exit.", "Main Character", view_bottom, view_left)
            # MalMart Event
            elif event_ID == "2":
                if current_dialogue_line == 1:
                    # When creating an event make sure to list the number of lines in the first dialogue check (match lowest line)
                    self.event_num_lines = 4
                    overlay.draw_dialogue_box("(As you walk up to Malmart you sense a dark presence inside.\nSomething doesn't seem right.)", "Main Character", view_bottom, view_left)
                elif current_dialogue_line == 2:
                    overlay.draw_dialogue_box("(A women walks out the door)", "Main Character", view_bottom, view_left)
                elif current_dialogue_line == 3:
                    overlay.draw_dialogue_box("MOVE! You're in the way!", "Karen", view_bottom, view_left)
                elif current_dialogue_line == 4:
                    overlay.draw_dialogue_box("(You move out of the women's way quickly)", "Main Character", view_bottom, view_left)
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
                        #Event Chaining - Add new event to Map
                        self.testSprite = arcade.Sprite("maps/dialogue_event_2.png", scale=1.25)
                        # Subtract 160 (V), use center_x and center_y as reference (or just test on Tiled)
                        self.testSprite.set_position(400, 4400)
                        # Give Event an ID tag so we know which ID to reference
                        self.testSprite.properties.__setitem__("ID", "2")
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