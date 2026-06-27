import maya.cmds as cmds

def creatWin() :
     if cmds.window("Anim" ,widthHeight=(100, 400), exists =True):
          cmds.deleteUI("Anim")
    
     cmds.window("Anim",widthHeight=(100, 400))
 
     cmds.columnLayout(adjustableColumn=True)
     cmds.button(l="Switch Anim IK/FK", c = anime)
      

     cmds.showWindow("Anim")
creatWin()

fk=["CTRL_FK_WRIST_L","CTRL_FK_ELBOW_L","CTRL_FK_SHOULDER_L"]
bones=["SHOULDER","ELBOW","WRIST"]
bonesIk =["ELBOW","WRIST"]

def anime(*agr) :
  key=cmds.keyframe( 'CTRL_IK_WRIST_L', attribute='translateZ', query=True, keyframeCount=True )

  for nbr in range(key) :

   anim=cmds.keyframe("CTRL_IK_WRIST_L_translateZ",index=(nbr,),query=True)
   
   for name in fk:
    cmds.setKeyframe(name,time=(anim))
    test=cmds.currentTime(anim[0])

    cmds.select('IK_FK_SWITCH_REVERSE_L')
    test = cmds.getAttr('.inputX')  
    if test == 0 :
      for name in bones :
        AXES = cmds.getAttr("IK_"+name+'_L' +'.rotate')[0]
        cmds.setAttr('CTRL_FK_'+name+'_L' +'.rotate',AXES[0],AXES[1],AXES[2])
       
       
cmds.setAttr('SWITCH_IK_FK_L.SWITCH',1)