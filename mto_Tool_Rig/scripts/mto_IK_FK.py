#CopyRights :

#Author: CASTILLO Mattheo 
#Contact :
#gmail : castillo.mattheo@gmail.com
#Special thanks to :

#- Creajeux video game school and all of its students for beta testing these tools.
#- Florian Delarque for helping about the code.
import maya.cmds as cmds 

def creatwin(*agr) :
     if cmds.window("Switch" ,widthHeight=(100, 400), exists =True):
          cmds.deleteUI("Switch")
    
     cmds.window("Switch",widthHeight=(100, 400))
 
     cmds.columnLayout(adjustableColumn=True)
     cmds.button(l="Switch IK/FK Arm L", c=ArmL)
     cmds.button(l="Switch IK/FK Arm R", c=ArmR) 

     cmds.showWindow("Switch")


bones=["SHOULDER","ELBOW","WRIST"]
bonesFk =["ELBOW","WRIST"]

def ArmL(*arg) :
    cmds.select('IK_FK_SWITCH_REVERSEHAND_L')
    test = cmds.getAttr('.inputX')

    if test == 0 :
        for name in bones :
         AXES = cmds.getAttr(name+'SHOULDER_IK_L' +'.rotate')[0]
         cmds.setAttr('CTRL_FK_'+name+'_L' +'.rotate',AXES[0],AXES[1],AXES[2])
         
    else:
         for names in bonesFk :
          AXE = cmds.xform(names+'_FK_L', ws=True ,t=True,q=True)
          cmds.xform('CTRL_IK_'+names+'_L' ,ws=True,t=AXE)
          

def ArmR(*arg) :
    cmds.select('IK_FK_SWITCH_REVERSEHAND_R')
    test = cmds.getAttr('.inputX')

    if test == 0 :
        for name in bones :
         AXES = cmds.getAttr(name+'_IK_R' +'.rotate')[0]
         cmds.setAttr('CTRL_FK_'+name+'_R' +'.rotate',AXES[0],AXES[1],AXES[2])
    
    else:
         for names in bonesFk :
          AXE = cmds.xform(names+'_FK_R', ws=True ,t=True,q=True)
          cmds.xform('CTRL_IK_'+names+'_R' ,ws=True,t=AXE)
         


