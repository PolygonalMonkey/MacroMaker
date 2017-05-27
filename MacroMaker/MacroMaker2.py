# MayaUI_Test
import sys
import maya.cmds as mc
import maya.mel as mm
import pymel.core as pm

def createUI(pWindowTitle):
    
    windowID = 'myWindowID'
    
    if mc.window(windowID, exists=True):
        mc.deleteUI(windowID)
        
    mc.window(windowID, title=pWindowTitle, sizeable=True, resizeToFitChildren=True, width=200)
    
    
    # OPENING ANS SAVING WINDOWS
    def pOpenFileCallback(*pArgs):
        fileOutput = pm.fileDialog2(fileMode=1) #fileOutput[0]
        myFile = "X:/Documents/SchoolWork/LMU/Fall2016/PipelineCS/FinalTools/history.txt"
        #string $filePath = myFile;
        #$fileId = "`mm.fopen $filePath "r"`";  

    def pSaveFileCallback(*pArgs):
        pm.fileDialog2(fileMode=0)
    
    def pPastaCallback(*pArgs):
        mm.eval("sphere -radius 3;")
        
         
    mc.menuBarLayout('Meun')
    mc.menu('File')
    mc.menuItem('Open', command=pOpenFileCallback)
    mc.menuItem('Save As...', command=pSaveFileCallback)
    mc.menuItem('CloseMM')
    mc.menu('Edit')
    mc.menuItem('Copy')
    mc.menuItem('Pasta', command=pPastaCallback)

    mc.rowColumnLayout(numberOfColumns=1, columnWidth=(1,400), columnOffset=(1,'left', 3) )

    # MENUBAR LAYOUT
    def pRecordCallback( *pArgs ):
        print 'Recording...'
        fileHistDir = "X:/Documents/SchoolWork/LMU/Fall2016/PipelineCS/FinalTools/history.txt"
        userHist = mc.scriptEditorInfo(historyFilename = fileHistDir, writeHistory = True)

    def pClearCallback( *pArgs ):
        print 'Clear button pressed.'
        outputField(clear=True)

    def pStopCallback( *pArgs ):
        mc.scriptEditorInfo(writeHistory = False)
        print 'Stopped Recording.'


    mc.separator(h=10, style="none")

    mc.rowLayout(numberOfColumns=2)    
    mc.button(label= 'Record', width=195, backgroundColor=(1, 1, 0), command=pRecordCallback)
    # mc.button(label= 'CLEAR', width=195, backgroundColor=(1, 1, 0), command=pClearCallback)
    mc.button(label= 'STOP', width=195, backgroundColor=(1, 0, 0), command=pStopCallback)
    mc.setParent("..")
    
    # mc.text(label='SELECTED STEPS')
    
    # TABS
    form = mc.formLayout()
    tabs = mc.tabLayout(innerMarginWidth= 5, innerMarginHeight= 5)
    mc.formLayout( form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)) )
    
    clearValue = True
    child1 = mc.rowLayout(numberOfColumns=2)
    outputField = mc.cmdScrollFieldReporter(width= 395, height=400, clear=clearValue, echoAllCommands=False, suppressStackTrace=True)
    mc.setParent('..')

    child2 = mc.rowLayout(numberOfColumns=2)
    inputField = mc.cmdScrollFieldExecuter(width= 395, height=400, showLineNumbers=True)
    mc.setParent("..")
    
    mc.tabLayout( tabs, edit=True, tabLabel=((child1, 'Selected Steps'), (child2, 'Editor')) )
    mc.setParent("..")
    
    mc.separator(h=10, style="none")
    #mc.button(label= 'Execute', width=395, backgroundColor=(0, 50, 0), command=pExecuteCallback)
    #mc.button(label= 'Clear', width=395)
    
    #mc.textScrollList(append=[''])
    
    
    mc.showWindow()

createUI('MacroMaker')
     
     