# Filename: rig_toolbox.py
# Author: Arthur Bodart
# Created: 2024-10-19
# Description: This is a basic toolbox with rigging functions for my dear and beloved students :).

import maya.cmds as cmds
import maya.api.OpenMaya as om


def transform_offset(objs=[], suffix='offset', joint=False):
    """
        This command creates either a transform or a joint offset onto items
        :param objs: objects to create an offset for
        :param suffix: suffix to be used
        :param joint: If set to true, creates a joint offset instead of a transform
        """
    if not objs:
        objs = cmds.ls(selection=True)

    # Statement d'une boucle for pour chaque objet à offset
    for o in objs:

        # Récupération des coordonnées dans le world space de l'objet
        tr = cmds.xform(o, query=True, translation=True, worldSpace=True)
        ro = cmds.xform(o, query=True, rotation=True, worldSpace=True)
        sc = cmds.xform(o, query=True, scale=True, worldSpace=True)

        # Création de mon group offset
        if joint:
            offset = cmds.createNode('joint', n=f'{o}_{suffix}')
        else:
            offset = cmds.createNode('transform', n=f'{o}_{suffix}')

        # Set les transformations du group offset
        axes = ['X', 'Y', 'Z']
        for a in axes:
            idx = axes.index(a)
            cmds.setAttr(f'{offset}.translate{a}', tr[idx])
            cmds.setAttr(f'{offset}.rotate{a}', ro[idx])
            cmds.setAttr(f'{offset}.scale{a}', sc[idx])

        # Récupération du parent de l'objet à offset
        op = cmds.listRelatives(o, parent=True)

        # Parent l'objet sous son offset, puis l'offset sous le parent initial
        cmds.parent(o, offset)

        if op:
            cmds.parent(offset, op)
        
    return offset


def matrix_constraint(child='', parent='', mo=True, tr=True, ro=True, sc=True):
    """
    This command creates a constraint between 2 objects using matrices
    :param child: constrained object
    :param parent: parent object of the constraint
    :param mo: If set to true, maintains offset between parent and child
    :param tr: If set to false, deactivates translate in the constraint
    :param ro: If set to false, deactivates rotate in the constraint
    :param sc: If set to false, deactivates scale in the constraint
    :return: returns a list containing the multMatrix and the blendMatrix nodes
    """
    if not parent:
        parent = cmds.ls(selection=True)[0]
    if not child:
        child = cmds.ls(selection=True)[1]

    mmtx = cmds.createNode('multMatrix', name=f'{parent}_mmtx')
    bmtx = cmds.createNode('blendMatrix', name=f'{parent}_bmtx')
    offset = cmds.listRelatives(child, parent=True)[0]

    if not tr:
        cmds.setAttr(f'{bmtx}.target[0].translateWeight', 0)
    if not ro:
        cmds.setAttr(f'{bmtx}.target[0].rotateWeight', 0)
    if not sc:
        cmds.setAttr(f'{bmtx}.target[0].scaleWeight', 0)

    if mo:
        mtx_1 = om.MMatrix(cmds.getAttr(f'{child}.worldMatrix[0]'))
        mtx_2 = om.MMatrix(cmds.getAttr(f'{parent}.worldInverseMatrix[0]'))

        mtx_sum = mtx_1 * mtx_2

        cmds.setAttr(f'{mmtx}.matrixIn[0]', mtx_sum, type='matrix')

    cmds.connectAttr(f'{parent}.worldMatrix[0]', f'{mmtx}.matrixIn[1]')
    cmds.connectAttr(f'{offset}.worldInverseMatrix[0]', f'{mmtx}.matrixIn[2]')

    cmds.connectAttr(f'{mmtx}.matrixSum', f'{bmtx}.target[0].targetMatrix')
    cmds.connectAttr(f'{bmtx}.outputMatrix', f'{child}.offsetParentMatrix')

    return [mmtx, bmtx]


def ctrls_on_joints(jnts=[], scale=2):
    """
    :param jnts: list
    :param scale: float
    :return:
    """
    controls = []
    offsets = []
    
    if not jnts:
        jnts = cmds.ls(sl=1)
    for j in jnts:
        # Generate control name from provided jnt name, deduce it's future parent
        ctrl_name = j.replace('_jnt', '_ctrl')
        controls.append(ctrl_name)
        # Create and match transform the curve onto the jnt
        cmds.circle(name=ctrl_name)
        cmds.matchTransform(ctrl_name, j)
        # Create an offset on the ctrl
        offset_name = transform_offset(objs=[ctrl_name])
        offsets.append(offset_name)
        # Select CVs then scale and rotate
        cmds.select(f'{ctrl_name}.cv[*]', replace=True)
        cmds.rotate(0, 90, 0, relative=True, objectSpace=True)
        cmds.scale(scale, scale, scale, r=True, os=True)
        # Enable drawing override prior to setting color
        cmds.setAttr(f'{ctrl_name}Shape.overrideEnabled', 1)
        # Query world space translate x and set color depending on the side (red for -x, blue for +x)
        pos = cmds.xform(ctrl_name, translation=True, query=True, worldSpace=True)
        if pos[0] > 0:
            cmds.setAttr(f'{ctrl_name}Shape.overrideColor', 13)
        elif pos[0] < 0:
            cmds.setAttr(f'{ctrl_name}Shape.overrideColor', 6)
        else :
            cmds.setAttr(f'{ctrl_name}Shape.overrideColor', 18)
        # Clear selection and history of the control
        cmds.select(clear=True)
        cmds.delete(ctrl_name, ch=True)
        
    for ctrl in controls:
        idx = controls.index(ctrl)
        jnt_name = ctrl.replace('_ctrl', '_jnt')
        try:
            parent_ctrl = cmds.listRelatives(jnt_name, parent=True)[0].replace('_jnt', '_ctrl')
        except:
            parent_ctrl = ''
        if cmds.objExists(parent_ctrl):
            cmds.parent(offsets[idx], parent_ctrl)
        
    


def copy_shape(objs=[]):
    """
    Copies shape from a nurbs curve to others.
    :param list objs: List of curves. Last item of selection will be copied.
    :return:
    """
    if not objs:
        objs = cmds.ls(selection=True)

    src_crv = cmds.listRelatives(objs[-1], shapes=True)
    objs.pop(-1)

    for o in objs:
        # Get number of control points in the shape
        tgt_shp = cmds.listRelatives(o, shapes=True)[0]
        pts = cmds.getAttr(o + '.spans') + 1
        for i in range(pts):
            cmds.setAttr(f'{o}.controlPoints[{i}].xValue', 0)
            cmds.setAttr(f'{o}.controlPoints[{i}].yValue', 0)
            cmds.setAttr(f'{o}.controlPoints[{i}].zValue', 0)
        # Connect to shape to flush it
        cmds.connectAttr(f'{src_crv[0]}.local', f'{tgt_shp}.create', force=True)
        cmds.currentTime(1)
        cmds.disconnectAttr(f'{src_crv[0]}.local', f'{tgt_shp}.create')


def mirror_shape(objs=[]):
    """
    Copies shape from a nurbs curve to others.
    :param list objs: List of curves. Last item of selection will be copied.
    :return:
    """
    if not objs:
        objs = cmds.ls(selection=True)
    for o in objs:
        src_shp = cmds.listRelatives(o, shapes=True)[0]
        # Get number of control points in the shape
        tgt_shp = src_shp.replace('L_', 'R_')
        if not cmds.objExists(tgt_shp):
            cmds.error(
                f'Could not find {tgt_shp}, please check your scene for possible naming errors or missing controls !')
        # Check if curve is open or closed before getting spans to deduce number of CVs
        if cmds.getAttr(f'{src_shp}.form') == 0:
            pts = cmds.getAttr(f'{src_shp}.spans') + 1
        else:
            pts = cmds.getAttr(f'{src_shp}.spans')
        # Connect to shape to flush it
        cmds.connectAttr(f'{src_shp}.local', f'{tgt_shp}.create', force=True)
        cmds.currentTime(1)
        cmds.disconnectAttr(f'{src_shp}.local', f'{tgt_shp}.create')
        # For each CV on target curve, get corresponding xform on source curve and apply with X value multiplied by -1
        for i in range(pts):
            tr = cmds.xform(f'{src_shp}.controlPoints[{i}]', query=True, translation=True, worldSpace=True)
            mirrored_tr = [tr[0] * -1, tr[1], tr[2]]
            cmds.xform(f'{tgt_shp}.controlPoints[{i}]', translation=mirrored_tr, absolute=True, worldSpace=True)
        print(f'### MIRRORED : {tgt_shp}')
