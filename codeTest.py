import tkinter as tk
from utils import tkutils

def on_check(tag):
    print(f"{tag} checkbox was toggled")

def main():
    # Create the main application window
    root = tk.Tk()
    root.geometry("300x200")

    # Define some example tags
    tags = {"Tag1", "Tag2", "Tag3", "Tag4"}

    # Create a frame to hold the checkboxes
    frame = tk.Frame(root)
    frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    # Create checkboxes and get the check_vars dictionary
    check_vars = tkutils.createCheckBox(frame, tags, on_check)

    # Function to check the state of the checkboxes
    def print_checked_states():
        print("Checked states:")
        for tag, var in check_vars.items():
            print(f"{tag}: {'Checked' if var.get() == 1 else 'Unchecked'}")

    # Button to print the current state of all checkboxes
    btn_show_states = tk.Button(root, text="Show Checked States", command=print_checked_states)
    btn_show_states.pack(pady=10)

    # Run the main loop
    root.mainloop()

if __name__ == "__main__":
    main()