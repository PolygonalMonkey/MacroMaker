# MayaUI_Test
import sys
import maya.cmds as mc
import maya.mel as mm
import pymel.core as pm


CALLBACK_ID = None

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
        print 'Record button pressed.'
        fileHistDir = "X:/Documents/SchoolWork/LMU/Fall2016/PipelineCS/FinalTools/history.txt"
        userHist = mc.scriptEditorInfo(historyFilename = fileHistDir, writeHistory = True)

    def pExecuteCallback( *pArgs ):
        mc.scriptEditorInfo(writeHistory = False)
        print 'Execute button pressed.'

    def pClearCallback( *pArgs ):
        print 'Clear button pressed.'
        outputField(clear=True)

    mc.separator(h=10, style="none")

    mc.rowLayout(numberOfColumns=3)    
    mc.button(label= 'Record', width=195, backgroundColor=(50, 0, 0), command=pRecordCallback)
    mc.button(label= 'Execute', width=195, backgroundColor=(0, 50, 0), command=pExecuteCallback)
    mc.setParent("..")
    
    mc.separator(h=10, style="none")
    
    mc.text(label='SELECTED STEPS')
    
    output = 'test test test'
    def pUpdateOutputField( *pArgs ):
        #outputField = mc.cmdScrollFieldExecuter(width= 395, height=400, showLineNumbers=True, sw=True, text= output)
        outputField = mc.cmdScrollFieldReporter(width= 395, height=400, echoAllCommands=True)
    pUpdateOutputField()
 
    mc.separator(h=10, style="none")
    
    #mc.button(label= 'Execute', width=395, backgroundColor=(0, 50, 0), command=pExecuteCallback)
    mc.button(label= 'Clear', width=395, command=pClearCallback)
    
    #mc.textScrollList(append=[''])
    mc.scriptEditorInfo(input="")
    
    mc.separator(h=10, style='none')
    
    mc.showWindow()

createUI('MacroMaker')
     