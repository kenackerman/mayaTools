def ka_trailToCurve():

    # This command can be used to convert motion trails into curves
    # this is useful when you want to attach a motionpath to, say, a bird, and have it fly close to the camera
    # I adapted this for python from a script on creativeCrash by user Joojaa
    
    import maya.cmds as cmds
    
    
    # this command will select any motion trails you have in the scene 
    motionTrails = cmds.ls(dag = True, et= 'snapshotShape')
    
    for trail in motionTrails:
        pts = cmds.getAttr(trail + ".pts")
        size = len(pts)
        #make a curve to start from
        curve = cmds.curve(name = (trail + "_curve"),d=3, p=[pts[0][0:3],pts[1][0:3]],k=[0,1,2,3])
        
        #now append on the rest of the points
        i=2
        while i < size:
            cmds.curve (curve, os=True, a=True, p= pts[i][0:3])
            i+= 1
            
        
        

