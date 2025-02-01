import tkinter as tk


# create the main window frame
root = tk.Tk()
root.title("SpartaHackX")

# set default window size (width*height)
root.geometry(f"{800}x{600}")

# Create different sections using nested frames
# add content to individual frames to maintain structure


#--
# Menu bar
#--
menubar = tk.Menu(root)
root.config(menu=menubar)

# Create File menu
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
# Create Edit menu
edit_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit_menu)
# Create Help menu
help_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help_menu)

# Add Exit command to File menu
file_menu.add_command(label="Exit", command=root.quit)

# Header section
header_frame = tk.Frame(root, relief="raised")
header_frame.pack(fill="x", pady=(0, 10))

tk.Label(header_frame, text="Header Area", font=("Arial", 14, "bold")).pack()


#---
# Top bar config
#---
top_nav_bar = tk.Frame(root, borderwidth=1)
top_nav_bar.pack(side="top", fill="x", padx=(0, 10))

# add weight to columns to make size them according to ratio
top_nav_bar.grid_columnconfigure(0, weight=1)
top_nav_bar.grid_columnconfigure(1, weight=1)
top_nav_bar.grid_columnconfigure(2, weight=2)

# tk.Label(top_nav_bar, text="Navigation").pack(pady=5)
tk.Button(top_nav_bar, text="View Preset", command=lambda: switch_frame(preset_frame)).grid(row=0, column=0, padx=5, pady=2, sticky="ew")
tk.Button(top_nav_bar, text="Create Preset", command=lambda: switch_frame(create_frame)).grid(row=0, column=1, padx=5, pady=2, sticky="ew")


#---
# Main Frame
# split into 2 views, top bar buttons change both the frame currently displaying
#---
# list preset frame
preset_frame = tk.Frame(root, borderwidth=1, bg="lightgreen")


# create preset frame
create_frame = tk.Frame(root, borderwidth=1, bg="lightblue")


# Hide all current frames, display selected frame
def switch_frame(frame):
    preset_frame.pack_forget()
    create_frame.pack_forget()
    # pack the current frame
    frame.pack(side="left", fill="both", expand=True)

# set and show initial frame:
switch_frame(preset_frame)

#
# start window
#
root.mainloop()