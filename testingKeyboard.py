import keyboard
import mouse
import json

curPreset = 'default'
presetDict = {'default' : {}}

cur_key_map = {}

def create_preset(name: str, key_map: dict):
    presetDict[name] = key_map


# removes the current preset if it is not the default preset
# and switches back to default preset
def remove_preset(name: str):
    if name == 'default':
        return
    del presetDict[name]
    switch_preset('default')



# switch the activated preset
def switch_preset(name: str):
    curPreset = name


# Bind a user action to hotkeys
def bind_action(action: str, keys: list[str]):
    presetDict[curPreset][action] = keys



def on_key_event(e):
    if e.name == 'm' and e.event_type == 'down':  # Press 'm' to move the mouse
        mouse.move(50, 50, absolute=False, duration=0.1)
        # mouse.click('left')  # Perform a left-click
        print("Mouse moved and clicked!")

# Hook the key event
keyboard.hook(on_key_event)


def simulate_hotkey(key1: str = None, key2: str = None, key3: str = None):
    if key1 is None:
        print("Not a valid key input!")
        return
    if key2 is None:
        keyboard.send(key1)
    elif key3 is None:
        keyboard.send(key1 + '+' + key2)
    else:
        keyboard.send(key1 + '+' + key2 + '+' + key3)


def simulate_mouse(btn: int, scroll: int = None):
    if btn == 0:
        mouse.click('left')
    elif btn == 1:
        mouse.click('right')
    elif btn == 2 and scroll is None:
        mouse.click('middle')
    elif btn == 2 and scroll is not None:
        mouse.wheel(scroll)

def record_hotkey():
    return# hotkeys = []
    # key1 = ''
    # while key1 == '':
    #     key1 = keyboard.read_event()
    #
    # hotkeys.append(key1)
    #
    # key2 = ''
    # while keyboard.is_pressed(key1) and key2 == '':