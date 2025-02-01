import keyboard
import mouse
import roboflow



def on_key_event(e):
    if e.name == 'm' and e.event_type == 'down':  # Press 'm' to move the mouse
        mouse.move(500, 500)  # Move the mouse to (500, 500)
        # mouse.click('left')  # Perform a left-click
        print("Mouse moved and clicked!")

# Hook the key event
keyboard.hook(on_key_event)

print("Press 'm' to move and click themmmmmm mouse. Press 'esc' to exit.")
keyboard.wait('esc')  # Keep the program running until 'esc' is pressed