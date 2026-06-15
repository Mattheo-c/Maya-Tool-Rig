import maya.cmds as cmds
import mto_makingmenu as menu  
import importlib



Rig_Menu = "makingmenu"

class makingmenu() :
    def __init__(self):
        self._removeOld()
        self._build()
    
    def _removeOld(self) :
        if cmds.popupMenu(Rig_Menu, ex=1):
            cmds.deleteUI(Rig_Menu)
    
    def _build(self):
        menu = cmds.popupMenu(Rig_Menu, mm=1 ,b=3, aob=1, ctl=1, alt=1, sh=1, p="viewPanes", pmo=1, pmc=self._buildMarkingMenu)
    
    def _buildMarkingMenu (self, menu, parent) :
        #Radial#
        cmds.menuItem(p=menu, l="Joint", rp="N", c="cmds.JointTool()",i="kinJoint.png")
        cmds.menuItem(p=menu, ob=1, c="cmds.JointToolOptions()")

        subMenu2 = cmds.menuItem(p=menu, l="Strok", rp="SE", c="print 'Strok'", subMenu=1,i='stroke.svg')
        subMenu1 = cmds.menuItem(p=menu, l="IK", rp="NE", c="print 'IK", subMenu=1,i='ikEffector.svg')
        subMenu3 = cmds.menuItem(p=menu, l="Contraint", rp="E", c="print 'Auto_Rig", subMenu=1,i='advancedSettings.png')
        subMenu4 = cmds.menuItem(p=menu, l="Curve", rp="SW", c="print'Curve", subMenu=1,i='curveVarGroup.svg')
        subMenu5 = cmds.menuItem(p=menu, l="Modify", rp="S", c="print 'Modify'",subMenu=1,i='materialX-document.png')
        cmds.menuItem(p=menu, l="Orient Joint", rp="W", c="cmds.OrientJoint()",i='orientJoint.png')
        cmds.menuItem(p=menu, ob=1, c="cmds.OrientJointOptions()")

        cmds.menuItem(p=menu, l="Miroir Joint", rp="NW", c="cmds.MirrorJoint()",i='HIKmirror.png')
        cmds.menuItem(p=menu, ob=1, c="cmds.MirrorJointOptions()")

        ##Sous Class Radial##
        #Sub Menu 1#
        cmds.menuItem(p=subMenu1, l="IK Handle",rp="NE", c="cmds.IKHandleTool()",i='ikHandle.svg')
        cmds.menuItem(p=subMenu1, ob=1, c="cmds.IKHandleToolOptions()") 

        cmds.menuItem(p=subMenu1, l="IK Spine",rp="E", c="cmds.IKSplineHandleTool()",i ='ikSplineSolver.svg')
        cmds.menuItem(p=subMenu1, ob=1, c="cmds.IKSplineHandleToolOptions()")

        #Sub Menu 2#
        cmds.menuItem(p=subMenu2, l="Creat Strok",rp="SE", c="cmds.AttachBrushToCurves()",i='stroke.svg')
        cmds.menuItem(p=subMenu2, l="Convert Poly",rp="E", c="cmds.PaintEffectsToPoly()",i='paintFXtoPoly.png')

        #Sub Menu 3#
        cmds.menuItem(p=subMenu3, l="Point",rp="E", c="cmds.PointConstraint()",i='pointConstraint.svg')
        cmds.menuItem(p=subMenu3, ob=1, c="cmds.PointConstraintOptions()")

        cmds.menuItem(p=subMenu3, l="Parent",rp="NE", c="cmds.ParentConstraint()",i='parentConstraint.svg')
        cmds.menuItem(p=subMenu3, ob=1, c="cmds.ParentConstraintOptions()")

        cmds.menuItem(p=subMenu3, l="Orient",rp="N", c="cmds.OrientConstraint()",i='orientConstraint.svg')
        cmds.menuItem(p=subMenu3, ob=1, c="cmds.OrientConstraintOptions()")

        cmds.menuItem(p=subMenu3, l="Aim",rp="SE", c="cmds.AimConstraint()",i='aimConstraint.png')
        cmds.menuItem(p=subMenu3, ob=1, c="cmds.AimConstraintOptions()")

        cmds.menuItem(p=subMenu3, l="Pole Vector",rp="S", c="cmds.PoleVectorConstraint()",i='poleVectorConstraint.svg')
        
        cmds.menuItem(p=subMenu3, l="Scale",rp="NW", c="cmds.ScaleConstraint()",i='scaleConstraint.svg')
        cmds.menuItem(p=subMenu3, ob=1, c="cmds.ScaleConstraintOptions()")

        #Sub Menu 4#
        cmds.menuItem(p=subMenu4, l="CV Curve",rp="SW", c="cmds.CVCurveTool()",i='curveCV.png')
        cmds.menuItem(p=subMenu4, ob=1, c="cmds.CVCurveToolOptions()")

        cmds.menuItem(p=subMenu4, l='Sphere',rp="W", c=sphere,i='polySphere.png')
        cmds.menuItem(p=subMenu4, l="Cube",rp="NW", c="cmds.curve(n='Cube',d=1, p=[(-1,0,-1),(1,0,-1),(1,0,1),(-1,0,1),(-1,0,-1),(-1,2,-1),(1,2,-1),(1,0,-1),(1,2,-1),(1,2,1),(1,0,1),(1,2,1),(-1,2,1),(-1,0,1),(-1,2,1),(-1,2,-1)])",i='polyCube.png')
        cmds.menuItem(p=subMenu4, l="Pyramide",rp="N", c="cmds.curve(n='Pyra',d=1, p=[(-1,0,-1),(1,0,-1),(1,0,1),(-1,0,1),(-1,0,-1),(0,1,0),(1,0,-1),(0,1,0),(1,0,1),(0,1,0),(-1,0,1)])",i='polyPyramid.svg')
        cmds.menuItem(p=subMenu4, l="Gear",rp="NE", c=Gear,i='polyGear.png')
        cmds.menuItem(p=subMenu4, l="Arrow",rp="E", c="cmds.curve(n='SimplyArrow',d=1, p=[(0,0,-1),(3,0,-1),(3,0,-2),(5,0,0),(3,0,2),(3,0,1),(0,0,1),(0,0,-1)])",i='item_down.png')
        cmds.menuItem(p=subMenu4, l="Arrow All Axe",rp="SE",c=AllAxes,i='fleur.png')
        cmds.menuItem(p=subMenu4, l="Cross",rp="S", c=Cross,i='createIcon.png')
        
        #Sub Menu 5#
        cmds.menuItem(p=subMenu5, l="Match All Transforms", rp="S", c="cmds.matchTransform()",i='channelBoxUseManips.png')
        cmds.menuItem(p=subMenu5, ob=1, c="cmds.MatchTransformOptions()")
        cmds.menuItem(p=subMenu5, l="Match Translation", rp="W", c="cmds.matchTransform(pos=1)",i='trackCursor.png')
        cmds.menuItem(p=subMenu5, ob=1, c="cmds.MatchTranslationOptions()")
        cmds.menuItem(p=subMenu5, l="Match Rotation", rp="E", c="cmds.matchTransform(rot=1)",i='rotate_M.png')
        cmds.menuItem(p=subMenu5, ob=1, c="cmds.MatchRotationOptions()")

        ##List##
        cmds.menuItem(p=menu, l='Curve Vertex', c='cmds.SelectCurveCVsAll()',i='curveEP.png')
        
        cmds.menuItem(p=menu, l='Skin Commamde', en = False)
        cmds.menuItem(p=menu, l='Bind Skin', c='cmds.SmoothBindSkin()',i='smoothSkin.png')
        cmds.menuItem(p=menu, ob=1, c="cmds.SmoothBindSkinOptions()")

        cmds.menuItem(p=menu, l='Skin Volum', c='cmds.InteractiveBindSkin()',i='interactiveBindTool.png')
        cmds.menuItem(p=menu, ob=1, c="cmds.InteractiveBindSkinOptions()")

        cmds.menuItem(p=menu, l='Unbind Skin', c='cmds.DetachSkin()',i='detachSkin.png')
        cmds.menuItem(p=menu, ob=1, c="cmds.DetachSkinOptions()")  
       
        cmds.menuItem(p=menu, l='Paint Skin', c='cmds.ArtPaintSkinWeightsTool()',i='paintSkinWeights.png')
        cmds.menuItem(p=menu, ob=1, c="cmds.ArtPaintSkinWeightsToolOptions()")

        cmds.menuItem(p=menu, l='Bake Deformation', c='cmds.BakeDeformerTool()',i='bakeBlendShape.png')

        cmds.menuItem(p=menu, l='Miror Skin', c='cmds.MirrorSkinWeights()',i='mirrorSkinWeight.png')
        cmds.menuItem(p=menu, ob=1, c="cmds.MirrorSkinWeightsOptions()")

        cmds.menuItem(p=menu, l='Copy Skin', c='cmds.CopySkinWeights()',i='copySkinWeight.png')
        cmds.menuItem(p=menu, ob=1, c="cmds.CopySkinWeightsOptions()")\
        
        cmds.menuItem(p=menu, l='Save Skin', en=False)
        cmds.menuItem(p=menu, l='Export Skin', c='cmds.ExportDeformerWeights()',i='exportSmoothSkin.png')
        cmds.menuItem(p=menu, l='Import Skin', c='cmds.ImportDeformerWeights()',i='importSmoothSkin.png')

        cmds.menuItem(p=menu, l='Deform', en = False)

        cmds.menuItem(p=menu, l='Delta Mush', c='cmds.DeltaMush()',i='deltaMush.png')
        cmds.menuItem(p=menu, ob=1, c="cmds.DeltaMushOptions()")

        cmds.menuItem(p=menu, l='Tension', c='cmds.Tension()',i='tension.png')
        cmds.menuItem(p=menu, ob=1, c="cmds.TensionOptions()")

        cmds.menuItem(p=menu, l='Cluster', c='cmds.CreateCluster()',i='cluster.png')
        cmds.menuItem(p=menu, l="Locator", c="cmds.CreateLocator()",i='locator.png')

        cmds.menuItem(p=menu, l='Joint Commande', en = False)
        cmds.menuItem(p=menu, l='Inset Joint', c='cmds.InsertJointTool()',i='kinInsert.png')

        cmds.menuItem(p=menu, l='Offset', en = False)
        cmds.menuItem(p=menu, l='Offset', c=offset,i='FreezeTransform.png')
        cmds.menuItem(p=menu, l='GRP', c=GroupOffset,i='folder-new.png')

        cmds.menuItem(p=menu, l='Animation', en = False)
        cmds.menuItem(p=menu, l='Clear Frame', c=DeleteFrame,i='deleteCacheFrame.png')


        # Rebuild
        crScriptPath = cmds.filePathEditor(query=True, listDirectories="c:/scripts/", status=True)
        cmds.menuItem(p=menu, l='Reload', en = False)
        cmds.menuItem(p=menu, l="Rebuild Marking Menu", c=startupCommands)
        

        ##ListCurve##
        cmds.menuItem(p=subMenu4, l="Circle Horizontal", c="cmds.circle(nr=(0,1,0))",i='circle.png')
        cmds.menuItem(p=subMenu4, l="Circle Vertical", c="cmds.circle()",i='circle.png')
        cmds.menuItem(p=subMenu4, l='Pin', c='cmds.curve(d=2, p=[(0,0,0),(2,0,0),(2,0,1),(4,0,1),(4,0,-1),(2,0,-1),(2,0,0),(0,0,0)])',i='pinRegularHover.png')

def offset (*arg) :
    selected_objects = cmds.ls(selection=True)
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

def startupCommands(*arg):
    importlib.reload(menu)
    menu.makingmenu()



#Creation Curve
def AllAxes(*arg):
 firstArrow=makeArrow()
 secondeArrow = makeArrow()
 threeArrow = makeArrow()
 fourArrow = makeArrow()
 cmds.setAttr(secondeArrow +".ry",90)
 cmds.setAttr(threeArrow +".ry",180)
 cmds.setAttr(fourArrow +".ry",-90)
 cmds.attachCurve(firstArrow,secondeArrow,threeArrow,fourArrow, rpo=False, n='Axe' )
 cmds.delete(firstArrow,secondeArrow,threeArrow,fourArrow)         
def makeArrow():
 myArrow = cmds.curve(d=1, p=[(1,0,-1),(3,0,-1),(3,0,-2),(5,0,0),(3,0,2),(3,0,1),(1,0,1)])
 return(myArrow)

def Cross(*arg):
 firstcross=makecross()
 secondecross = makecross()
 threecross = makecross()
 fourcross = makecross()
 cmds.setAttr(secondecross +".ry",90)
 cmds.setAttr(threecross +".ry",180)
 cmds.setAttr(fourcross +".ry",-90)
 cmds.attachCurve(firstcross,secondecross,threecross,fourcross, rpo=False, n='Cross' )
 cmds.delete(firstcross,secondecross,threecross,fourcross)
def makecross():
 mycross = cmds.curve(d=1, p=[(1,0,-1),(3,0,-1),(3,0,1),(1,0,1)])
 return(mycross)

def Gear(*arg):
 cmds.polyGear(sides=8,heightDivisions=2)
 cmds.select('pGear1')
 cmds.SelectEdgeMask()
 cmds.select("pGear1.e[57]","pGear1.e[59]","pGear1.e[61]","pGear1.e[63]","pGear1.e[65]","pGear1.e[67]","pGear1.e[70]","pGear1.e[72]","pGear1.e[74]","pGear1.e[76]","pGear1.e[78]","pGear1.e[80]","pGear1.e[83]","pGear1.e[85]","pGear1.e[87]","pGear1.e[89]","pGear1.e[91]","pGear1.e[93]","pGear1.e[96]","pGear1.e[98]","pGear1.e[100]","pGear1.e[102]","pGear1.e[104]","pGear1.e[106]","pGear1.e[109]","pGear1.e[111]","pGear1.e[113]","pGear1.e[115]","pGear1.e[117]","pGear1.e[119]","pGear1.e[122]","pGear1.e[124]","pGear1.e[126]","pGear1.e[128]","pGear1.e[130]","pGear1.e[132]","pGear1.e[135]","pGear1.e[137]","pGear1.e[139]","pGear1.e[141]","pGear1.e[143]","pGear1.e[145]","pGear1.e[148]","pGear1.e[150]","pGear1.e[152]","pGear1.e[154]","pGear1.e[156]","pGear1.e[158]")
 cmds.CreateCurveFromPoly()
 cmds.select('pGear1')
 cmds.delete()
 cmds.select("polyToCurve1")
 cmds.rename("Gear")

def sphere (*arg):
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
 grp =cmds.createNode('transform', n='CTRL')
 curve =cmds.select('curve1','curve2','curve3',grp)
 cmds.pickWalk(d='down')
 cmds.parent(  add=True, s=True )
 cmds.DeleteHistory('curveShape1','curveShape2','curveShape3')
 cmds.FreezeTransformations('curveShape1','curveShape2','curveShape3')
 cmds.delete('curve1','curve2','curve3')
 cmds.delete('stroke1','stroke2','stroke3')
 

def makeSphere(*arg):
 mySphere = cmds.circle(nr=(0,-1,0),r=1,)
 return(mySphere)
def makeSphere2():
 mySphere = cmds.circle(nr=(0,0,1),r=1,)
 return(mySphere)
def makeSphere3():
 mySphere = cmds.circle(nr=(1,0,0),r=1,)
 return(mySphere)

def GroupOffset(*arg):
  #Selection des curve
 curve=cmds.ls(type="nurbsCurve")
 cmds.select(curve)
 selection=cmds.pickWalk(d='up')
 #Creation du GRP
 for name in selection:
  grp=cmds.group(em=True,name="OFFSET_"+name)
  cmds.parent(name,grp)
 cmds.select(d=True) 

def DeleteFrame(*arg):
  frame=cmds.ls(type="animCurve")
  cmds.select(frame)
  cmds.delete()

# CopyRights :

#Code made by CASTILLO Mattheo / mto_...
#Contact :
#gmail : castillo.mattheo@gmail.com
#Special thanks to :

#- Creajeux video game school and all of its students for beta testing these tools.
#- Florian Delarque for helping about the code.