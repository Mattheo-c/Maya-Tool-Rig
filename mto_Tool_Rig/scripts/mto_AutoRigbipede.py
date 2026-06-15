# CopyRights :

#Author: CASTILLO Mattheo 
#Contact :
#gmail : castillo.mattheo@gmail.com
#Special thanks to :

#- Creajeux video game school and all of its students for beta testing these tools.
#- Florian Delarque for helping about the code.

import maya.cmds as cmds
import re
#__________________________________________________________
#List
locbiLL=['LEG_L','KNEE_L','ANKLE_L'] 
locbiMId=['PELVIS','HIP','ABS','CHEST_01','CHEST_02','NECK','HEAD'] 
locbiAL=['SHOULDER_L','ELBOW_L','WRIST_L']
loc1HL=['PINKY1_L','RING1_L','MID1_L','INDEX1_L','THUMB1_L','THUMB2_L','THUMB3_L']
loc2HL=['PINKY2_L','RING2_L','MID2_L','INDEX2_L']
loc3HL=['PINKY3_L','RING3_L','MID3_L','INDEX3_L']
locFL=['HEEL_L','TOE_L','END_L']
locY=['EYE_L','EYE_R']
locC=['CLAV_L','CLAV_R']
locRC=['INT_STS_L','EXT_STS_L']
Colone=['PELVIS','HIP','ABS','NECK']
locHL=['PINKY1_L','RING1_L','MID1_L','INDEX1_L','THUMB1_L','THUMB2_L','THUMB3_L','PINKY2_L','RING2_L','MID2_L','INDEX2_L','PINKY3_L','RING3_L','MID3_L','INDEX3_L']
liste1=["12","13","14","16","17","18"]
liste2=["5","6","7"]
liste3=["8","9","10"]
liste4=["4","11","15"]
#__________________________________________________________
#BOUTON#
#__________________________________________________________
#Bouton placement LOC
def Locbipede (*arg):
 downL= 70
 upM= 75
 OriL= 19
 down= 130
 OriHL= -1
 Ori2HL= -1
 Ori3HL= -1
 FrontFL= -10
 Eye= 4
 Clav= 10
 RC=10 
    #Leg
 for nameL in locbiLL :
     cmds.spaceLocator(n='LOC_'+nameL, p=(15,downL,0))
     downL= downL - 30
     cmds.CenterPivot()
     symtool('LOC_'+nameL)
    

   
   #colone Vertabrale 
 for nameC in locbiMId :
     cmds.spaceLocator(n='LOC_'+nameC, p=(0,upM,0))
     upM = upM + 12
     cmds.CenterPivot()
    
     
   #Arm
 for nameA in locbiAL :
     cmds.spaceLocator(n='LOC_'+nameA, p=(OriL,down,0))
     OriL = OriL + 5
     down= down -23
     cmds.CenterPivot()
     symtool('LOC_'+nameA)
     
  #Eye
 for nameC in locC :
     cmds.spaceLocator(n='LOC_'+nameC, p=(Clav,130,0))
     Clav = Clav -20 
     cmds.CenterPivot()
    
   #Hand01
 for nameH1 in loc1HL :
     cmds.spaceLocator(n='LOC_'+nameH1, p=(32,76,OriHL))
     OriHL = OriHL + 2
     cmds.CenterPivot()
     symtool('LOC_'+nameH1)
     
   #Hand02 
 for nameH2 in loc2HL :
     cmds.spaceLocator(n='LOC_'+nameH2, p=(34,72,Ori2HL))
     Ori2HL = Ori2HL + 2
     cmds.CenterPivot()
     symtool('LOC_'+nameH2)
     
   #Hand03 
 for nameH3 in loc3HL :
     cmds.spaceLocator(n='LOC_'+nameH3, p=(32,68,Ori3HL))
     Ori3HL = Ori3HL + 2
     cmds.CenterPivot()
     symtool('LOC_'+nameH3)
     
   #Foot Reverse
 for nameFR in locFL :
     cmds.spaceLocator(n='LOC_'+nameFR, p=(15,2,FrontFL))
     FrontFL = FrontFL + 11
     cmds.CenterPivot()
     symtool('LOC_'+nameFR)
     
   #Eye
 for nameM in locY :
     cmds.spaceLocator(n='LOC_'+nameM, p=(Eye,149,15))
     Eye = Eye - 8
     cmds.CenterPivot()
    
 cmds.spaceLocator(n='LOC_JAW', p=(0,144,10))
 cmds.CenterPivot()

 for nameSTS in locRC :
     cmds.spaceLocator(n='LOC_'+nameSTS, p=(RC,2,7))
     RC = RC + 10
     cmds.CenterPivot()
     symtool('LOC_'+nameSTS)
 cmds.select("LOC_LEG_L","LOC_REG_R","LOC_KNEE_L","LOC_KNEE_R",\
             "LOC_ANKLE_L","LOC_ANKLE_R","LOC_PELVIS","LOC_HIP",\
              "LOC_ABS","LOC_CHEST_01","LOC_CHEST_02","LOC_NECK",\
                "LOC_HEAD","LOC_SHOULDER_L","LOC_SHOULDER_R","LOC_ELBOW_L",\
                  "LOC_ELBOW_R","LOC_WRIST_L","LOC_WRIST_R","LOC_CLAV_L",\
                    "LOC_CLAV_R","LOC_PINKY1_L","LOC_PINKY1_R","LOC_RING1_L",\
                      "LOC_RING1_R","LOC_MID1_L","LOC_MID1_R","LOC_INDEX1_L",\
                        "LOC_INDEX1_R","LOC_THUMB1_L","LOC_THUMB1_R","LOC_THUMB2_L",\
                          "LOC_THUMB2_R","LOC_THUMB3_L","LOC_THUMB3_R","LOC_PINKY2_L",\
                            "LOC_PINKY2_R","LOC_RING2_L","LOC_RING2_R","LOC_MID2_L",\
                              "LOC_MID2_R","LOC_INDEX2_L","LOC_INDEX2_R","LOC_PINKY3_L",\
                                "LOC_PINKY3_R","LOC_RING3_L","LOC_RING3_R","LOC_MID3_L",\
                                  "LOC_MID3_R","LOC_INDEX3_L","LOC_INDEX3_R","LOC_HEEL_L",\
                                    "LOC_HEEL_R","LOC_TOE_L","LOC_TOE_R","LOC_END_L","LOC_END_R",\
                                      "LOC_EYE_L","LOC_EYE_R","LOC_JAW")
 cmds.sets(n='LOC')  
 cmds.select(d=True)
 cmds.OrientJointOptions(d=True) 
#__________________________________________________________
#Bouton placement Bone/CTRL et Contrainte
def Rigbipede(*arg) :
 cmds.SelectAll()
 cmds.FreezeTransformations()
 cmds.select(d=True)
 #creation des Joints avec Mirroir    
 Rig(locbiLL)
 mirror(locbiLL)                
 Rig(loc1HL)
 mirror(loc1HL)
 Rig(loc2HL)
 mirror(loc2HL)
 Rig(loc3HL)
 mirror(loc3HL)
 Rig(locbiAL)
 mirror(locbiAL)
 Rig(locbiMId)
 Rig(locC)
 Rig(locFL)
 mirror(locFL)
 Rig(locY)
 RigEYEBOT(locY)
 RigEYETOP(locY)
 position = cmds.getAttr('LOC_JAW' +'Shape.localPosition')[0]
 joint = cmds.joint(n='JAW',p=position)
 cmds.select(d=True)
 cmds.joint(n='ROOT',p=(0,0,0,))
 #Supprission des Locteurs
 cmds.select('LOC')
 cmds.Delete()
 #Parent Bones
 #LEG L
 cmds.parent('ANKLE_L','KNEE_L')
 cmds.parent('KNEE_L','LEG_L')
 cmds.parent('TOE_L','ANKLE_L')
 cmds.parent('END_L','TOE_L')
 cmds.parent('HEEL_L','END_L')
 #LEG R
 cmds.parent('ANKLE_R','KNEE_R')
 cmds.parent('KNEE_R','LEG_R')
 cmds.parent('TOE_R','ANKLE_R')
 cmds.parent('END_R','TOE_R')
 cmds.parent('HEEL_R','END_R')
 #HAND L
 cmds.parent('PINKY3_L','PINKY2_L')
 cmds.parent('PINKY2_L','PINKY1_L')
 cmds.parent('RING3_L','RING2_L')
 cmds.parent('RING2_L','RING1_L')
 cmds.parent('MID3_L','MID2_L')
 cmds.parent('MID2_L','MID1_L')
 cmds.parent('INDEX3_L','INDEX2_L')
 cmds.parent('INDEX2_L','INDEX1_L')
 cmds.parent('THUMB3_L','THUMB2_L')
 cmds.parent('THUMB2_L','THUMB1_L')
 #Orient Hand
 #Pinly
 cmds.select('PINKY3_L') 
 cmds.duplicate()
 cmds.parent('PINKY3_L1','PINKY3_L')   
 cmds.select('PINKY1_L','PINKY2_L','PINKY3_L')
 cmds.OrientJoint(oj='X,Y,Z',sao='x,u,p',aso=True,ch=True,zso=True)
 cmds.select('PINKY3_L1')
 cmds.delete()
 #Ring
 cmds.select('RING3_L') 
 cmds.duplicate()
 cmds.parent('RING3_L1','RING3_L')   
 cmds.select('RING1_L','RING2_L','RING3_L')
 cmds.OrientJoint(oj='X,Y,Z',sao='x,u,p',aso=True,ch=True,zso=True)
 cmds.select('RING3_L1')
 cmds.delete()
 #Mid
 cmds.select('MID3_L') 
 cmds.duplicate()
 cmds.parent('MID3_L1','MID3_L')   
 cmds.select('MID1_L','MID2_L','MID3_L')
 cmds.OrientJoint(oj='X,Y,Z',sao='x,u,p',aso=True,ch=True,zso=True)
 cmds.select('MID3_L1')
 cmds.delete()
 #Index
 cmds.select('INDEX3_L') 
 cmds.duplicate()
 cmds.parent('INDEX3_L1','INDEX3_L')   
 cmds.select('INDEX1_L','INDEX2_L','INDEX3_L')
 cmds.OrientJoint(oj='X,Y,Z',sao='x,u,p',aso=True,ch=True,zso=True)
 cmds.select('INDEX3_L1')
 cmds.delete()
 #Thumb
 cmds.select('THUMB3_L') 
 cmds.duplicate()
 cmds.parent('THUMB3_L1','THUMB3_L')   
 cmds.select('THUMB1_L','THUMB2_L','THUMB3_L')
 cmds.OrientJoint(oj='X,Y,Z',sao='x,u,p',aso=True,ch=True,zso=True)
 cmds.select('THUMB3_L1')
 cmds.delete()
 #HAND R
 cmds.parent('PINKY3_R','PINKY2_R')
 cmds.parent('PINKY2_R','PINKY1_R')
 cmds.parent('RING3_R','RING2_R')
 cmds.parent('RING2_R','RING1_R')
 cmds.parent('MID3_R','MID2_R')
 cmds.parent('MID2_R','MID1_R')
 cmds.parent('INDEX3_R','INDEX2_R')
 cmds.parent('INDEX2_R','INDEX1_R')
 cmds.parent('THUMB3_R','THUMB2_R')
 cmds.parent('THUMB2_R','THUMB1_R') 
 #Orient Hand
 #Pinly
 cmds.select('PINKY3_R') 
 cmds.duplicate()
 cmds.parent('PINKY3_R1','PINKY3_R')   
 cmds.select('PINKY1_R','PINKY2_R','PINKY3_R')
 cmds.OrientJoint(oj='X,Y,Z',sao='x,u,p',aso=True,ch=True,zso=True)
 cmds.select('PINKY3_R1')
 cmds.delete()
 #Ring
 cmds.select('RING3_R') 
 cmds.duplicate()
 cmds.parent('RING3_R1','RING3_R')   
 cmds.select('RING1_R','RING2_R','RING3_R')
 cmds.OrientJoint(oj='X,Y,Z',sao='x,u,p',aso=True,ch=True,zso=True)
 cmds.select('RING3_R1')
 cmds.delete()
 #Mid
 cmds.select('MID3_R') 
 cmds.duplicate()
 cmds.parent('MID3_R1','MID3_R')   
 cmds.select('MID1_R','MID2_R','MID3_R')
 cmds.OrientJoint(oj='X,Y,Z',sao='x,u,p',aso=True,ch=True,zso=True)
 cmds.select('MID3_R1')
 cmds.delete()
 #Index
 cmds.select('INDEX3_R') 
 cmds.duplicate()
 cmds.parent('INDEX3_R1','INDEX3_R')   
 cmds.select('INDEX1_R','INDEX2_R','INDEX3_R')
 cmds.OrientJoint(oj='X,Y,Z',sao='x,u,p',aso=True,ch=True,zso=True)
 cmds.select('INDEX3_R1')
 cmds.delete()
 #Thumb
 cmds.select('THUMB3_R') 
 cmds.duplicate()
 cmds.parent('THUMB3_R1','THUMB3_R')   
 cmds.select('THUMB1_R','THUMB2_R','THUMB3_R')
 cmds.OrientJoint(oj='X,Y,Z',sao='x,u,p',aso=True,ch=True,zso=True)
 cmds.select('THUMB3_R1')
 cmds.delete()
 #ARM L
 cmds.parent('SHOULDER_L','CLAV_L')
 cmds.parent('ELBOW_L','SHOULDER_L')
 cmds.parent('WRIST_L','ELBOW_L')
 cmds.select('WRIST_L') 
 cmds.duplicate()
 cmds.parent('WRIST_L1','WRIST_L')   
 cmds.select('SHOULDER_L','ELBOW_L','WRIST_L')
 cmds.OrientJoint(oj='X,Y,Z',sao='x,u,p',aso=True,ch=True,zso=True)
 cmds.select('WRIST_L1')
 cmds.delete() 
 cmds.parent('PINKY1_L','WRIST_L')
 cmds.parent('RING1_L','WRIST_L')
 cmds.parent('MID1_L','WRIST_L')
 cmds.parent('INDEX1_L','WRIST_L')
 cmds.parent('THUMB1_L','WRIST_L') 
 #ARM R
 cmds.parent('SHOULDER_R','CLAV_R')
 cmds.parent('ELBOW_R','SHOULDER_R')
 cmds.parent('WRIST_R','ELBOW_R')
 cmds.select('WRIST_R') 
 cmds.duplicate()
 cmds.select('WRIST_R1','WRIST_R')   
 cmds.select('SHOULDER_R','ELBOW_R','WRIST_R')
 cmds.OrientJoint(oj='X,Y,Z',sao='x,u,p',aso=True,ch=True,zso=True,)
 cmds.select('WRIST_R1')
 cmds.delete()
 cmds.parent('PINKY1_R','WRIST_R')
 cmds.parent('RING1_R','WRIST_R')
 cmds.parent('MID1_R','WRIST_R')
 cmds.parent('INDEX1_R','WRIST_R')
 cmds.parent('THUMB1_R','WRIST_R') 
 #HEAD
 cmds.parent('EYE_L','HEAD')
 cmds.parent('EYE_R','HEAD')
 cmds.parent('BOT_EYE_L','HEAD')
 cmds.parent('BOT_EYE_R','HEAD')
 cmds.parent('TOP_EYE_L','HEAD')
 cmds.parent('TOP_EYE_R','HEAD')
 cmds.parent('JAW','HEAD')
 cmds.parent('HEAD','NECK')
 #COLONE
 cmds.parent('NECK','CHEST_02')
 cmds.parent('CHEST_02','CHEST_01')
 cmds.parent('CHEST_01','ABS')
 cmds.parent('ABS','HIP')
 cmds.parent('HIP','PELVIS')
 cmds.parent('LEG_L','HIP')
 cmds.parent('LEG_R','HIP')
 cmds.parent('CLAV_L','CHEST_02')
 cmds.parent('CLAV_R','CHEST_02')
 cmds.parent('PELVIS','ROOT')
 cmds.select(d=True) 
#__________________________________________________________
#placement CTRL
  #Controleur
 #ankle
 CTRL = cmds.circle(n="CTRL_ANKLE_L",nr=(0,1,0),r=5)
 cmds.parentConstraint("ANKLE_L",CTRL,w=1)
 cmds.select("CTRL_ANKLE_L_parentConstraint1")
 cmds.delete()
 cmds.select(CTRL)
 cmds.FreezeTransformations()
 cmds.select('CTRL_ANKLE_L.cv[0:7]')
 cmds.setAttr('makeNurbCircle1'+'.center',0 ,-10,0)
 cmds.select('CTRL_ANKLE_L.cv[0:7]')
 cmds.scale(1, 1, 3)
 cmds.select('CTRL_ANKLE_L.cv[4]','CTRL_ANKLE_L.cv[6]')
 cmds.move(16.5, z=True)
 cmds.SnapToPointRelease()
 cmds.select('CTRL_ANKLE_L.cv[4:6]')
 cmds.scale(1.5,1,1)
 cmds.select('CTRL_ANKLE_L.cv[2]','CTRL_ANKLE_L.cv[0]')
 cmds.move(-16.5, z=True)
 cmds.SnapToPointRelease()
 cmds.select('CTRL_ANKLE_L.cv[7]','CTRL_ANKLE_L.cv[3]')
 cmds.move(7.5, z=True)
 cmds.select('CTRL_ANKLE_L.cv[0:7]')
 cmds.scale(1.5,1,1)
 cmds.select(CTRL)
 cmds.addAttr(at = 'enum', keyable=True, en = '_____', longName='Foot_Reverse')
 cmds.addAttr( keyable=True,  longName='SIDE_TO_SIDE',defaultValue=0, minValue=-10, maxValue=10)
 cmds.addAttr( keyable=True,  longName='HEEL_ROLL')
 cmds.addAttr( keyable=True,  longName='TIPE_HEEL')
 cmds.addAttr( keyable=True,  longName='TIPE_TOE')
 cmds.addAttr( keyable=True,  longName='TOE_ROLL')
 cmds.addAttr( keyable=True,  longName='WIPE_ROLL')
 cmds.setAttr('CTRL_ANKLE_L.Foot_Reverse',lock=True)
 cmds.select(CTRL)
 cmds.duplicate()
 cmds.rename('CTRL_ANKLE_R')
 cmds.parentConstraint("ANKLE_R","CTRL_ANKLE_R")
 cmds.select("CTRL_ANKLE_R_parentConstraint1")
 cmds.delete()
 cmds.select('CTRL_ANKLE_R')
 cmds.FreezeTransformations()
 cmds.select(CTRL)
 cmds.DeleteHistory()
 #Knee
 piramide =cmds.curve(n='Pyra',d=1, p=[(-1,0,-1),(1,0,-1),(1,0,1),(-1,0,1),(-1,0,-1),(0,1,0),(1,0,-1),(0,1,0),(1,0,1),(0,1,0),(-1,0,1)])
 cmds.select(piramide)
 cmds.scale(3,5,3)
 cmds.parentConstraint("KNEE_L","Pyra")
 cmds.rotate(-90,x=True)
 cmds.move(30,z=True)
 pyra=cmds.rename('CTRL_KNEE_L')
 cmds.select("Pyra_parentConstraint1")
 cmds.delete()
 cmds.select(pyra)
 cmds.FreezeTransformations()
 cmds.DeleteHistory()
 cmds.select(pyra)
 cmds.duplicate()
 cmds.rename('CTRL_KNEE_R')
 cmds.select(d=True)
 cmds.Group()
 cmds.rename('grp')
 cmds.parent('CTRL_KNEE_R','grp')
 cmds.setAttr('grp.scaleX',-1)
 cmds.Unparent()
 cmds.FreezeTransformations()
 cmds.select('grp')
 cmds.delete()
 #Colone
 for name in Colone :    
  cmds.circle(n="CTRL_"+name,nr=(0,1,0),r=20)
 cmds.select('CTRL_PELVIS.cv[0:7]')
 cmds.scale(1.2,1.2,1.2)
 cmds.parentConstraint('HIP',"CTRL_HIP")
 cmds.parentConstraint('PELVIS',"CTRL_PELVIS")
 cmds.parentConstraint('ABS',"CTRL_ABS")
 cmds.parentConstraint('NECK',"CTRL_NECK")
 hip=cmds.xform("HIP", ws=True ,t=True,q=True)
 cmds.xform('CTRL_HIP.scalePivot' ,ws=True,t=hip,absolute=True)
 cmds.xform('CTRL_HIP.rotatePivot' ,ws=True,t=hip,absolute=True)
 cmds.select('CTRL_NECK.cv[0:7]')
 cmds.scale(0.5,0.5,0.5)
 for name in Colone:
    cmds.select('CTRL_'+name+'_parentConstraint1')
    cmds.delete()
    cmds.select('CTRL_'+name)
    cmds.FreezeTransformations()
    cmds.DeleteHistory()
 cross=cmds.curve(n='CTRL_CHEST',d=1, 
 p=[(1,0.5,-1),(1,0,-1),(3,0,-1),(3,0.5,-1),(3,0,-1)\
    ,(3,0,1),(3,0.5,1),(3,0,1),(1,0,1),(1,0.5,1),(1,0,1)\
    ,(1,0,3),(1,0.5,3),(1,0,3),(-1,0,3),(-1,0.5,3),(-1,0,3)\
    ,(-1,0,1),(-1,0.5,1),(-1,0,1),(-3,0,1),(-3,0.5,1),(-3,0,1)\
    ,(-3,0,-1),(-3,0.5,-1),(-3,0,-1),(-1,0,-1),(-1,0.5,-1),(-1,0,-1)\
    ,(-1,0,-3),(-1,0.5,-3),(-1,0,-3),(1,0,-3),(1,0.5,-3),(1,0,-3),(1,0,-1)\
    ,(1,0.5,-1),(3,0.5,-1),(3,0.5,1),(1,0.5,1),(1,0.5,3),(-1,0.5,3),(-1,0.5,1)\
    ,(-3,0.5,1),(-3,0.5,-1),(-1,0.5,-1),(-1,0.5,-3),(1,0.5,-3),(1,0.5,-1)])    
 cmds.select(cross)
 cmds.scale(5,5,5)
 cmds.parentConstraint('CHEST_02',cross)
 cmds.setAttr(cross +".rx",90)
 cmds.select('curveShape2.cv[0]','curveShape2.cv[3]', 'curveShape2.cv[6]' ,'curveShape2.cv[9]', 'curveShape2.cv[12]' ,'curveShape2.cv[15]', 'curveShape2.cv[18]', 'curveShape2.cv[21]', 'curveShape2.cv[24]', 'curveShape2.cv[27]', 'curveShape2.cv[30]', 'curveShape2.cv[33]', 'curveShape2.cv[36:48]')
 cmds.move(-16,z=True)
 cmds.select('curveShape2.cv[1:2]', 'curveShape2.cv[4:5]' ,'curveShape2.cv[7:8]', 'curveShape2.cv[10:11]' ,'curveShape2.cv[13:14]' ,'curveShape2.cv[16:17]' ,'curveShape2.cv[19:20]' ,'curveShape2.cv[22:23]' ,'curveShape2.cv[25:26]' ,'curveShape2.cv[28:29]' ,'curveShape2.cv[31:32]' ,'curveShape2.cv[34:35]')
 cmds.move(-19,z=True)
 cmds.select(cross+'_parentConstraint1')
 cmds.delete()
 cmds.select(cross)
 cmds.FreezeTransformations()
 cmds.select(d=True)
 #head
 cube=cmds.curve(n='Cube',d=1\
 , p=[(-1,0,-1),(1,0,-1),(1,0,1),(-1,0,1)\
 ,(-1,0,-1),(-1,2,-1),(1,2,-1),(1,0,-1)\
 ,(1,2,-1),(1,2,1),(1,0,1),(1,2,1)\
 ,(-1,2,1),(-1,0,1),(-1,2,1),(-1,2,-1)])
 cmds.select(cube)
 cmds.scale(10,10,10)
 cmds.CenterPivot()
 cmds.parentConstraint('HEAD','Cube' , w=1)
 cmds.select(cube+'_parentConstraint1')
 cmds.delete()
 cmds.select(cube)
 cmds.FreezeTransformations()
 cmds.rename('CTRL_HEAD')
 #EYE
 for name in locY:
  CTRL = cmds.circle(n="CTRL_"+name,nr=(0,0,0),r=2)
 #CTRL EYE 
 cmds.parentConstraint('EYE_L','CTRL_EYE_L')
 cmds.parentConstraint('EYE_R','CTRL_EYE_R')
 for name in locY:
  eye=cmds.select("CTRL_"+name+"_parentConstraint1")
  cmds.delete()
  cmds.select("CTRL_"+name) 
  cmds.move(50,z=True)
  cmds.FreezeTransformations()
 cmds.select("CTRL_EYE_L","CTRL_EYE_R")
 cmds.cluster()
 #CTRL GENREAL 
 cmds.circle(n="CTRL_GENERAL_EYE",nr=(0,0,0),r=10.)
 cmds.scale(1,0.5,1)
 cmds.select('CTRL_GENERAL_EYE.cv[5]')
 cmds.move(3,y=True)
 cmds.select('CTRL_GENERAL_EYE.cv[6]','CTRL_GENERAL_EYE.cv[4]')
 cmds.move(-8,y=True)
 cmds.select('CTRL_GENERAL_EYE.cv[2]','CTRL_GENERAL_EYE.cv[0]')
 cmds.move(6,y=True)
 cmds.select("CTRL_GENERAL_EYE")
 cmds.parentConstraint("cluster1Handle","CTRL_GENERAL_EYE")
 view=cmds.xform("EYE_L", ws=True ,t=True,q=True)
 cmds.xform("CTRL_GENERAL_EYE", ws=True ,t=view[1],q=True)
 cmds.select("CTRL_GENERAL_EYE_parentConstraint1",'cluster1Handle')
 cmds.delete()
 cmds.select("CTRL_GENERAL_EYE")
 cmds.FreezeTransformations()
 cmds.DeleteHistory()
 cmds.addAttr(at = 'enum', keyable=True, en = '_____', longName='EYE')
 cmds.addAttr( keyable=True,  longName='OPEN_CLOSE',defaultValue=0, minValue=0, maxValue=1)
 cmds.addAttr( keyable=True,  longName='OPEN_CLOSE_L',defaultValue=0, minValue=0, maxValue=1)
 cmds.addAttr( keyable=True,  longName='OPEN_CLOSE_R',defaultValue=0, minValue=0, maxValue=1)
 #POINT DE PIVOT CTRL EYE    
 cmds.select("CTRL_GENERAL_EYE")
 cmds.CenterPivot()
 cmds.cluster()
 cmds.parentConstraint('cluster1Handle','CTRL_EYE_L')
 cmds.parentConstraint('cluster1Handle','CTRL_EYE_R')
 cmds.select("CTRL_EYE_LShape.cv[0:7]")
 cmds.setAttr('makeNurbCircle1'+'.center',5,2.5,0)
 cmds.select("CTRL_EYE_RShape.cv[0:7]")
 cmds.setAttr('makeNurbCircle2'+'.center',-5,2.5,0)
 cmds.select("cluster1Handle")
 cmds.delete() 
 for name in locY:
  cmds.select("CTRL_"+name) 
  cmds.DeleteHistory()
  cmds.select(d=True)
 #ROOT
 def makeArrow():
  myArrow = cmds.curve(d=1, p=[(1,0,-1),(3,0,-1),(3,0,-2),(5,0,0),(3,0,2),(3,0,1),(1,0,1)])
  return(myArrow)
 firstArrow=makeArrow()
 secondeArrow = makeArrow()
 threeArrow = makeArrow()
 fourArrow = makeArrow()
 cmds.setAttr(secondeArrow +".ry",90)
 cmds.setAttr(threeArrow +".ry",180)
 cmds.setAttr(fourArrow +".ry",-90)
 cmds.attachCurve(firstArrow,secondeArrow,threeArrow,fourArrow, rpo=False, n='Axe' )
 cmds.delete(firstArrow,secondeArrow,threeArrow,fourArrow)         
 cmds.rename("CTRL_ROOT")
 cmds.scale(20,20,20,)
 #General
 cmds.polyGear(sides=8,heightDivisions=2)
 cmds.select('pGear1')
 cmds.SelectEdgeMask()
 cmds.select("pGear1.e[57]","pGear1.e[59]","pGear1.e[61]","pGear1.e[63]","pGear1.e[65]","pGear1.e[67]","pGear1.e[70]","pGear1.e[72]","pGear1.e[74]","pGear1.e[76]","pGear1.e[78]","pGear1.e[80]","pGear1.e[83]","pGear1.e[85]","pGear1.e[87]","pGear1.e[89]","pGear1.e[91]","pGear1.e[93]","pGear1.e[96]","pGear1.e[98]","pGear1.e[100]","pGear1.e[102]","pGear1.e[104]","pGear1.e[106]","pGear1.e[109]","pGear1.e[111]","pGear1.e[113]","pGear1.e[115]","pGear1.e[117]","pGear1.e[119]","pGear1.e[122]","pGear1.e[124]","pGear1.e[126]","pGear1.e[128]","pGear1.e[130]","pGear1.e[132]","pGear1.e[135]","pGear1.e[137]","pGear1.e[139]","pGear1.e[141]","pGear1.e[143]","pGear1.e[145]","pGear1.e[148]","pGear1.e[150]","pGear1.e[152]","pGear1.e[154]","pGear1.e[156]","pGear1.e[158]")
 cmds.CreateCurveFromPoly()
 cmds.select('pGear1')
 cmds.delete()
 cmds.select("polyToCurve1")
 cmds.rename("CTRL_GENERAL")
 cmds.scale(8,8,8)
 cmds.rotate(90)
 cmds.move(180,y=True)
 cmds.select("CTRL_ROOT","CTRL_GENERAL")
 cmds.FreezeTransformations()
 cmds.select(d=True)
 #ARM L
 for name in locbiAL:
  cmds.circle(n="CTRL_FK_"+name,nr=(0,0,0),r=8)
 cmds.circle(n="CTRL_IK_WRIST_L",nr=(0,0,0),r=10) 
 cmds.parentConstraint("SHOULDER_L","CTRL_FK_SHOULDER_L")
 cmds.parentConstraint("ELBOW_L","CTRL_FK_ELBOW_L")
 cmds.parentConstraint("WRIST_L","CTRL_FK_WRIST_L")
 cmds.parentConstraint("WRIST_L","CTRL_IK_WRIST_L")
 cmds.select("CTRL_FK_WRIST_LShape.cv[0:7]")
 cmds.rotate(90,y=True)
 cmds.select("CTRL_FK_ELBOW_LShape.cv[0:7]")
 cmds.rotate(90,y=True)
 cmds.select("CTRL_FK_SHOULDER_LShape.cv[0:7]")
 cmds.rotate(45,y=True)
 cmds.select("CTRL_IK_WRIST_LShape.cv[0:7]")
 cmds.rotate(90,y=True)
 cmds.select('CTRL_FK_SHOULDER_L_parentConstraint1',"CTRL_FK_ELBOW_L_parentConstraint1","CTRL_FK_WRIST_L_parentConstraint1","CTRL_IK_WRIST_L_parentConstraint1")
 cmds.delete()
 cmds.select("CTRL_FK_SHOULDER_L","CTRL_FK_ELBOW_L","CTRL_FK_WRIST_L","CTRL_IK_WRIST_L")
 cmds.DeleteHistory()
 slecte=cmds.select("CTRL_FK_SHOULDER_L","CTRL_IK_WRIST_L",)
 selection(slecte)
 cmds.parent("CTRL_FK_ELBOW_L","CTRL_FK_SHOULDER_L")
 cmds.parent("CTRL_FK_WRIST_L","CTRL_FK_ELBOW_L")
 cmds.select("CTRL_FK_ELBOW_L","CTRL_FK_WRIST_L")
 cmds.FreezeTransformations()
 cmds.select(d=True)
 #Arm R
 cmds.group(em=True,name='Sym')
 cmds.select("CTRL_FK_SHOULDER_L") 
 cmds.duplicate()
 cmds.parent("CTRL_FK_SHOULDER_L1","Sym")
 cmds.select("Sym")
 cmds.scale(-1,1,1)
 sym=cmds.select("CTRL_FK_SHOULDER_L1")
 cmds.Unparent("CTRL_FK_SHOULDER_L1")
 selection(sym)
 cmds.select("Sym")
 cmds.delete()
 cmds.select("CTRL_FK_SHOULDER_L1")
 cmds.rename("CTRL_FK_SHOULDER_R")
 cmds.select("CTRL_FK_SHOULDER_R|CTRL_FK_ELBOW_L")
 cmds.rename("CTRL_FK_ELBOW_R")
 cmds.select("CTRL_FK_SHOULDER_R|CTRL_FK_ELBOW_R|CTRL_FK_WRIST_L")
 cmds.rename("CTRL_FK_WRIST_R")
 cmds.select(d=True)
 cmds.circle(n="CTRL_IK_WRIST_R",nr=(0,0,0),r=10) 
 cmds.parentConstraint("WRIST_R","CTRL_IK_WRIST_R")
 cmds.select("CTRL_IK_WRIST_RShape.cv[0:7]")
 cmds.rotate(90,y=True)
 cmds.select("CTRL_IK_WRIST_R_parentConstraint1")
 cmds.delete()
 cmds.select("CTRL_IK_WRIST_R")
 cmds.DeleteHistory()
 selection("CTRL_IK_WRIST_R")
 cmds.select(d=True)
 #Hand L
 for name in locHL:
  cmds.curve(n="CTRL_"+name ,d=2, p=[(0,0,0),(2,0,0),(2,0,1),(4,0,1),(4,0,-1),(2,0,-1),(2,0,0),(0,0,0)])
  cmds.select("CTRL_"+name)
  cmds.scale(0.75,0.75,0.75)
 cmds.parentConstraint("PINKY1_L","CTRL_PINKY1_L")
 cmds.parentConstraint("PINKY2_L","CTRL_PINKY2_L")
 cmds.parentConstraint("PINKY3_L","CTRL_PINKY3_L")
 cmds.parentConstraint("RING1_L","CTRL_RING1_L")
 cmds.parentConstraint("RING2_L","CTRL_RING2_L")
 cmds.parentConstraint("RING3_L","CTRL_RING3_L")
 cmds.parentConstraint("MID1_L","CTRL_MID1_L")
 cmds.parentConstraint("MID2_L","CTRL_MID2_L")
 cmds.parentConstraint("MID3_L","CTRL_MID3_L")
 cmds.parentConstraint("INDEX1_L","CTRL_INDEX1_L")
 cmds.parentConstraint("INDEX2_L","CTRL_INDEX2_L")
 cmds.parentConstraint("INDEX3_L","CTRL_INDEX3_L")
 cmds.parentConstraint("THUMB1_L","CTRL_THUMB1_L")
 cmds.parentConstraint("THUMB2_L","CTRL_THUMB2_L")
 cmds.parentConstraint("THUMB3_L","CTRL_THUMB3_L")
 for nbr in liste1:
  cmds.select("curveShape"+nbr+".cv[0:7]")
  cmds.rotate(90,x=True)
  cmds.rotate(90,y=True)
 for nbr in liste2:
  cmds.select("curveShape"+nbr+".cv[0:7]")
  cmds.rotate(90,x=True)
  cmds.rotate(90,y=True)
 for nbr in liste3:
  cmds.select("curveShape"+nbr+".cv[0:7]")
  cmds.rotate(90,z=True)
  cmds.rotate(90,x=True)
 for nbr in liste4:
  cmds.select("curveShape"+nbr+".cv[0:7]")
  cmds.rotate(90,z=True)
  cmds.rotate(90,x=True)
 for name in locHL:
  cmds.select("CTRL_"+name+"_parentConstraint1")
  cmds.delete()
  cmds.select("CTRL_"+name)
  cmds.DeleteHistory()
 hand=cmds.select("CTRL_PINKY1_L","CTRL_RING1_L","CTRL_MID1_L","CTRL_INDEX1_L","CTRL_THUMB1_L")
 selection(hand)
 cmds.parent("CTRL_PINKY2_L","CTRL_PINKY1_L")
 cmds.parent("CTRL_PINKY3_L","CTRL_PINKY2_L")
 cmds.select("CTRL_PINKY2_L","CTRL_PINKY3_L")
 cmds.FreezeTransformations()
 cmds.parent("CTRL_RING2_L","CTRL_RING1_L")
 cmds.parent("CTRL_RING3_L","CTRL_RING2_L")
 cmds.select("CTRL_RING2_L","CTRL_RING3_L")
 cmds.FreezeTransformations()
 cmds.select(d=True)
 cmds.parent("CTRL_MID2_L","CTRL_MID1_L")
 cmds.parent("CTRL_MID3_L","CTRL_MID2_L")
 cmds.select("CTRL_MID2_L","CTRL_MID3_L")
 cmds.FreezeTransformations()
 cmds.select(d=True)
 cmds.parent("CTRL_INDEX2_L","CTRL_INDEX1_L") 
 cmds.parent("CTRL_INDEX3_L","CTRL_INDEX2_L")
 cmds.select("CTRL_INDEX2_L","CTRL_INDEX3_L")
 cmds.FreezeTransformations()
 cmds.select(d=True)
 cmds.parent("CTRL_THUMB2_L","CTRL_THUMB1_L")
 cmds.parent("CTRL_THUMB3_L","CTRL_THUMB2_L")
 cmds.select("CTRL_THUMB2_L","CTRL_THUMB3_L")
 cmds.FreezeTransformations()
 cmds.select(d=True)
 #Hand R
 cmds.group(em=True,n="Sym")
 cmds.select("CTRL_PINKY1_L","CTRL_RING1_L","CTRL_MID1_L","CTRL_INDEX1_L","CTRL_THUMB1_L")
 cmds.duplicate()
 cmds.parent("CTRL_PINKY1_L1",'Sym')
 cmds.parent("CTRL_RING1_L1",'Sym')
 cmds.parent("CTRL_MID1_L1",'Sym')
 cmds.parent("CTRL_INDEX1_L1",'Sym')
 cmds.parent("CTRL_THUMB1_L1",'Sym')
 cmds.select("Sym")
 cmds.scale(-1,x=True)
 cmds.select("CTRL_PINKY1_L1","CTRL_RING1_L1","CTRL_MID1_L1","CTRL_INDEX1_L1","CTRL_THUMB1_L1")
 cmds.Unparent()
 sym=cmds.select("CTRL_PINKY1_L1","CTRL_RING1_L1","CTRL_MID1_L1","CTRL_INDEX1_L1","CTRL_THUMB1_L1")
 selection(sym)
 cmds.select("Sym")
 cmds.delete()
 #rename
 cmds.select("CTRL_PINKY1_L1")
 cmds.rename("CTRL_PINKY1_R")
 cmds.select("CTRL_PINKY1_R|CTRL_PINKY2_L")
 cmds.rename("CTRL_PINKY2_R")
 cmds.select("CTRL_PINKY1_R|CTRL_PINKY2_R|CTRL_PINKY3_L")
 cmds.rename("CTRL_PINKY3_R")
 cmds.select("CTRL_RING1_L1")
 cmds.rename("CTRL_RING1_R")
 cmds.select("CTRL_RING1_R|CTRL_RING2_L")
 cmds.rename("CTRL_RING2_R")
 cmds.select("CTRL_RING1_R|CTRL_RING2_R|CTRL_RING3_L")
 cmds.rename("CTRL_RING3_R")
 cmds.select("CTRL_MID1_L1")
 cmds.rename("CTRL_MID1_R")
 cmds.select("CTRL_MID1_R|CTRL_MID2_L")
 cmds.rename("CTRL_MID2_R")
 cmds.select("CTRL_MID1_R|CTRL_MID2_R|CTRL_MID3_L")
 cmds.rename("CTRL_MID3_R")
 cmds.select("CTRL_INDEX1_L1")
 cmds.rename("CTRL_INDEX1_R")
 cmds.select("CTRL_INDEX1_R|CTRL_INDEX2_L")
 cmds.rename("CTRL_INDEX2_R")
 cmds.select("CTRL_INDEX1_R|CTRL_INDEX2_R|CTRL_INDEX3_L")
 cmds.rename("CTRL_INDEX3_R")
 cmds.select("CTRL_THUMB1_L1")
 cmds.rename("CTRL_THUMB1_R")
 cmds.select("CTRL_THUMB1_R|CTRL_THUMB2_L")
 cmds.rename("CTRL_THUMB2_R")
 cmds.select("CTRL_THUMB1_R|CTRL_THUMB2_R|CTRL_THUMB3_L")
 cmds.rename("CTRL_THUMB3_R")
 cmds.select(d=True)
 #Elbow 
 def sphere ():
  fristcircle = makeSphere()
  secondecircle = makeSphere2()
  threecircle = makeSphere3()
  cmds.select(fristcircle,secondecircle,threecircle)
  cmds.AttachBrushToCurves()
  cmds.select('stroke1','stroke2','stroke3')
  cmds.PaintEffectsToCurve()
  cmds.select('curve1','curve2','curve3')
  cmds.Unparent()
  cmds.delete(fristcircle,secondecircle,threecircle,'strokeShape1Curves','strokeShape2Curves','strokeShape3Curves')
  cmds.select('curveShape2','curveShape3','curve1')
  grp =cmds.createNode('transform', n='CTRL_IK_ELBOW_L')
  curve =cmds.select('curve1','curve2','curve3',grp)
  cmds.pickWalk(d='down')
  cmds.parent(  add=True, s=True )
  cmds.DeleteHistory('curveShape1','curveShape2','curveShape3')
  cmds.FreezeTransformations('curveShape1','curveShape2','curveShape3')
  cmds.delete('curve1','curve2','curve3')
  cmds.delete('stroke1','stroke2','stroke3')
 def makeSphere():
  mySphere = cmds.circle(nr=(0,-1,0),r=4,)
  return(mySphere)
 def makeSphere2():
  mySphere = cmds.circle(nr=(0,0,1),r=4,)
  return(mySphere)
 def makeSphere3():
  mySphere = cmds.circle(nr=(1,0,0),r=4,)
  return(mySphere)
 sphere()
 #placement du CTRL L
 cmds.select("CTRL_IK_ELBOW_L")
 cmds.parentConstraint("ELBOW_L","CTRL_IK_ELBOW_L")
 cmds.select("CTRL_IK_ELBOW_L_parentConstraint1")
 cmds.delete()
 elbow=cmds.select("CTRL_IK_ELBOW_L")
 cmds.FreezeTransformations()
 selection(elbow)
 cmds.move(-30,z=True)
 bones=cmds.xform("ELBOW_L", ws=True ,t=True,q=True)
 cmds.xform('CTRL_IK_ELBOW_L.scalePivot' ,ws=True,t=bones,absolute=True)
 cmds.xform('CTRL_IK_ELBOW_L.rotatePivot' ,ws=True,t=bones,absolute=True)
 selection(elbow)
 #Elbow R
 symCTRL("IK_ELBOW")
 #clav L 
 cmds.circle(n="CTRL_CLAV_L",nr=(0,0,0),r=5)
 cmds.scale(1,0.4,1)
 cmds.select("CTRL_CLAV_L.cv[3]","CTRL_CLAV_L.cv[7]")
 cmds.softSelect(sse=1)
 cmds.move(-3,z=True)
 cmds.select("CTRL_CLAV_L.cv[1]")
 cmds.move(1,y=True)
 cmds.select("CTRL_CLAV_L.cv[5]")
 cmds.move(-3,y=True)
 cmds.select("CTRL_CLAV_LShape.cv[0:7]")
 cmds.rotate(20,z=True)
 cmds.select("CTRL_CLAV_L")
 cmds.CenterPivot()
 clav=cmds.xform("CLAV_L", ws=True ,t=True,q=True)
 cmds.xform('CTRL_CLAV_L' ,ws=True,t=clav,absolute=True)
 cmds.move(10,z=True)
 cmds.xform('CTRL_CLAV_L.scalePivot' ,ws=True,t=clav,absolute=True)
 cmds.xform('CTRL_CLAV_L.rotatePivot' ,ws=True,t=clav,absolute=True)
 cmds.DeleteHistory()
 cmds.FreezeTransformations()
 selection(cmds.select("CTRL_CLAV_L"))
 #Clav R
 symCTRL("CLAV")
 #Jaw
 cmds.circle(n="CTRL_JAW",nr=(0,0,0),r=5)
 cmds.scale(1,0.4,1)
 cmds.select("CTRL_JAW.cv[3]","CTRL_JAW.cv[7]")
 cmds.softSelect(sse=1)
 cmds.move(-4,z=True)
 cmds.select("CTRL_JAW")
 cmds.CenterPivot()
 Jaw=cmds.xform("JAW", ws=True ,t=True,q=True)
 cmds.xform('CTRL_JAW' ,ws=True,t=Jaw,absolute=True)
 cmds.move(20,z=True)
 cmds.rotate(35,x=True)
 jaw=cmds.xform("JAW", ws=True ,t=True,q=True)
 cmds.xform("CTRL_JAW", ws=True ,t=jaw[1],q=True)
 cmds.xform('CTRL_JAW.scalePivot' ,ws=True,t=Jaw,absolute=True)
 cmds.xform('CTRL_JAW.rotatePivot' ,ws=True,t=Jaw,absolute=True)
 cmds.DeleteHistory()
 cmds.FreezeTransformations()
 selection(cmds.select("CTRL_JAW"))
 #General Hand L        
 def Gear():
  cmds.polyGear(sides=8,heightDivisions=2)
  cmds.select('pGear1')
  cmds.SelectEdgeMask()
  cmds.select("pGear1.e[57]","pGear1.e[59]","pGear1.e[61]","pGear1.e[63]","pGear1.e[65]","pGear1.e[67]","pGear1.e[70]","pGear1.e[72]","pGear1.e[74]","pGear1.e[76]","pGear1.e[78]","pGear1.e[80]","pGear1.e[83]","pGear1.e[85]","pGear1.e[87]","pGear1.e[89]","pGear1.e[91]","pGear1.e[93]","pGear1.e[96]","pGear1.e[98]","pGear1.e[100]","pGear1.e[102]","pGear1.e[104]","pGear1.e[106]","pGear1.e[109]","pGear1.e[111]","pGear1.e[113]","pGear1.e[115]","pGear1.e[117]","pGear1.e[119]","pGear1.e[122]","pGear1.e[124]","pGear1.e[126]","pGear1.e[128]","pGear1.e[130]","pGear1.e[132]","pGear1.e[135]","pGear1.e[137]","pGear1.e[139]","pGear1.e[141]","pGear1.e[143]","pGear1.e[145]","pGear1.e[148]","pGear1.e[150]","pGear1.e[152]","pGear1.e[154]","pGear1.e[156]","pGear1.e[158]")
  cmds.CreateCurveFromPoly()
  cmds.select('pGear1')
  cmds.delete()
  cmds.select("polyToCurve1")
  cmds.rename("Gear")
 Gear()
 cmds.select('Gear')
 cmds.scale(5,5,5)
 cmds.FreezeTransformations()
 cmds.DeleteHistory()
 cmds.parentConstraint("WRIST_L","Gear")
 cmds.select("Gear_parentConstraint1")
 cmds.delete()
 gear=cmds.select("Gear")
 cmds.CenterPivot()
 cmds.FreezeTransformations()
 cmds.move(10,x=True)
 selection(gear)
 Wrist=cmds.xform("WRIST_L", ws=True ,t=True,q=True)
 cmds.xform('Gear.scalePivot' ,ws=True,t=Wrist,absolute=True)
 cmds.xform('Gear.rotatePivot' ,ws=True,t=Wrist,absolute=True)
 cmds.rename("CTRL_GENERAL_HAND_L")
 cmds.addAttr(at = 'enum', keyable=True, en = '_____', longName='Switch')
 cmds.addAttr( keyable=True,  longName='IK_Fk',defaultValue=0, minValue=0, maxValue=1)
 cmds.addAttr(at = 'enum', keyable=True, en = '_____', longName='Stretch')
 cmds.addAttr( keyable=True,  longName='ON_OFF',defaultValue=0, minValue=0, maxValue=1)
 #hand R
 symCTRL('GENERAL_HAND')
 test=cmds.xform('CTRL_GENERAL_HAND_R' ,ws=True,worldSpace=True)
 #Hand L
 #Parrentage CTRL
 cmds.parent("CTRL_EYE_L","CTRL_HEAD")
 cmds.parent("CTRL_EYE_R","CTRL_HEAD")
 eye= cmds.select("CTRL_EYE_L","CTRL_EYE_R")
 selection(eye)
 cmds.parent("CTRL_JAW","CTRL_HEAD")
 cmds.parent("CTRL_GENERAL_EYE","CTRL_HEAD")
 cmds.parent("CTRL_EYE_L","CTRL_GENERAL_EYE")
 cmds.parent("CTRL_EYE_R","CTRL_GENERAL_EYE")
 cmds.parent("CTRL_HEAD","CTRL_NECK")
 cmds.parent("CTRL_ANKLE_L","CTRL_ROOT")
 cmds.parent("CTRL_ANKLE_R","CTRL_ROOT")
 cmds.parent("CTRL_KNEE_L","CTRL_ROOT")
 cmds.parent("CTRL_KNEE_R","CTRL_ROOT")
 cmds.parent("CTRL_GENERAL","CTRL_ROOT")
 cmds.parent("CTRL_ABS","CTRL_PELVIS")
 cmds.parent("CTRL_CHEST","CTRL_ABS")
 cmds.parent("CTRL_NECK","CTRL_CHEST")
 cmds.parent("CTRL_HIP","CTRL_PELVIS")
 cmds.parent("CTRL_CLAV_L","CTRL_CHEST")
 cmds.parent("CTRL_CLAV_R","CTRL_CHEST")
 cmds.parent("CTRL_FK_SHOULDER_L","CTRL_CLAV_L")
 cmds.parent("CTRL_FK_SHOULDER_R","CTRL_CLAV_R")
 cmds.parent("CTRL_PELVIS","CTRL_ROOT")
 cmds.parent("CTRL_IK_WRIST_R","CTRL_ROOT")
 cmds.parent("CTRL_IK_WRIST_L","CTRL_ROOT")
 cmds.parent("CTRL_IK_ELBOW_R","CTRL_ROOT")
 cmds.parent("CTRL_IK_ELBOW_L","CTRL_ROOT")
 cmds.parent("CTRL_PINKY1_L","CTRL_ROOT")
 cmds.parent("CTRL_RING1_L","CTRL_ROOT")
 cmds.parent("CTRL_MID1_L","CTRL_ROOT")
 cmds.parent("CTRL_INDEX1_L","CTRL_ROOT")
 cmds.parent("CTRL_THUMB1_L","CTRL_ROOT")
 cmds.parent("CTRL_GENERAL_HAND_L","CTRL_ROOT")
 cmds.parent("CTRL_PINKY1_R","CTRL_ROOT")
 cmds.parent("CTRL_RING1_R","CTRL_ROOT")
 cmds.parent("CTRL_MID1_R","CTRL_ROOT")
 cmds.parent("CTRL_INDEX1_R","CTRL_ROOT")
 cmds.parent("CTRL_THUMB1_R","CTRL_ROOT")
 cmds.parent("CTRL_GENERAL_HAND_R","CTRL_ROOT")
#__________________________________________________________
#Contrainte et fonction 
 #HIP
 cmds.parentConstraint("CTRL_HIP","HIP",mo=True)
 cmds.parentConstraint("CTRL_PELVIS","PELVIS",mo=True)
 #HEAD
 cmds.orientConstraint("CTRL_JAW","JAW",mo=True)
 cmds.orientConstraint("CTRL_HEAD","HEAD",mo=True)
 cmds.aimConstraint("CTRL_EYE_L","EYE_L")
 cmds.aimConstraint("CTRL_EYE_R","EYE_R")
 cmds.parentConstraint("CTRL_NECK","NECK",mo=True)
 #CLAV
 cmds.parentConstraint("CTRL_CLAV_L","CLAV_L",mo=True)
 cmds.parentConstraint("CTRL_CLAV_R","CLAV_R",mo=True)
 #ANKLE
 cmds.orientConstraint("CTRL_ANKLE_L","ANKLE_L",mo=True)
 cmds.orientConstraint("CTRL_ANKLE_R","ANKLE_R",mo=True)
 #HAND R AND L
 #PINKY
 cmds.orientConstraint("CTRL_PINKY1_L","PINKY1_L",mo=True)
 cmds.orientConstraint("CTRL_PINKY2_L","PINKY2_L",mo=True)
 cmds.orientConstraint("CTRL_PINKY3_L","PINKY3_L",mo=True)
 cmds.orientConstraint("CTRL_PINKY1_R","PINKY1_R",mo=True)
 cmds.orientConstraint("CTRL_PINKY2_R","PINKY2_R",mo=True)
 cmds.orientConstraint("CTRL_PINKY3_R","PINKY3_R",mo=True)
 #RING
 cmds.orientConstraint("CTRL_RING1_L","RING1_L",mo=True)
 cmds.orientConstraint("CTRL_RING2_L","RING2_L",mo=True)
 cmds.orientConstraint("CTRL_RING3_L","RING3_L",mo=True)
 cmds.orientConstraint("CTRL_RING1_R","RING1_R",mo=True)
 cmds.orientConstraint("CTRL_RING2_R","RING2_R",mo=True)
 cmds.orientConstraint("CTRL_RING3_R","RING3_R",mo=True)
 #MID
 cmds.orientConstraint("CTRL_MID1_L","MID1_L",mo=True)
 cmds.orientConstraint("CTRL_MID2_L","MID2_L",mo=True)
 cmds.orientConstraint("CTRL_MID3_L","MID3_L",mo=True)
 cmds.orientConstraint("CTRL_MID1_R","MID1_R",mo=True)
 cmds.orientConstraint("CTRL_MID2_R","MID2_R",mo=True)
 cmds.orientConstraint("CTRL_MID3_R","MID3_R",mo=True)
 #INDEX
 cmds.orientConstraint("CTRL_INDEX1_L","INDEX1_L",mo=True)
 cmds.orientConstraint("CTRL_INDEX2_L","INDEX2_L",mo=True)
 cmds.orientConstraint("CTRL_INDEX3_L","INDEX3_L",mo=True)
 cmds.orientConstraint("CTRL_INDEX1_R","INDEX1_R",mo=True)
 cmds.orientConstraint("CTRL_INDEX2_R","INDEX2_R",mo=True)
 cmds.orientConstraint("CTRL_INDEX3_R","INDEX3_R",mo=True)
 #THUMB
 cmds.orientConstraint("CTRL_THUMB1_L","THUMB1_L",mo=True)
 cmds.orientConstraint("CTRL_THUMB2_L","THUMB2_L",mo=True)
 cmds.orientConstraint("CTRL_THUMB3_L","THUMB3_L",mo=True)
 cmds.orientConstraint("CTRL_THUMB1_R","THUMB1_R",mo=True)
 cmds.orientConstraint("CTRL_THUMB2_R","THUMB2_R",mo=True)
 cmds.orientConstraint("CTRL_THUMB3_R","THUMB3_R",mo=True)
 #MECA ARM L
 #FK
 cmds.select("SHOULDER_L")
 cmds.duplicate()
 cmds.select("SHOULDER_L1|ELBOW_L|WRIST_L|PINKY1_L",\
 "SHOULDER_L1|ELBOW_L|WRIST_L|THUMB1_L","SHOULDER_L1|ELBOW_L|WRIST_L|INDEX1_L",\
 "SHOULDER_L1|ELBOW_L|WRIST_L|MID1_L","SHOULDER_L1|ELBOW_L|WRIST_L|RING1_L")
 cmds.delete()
 cmds.select("SHOULDER_L1")
 cmds.Unparent()
 cmds.duplicate()
 cmds.select("SHOULDER_L1")
 cmds.rename("SHOULDER_FK_L")
 cmds.setAttr("SHOULDER_FK_L.radius",2)
 cmds.select("SHOULDER_FK_L|ELBOW_L")
 cmds.rename("ELBOW_FK_L")
 cmds.setAttr("ELBOW_FK_L.radius",2)
 cmds.select("SHOULDER_FK_L|ELBOW_FK_L|WRIST_L")
 cmds.rename("WRIST_FK_L")
 cmds.setAttr("WRIST_FK_L.radius",2)
 cmds.mirrorJoint("SHOULDER_FK_L",searchReplace=('_L', '_R'))
 cmds.OrientJoint(oj='X,Y,Z',sao='x,u,p',aso=True,ch=True,zso=True)
 #IK
 cmds.select("SHOULDER_L2")
 cmds.rename("SHOULDER_IK_L")
 cmds.setAttr("SHOULDER_IK_L.radius",3)
 cmds.select("SHOULDER_IK_L|ELBOW_L")
 cmds.rename("ELBOW_IK_L")
 cmds.setAttr("ELBOW_IK_L.radius",3)
 cmds.select("SHOULDER_IK_L|ELBOW_IK_L|WRIST_L")
 cmds.rename("WRIST_IK_L")
 cmds.setAttr("WRIST_IK_L.radius",3)
 cmds.mirrorJoint("SHOULDER_IK_L",searchReplace=('_L', '_R'))
 cmds.OrientJoint(oj='X,Y,Z',sao='x,u,p',aso=True,ch=True,zso=True)
 #GROUP
 cmds.group(em=True,n='SHADOW')
 cmds.group(em=True,n='GRP_MECA_ARM_L')
 cmds.parent("SHOULDER_FK_L","GRP_MECA_ARM_L")
 cmds.parent("SHOULDER_IK_L","GRP_MECA_ARM_L")
 cmds.parent("GRP_MECA_ARM_L","SHADOW")
 cmds.group(em=True,n='GRP_MECA_ARM_R')
 cmds.parent("SHOULDER_FK_R","GRP_MECA_ARM_R")
 cmds.parent("SHOULDER_IK_R","GRP_MECA_ARM_R")
 cmds.parent("GRP_MECA_ARM_R","SHADOW")
 #ConstraintFk+IK L
 fk("SHOULDER","ELBOW","WRIST","_L")
 ik_Stretech('SHOULDER_IK','ELBOW_IK',"WRIST_IK","IK_ELBOW","IK_WRIST","_L","ARM")
 #ConstraintFk+IK L
 fk("SHOULDER","ELBOW","WRIST","_R")
 ik_Stretech('SHOULDER_IK','ELBOW_IK',"WRIST_IK","IK_ELBOW","IK_WRIST","_R","ARM")
 cmds.select(d=True)
 cmds.parent("CTRL_IK_WRIST_L","CTRL_ROOT")
 cmds.parent("CTRL_IK_ELBOW_L","CTRL_ROOT")
 cmds.parent("CTRL_IK_WRIST_R","CTRL_ROOT")
 cmds.parent("CTRL_IK_ELBOW_R","CTRL_ROOT")
 cmds.parent("GRP_ARM_IK_L","GRP_MECA_ARM_L")
 cmds.parent("GRP_ARM_IK_R","GRP_MECA_ARM_R")
 #IK Spine
 cmds.select("HIP","LEG_L","LEG_R","NECK","CLAV_L","CLAV_R")
 cmds.Unparent()
 spine=cmds.xform("HIP", ws=True,t=True ,q=True)
 spine1=cmds.xform("ABS", ws=True,t=True ,q=True)
 spine2=cmds.xform("CHEST_01", ws=True,t=True ,q=True)
 spine3=cmds.xform("CHEST_02", ws=True,t=True ,q=True)
 cmds.curve(n="Spine_IK" ,d=2, p=[(spine),(spine1),(spine2),(spine3)])
 cmds.ikHandle( n='IK_SPINE', sj='HIP', ee='CHEST_02',sol="ikSplineSolver",c="Spine_IK",ccv=False)
 cmds.select("Spine_IK.cv[2:3]")
 cmds.cluster()
 cmds.select("cluster1Handle")
 cmds.rename("CLUSTER_TOP")
 cmds.select("Spine_IK.cv[0:1]")
 cmds.cluster()
 cmds.select("cluster1Handle")
 cmds.rename("CLUSTER_BOT")
 cmds.setAttr("CLUSTER_BOTShape.originZ",-20)
 cmds.setAttr("CLUSTER_TOPShape.originZ",-20)
 cmds.parent("CLUSTER_BOT","CTRL_HIP")
 cmds.parent("CLUSTER_TOP","CTRL_CHEST")
 cmds.connectAttr("CTRL_HIP.rotateY","IK_SPINE.roll")
 cmds.connectAttr("CTRL_CHEST.rotateY","IK_SPINE.twist")
 cmds.parent('LEG_L','HIP')
 cmds.parent('LEG_R','HIP')
 cmds.parent('HIP','PELVIS')
 cmds.parent('CLAV_L','CHEST_02')
 cmds.parent('CLAV_R','CHEST_02')
 cmds.parent('NECK','CHEST_02')
 cmds.parent("IK_SPINE","SHADOW")
 cmds.parent("Spine_IK","SHADOW")
 cmds.select(d=True)
 #IK Leg  
 ik("LEG","KNEE","ANKLE","_L") 
 ik("LEG","KNEE","ANKLE","_R")
 #Bridge Hand
 bridgeHand("_L")
 bridgeHand("_R")
 finger=cmds.select("CTRL_PINKY1_L","CTRL_RING1_L","CTRL_MID1_L","CTRL_INDEX1_L","CTRL_THUMB1_L","CTRL_PINKY1_R","CTRL_RING1_R","CTRL_MID1_R","CTRL_INDEX1_R","CTRL_THUMB1_R")
 selection(finger)
 cmds.select(d=True)
 #GRP Meca Arm
 bridge("SHOULDER",'CLAV',"ARM","_L")
 bridge("SHOULDER",'CLAV',"ARM","_R")
 #Aim IK
 AimELBOW("_L")
 AimELBOW("_R")
 AimKnee("_L")
 AimKnee("_R")
 #switch IK Fk arm CTRL GENREAL HAND
 switch("SHOULDER","ELBOW","WRIST","HAND","_L")
 switch("SHOULDER","ELBOW","WRIST","HAND","_R")
 #Creation RC chaine
 Side_to_Side_L("_L")
 Side_to_Side_R("_R")
 #Group and Layer
 cmds.select("AIM_CTRL_ELBOW_L","AIM_CTRL_ELBOW_R","AIM_CTRL_KNEE_R","AIM_CTRL_KNEE_L")
 cmds.group(n="AIM")
 cmds.select("CLUSTER_ELBOW_L_BONES","CLUSTER_ELBOW_R_BONES","CLUSTER_KNEE_L_BONES","CLUSTER_KNEE_R_BONES","CLUSTER_KNEE_L_CTRL","CLUSTER_KNEE_R_CTRL","CLUSTER_TOP","CLUSTER_BOT","CLUSTER_ELBOW_L_CTRL","CLUSTER_ELBOW_R_CTRL")
 cmds.createDisplayLayer(n="CLUSTER",)
 cmds.select(d=True)
#__________________________________________________________
#Reaload

  
#__________________________________________________________
## Windows##
def CreatWin(*arg) :
 if cmds.window("AutoRig" ,widthHeight=(100, 400), exists =True):
    cmds.deleteUI("AutoRig")
    
 cmds.window("AutoRig",widthHeight=(100, 400))
 
 cmds.columnLayout(adjustableColumn=True)
 cmds.button(l="Locator", c=Locbipede)
 cmds.button(l="Rig ", c=Rigbipede)
 
 cmds.showWindow("AutoRig")

#__________________________________________________________
#Fontion repete
#__________________________________________________________
def selection(null):
  null= cmds.ls(selection=True)
  selected_objects = null
  if len(selected_objects) !=0:
        for obj in selected_objects:

         translate = cmds.getAttr(obj + ".translate")[0]
         rotate = cmds.getAttr(obj + ".rotate")[0]
         scale = cmds.getAttr(obj + ".scale")[0]


         transform_matrix = cmds.xform(obj, query=True, matrix=True, worldSpace=True)

         cmds.setAttr(obj + ".offsetParentMatrix", transform_matrix, type="matrix")

         cmds.setAttr(obj + ".translate", 0, 0, 0)
         cmds.setAttr(obj + ".rotate", 0, 0, 0)
         cmds.setAttr(obj + ".scale", 1, 1, 1)
#_____________________________
def AimELBOW(ori):
  CTRL=cmds.xform('CTRL_IK_ELBOW'+ori+'|curveShape19.cv[0]', query=True, t=True, worldSpace=True)
  BONE=cmds.xform('ELBOW'+ori, query=True, t=True, worldSpace=True)
  cmds.curve(d=1,p=[(BONE),(CTRL)])
  cmds.rename("AIM_CTRL_ELBOW"+ori)
  cmds.select("AIM_CTRL_ELBOW"+ori+".cv[1]")
  cmds.cluster()
  cmds.rename("cluster1Handle","CLUSTER_ELBOW"+ori+"_CTRL")
  cmds.select("AIM_CTRL_ELBOW"+ori+".cv[0]")
  cmds.cluster()
  cmds.rename("cluster1Handle","CLUSTER_ELBOW"+ori+"_BONES")
  cmds.parent("CLUSTER_ELBOW"+ori+"_CTRL","CTRL_IK_ELBOW"+ori)
  cmds.parent("CLUSTER_ELBOW"+ori+"_BONES","ELBOW"+ori)
#_____________________________
def AimKnee(ori):
  CTRL=cmds.xform('CTRL_KNEE'+ori+'.cv[5]', query=True, t=True, worldSpace=True)
  BONE=cmds.xform('KNEE'+ori, query=True, t=True, worldSpace=True)
  cmds.curve(d=1,p=[(BONE),(CTRL)])
  cmds.rename("AIM_CTRL_KNEE"+ori)
  cmds.select("AIM_CTRL_KNEE"+ori+".cv[1]")
  cmds.cluster()
  cmds.rename("cluster1Handle","CLUSTER_KNEE"+ori+"_CTRL")
  cmds.select("AIM_CTRL_KNEE"+ori+".cv[0]")
  cmds.cluster()
  cmds.rename("cluster1Handle","CLUSTER_KNEE"+ori+"_BONES")
  cmds.parent("CLUSTER_KNEE"+ori+"_CTRL","CTRL_KNEE"+ori)
  cmds.parent("CLUSTER_KNEE"+ori+"_BONES","KNEE"+ori)
  cmds.select(d=True)
#_____________________________
def symCTRL(null):
 cmds.group(em=True,n="Sym")
 cmds.select("CTRL_"+null+"_L")
 cmds.duplicate()
 cmds.parent("CTRL_"+null+"_L1","Sym")
 cmds.select("Sym")
 cmds.scale(-1,x=True)
 symm=cmds.select("CTRL_"+null+"_L1")
 cmds.Unparent()
 cmds.FreezeTransformations()
 selection(symm)
 cmds.rename("CTRL_"+null+"_R")
 cmds.select("Sym")
 cmds.delete()
#_____________________________
def symtool(listOfName):
     sym= re.sub(r'_L', '_R', listOfName)
     cmds.spaceLocator(n=sym)
     cmds.parentConstraint(listOfName,sym,maintainOffset=False)
     position=cmds.getAttr(listOfName+'Shape.localPositionX')
     cmds.setAttr(sym+'.translateX',-position)
     cmds.select(sym+'_parentConstraint1')
     cmds.delete()
     cmds.select(sym)
     cmds.FreezeTransformations()
#_____________________________
def fk(null1,null2,null3,orientation):
 cmds.orientConstraint("CTRL_FK_"+null1+orientation,null1+"_FK"+orientation,mo=True)
 cmds.orientConstraint("CTRL_FK_"+null2+orientation,null2+"_FK"+orientation,mo=True)
 cmds.orientConstraint("CTRL_FK_"+null3+orientation,null3+"_FK"+orientation,mo=True)
#_____________________________
def ik(null1,null2,null3,orientation):
 cmds.ikHandle( n="IK_"+null3+orientation, sj=null1+orientation, ee=null3+orientation )
 cmds.pointConstraint("CTRL_"+null3+orientation,"IK_"+null3+orientation)
 cmds.orientConstraint("CTRL_"+null3+orientation,null3+orientation)
 cmds.poleVectorConstraint("CTRL_"+null2+orientation,"IK_"+null3+orientation,tl=True)
 cmds.parent("IK_"+null3+orientation,"SHADOW")
 cmds.select(d=True)
#_____________________________
def ik_Stretech(null1,null5,null3,null2,null4,orientation,zone):
 ##Creation IK and contrainte
 cmds.ikHandle( n=null4+orientation, sj=null1+orientation, ee=null3+orientation )
 cmds.pointConstraint("CTRL_"+null4+orientation,null4+orientation)
 cmds.orientConstraint("CTRL_"+null4+orientation,null3+orientation)
 cmds.poleVectorConstraint("CTRL_"+null2+orientation,null4+orientation,tl=True)
 cmds.select(d=True)
 ##Distance et mise ne place des loc
 dis=["LOC_DISTANCE_BOT"+orientation,"LOC_DISTANCE_TOP"+orientation]
 for loc in dis:
  cmds.spaceLocator(n=loc , p=(0,0,0))
 distancebot=cmds.xform(null3+orientation, query=True, t=True, worldSpace=True)
 distancetop=cmds.xform(null1+orientation, query=True, t=True, worldSpace=True)
 cmds.xform(dis[0],ws=True,t=distancebot,absolute=True)
 cmds.xform(dis[1],ws=True,t=distancetop,absolute=True)
 locbot=cmds.xform(dis[0], query=True, t=True, worldSpace=True)
 loctop=cmds.xform(dis[1], query=True, t=True, worldSpace=True)
 cmds.distanceDimension(sp=locbot,ep=loctop) 
 ##Rename##
 cmds.select( "distanceDimension1" )
 cmds.rename("DM_ARM"+orientation,)
 ##Contrainte et Rangement##
 name=["CTRL_"+null4+orientation,null1+orientation,"CTRL_"+null2+orientation,"LOC_DISTANCE_TOP"+orientation,"GRP_"+zone+"_IK"+orientation]
 cmds.pointConstraint(null1+orientation,"LOC_DISTANCE_TOP"+orientation, mo=True)
 cmds.parent("LOC_DISTANCE_BOT"+orientation,"CTRL_"+null4+orientation)
 grp=cmds.group(em =True, name="GRP_ARM_IK"+orientation)
 cmds.parent(name, nc=True)
 #Creation Node and Rename#
 cmds.createNode('multiplyDivide')
 cmds.createNode('condition')
 cmds.createNode('condition')
 cmds.createNode('multiplyDivide')
 cmds.createNode('clamp')
 cmds.select('multiplyDivide1')
 cmds.rename('ScaleCompensateMD_'+zone+orientation)
 cmds.select('multiplyDivide2')
 cmds.rename('StretchDivideMD_'+zone+orientation)
 cmds.select('condition1')
 cmds.rename('Stretch_Condition_'+zone+orientation)
 cmds.select('condition2')
 cmds.rename('Stretch_ON_OFF_'+zone+orientation)
 cmds.select('clamp1')
 cmds.rename('Value_max_Stretch_CLAMP'+orientation)
 #Connection#
 cmds.connectAttr('StretchDivideMD_'+zone+orientation+'.outputX','Stretch_Condition_'+zone+ orientation+'.colorIfTrueR')
 cmds.connectAttr('StretchDivideMD_'+zone+orientation+'.outputX','Stretch_Condition_'+zone+orientation+'.firstTerm')
 cmds.connectAttr('ScaleCompensateMD_'+zone+orientation+'.outputX','StretchDivideMD_'+zone+orientation+'.input2X')
 cmds.connectAttr('DM_'+zone+orientation+'Shape.distance','StretchDivideMD_'+zone+orientation+'.input1X')
 cmds.connectAttr('GRP_'+zone+'_IK'+orientation+'.scaleX','ScaleCompensateMD_'+zone+orientation+'.input2X')
 cmds.connectAttr('Stretch_Condition_'+zone+orientation+'.outColorR','Stretch_ON_OFF_'+zone+orientation+'.colorIfTrueR')
 cmds.connectAttr('Stretch_ON_OFF_'+zone+orientation+'.outColorR',null1+orientation+'.scaleX')
 cmds.connectAttr('Stretch_ON_OFF_'+zone+orientation+'.outColorR',null5+orientation+'.scaleX')
 cmds.connectAttr('Stretch_ON_OFF_'+zone+orientation+'.outColorR',null3+orientation+'.scaleX')
 cmds.connectAttr('DM_'+zone+orientation+'Shape.distance',"Value_max_Stretch_CLAMP"+orientation+".minR")
 max=cmds.getAttr("DM_"+zone+orientation+"Shape.distance")
 cmds.setAttr("Value_max_Stretch_CLAMP"+orientation+".maxR",max+5)
 cmds.connectAttr('Value_max_Stretch_CLAMP'+orientation+'.outputR',"ScaleCompensateMD_"+zone+orientation+".input1X")
 cmds.connectAttr('CTRL_GENERAL_HAND'+orientation+'.ON_OFF','Stretch_ON_OFF_'+zone+orientation+'.firstTerm')
 #Attribute#
 cmds.setAttr('StretchDivideMD_'+zone+orientation+'.operation',2)
 cmds.setAttr('Stretch_Condition_'+zone+orientation+'.operation',3)
 cmds.setAttr('Stretch_Condition_'+zone+orientation+'.secondTerm',1)
 cmds.parent(null4+orientation,"SHADOW")
 cmds.parent('DM_'+zone+orientation,"SHADOW")
 cmds.parent('GRP_'+zone+'_IK'+orientation,"SHADOW")
#_____________________________
def bridgeHand(orientation):
 cmds.spaceLocator(n="LOC_BRIDGE_HAND"+orientation)
 hande=cmds.xform("WRIST"+orientation, query=True, t=True, worldSpace=True)
 cmds.xform("LOC_BRIDGE_HAND"+orientation,ws=True,t=hande,absolute=True)
 cmds.parentConstraint("LOC_BRIDGE_HAND"+orientation,"CTRL_GENERAL_HAND"+orientation,mo=True)
 cmds.parentConstraint("LOC_BRIDGE_HAND"+orientation,"CTRL_PINKY1"+orientation,mo=True)
 cmds.parentConstraint("LOC_BRIDGE_HAND"+orientation,"CTRL_RING1"+orientation,mo=True)
 cmds.parentConstraint("LOC_BRIDGE_HAND"+orientation,"CTRL_MID1"+orientation,mo=True)
 cmds.parentConstraint("LOC_BRIDGE_HAND"+orientation,"CTRL_INDEX1"+orientation,mo=True)
 cmds.parentConstraint("LOC_BRIDGE_HAND"+orientation,"CTRL_THUMB1"+orientation,mo=True)
 cmds.parentConstraint("WRIST"+orientation,"LOC_BRIDGE_HAND"+orientation,mo=True)
 cmds.parent('LOC_BRIDGE_HAND'+orientation,'SHADOW')
#_____________________________ 
def bridge(null1,null2,zone,ori):
  cmds.spaceLocator(n="LOC_BRIDGE_"+zone+ori)
  placement=cmds.xform(null1+ori, query=True, t=True, worldSpace=True)
  cmds.xform("LOC_BRIDGE_"+zone+ori,ws=True,t=placement,absolute=True)
  pivot=cmds.xform(null2+ori, query=True, t=True, worldSpace=True)
  cmds.xform("LOC_BRIDGE_"+zone+ori+".scalePivot",ws=True,t=pivot,absolute=True)
  cmds.xform("LOC_BRIDGE_"+zone+ori+".rotatePivot",ws=True,t=pivot,absolute=True)
  cmds.select("LOC_BRIDGE_"+zone+ori)
  cmds.FreezeTransformations()
  cmds.parentConstraint("CTRL_"+null2+ori,"LOC_BRIDGE_"+zone+ori,mo=True)
  cmds.parentConstraint("LOC_BRIDGE_"+zone+ori,"GRP_MECA_"+zone+ori,mo=True)
  cmds.parent("LOC_BRIDGE_"+zone+ori,"SHADOW")
  cmds.select(d=True)
#_____________________________ 
def Side_to_Side_L (position):
 cmds.select("ANKLE"+position)
 cmds.duplicate()
 cmds.rename("RC_ANKLE"+position)
 cmds.setAttr("RC_ANKLE"+position+".radius",0.5)
 cmds.select("RC_ANKLE"+position+"|TOE"+position)
 cmds.rename("RC_TOE"+position)
 cmds.setAttr("RC_TOE"+position+".radius",0.5)
 cmds.select("RC_ANKLE"+position+"|RC_TOE"+position+"|END"+position)
 cmds.rename("RC_END"+position)
 cmds.setAttr("RC_END"+position+".radius",0.5)
 cmds.select("RC_ANKLE"+position+"|RC_TOE"+position+"|RC_END"+position+"|HEEL"+position)
 cmds.rename('RC_HEEL'+position)
 cmds.setAttr("RC_HEEL"+position+".radius",0.5)
 cmds.select("HEEL"+position)
 cmds.delete()
 cmds.select("RC_ANKLE"+position+"|ANKLE"+position+"_orientConstraint1")
 cmds.delete()
 cmds.select("RC_ANKLE"+position)
 cmds.Unparent()
 cmds.SelectHierarchy()
 cmds.Unparent()
 cmds.select("RC_HEEL"+position)
 cmds.duplicate()
 cmds.rename("BRIDGE_RC"+position)
 cmds.setAttr("BRIDGE_RC"+position+".radius",1)
 cmds.parent("RC_ANKLE"+position,"RC_TOE"+position)
 cmds.parent("RC_TOE"+position,"RC_END"+position)
 cmds.parent("RC_END"+position,"RC_HEEL"+position)
 cmds.parent("RC_HEEL"+position,"BRIDGE_RC"+position)
 cmds.select(d=True)
 #Parent IK /Creation IK
 cmds.parent("IK_ANKLE"+position,"RC_ANKLE"+position)
 cmds.ikHandle( n="IK_TOE"+position, sj="ANKLE"+position, ee="TOE"+position,sol="ikSCsolver" )
 cmds.parent("IK_TOE"+position,"RC_TOE"+position)
 cmds.ikHandle( n="IK_END"+position, sj="TOE"+position, ee="END"+position,sol="ikSCsolver" )
 cmds.parent("IK_END"+position,"RC_END"+position)
 cmds.select("IK_ANKLE"+position+"_pointConstraint1")
 cmds.delete()
 #Connection Editor
 cmds.connectAttr("CTRL_ANKLE"+position+".TOE_ROLL","RC_TOE"+position+".rotateX")
 cmds.connectAttr("CTRL_ANKLE"+position+".WIPE_ROLL","RC_END"+position+".rotateY")
 cmds.connectAttr("CTRL_ANKLE"+position+".HEEL_ROLL","RC_HEEL"+position+".rotateY")
 cmds.connectAttr("CTRL_ANKLE"+position+".TIPE_HEEL","RC_HEEL"+position+".rotateX")
 cmds.connectAttr("CTRL_ANKLE"+position+".TIPE_TOE","RC_END"+position+".rotateX")
 #Constrainte/ Parent
 cmds.parentConstraint("CTRL_ANKLE"+position,"LOC_INT_STS"+position,mo=True)
 cmds.parentConstraint("CTRL_ANKLE"+position,"LOC_EXT_STS"+position,mo=True)
 cmds.parentConstraint("CTRL_ANKLE"+position,"BRIDGE_RC"+position,mo=True)
 cmds.parent("LOC_INT_STS"+position,"SHADOW")
 cmds.parent("LOC_EXT_STS"+position,"SHADOW")
 cmds.parent("BRIDGE_RC"+position,"SHADOW")
 cmds.select(d=True)
 #SetAttr Constrainte
 #neutre
 cmds.parentConstraint("LOC_INT_STS"+position,"LOC_EXT_STS"+position,"BRIDGE_RC"+position,mo=True)
 cmds.setAttr("BRIDGE_RC"+position+"_parentConstraint1.LOC_EXT_STS"+position+"W2",0)
 cmds.setAttr("BRIDGE_RC"+position+"_parentConstraint1.LOC_INT_STS"+position+"W1",0)
 cmds.select("BRIDGE_RC"+position+"_parentConstraint1")
 cmds.setDrivenKeyframe("BRIDGE_RC"+position+"_parentConstraint1.LOC_EXT_STS"+position+"W2",cd="CTRL_ANKLE"+position+".SIDE_TO_SIDE")
 cmds.setDrivenKeyframe("BRIDGE_RC"+position+"_parentConstraint1.LOC_INT_STS"+position+"W1",cd="CTRL_ANKLE"+position+".SIDE_TO_SIDE")
 #ext
 cmds.setAttr("CTRL_ANKLE"+position+".SIDE_TO_SIDE",0.01)
 cmds.setAttr("BRIDGE_RC"+position+"_parentConstraint1.LOC_EXT_STS"+position+"W2",1)
 cmds.setAttr("BRIDGE_RC"+position+"_parentConstraint1.LOC_INT_STS"+position+"W1",0)
 cmds.setDrivenKeyframe("BRIDGE_RC"+position+"_parentConstraint1.LOC_EXT_STS"+position+"W2",cd="CTRL_ANKLE"+position+".SIDE_TO_SIDE")
 cmds.setDrivenKeyframe("BRIDGE_RC"+position+"_parentConstraint1.LOC_INT_STS"+position+"W1",cd="CTRL_ANKLE"+position+".SIDE_TO_SIDE")
 cmds.setAttr("CTRL_ANKLE"+position+".SIDE_TO_SIDE",10)
 cmds.setAttr("BRIDGE_RC"+position+"_parentConstraint1.LOC_EXT_STS"+position+"W2",1)
 cmds.setAttr("BRIDGE_RC"+position+"_parentConstraint1.LOC_INT_STS"+position+"W1",0)
 cmds.setDrivenKeyframe("BRIDGE_RC"+position+"_parentConstraint1.LOC_EXT_STS"+position+"W2",cd="CTRL_ANKLE"+position+".SIDE_TO_SIDE")
 cmds.setDrivenKeyframe("BRIDGE_RC"+position+"_parentConstraint1.LOC_INT_STS"+position+"W1",cd="CTRL_ANKLE"+position+".SIDE_TO_SIDE")
 #int
 cmds.setAttr("CTRL_ANKLE"+position+".SIDE_TO_SIDE",-0.01)
 cmds.setAttr("BRIDGE_RC"+position+"_parentConstraint1.LOC_EXT_STS"+position+"W2",0)
 cmds.setAttr("BRIDGE_RC"+position+"_parentConstraint1.LOC_INT_STS"+position+"W1",1)
 cmds.setDrivenKeyframe("BRIDGE_RC"+position+"_parentConstraint1.LOC_EXT_STS"+position+"W2",cd="CTRL_ANKLE"+position+".SIDE_TO_SIDE")
 cmds.setDrivenKeyframe("BRIDGE_RC"+position+"_parentConstraint1.LOC_INT_STS"+position+"W1",cd="CTRL_ANKLE"+position+".SIDE_TO_SIDE")
 cmds.setAttr("CTRL_ANKLE"+position+".SIDE_TO_SIDE",-10)
 cmds.setAttr("BRIDGE_RC"+position+"_parentConstraint1.LOC_EXT_STS"+position+"W2",0)
 cmds.setAttr("BRIDGE_RC"+position+"_parentConstraint1.LOC_INT_STS"+position+"W1",1)
 cmds.setDrivenKeyframe("BRIDGE_RC"+position+"_parentConstraint1.LOC_EXT_STS"+position+"W2",cd="CTRL_ANKLE"+position+".SIDE_TO_SIDE")
 cmds.setDrivenKeyframe("BRIDGE_RC"+position+"_parentConstraint1.LOC_INT_STS"+position+"W1",cd="CTRL_ANKLE"+position+".SIDE_TO_SIDE")
 #SET Attr Rotation
 #ext
 cmds.setAttr("CTRL_ANKLE"+position+".SIDE_TO_SIDE",10)
 cmds.setAttr("LOC_EXT_STS"+position+".rz",-70)
 cmds.setAttr("LOC_INT_STS"+position+".rz",0)
 cmds.setDrivenKeyframe("LOC_EXT_STS"+position+".rz",cd="CTRL_ANKLE"+position+".SIDE_TO_SIDE")
 cmds.setDrivenKeyframe("LOC_INT_STS"+position+".rz",cd="CTRL_ANKLE"+position+".SIDE_TO_SIDE")
 #int
 cmds.setAttr("CTRL_ANKLE"+position+".SIDE_TO_SIDE",-10)
 cmds.setAttr("LOC_EXT_STS"+position+".rz",0)
 cmds.setAttr("LOC_INT_STS"+position+".rz",60)
 cmds.setDrivenKeyframe("LOC_EXT_STS"+position+".rz",cd="CTRL_ANKLE"+position+".SIDE_TO_SIDE")
 cmds.setDrivenKeyframe("LOC_INT_STS"+position+".rz",cd="CTRL_ANKLE"+position+".SIDE_TO_SIDE")
 #neutre
 cmds.setAttr("CTRL_ANKLE"+position+".SIDE_TO_SIDE",0)
 cmds.setAttr("LOC_EXT_STS"+position+".rz",0)
 cmds.setAttr("LOC_INT_STS"+position+".rz",0)
 cmds.setDrivenKeyframe("LOC_EXT_STS"+position+".rz",cd="CTRL_ANKLE"+position+".SIDE_TO_SIDE")
 cmds.setDrivenKeyframe("LOC_INT_STS"+position+".rz",cd="CTRL_ANKLE"+position+".SIDE_TO_SIDE")
#_____________________________
def Side_to_Side_R (position):
 cmds.select("ANKLE"+position)
 cmds.duplicate()
 cmds.rename("RC_ANKLE"+position)
 cmds.setAttr("RC_ANKLE"+position+".radius",0.5)
 cmds.select("RC_ANKLE"+position+"|TOE"+position)
 cmds.rename("RC_TOE"+position)
 cmds.setAttr("RC_TOE"+position+".radius",0.5)
 cmds.select("RC_ANKLE"+position+"|RC_TOE"+position+"|END"+position)
 cmds.rename("RC_END"+position)
 cmds.setAttr("RC_END"+position+".radius",0.5)
 cmds.select("RC_ANKLE"+position+"|RC_TOE"+position+"|RC_END"+position+"|HEEL"+position)
 cmds.rename('RC_HEEL'+position)
 cmds.setAttr("RC_HEEL"+position+".radius",0.5)
 cmds.select("HEEL"+position)
 cmds.delete()
 cmds.select("RC_ANKLE"+position+"|ANKLE"+position+"_orientConstraint1")
 cmds.delete()
 cmds.select("RC_ANKLE"+position)
 cmds.Unparent()
 cmds.SelectHierarchy()
 cmds.Unparent()
 cmds.select("RC_HEEL"+position)
 cmds.duplicate()
 cmds.rename("BRIDGE_RC"+position)
 cmds.setAttr("BRIDGE_RC"+position+".radius",1)
 cmds.parent("RC_ANKLE"+position,"RC_TOE"+position)
 cmds.parent("RC_TOE"+position,"RC_END"+position)
 cmds.parent("RC_END"+position,"RC_HEEL"+position)
 cmds.parent("RC_HEEL"+position,"BRIDGE_RC"+position)
 cmds.select(d=True)
 #Parent IK /Creation IK
 cmds.parent("IK_ANKLE"+position,"RC_ANKLE"+position)
 cmds.ikHandle( n="IK_TOE"+position, sj="ANKLE"+position, ee="TOE"+position,sol="ikSCsolver" )
 cmds.parent("IK_TOE"+position,"RC_TOE"+position)
 cmds.ikHandle( n="IK_END"+position, sj="TOE"+position, ee="END"+position,sol="ikSCsolver" )
 cmds.parent("IK_END"+position,"RC_END"+position)
 cmds.select("IK_ANKLE"+position+"_pointConstraint1")
 cmds.delete()
 #Connection Editor
 cmds.connectAttr("CTRL_ANKLE"+position+".TOE_ROLL","RC_TOE"+position+".rotateX")
 cmds.connectAttr("CTRL_ANKLE"+position+".WIPE_ROLL","RC_END"+position+".rotateY")
 cmds.connectAttr("CTRL_ANKLE"+position+".HEEL_ROLL","RC_HEEL"+position+".rotateY")
 cmds.connectAttr("CTRL_ANKLE"+position+".TIPE_HEEL","RC_HEEL"+position+".rotateX")
 cmds.connectAttr("CTRL_ANKLE"+position+".TIPE_TOE","RC_END"+position+".rotateX")
 #Constrainte/ Parent
 cmds.parentConstraint("CTRL_ANKLE"+position,"LOC_INT_STS"+position,mo=True)
 cmds.parentConstraint("CTRL_ANKLE"+position,"LOC_EXT_STS"+position,mo=True)
 cmds.parentConstraint("CTRL_ANKLE"+position,"BRIDGE_RC"+position,mo=True)
 cmds.parent("LOC_INT_STS"+position,"SHADOW")
 cmds.parent("LOC_EXT_STS"+position,"SHADOW")
 cmds.parent("BRIDGE_RC"+position,"SHADOW")
 cmds.select(d=True)
 #SetAttr Constrainte
 #neutre
 cmds.parentConstraint("LOC_INT_STS"+position,"LOC_EXT_STS"+position,"BRIDGE_RC"+position,mo=True)
 cmds.setAttr("BRIDGE_RC"+position+"_parentConstraint1.LOC_EXT_STS"+position+"W2",0)
 cmds.setAttr("BRIDGE_RC"+position+"_parentConstraint1.LOC_INT_STS"+position+"W1",0)
 cmds.select("BRIDGE_RC"+position+"_parentConstraint1")
 cmds.setDrivenKeyframe("BRIDGE_RC"+position+"_parentConstraint1.LOC_EXT_STS"+position+"W2",cd="CTRL_ANKLE"+position+".SIDE_TO_SIDE")
 cmds.setDrivenKeyframe("BRIDGE_RC"+position+"_parentConstraint1.LOC_INT_STS"+position+"W1",cd="CTRL_ANKLE"+position+".SIDE_TO_SIDE")
 #ext
 cmds.setAttr("CTRL_ANKLE"+position+".SIDE_TO_SIDE",0.01)
 cmds.setAttr("BRIDGE_RC"+position+"_parentConstraint1.LOC_EXT_STS"+position+"W2",1)
 cmds.setAttr("BRIDGE_RC"+position+"_parentConstraint1.LOC_INT_STS"+position+"W1",0)
 cmds.setDrivenKeyframe("BRIDGE_RC"+position+"_parentConstraint1.LOC_EXT_STS"+position+"W2",cd="CTRL_ANKLE"+position+".SIDE_TO_SIDE")
 cmds.setDrivenKeyframe("BRIDGE_RC"+position+"_parentConstraint1.LOC_INT_STS"+position+"W1",cd="CTRL_ANKLE"+position+".SIDE_TO_SIDE")
 cmds.setAttr("CTRL_ANKLE"+position+".SIDE_TO_SIDE",10)
 cmds.setAttr("BRIDGE_RC"+position+"_parentConstraint1.LOC_EXT_STS"+position+"W2",1)
 cmds.setAttr("BRIDGE_RC"+position+"_parentConstraint1.LOC_INT_STS"+position+"W1",0)
 cmds.setDrivenKeyframe("BRIDGE_RC"+position+"_parentConstraint1.LOC_EXT_STS"+position+"W2",cd="CTRL_ANKLE"+position+".SIDE_TO_SIDE")
 cmds.setDrivenKeyframe("BRIDGE_RC"+position+"_parentConstraint1.LOC_INT_STS"+position+"W1",cd="CTRL_ANKLE"+position+".SIDE_TO_SIDE")
 #int
 cmds.setAttr("CTRL_ANKLE"+position+".SIDE_TO_SIDE",-0.01)
 cmds.setAttr("BRIDGE_RC"+position+"_parentConstraint1.LOC_EXT_STS"+position+"W2",0)
 cmds.setAttr("BRIDGE_RC"+position+"_parentConstraint1.LOC_INT_STS"+position+"W1",1)
 cmds.setDrivenKeyframe("BRIDGE_RC"+position+"_parentConstraint1.LOC_EXT_STS"+position+"W2",cd="CTRL_ANKLE"+position+".SIDE_TO_SIDE")
 cmds.setDrivenKeyframe("BRIDGE_RC"+position+"_parentConstraint1.LOC_INT_STS"+position+"W1",cd="CTRL_ANKLE"+position+".SIDE_TO_SIDE")
 cmds.setAttr("CTRL_ANKLE"+position+".SIDE_TO_SIDE",-10)
 cmds.setAttr("BRIDGE_RC"+position+"_parentConstraint1.LOC_EXT_STS"+position+"W2",0)
 cmds.setAttr("BRIDGE_RC"+position+"_parentConstraint1.LOC_INT_STS"+position+"W1",1)
 cmds.setDrivenKeyframe("BRIDGE_RC"+position+"_parentConstraint1.LOC_EXT_STS"+position+"W2",cd="CTRL_ANKLE"+position+".SIDE_TO_SIDE")
 cmds.setDrivenKeyframe("BRIDGE_RC"+position+"_parentConstraint1.LOC_INT_STS"+position+"W1",cd="CTRL_ANKLE"+position+".SIDE_TO_SIDE")
 #SET Attr Rotation
 #ext
 cmds.setAttr("CTRL_ANKLE"+position+".SIDE_TO_SIDE",10)
 cmds.setAttr("LOC_EXT_STS"+position+".rz",70)
 cmds.setAttr("LOC_INT_STS"+position+".rz",0)
 cmds.setDrivenKeyframe("LOC_EXT_STS"+position+".rz",cd="CTRL_ANKLE"+position+".SIDE_TO_SIDE")
 cmds.setDrivenKeyframe("LOC_INT_STS"+position+".rz",cd="CTRL_ANKLE"+position+".SIDE_TO_SIDE")
 #int
 cmds.setAttr("CTRL_ANKLE"+position+".SIDE_TO_SIDE",-10)
 cmds.setAttr("LOC_EXT_STS"+position+".rz",0)
 cmds.setAttr("LOC_INT_STS"+position+".rz",-60)
 cmds.setDrivenKeyframe("LOC_EXT_STS"+position+".rz",cd="CTRL_ANKLE"+position+".SIDE_TO_SIDE")
 cmds.setDrivenKeyframe("LOC_INT_STS"+position+".rz",cd="CTRL_ANKLE"+position+".SIDE_TO_SIDE")
 #neutre
 cmds.setAttr("CTRL_ANKLE"+position+".SIDE_TO_SIDE",0)
 cmds.setAttr("LOC_EXT_STS"+position+".rz",0)
 cmds.setAttr("LOC_INT_STS"+position+".rz",0)
 cmds.setDrivenKeyframe("LOC_EXT_STS"+position+".rz",cd="CTRL_ANKLE"+position+".SIDE_TO_SIDE")
 cmds.setDrivenKeyframe("LOC_INT_STS"+position+".rz",cd="CTRL_ANKLE"+position+".SIDE_TO_SIDE")
#_____________________________ 
def switch (null1,null2,null3,zone,orientation):
 ##Contrainte##
 cmds.parentConstraint(null3+"_IK"+orientation,null3+"_FK"+orientation,null3+orientation, mo=True)
 cmds.parentConstraint(null2+"_IK"+orientation,null2+"_FK"+orientation,null2+orientation, mo=True)
 cmds.parentConstraint(null1+"_IK"+orientation,null1+"_FK"+orientation,null1+orientation, mo=True)
 ##Selection node + creation##
 joint=[null3+orientation,null2+orientation,null1+orientation]
 for each_int in joint :
  cmds.select(each_int +"_parentConstraint1",tgl =True)
  cmds.select("CTRL_FK_"+null1+orientation,"CTRL_FK_"+null2+orientation,"CTRL_FK_"+null3+orientation,"CTRL_IK_"+null3+orientation,"CTRL_IK_"+null2+orientation,"CTRL_GENERAL_"+zone+orientation)
  cmds.NodeEditorGraphClearGraph()
  cmds.NodeEditorGraphAddSelected()
  cmds.createNode("reverse")
  cmds.select("reverse1")
  cmds.rename("IK_FK_SWITCH_REVERSE"+zone+orientation)
  cmds.NodeEditorGraphAddSelected()
 ##Connections##
  #Connection CTRL#
 cmds.connectAttr("CTRL_IK_"+null3+orientation+".visibility","CTRL_IK_"+null2+orientation+".visibility")
 cmds.connectAttr("CTRL_IK_"+null2+orientation+".visibility","AIM_CTRL_ELBOW"+orientation+".visibility")
 cmds.connectAttr("CTRL_FK_"+null3+orientation+".visibility","CTRL_FK_"+null2+orientation+".visibility")
 cmds.connectAttr("CTRL_FK_"+null2+orientation+".visibility","CTRL_FK_"+null1+orientation+".visibility")
 #Connection SWITCH#
 cmds.connectAttr("CTRL_GENERAL_"+zone+orientation+".IK_Fk",null1+orientation+"_parentConstraint1."+null1+"_FK"+orientation+"W1")
 cmds.connectAttr("CTRL_GENERAL_"+zone+orientation+".IK_Fk",null2+orientation+"_parentConstraint1."+null2+"_FK"+orientation+"W1")
 cmds.connectAttr("CTRL_GENERAL_"+zone+orientation+".IK_Fk",null3+orientation+"_parentConstraint1."+null3+"_FK"+orientation+"W1")
 cmds.connectAttr("CTRL_GENERAL_"+zone+orientation+".IK_Fk","CTRL_FK_"+null3+orientation+".visibility")
 cmds.connectAttr("CTRL_GENERAL_"+zone+orientation+".IK_Fk","IK_FK_SWITCH_REVERSE"+zone+orientation+".inputX")
 #Reverse#
 cmds.connectAttr("IK_FK_SWITCH_REVERSE"+zone+orientation+".outputX",null1+orientation+"_parentConstraint1."+null1+"_IK"+orientation+"W0")
 cmds.connectAttr("IK_FK_SWITCH_REVERSE"+zone+orientation+".outputX",null2+orientation+"_parentConstraint1."+null2+"_IK"+orientation+"W0")
 cmds.connectAttr("IK_FK_SWITCH_REVERSE"+zone+orientation+".outputX",null3+orientation+"_parentConstraint1."+null3+"_IK"+orientation+"W0")
 cmds.connectAttr("IK_FK_SWITCH_REVERSE"+zone+orientation+".outputX","CTRL_IK_"+null3+orientation+".visibility")
#__________________________________________________________
 #Creation de def pour les joints et le Mirroir et du delete
def Rig(listofname):
    for name in listofname :
     position = cmds.getAttr('LOC_'+name +'Shape.localPosition')[0]
     joint = cmds.joint(n=name,p=position)
     cmds.select(d=True)
#_____________________________
def RigEYEBOT(listofname):
    for name in listofname :
     position = cmds.getAttr('LOC_'+name +'Shape.localPosition')[0]
     joint = cmds.joint(n='BOT_'+name,p=position,rad=0.5)
     cmds.select(d=True)
#_____________________________
def RigEYETOP(listofname):
    for name in listofname :
     position = cmds.getAttr('LOC_'+name +'Shape.localPosition')[0]
     joint = cmds.joint(n='TOP_'+name,p=position,rad=0.75)
     cmds.select(d=True)
#_____________________________
def mirror(listeofname):
    for joint in listeofname :
     cmds.mirrorJoint(joint,searchReplace=('_L', '_R'))
     cmds.select(d=True)
