import tkinter as tk
import subprocess

class ScripObj:
    """
    Class to handle saved scripts
    """
    def __init__(self, json):
        self.id          = json['id']
        self.file_name   = json['fileName']
        self.script_name = json.get('name', self.file_name)
        self.file_path   = json['path']
        self.description = json.get('description', '')
        self.arguments   = json.get('arguments', [])
        self.tags        = json.get('tags').split(',')

    def nameLabel(self, location):
        return tk.Label(master=location, text=self.script_name, height = 2)
    
    def descLabel(self, location):
        return tk.Label(master=location, text=self.description, height = 2)
    
    def runButton(self, location):
        return tk.Button(master=location, text="Run", command=self.runScript)
    
    def runScript(self):
        self.file_path = self.file_path.replace("/", "\\")
        subprocess.call(f'python "{self.file_path}" 1', shell=True)