#CopyRights :

#Author: CASTILLO Mattheo 
#Contact :
#gmail : castillo.mattheo@gmail.com
#Special thanks to :

#- Creajeux video game school and all of its students for beta testing these tools.
#- Florian Delarque for helping about the code.

import maya.cmds as cmds

def creatWin(*arg) :
     if cmds.window("Anim" ,widthHeight=(100, 400), exists =True):
          cmds.deleteUI("Anim")
    
     cmds.window("Anim",widthHeight=(100, 400))
 
     cmds.columnLayout(adjustableColumn=True)
     cmds.button(l="Switch Anim IK/FK", c=anime)
      

     cmds.showWindow("Anim")


fk=["ctrl_fk_upperarme_l","ctrl_fk_lowerarme_l","ctrl_fk_hand_l"]
bones=["upperarme","lowerarme","hand"]


def anime(*agr) :
  key=cmds.keyframe( 'ctrl_ik_wrist_l', attribute='translateZ', query=True, keyframeCount=True )

  for nbr in range(key) :

   anim=cmds.keyframe("ctrl_ik_wrist_l_translateZ",index=(nbr,),query=True)
   
   for name in fk:
    cmds.setKeyframe(name,time=(anim))
    test=cmds.currentTime(anim[0])

    cmds.select('switch_arm_l')
    test = cmds.getAttr('.inputX')  
    if test == 0 :
      for name in bones :
        AXES = cmds.getAttr(name+'_ik_l' +'.rotate')[0]
        cmds.setAttr('ctrl_fk_'+name+'_l' +'.rotate',AXES[0],AXES[1],AXES[2])

print("test")