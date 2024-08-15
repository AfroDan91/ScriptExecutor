import tkinter as tk
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
        