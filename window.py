import tkinter as tk

# create the main window frame
root = tk.Tk()
root.title("SpartaHackX")

# set default window size (width*height)
root.geometry(f"{800}x{600}")

# Create different sections using nested frames
# add content to individual frames to maintain structure

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
top_nav_bar.grid_columnconfigure(2, weight=1)

# tk.Label(top_nav_bar, text="Navigation").pack(pady=5)
tk.Button(top_nav_bar, text="Record").grid(row=0, column=0, padx=5, pady=2, sticky="ew")
tk.Button(top_nav_bar, text="Option 2").grid(row=0, column=1, padx=5, pady=2, sticky="ew")
tk.Button(top_nav_bar, text="Option 3").grid(row=0, column=2, padx=5, pady=2, sticky="ew")


#---
# Main content area
#---
main_frame = tk.Frame(root, borderwidth=1)
main_frame.pack(side="left", fill="both", expand=True)

# sample text
content_label = tk.Label(main_frame, text="Main Content Area", font="bold", pady=10)
content_label.pack()

#
# start window
#
root.mainloop()