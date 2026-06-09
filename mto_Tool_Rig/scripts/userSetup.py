import maya.cmds as cmds
import mto_makingmenu as menu   
import mto_shelve as shelf
import importlib

importlib.reload(menu)
importlib.reload(shelf)

def startupCommands():    
    menu.makingmenu()
    class_Inst = shelf.customShelf("mto_Rigging")
    class_Inst.buildUI()

cmds.evalDeferred("print('userSetup.py TEST.')")
cmds.evalDeferred('startupCommands()')