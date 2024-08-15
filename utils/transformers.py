from utils import json_processor
import json

def jsonToObj():
    with open('utils\script_list.json') as scriptJson:
        data = json.load(scriptJson)
    scriptList = []
    for script in data:
        scriptList.append(json_processor.ScripObj(script))

    return scriptList