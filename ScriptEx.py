import tkinter as tk
import json
from utils import tkutils, json_processor, transformers
 

# globals
scriptList = []    
allTags = set()
# selectedTags = []

# application setup 
window = tk.Tk()
alwaysOnTop = True
window.geometry("1200x300")
window.attributes('-topmost', alwaysOnTop)
window.grid_columnconfigure(0,weight=1)

# Opens json when scripts are saved
with open('utils\script_list.json') as scriptJson:
    data = json.load(scriptJson)

# Turns scripts into objects and lists them and creates a set of all unique tags
for script in data:
    scriptList.append(json_processor.ScripObj(script))
    allTags.update(scriptList[-1].tags)

##### Top row area #####
frm_Ribbon = tkutils.createFrame(window,"ribbon")
frm_Ribbon.grid(row=0,column=0,sticky="ew")

lbl_size = tkutils.createLabel(frm_Ribbon,"Filter by Tag")
lbl_size.grid(row=0,column=0)

def filterByTags(tag):
    """
    Filters and displays scripts based on selected tags.

    This function checks the `tagList` dictionary for tags whose associated
    `IntVar` value is `1` (indicating that the corresponding checkbox is checked).
    If any tags are selected, it calls `displaySelectedScripts` with the list of
    selected tags to filter the script list accordingly. If no tags are selected,
    it calls `displaySelectedScripts` with the full script list.

    Parameters:
    tag (str): The tag associated with the checkbox that triggered the function.
               Although passed in, it is not used in the function's current implementation.

    Returns:
    None

    Example:
    When a user toggles a checkbox, this function is triggered to update the displayed
    scripts based on the tags that are currently selected.
    """
    selectedTags = []
    filtered = False
    # iterate through key value pairs
    for tag, var in tagList.items():
        # if a value bool is 1 (the var.get() method is used as it is a tkVar)
        if var.get() == 1:
            filtered = True
            selectedTags.append(tag)
                                       
    if filtered == True:
        displaySelectedScripts(scriptList,selectedTags)
    else:
        displaySelectedScripts(scriptList)

# creates check boxes for each tag and returns their tkVars as tagList
tagList = tkutils.createCheckBox(frm_Ribbon,allTags,filterByTags)




##### Script Area #####
frm_Script_List = tkutils.createFrame(window,"scriptList")
frm_Script_List.grid(row=1,column=0,sticky="ew")




def displaySelectedScripts(scriptList, tags=allTags):
    '''
    sends the ui the correct scripts as dictated by tags

    Parameters:
    scriptList (list): A list of script objects to be filtered and displayed.
    tags (list, optional): A list of tags to filter the scripts. If empty, all scripts will be displayed. Defaults to an empty list.

    Returns:
    None

    Example:
    >>> scripts = [ScriptObject1, ScriptObject2, ScriptObject3]
    >>> tags = ['important', 'urgent']
    >>> displaySelectedScripts(scripts, tags)
    This will clear the current script display in the UI, filter the scripts by the given tags, 
    and display only those that match. If no tags are provided, all scripts will be displayed.
    '''
    refinedScriptList = []

    # clear out old scripts list
    for item in frm_Script_List.winfo_children():
        item.destroy()

    # refine list to be displayed by selected tags, if any
    if tags == []:
        refinedScriptList = scriptList
    else:
        for i in scriptList:
            if any(t in i.tags for t in tags):
                refinedScriptList.append(i)

    # display refined list  
    for i in refinedScriptList:
        frm_script_item = tkutils.createFrame(frm_Script_List,"scriptItem")
        frm_script_item.pack(side='top', expand=True, fill='both')

        lbl_script_name = i.nameLabel(frm_script_item)
        lbl_script_name.pack(side='left')

        lbl_script_desc = i.descLabel(frm_script_item)
        lbl_script_desc.pack(side='left')

        btn_run = i.runButton(frm_script_item)
        btn_run.pack(side='right',padx=5)

displaySelectedScripts(scriptList)



window.mainloop()
