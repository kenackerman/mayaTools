import maya.cmds as cmds

#This command is meant to be assigned to a hotkey. It will only work if you have the modeleditor selected. It toggles Nurbs Curves on and off. It used to be an explicit command in maya but at some point it changed.
# Ken Ackerman 2016

def toggleNurbsCurves():


    myPanel = cmds.getPanel(wf = True)

    
    if(cmds.modelEditor(myPanel, query = True, nurbsCurves = True)):
        cmds.modelEditor(myPanel, edit = True,nurbsCurves = False)
        print "nurbsCurves hidden"
    else:
        cmds.modelEditor(myPanel, edit = True, nurbsCurves=True)
        print "nurbsCurves visible"


toggleNurbsCurves()
