import arcade

class Event:

    def __init__(self):
        self.event_num_lines = 0

    # Handle Dialogue Events in the world
    def handle_dialogue_event(self, event_ID, overlay, current_dialogue_line, view_left, view_bottom):
        # House Event
        if event_ID == "1":
            if current_dialogue_line == 1:
                # When creating an event make sure to list the number of lines in the first dialogue check (match lowest line)
                self.event_num_lines = 1
                overlay.draw_dialogue_box("Why can't I enter my own house?", "Main Character", view_bottom, view_left)
        # MalMart Event
        if event_ID == "2":
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