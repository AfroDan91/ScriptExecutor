import tkinter as tk
import json
from utils import tkutils, json_processor, transformers
 

# globals


# application setup 
window = tk.Tk()
alwaysOnTop = True
window.geometry("1200x300")
window.attributes('-topmost', alwaysOnTop)

##### Top row area #####
frm_Ribbon = tkutils.createFrame(window,"ribbon")
frm_Ribbon.grid(row=0,column=0)

lbl_size = tkutils.createLabel(frm_Ribbon,"Filter")
lbl_size.grid(row=0,column=0)

##### Script Area #####
frm_Script_List = tkutils.createFrame(window,"scriptList")
frm_Script_List.grid(row=1,column=0)


with open('utils\script_list.json') as scriptJson:
    data = json.load(scriptJson)
scriptList = []
count = 0
for script in data:
    scriptList.append(json_processor.ScripObj(script))
    frm_script_item = tkutils.createFrame(frm_Script_List,"scriptItem")
    frm_script_item.pack(side='top')
    lbl_script_name = tkutils.createLabel(frm_script_item,scriptList[-1].script_name)
    lbl_script_name.pack(side='left')
    lbl_script_desc = tkutils.createLabel(frm_script_item,scriptList[-1].description)
    lbl_script_desc.pack(side='left')
    btn_run = tkutils.createButton(frm_script_item,"Run",scriptList[-1].file_path)
    btn_run.pack(side='left')



window.mainloop()
