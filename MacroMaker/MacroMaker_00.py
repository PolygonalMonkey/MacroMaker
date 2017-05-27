# __MakroMaker__
# PolygonalMonkey

import sys
import maya.cmds as mc
import maya.mel as mm

def createUI(pWindowTitle):
    
    windowID = 'myWindowID'
    
    if mc.window(windowID, exists=True):
        mc.deleteUI(windowID)
        
    mc.window(windowID, title=pWindowTitle, sizeable=True, resizeToFitChildren=True, width=200)
    
    # OPENING ANS SAVING WINDOWS
    def pOpenFileCallback(*pArgs):
        mc.cmdScrollFieldReporter("outputField", e = True, clear = True)
        fileOutput = mc.fileDialog2(fileMode=1)
        fileContent = fileOutput[0]
        
        mm.eval('string $filePath = "' + str(fileContent) + '"')
        mm.eval('$fileId = `fopen $filePath "r"`')
        mm.eval("string $data = `fread $fileId $data`")

        transferMELVar = maya.mel.eval("$temp=$data")
        print transferMELVar
        test = str(transferMELVar)
        #myFile = "E:/Users/candrad6/Desktop/FinalTools/TestFiles/history.txt"
        #string $filePath = myFile;
        #$fileId = "`mm.fopen $filePath "r"`";  

    def pSaveFileCallback(*pArgs):
        filePathDir = mc.fileDialog2(fileMode=0)
        print filePathDir[0]
        if saveAsFilePath == None:
            mc.error("Didn't select a file to open.")
        print saveAsFilePath
        
        output = mc.cmdScrollFieldReporter("outputField", q = True, t = True)
        
    def pPastaCallback(*pArgs):
        mm.eval("sphere -radius 3;")
        
         
    mc.menuBarLayout('Meun')
    mc.menu('File')
    mc.menuItem('Open', command=pOpenFileCallback)
    mc.menuItem('Save As...', command=pSaveFileCallback)



    mc.rowColumnLayout(numberOfColumns=1, columnWidth=(1,400), columnOffset=(1,'left', 3) )

    # MENUBAR LAYOUT
    def pRecordCallback( *pArgs ):
        print 'Recording...'
        fileHistDir = mc.fileDialog2(fileMode=0)
        savingDir = fileHistDir[0]
        userHist = mc.scriptEditorInfo(historyFilename = savingDir, writeHistory = True)

    def pClearCallback( *pArgs ):
        print 'Clear button pressed.'
        outputField(clear=True, enable=True)
   

    def pStopCallback( *pArgs ):
        print 'Stopped Recording.'
        mc.scriptEditorInfo(writeHistory = False)
        outputField(enable=False)
        
    def clearTF(*pArgs):
        mc.cmdScrollFieldReporter("outputField", e = True, clear = True)
        
    def pRunCallback(*pArgs):
        output = mc.cmdScrollFieldReporter("outputField", q = True, t = True)
        mm.eval(output)
        
    mc.separator(h=10, style="none")

    mc.rowLayout(numberOfColumns=2)    
    mc.button(label= 'RECORD', width=195, backgroundColor=(1, 0, 0), command=pRecordCallback)
    # mc.button(label= 'CLEAR', width=195, backgroundColor=(1, 1, 0), command=pClearCallback)
    mc.button(label= 'STOP', width=195, backgroundColor=(1, 0, 0), command=pStopCallback)
    
    mc.setParent("..")
    
    mc.rowLayout(numberOfColumns=2)   
    mc.button(label = 'CLEAR', width=195, backgroundColor=(1, 1, 0), command= clearTF)
    mc.button(label = 'RUN', width=195, backgroundColor=(0, 1, 0), command= pRunCallback)
    mc.setParent("..")
    
    # mc.text(label='SELECTED STEPS')
    
    # TABS
    form = mc.formLayout()
    tabs = mc.tabLayout(innerMarginWidth= 5, innerMarginHeight= 5)
    mc.formLayout( form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)) )
    
    clearValue = True
    child1 = mc.rowLayout(numberOfColumns=2)
    outputField = mc.cmdScrollFieldReporter("outputField", width= 395, height=400, clear=clearValue, echoAllCommands=False, suppressInfo=True, suppressStackTrace=True, suppressResults=True, enable=False)
    mc.setParent('..')

    child2 = mc.rowLayout(numberOfColumns=2)
    inputField = mc.cmdScrollFieldExecuter(width= 395, height=400, showLineNumbers=True)
    mc.setParent("..")
    
    mc.tabLayout( tabs, edit=True, tabLabel=((child1, 'Actions List'), (child2, 'Edit Actions')) )
    mc.setParent("..")
    
    mc.separator(h=10, style="none")
    #mc.button(label= 'Execute', width=395, backgroundColor=(0, 50, 0), command=pExecuteCallback)
    #mc.button(label= 'Clear', width=395)
    
    #mc.textScrollList(append=[''])
     
    mc.showWindow()

createUI('MacroMaker')