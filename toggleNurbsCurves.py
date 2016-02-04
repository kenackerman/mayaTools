import maya.cmds as cmds

'''
Ken Ackerman 2016
This command toggles Nurbs Curves on and off. 
The purpose is to make the animation process more efficient when working with rigs that utilize nurbsCurves as controls heavily.
It used to be built in to maya, but at some point the command to toggle these on and off was removed??
It uses the "withFocus" parameter so it works on the panel you have active.
This works well as a shelf button, but even better when mapped to a hotkey.
'''

def toggleNurbsCurves():


    myPanel = cmds.getPanel(withFocus = True)

    
    if(cmds.modelEditor(myPanel, query = True, nurbsCurves = True)):
        cmds.modelEditor(myPanel, edit = True,nurbsCurves = False)
        print "nurbsCurves hidden"
    else:
        cmds.modelEditor(myPanel, edit = True, nurbsCurves=True)
        print "nurbsCurves visible"


toggleNurbsCurves()
