import Entity
import koronakombat as kk
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
    def handle_dialogue_event(self, event_ID, overlay, current_dialogue_line, map_name, player_items, view_left, view_bottom, player):
        if map_name == "overworld":
            # Intro Event
            if event_ID == "1":
                if current_dialogue_line == 1:
                    # When creating an event make sure to list the number of lines in the first dialogue check (match lowest line)
                    self.event_num_lines = 4
                    overlay.draw_dialogue_box("(Welcome to Korona Kingdom! To cycle through dialogue press [Enter]!)", "Main Character", view_bottom, view_left)
                elif current_dialogue_line == 2:
                    overlay.draw_dialogue_box("(The goal of the game is to find a roll of toilet paper.)", "Main Character", view_bottom, view_left)
                elif current_dialogue_line == 3:
                    overlay.draw_dialogue_box("(You’ve heard that the Dollar Store east of here may be selling some.)", "Main Character", view_bottom, view_left)
                elif current_dialogue_line == 4:
                    overlay.draw_dialogue_box("(Tip: Be sure to explore the map to find the tools needed to surive the \n Korona-polcalypse (Some items may be hidden for you to discover...))", "Main Character", view_bottom, view_left)
                    if self.need_to_add_item:
                        player_items[1].append(Entity.Fists())
                        self.need_to_add_item = False
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
            elif event_ID == "100":
                #using the same concept for weapon adding, so that health deducted
                #only one time per encounter
                overlay.draw_dialogue_box("This fire is intense, maybe its fueled by Tabasco sauce...", "Main Character", view_bottom, view_left)
                if self.need_to_add_item:
                    player.hp -= 1
                    self.need_to_add_item = False
            elif event_ID == "200":
                overlay.draw_dialogue_box("(You found a SHOTGUN)", "Main Character", view_bottom, view_left)
                if self.need_to_add_item:
                    player_items[1].append(Entity.Shotgun())
                    self.need_to_add_item = False
                    self.testSprite = arcade.Sprite("maps/dialogue_event_5.png", scale=1.25)
                    # Subtract 160 (V), use center_x and center_y as reference (or just test on Tiled)
                    self.testSprite.set_position(6960, 5040)
                    # Give Event an ID tag so we know which ID to reference
                    self.testSprite.properties.__setitem__("ID", "5")
                    # Add event to appropriate list (overworld event)
                    self.dialogue_events_overworld.append(self.testSprite)
            elif event_ID == "420":
                if current_dialogue_line == 1:
                    self.event_num_lines = 3
                    overlay.draw_dialogue_box("Ay brah", "Chad", view_bottom, view_left)
                elif current_dialogue_line == 2:
                    overlay.draw_dialogue_box("Quaratine sucks brah", "Chad", view_bottom, view_left)
                elif current_dialogue_line == 3:
                    overlay.draw_dialogue_box("I just wanna hit the gym brah", "Chad", view_bottom, view_left)
            elif event_ID == "421":
                overlay.draw_dialogue_box("You find a packaged, unopened mask...", "Main Character", view_bottom, view_left)
                if self.need_to_add_item:
                    player_items[0].append(Entity.Mask())
                    self.need_to_add_item = False
            elif event_ID == "422":
                overlay.draw_dialogue_box("This hat should keep away the non-mask wearers", "Main Character", view_bottom, view_left)
                if self.need_to_add_item:
                    player_items[0].append(Entity.NoodleHat())
                    self.need_to_add_item = False
            elif event_ID == "424":
                overlay.draw_dialogue_box("I don't know what will get me first:\n Corona or this?", "Main Character", view_bottom, view_left)
                if self.need_to_add_item:
                    player_items[6].append(Entity.Drink())
                    self.need_to_add_item = False
            elif event_ID == "425":
                overlay.draw_dialogue_box("I think the nuggets are still warm...", "Main Character", view_bottom, view_left)
                if self.need_to_add_item:
                    player_items[6].append(Entity.MedKit())
                    self.need_to_add_item = False
            elif event_ID == "426":
                overlay.draw_dialogue_box("This stuff works, depending upon your \n political alignment", "Main Character", view_bottom, view_left)
                if self.need_to_add_item:
                    player_items[6].append(Entity.H0CQ())
                    self.need_to_add_item = False
            elif event_ID == "102":
                overlay.draw_dialogue_box("Mein Gott!", "Main Character", view_bottom, view_left)
                if self.need_to_add_item:
                    player_items[1].append(Entity.MP40())
                    self.need_to_add_item = False
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
                    # # We need to add an event after our boss fight.
                    # if self.need_to_add_item:
                    #     # Event Chaining - Add new event to Overworld Map (use grass to hide it later, or just use grass)
                    #     self.dollar_store_boss_aftermath = arcade.Sprite("maps/dialogue_event_6.png", scale=1.25)
                    #     # Add 160x2 (>), use center_x and center_y as reference (or just test on Tiled)
                    #     self.dollar_store_boss_aftermath.set_position(6960, 5040)
                    #     # Give Event an ID tag so we know which ID to reference
                    #     self.dollar_store_boss_aftermath.properties.__setitem__("ID", "6")
                    #     # Add event to appropriate list (overworld event)
                    #     self.dialogue_events_overworld.append(self.dollar_store_boss_aftermath)
                    #     # No longer need to add item to the array
                    #     self.need_to_add_item = False
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
                        #Event Chaining - Add new event to Map (testing event 5 for overworld spawn, hidden in grass near front of dollar store)
                        self.testSprite = arcade.Sprite("maps/dialogue_event_5.png", scale=1.25)
                        # Subtract 160 (V), use center_x and center_y as reference (or just test on Tiled)
                        self.testSprite.set_position(6960, 5040)
                        # Give Event an ID tag so we know which ID to reference
                        self.testSprite.properties.__setitem__("ID", "5")
                        # Add event to appropriate list (overworld event)
                        self.dialogue_events_overworld.append(self.testSprite)
                        # Delete Events not used initially
                        #print(player_items)
        elif map_name == "DollarStore":
            # Entered Dollar Store Event
            if event_ID == "1":
                if current_dialogue_line == 1:
                    # When creating an event make sure to list the number of lines in the first dialogue check (match lowest line)
                    self.event_num_lines = 1
                    overlay.draw_dialogue_box("(There has to be some toilet paper in here somewhere right?)", "Main Character", view_bottom, view_left)

            # Leaving Dollar Store Event
            if event_ID == "2":
                if current_dialogue_line == 1:
                    # When creating an event make sure to list the number of lines in the first dialogue check (match lowest line)
                    self.event_num_lines = 3
                    overlay.draw_dialogue_box("(As you are about to exit, an angry man walks up to you)", "Main Character", view_bottom, view_left)
                elif current_dialogue_line == 2:
                    overlay.draw_dialogue_box("Gimme that last roll, I know you found it!", "Man", view_bottom, view_left)
                elif current_dialogue_line == 3:
                    overlay.draw_dialogue_box("(The man swipes the toilet from your hand and runs out the door)", "Man", view_bottom, view_left)
                #Chaining to event 5 outside dollar store
                if self.need_to_add_item:
                    # Insert into Weapons Array
                    player_items[1].append(Entity.Revolver())
                    # No longer need to add item to the array
                    self.need_to_add_item = False
                    self.testSprite = arcade.Sprite("maps/dialogue_event_5.png", scale=1.25)
                    # Subtract 160 (V), use center_x and center_y as reference (or just test on Tiled)
                    self.testSprite.set_position(6960, 5040)
                    # Give Event an ID tag so we know which ID to reference
                    self.testSprite.properties.__setitem__("ID", "5")
                    # Add event to appropriate list (overworld event)
                    self.dialogue_events_overworld.append(self.testSprite)
                    print(player_items)
            # Found Item events
            # Revolver
            elif event_ID == "50":
                if current_dialogue_line == 1:
                    # When creating an event make sure to list the number of lines in the first dialogue check (match lowest line)
                    self.event_num_lines = 1
                    overlay.draw_dialogue_box("(You found a REVOLVER)", "Main Character", view_bottom, view_left)
                    # For items we need this check or else we'll continuously create objects while drawing when
                    # we only want 1
                    #Chaining to event 2 inside dollar store
                    if self.need_to_add_item:
                        # Insert into Weapons Array
                        player_items[1].append(Entity.Revolver())
                        # No longer need to add item to the array
                        self.need_to_add_item = False
                        self.testSprite = arcade.Sprite("maps/dialogue_event_3.png", scale=1.25)
                        # Subtract 160 (V), use center_x and center_y as reference (or just test on Tiled)
                        self.testSprite.set_position(240, 2960)
                        # Give Event an ID tag so we know which ID to reference
                        self.testSprite.properties.__setitem__("ID", "2")
                        # Add event to appropriate list (overworld event)
                        self.dialogue_events_dollarstore.append(self.testSprite)
                        print(player_items)
            # Toilet paper  //requires creation of ToiletPaper entity
            #elif event_ID == "51":
                #if current_dialogue_line == 1:
                    # When creating an event make sure to list the number of lines in the first dialogue check (match lowest line)
                    #self.event_num_lines = 1
                   # overlay.draw_dialogue_box("(You found Toilet Paper)", "Main Character", view_bottom, view_left)
                    # For items we need this check or else we'll continuously create objects while drawing when
                    # we only want 1
                    #if self.need_to_add_item:
                        # Insert into Weapons Array
                        #player_items[1].append(Entity.ToiletPaper())
                        # No longer need to add item to the array
                        #self.need_to_add_item = False
                        #print(player_items)
        elif map_name == "MalMart":
            # Entered MalMart Event
            if event_ID == "1":
                if current_dialogue_line == 1:
                    # When creating an event make sure to list the number of lines in the first dialogue check (match lowest line)
                    self.event_num_lines = 1
                    overlay.draw_dialogue_box("(Many have entered, none have left)", "Main Character", view_bottom, view_left)
            #When player hits fire, then issue damage
            elif event_ID == "100":
                #using the same concept for weapon adding, so that health deducted
                #only one time per encounter
                overlay.draw_dialogue_box("The hellfire burns your skin...", "Main Character", view_bottom, view_left)
                if self.need_to_add_item:
                    player.hp -= 1
                    self.need_to_add_item = False
            elif event_ID == "101":
                #using the same concept for weapon adding, so that health deducted
                #only one time per encounter
                overlay.draw_dialogue_box("The lava begins to melt your flesh...", "Main Character", view_bottom, view_left)
                if self.need_to_add_item:
                    player.hp -= 3
                    self.need_to_add_item = False
            elif event_ID == "51":
                #using the same concept for weapon adding, so that health deducted
                #only one time per encounter
                overlay.draw_dialogue_box("You finally found it, the legendary toilet roll. But others seek to disposses \nyou of your treasure", "Main Character", view_bottom, view_left)
                if self.need_to_add_item:
                    player_items[1].append(Entity.ToiletPaper())
                    # No longer need to add item to the array
                    self.need_to_add_item = False
                    #print(player_items)
            #When player hits fire, then issue damage
            if player.hp <= 0:
                print("Defeat!")
                exit()

        elif map_name == "TheSchool":
            # Entered School Event
            if event_ID == "1":
                if current_dialogue_line == 1:
                    # When creating an event make sure to list the number of lines in the first dialogue check (match lowest line)
                    self.event_num_lines = 1
                    overlay.draw_dialogue_box("(I wonder what I can find here)", "Main Character", view_bottom, view_left)

    # Create an encounter after dialogue event is over (pressed [Enter] on last dialogue string)
    def handle_add_encounter_after_event(self, event_id, map_name, encounter, view_bottom, view_left):
        if map_name == "overworld":
            # Create Hobo Boss Event at the end of Event #5
            if event_id == "5":
                encounter.active_encounter = True
                encounter.setup_kombat("hobo", view_left, view_bottom)
        elif map_name == "DollarStore":
            pass
