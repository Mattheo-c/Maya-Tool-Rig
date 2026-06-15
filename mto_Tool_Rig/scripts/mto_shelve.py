#CopyRights :

#Author: CASTILLO Mattheo 
#Contact :
#gmail : castillo.mattheo@gmail.com
#Special thanks to :

#- Creajeux video game school and all of its students for beta testing these tools.
#- Florian Delarque for helping about the code.

import maya.cmds as cmds 
import mto_IK_FK as mto_IKFK
import mto_AutoRigbipede as mto_auto
import importlib

importlib.reload(mto_IKFK)


def _null(*args):
    pass

class shelf_base():
    def __init__(self, name="mto_Rigging", iconPath = ""):
        self.name = name

        self.iconPath = iconPath

        self.labelBackground = (0, 0, 0, 0)
        self.labelColour = (.9, .9, .9)

        self._cleanOldShelf()
        cmds.setParent(self.name)
        self.build()

    def build(self):
        pass

    def addButton(self, label, icon="commandButton.png", ann = _null, enable = _null, command=_null, doubleCommand=_null):
        
        cmds.setParent(self.name)
        if icon:
            icon = self.iconPath + icon
        cmds.shelfButton(width=37, height=37, image=icon, l=label, command=command, dcc=doubleCommand, imageOverlayLabel=label, olb=self.labelBackground, olc=self.labelColour)

    def addSeparator(self):
        cmds.separator(enable = True, w = 12, h = 35, manage = True, vis = True, po = True, highlightColor = (0.321, 0.521, 0.650), style = 'shelf', horizontal = False)

    def _cleanOldShelf(self):
        if cmds.shelfLayout(self.name, ex=1):
            if cmds.shelfLayout(self.name, q=1, ca=1):
                for each in cmds.shelfLayout(self.name, q=1, ca=1):
                    cmds.deleteUI(each)
        else:
            cmds.shelfLayout(self.name, p="ShelfLayout")

class customShelf(shelf_base):
    def buildUI(self):
        self.addButton(label = '', icon = 'reloadReference.png',enable = True,command = _null, ann = 'Reload Shelve')

        self.addSeparator()

        self.addButton(label = '', icon = 'swapBG.png',enable = True,command = mto_IKFK.creatWin, ann = 'Switch IK Fk Tool')

        self.addSeparator()

        self.addButton(label = '', icon = 'addSkinInfluence.png',enable = True,command = mto_auto.CreatWin, ann = 'Switch IK Fk Tool')



