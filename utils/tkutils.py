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
        return tk.Button(master=location, text="Run", command=lambda *args:runScript(path))
    else:
        raise ValueError(f"missing location, text or path. location = {location}  Type = {text}  path = {path}")
    

def runScript(filePath):
    filePath = filePath.replace("/", "\\")
    subprocess.call(f'python "{filePath}" 1', shell=True)




# radio buttons
# def createRadio(location, bool, type command=toggleBool):
#     if type == "alwaysOnTop":
#         return tk.Checkbutton(location, text="Always on top", variable=bool, 
#                              onvalue=1, offvalue=0, command=lambda *args:toggleBool(bool))
# def toggleBool(bool):
#     return not bool

def scriptRow(location, obj):
    new_frame = createFrame(location,"scriptItem")
    createLabel(new_frame, obj.script_name)
