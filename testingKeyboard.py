import time

import keyboard
import mouse
import json

curPreset = 'default'
presetDict = {'default': {'test' : ['ctrl', '', '', 'true', 'true']}}

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


# call 
def handle_action(action: str):
    elements = presetDict[curPreset][action]
    key1, key2, key3 = elements[0], elements[1], elements[2]
    hold = elements[3]
    track_movement = elements[4]

    if hold == 'true':
        simulate_hotkey_hold(key1, key2, key3)
    else:
        simulate_hotkey_press(key1, key2, key3)

    #if this action's delta should move the mouse
    if track_movement == 'true':
        mouse.move(5, 5, absolute=False, duration=0.1)
        return

def simulate_mouse(btn: int, scroll: int = None):
    if btn == 0:
        mouse.click('left')
    elif btn == 1:
        mouse.click('right')
    elif btn == 2 and scroll is None:
        mouse.click('middle')
    elif btn == 2 and scroll is not None:
        mouse.wheel(scroll)


def simulate_hotkey_press(key1: str = '', key2: str = '', key3: str = ''):
    # check if the third key is a mouse button
    hotkey = ''
    if key1 != '':
        hotkey += key1

        if key2 != '':
            hotkey += '+'
            hotkey += key2
            if key3 != '':
                hotkey += '+'
                hotkey += key3
    elif key2 != '':
        hotkey += key2
        if key3 != '':
            hotkey += '+'
            hotkey += key3


    if key3 == 'left' or key3 == 'right' or key3 == 'middle' or key3 == 'scroll':
        if key3 == 'left':
            simulate_mouse(0)
        elif key3 == 'right':
            simulate_mouse(1)
        elif key3 == 'middle':
            simulate_mouse(2)
        else:
            simulate_mouse(2, 1)
    elif key3 != '':
        hotkey += key3

    if hotkey != '':
        return hotkey
        #keyboard.send(hotkey)
    return hotkey

def simulate_hotkey_hold(key1: str = '', key2: str = '', key3: str = ''):
    if key1 != '':
        keyboard.press(key1)
    if key2 != '':
        keyboard.press(key2)
    if key3 != '':
        keyboard.press(key3)

    print("holding " + key1)

def stop_simulated_hotkey_hold(key1: str = '', key2: str = '', key3: str = ''):
    if key1 != '':
        keyboard.release(key1)
    if key2 != '':
        keyboard.release(key2)
    if key3 != '':
        keyboard.release(key3)

    print("stopped holding " + key1)

handle_action('test')

time.sleep(1)
stop_simulated_hotkey_hold('ctrl', '', '')



def record_hotkey():
    return  # hotkeys = []
    # key1 = ''
    # while key1 == '':
    #     key1 = keyboard.read_event()
    #
    # hotkeys.append(key1)
    #
    # key2 = ''
    # while keyboard.is_pressed(key1) and key2 == '':
