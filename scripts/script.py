import time

ZOOM = 2.0

# NOTE:
# the session file must first be loaded in

################################################################

def println(str):
    print("\n\t" + str + "\n")

def pause(command):
    print("\n\tto run " + command + " press [enter, enter]")
    s = raw_input()
    print("\t" + command + "\n")

def printScreen(capture, num):
    if capture:
        for i in range(num):
            time.sleep(4)
            SaveWindow()
    
################################################################

def setup(capture):
    SetActivePlots(1)
    t1 = TransformAttributes()
    t1.translateZ = 3
    SetOperatorOptions(t1, 1, 0)

    SetActivePlots(3)
    t3 = TransformAttributes()
    t3.translateZ = 6
    SetOperatorOptions(t3, 1, 0)

    SetActivePlots(4)
    t4 = TransformAttributes()
    t4.translateZ = 9
    SetOperatorOptions(t4, 1, 0)

    ######## Set layer color/opacity attributes

    SetActivePlots(0)
    p0 = PseudocolorAttributes()
    p0.minFlag = 1
    p0.min = 1.1
    p0.useBelowMinColor = 1
    p0.belowMinColor = (0, 0, 0, 255)
    p0.maxFlag = 0
    p0.max = 10
    p0.useAboveMaxColor = 0
    p0.aboveMaxColor = (0, 0, 0, 255)
    p0.colorTableName = "_black"
    p0.invertColorTable = 0
    p0.opacityType = p0.Constant  # ColorTable, FullyOpaque, Constant, Ramp, VariableRange
    p0.opacity = 0
    SetPlotOptions(p0)
    
    SetActivePlots(1)
    p1 = PseudocolorAttributes()
    p1.minFlag = 0
    p1.min = 0
    p1.useBelowMinColor = 0
    p1.belowMinColor = (0, 0, 0, 255)
    p1.maxFlag = 0
    p1.max = 0
    p1.useAboveMaxColor = 0
    p1.aboveMaxColor = (0, 0, 0, 255)
    p1.colorTableName = "_blue"
    p1.invertColorTable = 0
    p1.opacityType = p1.Constant  # ColorTable, FullyOpaque, Constant, Ramp, VariableRange
    p1.opacity = 0
    SetPlotOptions(p1)

    SetActivePlots(3)
    p3 = PseudocolorAttributes()
    p3.minFlag = 0
    p3.min = 0
    p3.useBelowMinColor = 0
    p3.belowMinColor = (0, 0, 0, 255)
    p3.maxFlag = 0
    p3.max = 0
    p3.useAboveMaxColor = 0
    p3.aboveMaxColor = (0, 0, 0, 255)
    p3.colorTableName = "_yellow"
    p3.invertColorTable = 1
    p3.opacityType = p3.Constant  # ColorTable, FullyOpaque, Constant, Ramp, VariableRange
    p3.opacity = 0
    SetPlotOptions(p3)

    SetActivePlots(4)
    p4 = PseudocolorAttributes()
    p4.minFlag = 1
    p4.min = 8
    p4.useBelowMinColor = 0
    p4.belowMinColor = (0, 0, 0, 255)
    p4.maxFlag = 1
    p4.max = 8.1
    p4.useAboveMaxColor = 1
    p4.aboveMaxColor = (0, 0, 0, 0)
    p4.colorTableName = "PuRd"
    p4.invertColorTable = 0
    p4.opacityType = p4.Ramp  # ColorTable, FullyOpaque, Constant, Ramp, VariableRange
    p4.opacity = 0
    SetPlotOptions(p4)
    
    SetActivePlots(0)
    
    # Begin spontaneous state
    View3DAtts = View3DAttributes()
    View3DAtts.viewNormal = (0, 0, 1)
    View3DAtts.focus = (-19, 65, .5)
    View3DAtts.viewUp = (0, 1, 0)
    View3DAtts.viewAngle = 30
    View3DAtts.parallelScale = 6
    View3DAtts.nearPlane = -11.5
    View3DAtts.farPlane = 11.5
    View3DAtts.imagePan = (0, 0)
    View3DAtts.imageZoom = ZOOM
    View3DAtts.perspective = 1
    View3DAtts.eyeAngle = 2
    View3DAtts.centerOfRotationSet = 0
    View3DAtts.centerOfRotation = (0, 0, 0)
    View3DAtts.axis3DScaleFlag = 0
    View3DAtts.axis3DScales = (1, 1, 1)
    View3DAtts.shear = (0, 0, 1)
    View3DAtts.windowValid = 1
    SetView3D(View3DAtts)
    # End spontaneous state

def topo(capture):

    SetActivePlots(0)
    p0 = PseudocolorAttributes()
    p0.minFlag = 1
    p0.maxFlag = 0
    p0.min = 1.1
    p0.useBelowMinColor = 1
    p0.belowMinColor = (0, 0, 0, 255)
    p0.colorTableName = "_black"
    p0.invertColorTable = 0
    p0.opacityType = p0.Constant  # ColorTable, FullyOpaque, Constant, Ramp, VariableRange
    p0.opacity = 0
    SetPlotOptions(p0)

    SetActivePlots((0, 2))
    SetActivePlots(2)
    SetActivePlots(2)
    SetActivePlots(2)
    HideActivePlots()

    IsosurfaceAtts = IsosurfaceAttributes()
    IsosurfaceAtts.contourNLevels = 20
    IsosurfaceAtts.contourValue = (10,)
    IsosurfaceAtts.contourPercent = ()
    IsosurfaceAtts.contourMethod = IsosurfaceAtts.Value  # Level, Value, Percent
    IsosurfaceAtts.minFlag = 0
    IsosurfaceAtts.min = 0
    IsosurfaceAtts.maxFlag = 0
    IsosurfaceAtts.max = 1
    IsosurfaceAtts.scaling = IsosurfaceAtts.Log  # Linear, Log
    IsosurfaceAtts.variable = "height"
    SetOperatorOptions(IsosurfaceAtts, 2, 0)

    printScreen(capture, 15)

    contour = 0
    contourSet = (10,)
    for i in range(13):

        contour += 150
        temp = (contourSet, (contour,))
        contourSet = sum(temp, ())
        IsosurfaceAtts.contourValue = contourSet
        SetOperatorOptions(IsosurfaceAtts, 2, 0)
        
        printScreen(capture, 15)

    return contourSet


################################################################

def untopo(contourSet, capture):

    SetActivePlots(0)
    PseudocolorAtts = PseudocolorAttributes()
    PseudocolorAtts.maxFlag = 0
    PseudocolorAtts.minFlag = 1
    PseudocolorAtts.min = 1.1
    PseudocolorAtts.useBelowMinColor = 1
    PseudocolorAtts.belowMinColor = (0, 0, 0, 255)
    PseudocolorAtts.colorTableName = "_black"
    PseudocolorAtts.invertColorTable = 0
    PseudocolorAtts.opacityType = PseudocolorAtts.FullyOpaque  # ColorTable, FullyOpaque, Constant, Ramp, VariableRange
    SetPlotOptions(PseudocolorAtts)

    SetActivePlots((0, 2))
    SetActivePlots(2)

    printScreen(capture, 2)

    IsosurfaceAtts = IsosurfaceAttributes()
    IsosurfaceAtts.contourNLevels = 14
    IsosurfaceAtts.contourValue = contourSet
    IsosurfaceAtts.contourPercent = ()
    IsosurfaceAtts.contourMethod = IsosurfaceAtts.Value  # Level, Value, Percent
    IsosurfaceAtts.minFlag = 0
    IsosurfaceAtts.min = 0
    IsosurfaceAtts.maxFlag = 0
    IsosurfaceAtts.max = 1
    IsosurfaceAtts.scaling = IsosurfaceAtts.Log  # Linear, Log
    IsosurfaceAtts.variable = "height"
    SetOperatorOptions(IsosurfaceAtts, 2, 0)

    for i in range(13):
        contourSet = contourSet[:-1]
        #print(contourSet)
        IsosurfaceAtts.contourValue = contourSet
        #print(IsosurfaceAtts.contourValue)
        SetOperatorOptions(IsosurfaceAtts, 2, 0)

        printScreen(capture, 10)

    HideActivePlots()

    printScreen(capture, 2)

################################################################

def rotate(capture):
    # Begin spontaneous state
    View3DAtts = View3DAttributes()    
    View3DAtts.viewNormal = (0, 0, 1)
    View3DAtts.focus = (-19, 65, .5)
    View3DAtts.viewUp = (0, 1, 0)
    View3DAtts.viewAngle = 30
    View3DAtts.parallelScale = 6
    View3DAtts.nearPlane = -11.5
    View3DAtts.farPlane = 11.5
    View3DAtts.imagePan = (0, 0)
    View3DAtts.imageZoom = ZOOM
    View3DAtts.perspective = 1
    View3DAtts.eyeAngle = 2
    View3DAtts.centerOfRotationSet = 0
    View3DAtts.centerOfRotation = (0, 0, 0)
    View3DAtts.axis3DScaleFlag = 0
    View3DAtts.axis3DScales = (1, 1, 1)
    View3DAtts.shear = (0, 0, 1)
    View3DAtts.windowValid = 1
    SetView3D(View3DAtts)
    # End spontaneous state

    printScreen(capture, 2)

    y = 0
    for i in range(50):
        y -= 0.025

        # Begin spontaneous state  
        View3DAtts.viewNormal = (0, y, 1)
        SetView3D(View3DAtts)
        # End spontaneous state

        printScreen(capture, 1)

    View3DAtts.viewNormal = (0, -1.25, 1)
    SetView3D(View3DAtts)

################################################################

def fadeInBase(capture):
    SetActivePlots(0)
    #HideActivePlots()

    PseudocolorAtts = PseudocolorAttributes()
    PseudocolorAtts.opacityType = PseudocolorAtts.Constant  # ColorTable, FullyOpaque, Constant, Ramp, VariableRange 
    PseudocolorAtts.opacity = 0.0
    PseudocolorAtts.minFlag = 1
    PseudocolorAtts.min = 1.1
    PseudocolorAtts.maxFlag = 0
    PseudocolorAtts.useBelowMinColor = 1
    PseudocolorAtts.belowMinColor = (0, 0, 0, 255)
    PseudocolorAtts.colorTableName = "_black"
    PseudocolorAtts.invertColorTable = 0
    SetPlotOptions(PseudocolorAtts)
    print(PseudocolorAtts.opacity)

    opac = 0.0
    #for i in range(199):
        #opac += .005
    for i in range(9):
        opac += .1
        #PseudocolorAtts = PseudocolorAttributes()
        PseudocolorAtts.opacity = opac
        print(PseudocolorAtts.opacity)
        SetPlotOptions(PseudocolorAtts)

        printScreen(capture, 1)


    PseudocolorAtts.maxFlag = 0
    PseudocolorAtts.minFlag = 1
    PseudocolorAtts.min = 1.1
    PseudocolorAtts.useBelowMinColor = 1
    PseudocolorAtts.belowMinColor = (0, 0, 0, 255)
    PseudocolorAtts.colorTableName = "_black"
    PseudocolorAtts.invertColorTable = 0
    PseudocolorAtts.opacityType = PseudocolorAtts.FullyOpaque  # ColorTable, FullyOpaque, Constant, Ramp, VariableRange
    SetPlotOptions(PseudocolorAtts)
    
################################################################

def zoomOut(capture):
    global ZOOM

    View3DAtts = View3DAttributes()
    View3DAtts.viewNormal = (0, -1.25, 1)
    View3DAtts.focus = (-19, 65, .5)
    View3DAtts.viewUp = (0, 1, 0)
    View3DAtts.viewAngle = 30
    View3DAtts.parallelScale = 6
    View3DAtts.nearPlane = -11.5
    View3DAtts.farPlane = 11.5
    View3DAtts.imagePan = (0, 0)
    View3DAtts.imageZoom = ZOOM
    View3DAtts.perspective = 1
    View3DAtts.eyeAngle = 2
    View3DAtts.centerOfRotationSet = 0
    View3DAtts.centerOfRotation = (0, 0, 0)
    View3DAtts.axis3DScaleFlag = 0
    View3DAtts.axis3DScales = (1, 1, 1)
    View3DAtts.shear = (0, 0, 1)
    View3DAtts.windowValid = 1
    SetView3D(View3DAtts)

    for i in range(125):
        ZOOM -= 0.01
        View3DAtts.imageZoom = ZOOM
        SetView3D(View3DAtts)
        
        printScreen(capture, 1)

    SetActivePlots(0)
    time.sleep(1)
    p0 = PseudocolorAttributes() 
    p0.opacity = 0.99
    p0.opacityType = p0.FullyOpaque  # ColorTable, FullyOpaque, Constant, Ramp, VariableRange
    p0.minFlag = 1
    p0.min = 1.1
    p0.maxFlag = 0
    p0.useBelowMinColor = 1
    p0.belowMinColor = (0, 0, 0, 255)
    p0.colorTableName = "_black"
    p0.invertColorTable = 0
    SetPlotOptions(p0)

################################################################

def fadeInLayers(capture):
	
    SetActivePlots(1)
    time.sleep(1)
    p1 = PseudocolorAttributes()   
    p1.opacityType = p1.Constant  # ColorTable, FullyOpaque, Constant, Ramp, VariableRange 
    p1.opacity = 0.0
    p1.colorTableName = "_blue"
    p1.maxFlag = 0
    p1.minFlag = 0
    SetPlotOptions(p1)

    SetActivePlots(3)
    time.sleep(1)
    p3 = PseudocolorAttributes() 
    p3.opacityType = p3.Constant  # ColorTable, FullyOpaque, Constant, Ramp, VariableRange    
    p3.opacity = 0.0
    p3.colorTableName = "_yellow"
    p3.maxFlag = 0
    p3.minFlag = 0
    SetPlotOptions(p3)

    SetActivePlots(4)
    time.sleep(1)
    p4 = PseudocolorAttributes()  
    p4.opacityType = p4.Ramp  # ColorTable, FullyOpaque, Constant, Ramp, VariableRange   
    #p4.opacity = 0.0
    p4.minFlag = 1
    p4.min = 8
    p4.useBelowMinColor = 0
    p4.belowMinColor = (0, 0, 0, 255)
    p4.maxFlag = 1
    p4.max = 8.1
    p4.useAboveMaxColor = 1
    p4.aboveMaxColor = (0, 0, 0, 0)
    p4.colorTableName = "RdPu"
    SetPlotOptions(p4)

    printScreen(capture, 1)

    counter = 0.0
    for i in range(75):
        counter += .0125

        SetActivePlots(1)
        time.sleep(1)   
        p1.opacityType = p1.Constant  # ColorTable, FullyOpaque, Constant, Ramp, VariableRange 
        p1.opacity = counter
        p1.colorTableName = "_blue"
        SetPlotOptions(p1)

        SetActivePlots(3)
        time.sleep(1)   
        p3.opacityType = p3.Constant  # ColorTable, FullyOpaque, Constant, Ramp, VariableRange 
        p3.opacity = counter / 1.5
        p3.colorTableName = "_yellow"
        SetPlotOptions(p3)

        SetActivePlots(4)
        time.sleep(1)   
        p4.opacityType = p4.Ramp  # ColorTable, FullyOpaque, Constant, Ramp, VariableRange 
        #p4.opacity = counter
        p4.colorTableName = "PuRd"
        # 153, 51, 102  
        p4.useBelowMinColor = 0
        p4.aboveMaxColor = (i * 2, i * 2 / 3, i + 25, 255)
        SetPlotOptions(p4)

        printScreen(capture, 2)

    SetActivePlots(4)  
    p4.opacity = counter
    p4.colorTableName = "PuRd"
    p4.opacityType = p4.Ramp  # ColorTable, FullyOpaque, Constant, Ramp, VariableRange
    #p4.aboveMaxColor = (128, 0, 128, 255)
    SetPlotOptions(p4)

    printScreen(capture, 2)


################################################################

def stackAndZoom(capture):
    global ZOOM

    View3DAtts = View3DAttributes()
    View3DAtts.viewNormal = (0, -1.25, 1)
    View3DAtts.focus = (-19, 65, 0.5)
    View3DAtts.viewUp = (0, 1, 0)
    View3DAtts.viewAngle = 30
    View3DAtts.parallelScale = 6
    View3DAtts.nearPlane = -11.5
    View3DAtts.farPlane = 11.5
    View3DAtts.imagePan = (0, 0)
    View3DAtts.imageZoom = ZOOM
    View3DAtts.perspective = 1
    View3DAtts.eyeAngle = 2
    View3DAtts.centerOfRotationSet = 0
    View3DAtts.centerOfRotation = (0, 0, 0)
    View3DAtts.axis3DScaleFlag = 0
    View3DAtts.axis3DScales = (1, 1, 1)
    View3DAtts.shear = (0, 0, 1)
    View3DAtts.windowValid = 1
    SetView3D(View3DAtts)

    SetActivePlots(1)
    time.sleep(1)
    p1 = PseudocolorAttributes()   
    p1.opacityType = p1.Constant  # ColorTable, FullyOpaque, Constant, Ramp, VariableRange 
    p1.opacity = 0.93
    p1.colorTableName = "_blue"
    p1.maxFlag = 0
    p1.minFlag = 0
    SetPlotOptions(p1)

    SetActivePlots(3)
    time.sleep(1)
    p3 = PseudocolorAttributes() 
    p3.opacityType = p3.Constant  # ColorTable, FullyOpaque, Constant, Ramp, VariableRange    
    p3.opacity = 0.62
    p3.colorTableName = "_yellow"
    p3.maxFlag = 0
    p3.minFlag = 0
    SetPlotOptions(p3)

    SetActivePlots(4)
    time.sleep(1)
    p4 = PseudocolorAttributes()  
    p4.opacityType = p4.Ramp  # ColorTable, FullyOpaque, Constant, Ramp, VariableRange   
    p4.opacity = 0.93
    p4.maxFlag = 1
    p4.max = 8.1
    p4.useAboveMaxColor = 1
    p4.aboveMaxColor = (74 * 2, 74 * 2 / 3, 74 + 25, 255)
    p4.useBelowMinColor = 0
    p4.colorTableName = "RdPu"
    SetPlotOptions(p4)

    elevs = [3, 6, 9]

    SetActivePlots(1)
    t1 = TransformAttributes()
    t1.translateZ = elevs[0]
    t1.scaleZ = 0.05
    SetOperatorOptions(t1, 1, 0)
    time.sleep(1)

    SetActivePlots(3)
    t3 = TransformAttributes()
    t3.translateZ = elevs[1]
    t3.scaleZ = 0.035
    SetOperatorOptions(t3, 1, 0)
    time.sleep(1)

    SetActivePlots(4)
    t4 = TransformAttributes()
    t4.translateZ = elevs[2]
    t4.scaleZ = 0.05
    SetOperatorOptions(t4, 1, 0)
    time.sleep(1)

    #elevsDelta = [0.04, 0.08, 0.12]
    #for i in range(75):
    #elevsDelta = [0.02, 0.04, 0.06]
    #for i in range(150):
    elevsDelta = [0.04, 0.08, 0.12]
    for i in range(75):
        print("\t\t" + str(i))
    
   
        SetActivePlots(1)
        elevs[0] -= elevsDelta[0]
        t1.translateZ = elevs[0]
        t1.scaleZ = 0.05
        SetOperatorOptions(t1, 1, 0)

        SetActivePlots(3)
        elevs[1] -= elevsDelta[1]
        t3.translateZ = elevs[1]
        t3.scaleZ = 0.035
        SetOperatorOptions(t3, 1, 0)

        SetActivePlots(4)
        elevs[2] -= elevsDelta[2]
        t4.translateZ = elevs[2]
        t4.scaleZ = 0.05
        #p4.opacityType = PseudocolorAtts.Ramp  # ColorTable, FullyOpaque, Constant, Ramp, VariableRange
        SetOperatorOptions(t4, 1, 0)

        View3DAtts.viewNormal = (0, -1.25, 1)
        View3DAtts.focus = (-19, 65, 0.5)
        ZOOM += 0.016666
        View3DAtts.imageZoom = ZOOM
        SetView3D(View3DAtts)

        printScreen(capture, 1)
    

################################################################

def stackLayers(capture):
    global ZOOM

    View3DAtts = View3DAttributes()
    View3DAtts.viewNormal = (0, -1.25, 1)
    View3DAtts.focus = (-19, 65, 0.5)
    View3DAtts.viewUp = (0, 1, 0)
    View3DAtts.viewAngle = 30
    View3DAtts.parallelScale = 6
    View3DAtts.nearPlane = -11.5
    View3DAtts.farPlane = 11.5
    View3DAtts.imagePan = (0, 0)
    View3DAtts.imageZoom = ZOOM
    View3DAtts.perspective = 1
    View3DAtts.eyeAngle = 2
    View3DAtts.centerOfRotationSet = 0
    View3DAtts.centerOfRotation = (0, 0, 0)
    View3DAtts.axis3DScaleFlag = 0
    View3DAtts.axis3DScales = (1, 1, 1)
    View3DAtts.shear = (0, 0, 1)
    View3DAtts.windowValid = 1
    SetView3D(View3DAtts)

    SetActivePlots(1)
    time.sleep(1)
    p1 = PseudocolorAttributes()   
    p1.opacityType = p1.Constant  # ColorTable, FullyOpaque, Constant, Ramp, VariableRange 
    p1.opacity = 0.93
    p1.colorTableName = "_blue"
    p1.maxFlag = 0
    p1.minFlag = 0
    SetPlotOptions(p1)

    SetActivePlots(3)
    time.sleep(1)
    p3 = PseudocolorAttributes() 
    p3.opacityType = p3.Constant  # ColorTable, FullyOpaque, Constant, Ramp, VariableRange    
    p3.opacity = 0.62
    p3.colorTableName = "_yellow"
    p3.maxFlag = 0
    p3.minFlag = 0
    SetPlotOptions(p3)

    SetActivePlots(4)
    time.sleep(1)
    p4 = PseudocolorAttributes()  
    p4.opacityType = p4.Ramp  # ColorTable, FullyOpaque, Constant, Ramp, VariableRange   
    p4.opacity = 0.93
    p4.maxFlag = 1
    p4.max = 8.1
    p4.useAboveMaxColor = 1
    p4.aboveMaxColor = (74 * 2, 74 * 2 / 3, 74 + 25, 255)
    p4.useBelowMinColor = 0
    p4.colorTableName = "RdPu"
    SetPlotOptions(p4)

    elevs = [3, 6, 9]

    SetActivePlots(1)
    t1 = TransformAttributes()
    t1.translateZ = elevs[0]
    t1.scaleZ = 0.05
    SetOperatorOptions(t1, 1, 0)
    time.sleep(1)

    SetActivePlots(3)
    t3 = TransformAttributes()
    t3.translateZ = elevs[1]
    t3.scaleZ = 0.035
    SetOperatorOptions(t3, 1, 0)
    time.sleep(1)

    SetActivePlots(4)
    t4 = TransformAttributes()
    t4.translateZ = elevs[2]
    t4.scaleZ = 0.05
    SetOperatorOptions(t4, 1, 0)
    time.sleep(1)

    #elevsDelta = [0.04, 0.08, 0.12]
    #for i in range(75):
    #elevsDelta = [0.02, 0.04, 0.06]
    #for i in range(150):
    elevsDelta = [0.04, 0.08, 0.12]
    for i in range(75):
        print("\t\t" + str(i))
    
   
        SetActivePlots(1)
        elevs[0] -= elevsDelta[0]
        t1.translateZ = elevs[0]
        t1.scaleZ = 0.05
        SetOperatorOptions(t1, 1, 0)

        SetActivePlots(3)
        elevs[1] -= elevsDelta[1]
        t3.translateZ = elevs[1]
        t3.scaleZ = 0.035
        SetOperatorOptions(t3, 1, 0)

        SetActivePlots(4)
        elevs[2] -= elevsDelta[2]
        t4.translateZ = elevs[2]
        t4.scaleZ = 0.05
        #p4.opacityType = PseudocolorAtts.Ramp  # ColorTable, FullyOpaque, Constant, Ramp, VariableRange
        SetOperatorOptions(t4, 1, 0)

        View3DAtts.viewNormal = (0, -1.25, 1)
        View3DAtts.focus = (-19, 65, 0.5)
        View3DAtts.imageZoom = ZOOM
        SetView3D(View3DAtts)

        printScreen(capture, 1)
    

################################################################

def zoomIn(capture):
    global ZOOM

    View3DAtts = View3DAttributes()
    View3DAtts.viewNormal = (0, -1.25, 1)
    View3DAtts.focus = (-19, 65, .5)
    View3DAtts.imageZoom = ZOOM
    SetView3D(View3DAtts)

    for i in range(125):
        ZOOM += 0.01
        View3DAtts.imageZoom = ZOOM
        SetView3D(View3DAtts)
        
        printScreen(capture, 1)

################################################################

def rotate2(capture):
    # Begin spontaneous state
    View3DAtts = View3DAttributes()    
    # End spontaneous state

    printScreen(capture, 1)

    y = 0
    for i in range(50):
        y -= 0.025

        # Begin spontaneous state  
        View3DAtts.viewNormal = (0, y, 1)
        SetView3D(View3DAtts)
        # End spontaneous state

        printScreen(capture, 1)


#
# Main
#
################################################################


# Layers:
# 0 on
# 2 off
capture = True

pause("setup")
setup(False)

pause("topo")
contours = topo(False)
pause("rotate")
rotate(False)
pause("fadeInBase")
fadeInBase(False) 

pause("untopo")
untopo(contours, False) 
pause("zoomOut") 
zoomOut(False) #

# labels (manual, as not yet supported by VisIt)
pause("Labels: fade in labels manually") 

pause("fadeInLayers")
fadeInLayers(False)

#pause("stackAndZoom")
#stackAndZoom(capture)

pause("stackLayers")
stackLayers(False)
pause("zoomIn")
zoomIn(False)