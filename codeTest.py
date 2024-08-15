import subprocess

# Define the file path
filePath = "C:/Users/danie/Desktop/Python training/ScriptExecutor/utils/test.py"

def runScript(filePath):
    filePath = filePath.replace("/", "\\")
    subprocess.call(f'python "{filePath}" 1', shell=True)


subprocess.call(r'python "C:\\Users\\danie\\Desktop\\Python training\\ScriptExecutor\\utils\\testFiles\\test.py" 1', shell=True)
