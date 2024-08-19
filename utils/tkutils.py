import tkinter as tk
import subprocess

# frames
def createFrame(location,type):
    if location and type:
        if type == "ribbon":
            return tk.Frame(master=location,relief=tk.GROOVE,borderwidth=5)
            
        elif type == "scriptList":
            return tk.Frame(master=location,relief=tk.GROOVE,borderwidth=5)
        
        elif type == "scriptItem":
            return tk.Frame(master=location,relief=tk.GROOVE,borderwidth=5)
        else:
            raise ValueError("No frames match your choice")
    else:
        raise ValueError(f"missing location or type. location = {location}  Type = {type}")
        

# labels
def createLabel(location,text):
    if text and location:
        return tk.Label(master=location, text=text, height = 2)
    else:
        raise ValueError(f"missing location or text. location = {location}  Type = {text}")
    
# buttons
def createButton(location, text, path=''):
    if location and text and path:
        if text == "Run":
            return tk.Button(master=location, text="Run", command=lambda *args:runScript(path))
        elif text == "Edit":
            return tk.Button(master=location, text="Edit", command=lambda *args:runScript(path))
    else:
        raise ValueError(f"missing location, text or path. location = {location}  Type = {text}  path = {path}")
   

def runScript(filePath):
    filePath = filePath.replace("/", "\\")
    subprocess.call(f'python "{filePath}" 1', shell=True)

def editMode():
    pass
    
def createCheckBox(location, tags, command):
    """
    Creates a set of checkboxes for a given set of tags and associates them with a command.

    This function dynamically generates checkboxes for each tag in the provided `tags` list or set.
    The checkboxes are placed in the specified `location` (a Tkinter frame or widget) and are aligned
    in a row. Each checkbox is linked to an `IntVar` to track its state (checked or unchecked).
    When a checkbox is toggled, the `command` function is called with the tag associated with that checkbox.

    Parameters:
    location (tk.Widget): The parent widget (typically a Tkinter frame) where the checkboxes will be placed.
    tags (set or list): A set or list of strings representing the tags for which checkboxes will be created.
    command (function): A callback function that is executed when a checkbox is toggled. The function should
                        accept a single argument, which will be the tag associated with the toggled checkbox.

    Returns:
    dict: A dictionary where the keys are the tags and the values are `IntVar` instances associated with each checkbox.
          These `IntVar` objects can be used to check the state of each checkbox (1 for checked, 0 for unchecked).

    Example:
    ```python
    def on_check(tag):
        print(f"{tag} was toggled")

    frame = tk.Frame(root)
    tags = {"Tag1", "Tag2", "Tag3"}
    check_vars = createCheckBox(frame, tags, on_check)
    ```
    """

    check_vars = {}
    count = 1
    tags = sorted(list(tags))

    for tag in tags:
        print(tag)
        var = tk.IntVar()
        check_vars[tag] = var
        tag_check = tk.Checkbutton(location, text=tag, variable=var, command=lambda tag=tag:command(tag))
        tag_check.grid(row=0,column=count)
        count += 1

    count = 1
    return check_vars
