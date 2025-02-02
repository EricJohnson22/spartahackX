import tkinter as tk
import testingKeyboard as preset
from testingRoboflowModel import GestureRecognizer

"""
IMPORTANT: this is going to function as main from now on, i was too lazy to convert this file into class that could be initialized in
a seperate main function, ignore the previous main function -Eric
"""

buffer = .1
test = GestureRecognizer(buffer)
run = True
hold = 0
track = 0
repeat = 0

preset.load_user_settings()


# create the main window frame
root = tk.Tk()
root.title("SwiftFlow")

# set default window size (width*height)
root.geometry(f"{800}x{600}")

# Create different sections using nested frames
# add content to individual frames to maintain structure


#
# Menu bar
#
menubar = tk.Menu(root)
root.config(menu=menubar)

def exit_program():
    preset.save_user_settings()
    global run
    run = False
    #SAVE SHIT TO JSON FILE
    return
root.protocol('WM_DELETE_WINDOW', exit_program)
# Create File menu
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
# Add Exit command to File menu
file_menu.add_command(label="Exit", command=exit_program)
# Create Edit menu
edit_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit_menu)
# Create Help menu
help_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help_menu)


#
# Header
#
# Configure column weights for scaling
root.grid_columnconfigure(0, weight=3)  # Column 0 has a weight of 1
root.grid_columnconfigure(1, weight=1)  # Column 1 has a weight of 2

header_frame = tk.Frame(root)
header_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=15)
tk.Label(header_frame, text="Manage your SwiftFlow presets", font=("Arial", 14, "bold")).pack()


#
# Main Frame
#
# make the mainframe. THis is the frame which will be central for the application
mainframe = tk.Frame(root, borderwidth=1)
mainframe.grid(row=1, column=0, pady=10, padx=15)

def create_preset():
    key_dict = {}
    key_list = [key1_value.get(), key2_value.get(), key3_value.get(),bool_helper(hold),bool_helper(track),bool_helper(repeat)]
    key_dict[action_value.get()] = key_list
    curr_preset = preset_name.get()
    preset.update_preset(curr_preset, key_dict)
    populate_list() # repopulate list as it changed

def delete_preset():
    curr_preset = preset_name.get()
    preset.remove_preset(curr_preset)
    populate_list()

def bool_helper(val):
    if val:
        return 'true'
    else:
        return 'false'

def register_action():
    global hold
    global repeat
    preset.bind_action(action_value.get(), [key1_value.get(),key2_value.get(),key3_value.get(),bool_helper(hold),bool_helper(track),bool_helper(repeat)])
    if isinstance(key1_value.get(), str):
        print("working")
    print(key1_value.get())
    print(key2_value.get())
    print(key3_value.get())

    #gonna have to handle when certain binds arent available, or maybe not i dont know


# create button
tk.Button(mainframe, text="Create Preset", command=lambda: create_preset()).pack(padx=5, pady=10)

tk.Button(mainframe, text="Add Bind", command=lambda: register_action()).pack(padx=5, pady=14)


def toggle_hold():
    global hold
    if hold:
        hold = 0
    else:
        hold = 1


def toggle_track():
    global track
    if track:
        track = 0
    else:
        track = 1


def toggle_repeat():
    global repeat

    if repeat:
        repeat = 0
    else:
        repeat = 1
    print(bool_helper(repeat))


var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
c1 = tk.Checkbutton(mainframe, text='Press and Hold',variable=var1, onvalue=1, offvalue=0, command=toggle_hold)
c2 = tk.Checkbutton(mainframe, text='Track',variable=var2, onvalue=1, offvalue=0, command=toggle_track)
c3 = tk.Checkbutton(mainframe, text='Repeat',variable=var3, onvalue=1, offvalue=0, command=toggle_repeat)
c1.pack()
c2.pack()
c3.pack()


#
# Dropdowns
#

# make the dropdown frame. THis is the center frame for the application
dropdown_frame = tk.Frame(mainframe, borderwidth=1)
dropdown_frame.pack(side="top", pady=30)

alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]  # A-Z
# Number keys (0-9)
numbers = [str(i) for i in range(10)]  # 0-9
# Symbol keys (common symbols on a US QWERTY keyboard)
symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',  # Shift + 1-0
    '-', '_', '=', '+',  # - = keys
    '[', ']', '{', '}',  # [ ] keys
    '\\', '|',  # \ key
    ';', ':',  # ; key
    "'", '"',  # ' key
    ',', '<', '.', '>', '/', '?',  # , . / keys
    '`', '~', 'left', 'right' 'middle', 'scroll',''# ` key
]

key1_list = ["Ctrl", "Shift", "Alt", "Super", ""]   # options for one and two
key3_list = alphabet + numbers + symbols
actions_list = ["Rock", "Paper", "Scissors"]    # list of available actions for now

px1 = 10    # x padding for dropdowns
py1 = 5    # y padding for dropdowns

# Create a StringVar to store the selected value
key1_value = tk.StringVar(dropdown_frame)
key1_value.set(key1_list[0])  # Set default value

# Create a dropdown for Key 1
dropdown1 = tk.OptionMenu(dropdown_frame, key1_value, *key1_list)
dropdown1.grid(row=0, column=0, padx=px1, pady=py1)

# Create a dropdown for Key 2
key2_value = tk.StringVar()
key2_value.set(key1_list[0])  # Set default value

dropdown2 = tk.OptionMenu(dropdown_frame, key2_value, *key1_list)
dropdown2.grid(row=0, column=1, padx=px1, pady=py1)

# Create a dropdown for Key 3
key3_value= tk.StringVar()
key3_value.set(key3_list[0])  # Set default value

dropdown3 = tk.OptionMenu(dropdown_frame, key3_value, *key3_list)
dropdown3.grid(row=0, column=2, padx=px1, pady=py1)

# create dropdown for actions user can select
action_value= tk.StringVar()
action_value.set(actions_list[0])  # Set default value

dropdown4 = tk.OptionMenu(dropdown_frame, action_value, *actions_list)
dropdown4.grid(row=0, column=3, padx=px1, pady=py1)


#
# Form frame
#
form_frame = tk.Frame(mainframe, borderwidth=1)
form_frame.pack(side="bottom")

# text field for preset name. name: [    ]
label = tk.Label(form_frame, text="Name of Preset:")
label.pack(side="left")
preset_name = tk.Entry(form_frame, font=("Arial", 12), width=20)
preset_name.pack(side="right")


#
# Sidebar
#

side_frame = tk.Frame(root, borderwidth=1)
side_frame.grid(row=1, column=1, pady=10, padx=15, rowspan=4, sticky="nsew")

# Populate the Listbox with items from the list
# This function is called when creating a new preset as well
def populate_list():
    listbox.delete(0, tk.END)   # clear it
    for item in preset.presetDict.keys():
        listbox.insert(tk.END, item)

# Function to retrieve the selected item(s)
def get_selected_item():
    position = listbox.curselection()  # Get the indices of selected items
    selected_item = listbox.get(position)  # Get the items
    print(selected_item)
    preset.switch_preset(selected_item)
    # fetch values form dictionary

# Create a Listbox widget
listbox = tk.Listbox(side_frame)
listbox.pack(fill="both", expand=True)
populate_list()     # populate list at start

# Add a button to confirm the selection
confirm_button = tk.Button(side_frame, text="Select", command=lambda: get_selected_item())
confirm_button.pack(pady=10)


# start window
while run:
    test.recognizer_run()
    root.update()

test.recognizer_terminate()





