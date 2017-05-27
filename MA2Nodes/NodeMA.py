import sys
from qtpy import QtGui, QtWidgets, QtCore
from PyQt4 import QtGui, QtCore
from PyQt4.Qt import QFileDialog

# Add the pyflowgraph module to the current environment if it does not already exist
import imp
try:
    imp.find_module('pyflowgraph')
    found = True
except ImportError:
    import os, sys
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "..")))

from pyflowgraph.graph_view import GraphView
from pyflowgraph.graph_view_widget import GraphViewWidget
from pyflowgraph.node import Node
from pyflowgraph.port import InputPort, OutputPort, IOPort


class Window(QtGui.QMainWindow):

    def __init__(self):
        # REG WINDOW
        super(Window, self).__init__()
        self.setGeometry(810, 415, 300, 250)
        self.setWindowTitle("NodeMA Tool")

        extractAction = QtGui.QAction("&Open File...", self)
        extractAction.setShortcut("Ctrl+O")

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)
        extractAction.triggered.connect(self.showOpenFileWin)

        self.intro()
 
    # REG WIN STUFF
    def intro(self):
        # openBtn = QtGui.QPushButton("Open Nodes Window", self)
        # openBtn.clicked.connect(self.showNodesWin)
        # openBtn.setGeometry(0, 20, 150, 30)
     
        # btn2 = QtGui.QPushButton("addNode", self)
        # btn2.clicked.connect(self.addNode)
        # btn2.setGeometry(0, 50, 150, 25)

        label = QtGui.QLabel(self)
        label.setGeometry(0,20, 300, 250)
        label.setWordWrap(True)
        # label.alignment(Qt.AlignHCenter(True))
        label.setText("""<b>Open any Maya.ascii file to view its assets in node form<\b>""")
        self.show()

    # SHOW OPEN FILE WINDOW //ALSO READ FILE
    def showOpenFileWin(self):
        fileDir = QFileDialog.getOpenFileName()
        myFile = open(fileDir, "r")

        with myFile:
            global fileContent
            fileContent= myFile.read()

        self.showNodesWin()
        self.addNode()

    # NODES WINDOW
    def showNodesWin(self): 
        nodeWin = GraphViewWidget()
        global graph
        graph = GraphView(parent=nodeWin)
        nodeWin.setGraphView(graph)
        nodeWin.show()
        # print "NodeWin Visible"

    def addNode(self):
        # NODE COLORS
        # text = 'Green = MESHES'
        node = Node(graph, "NODE COLOR ASSOCIATION")
        node.addPort(InputPort(node, graph, "GREEN = Meshes ", QtGui.QColor(243, 207, 139), 'MyDataX'))
        node.addPort(InputPort(node, graph, "PINK = Materials", QtGui.QColor(243, 207, 139), 'MyDataY'))
        node.addPort(InputPort(node, graph, "YELLOW = Cameras", QtGui.QColor(243, 207, 139), 'MyDataY'))
        node.addPort(InputPort(node, graph, "BLUE = SpotLights", QtGui.QColor(243, 207, 139), 'MyDataY'))
        node.setGraphPos(QtCore.QPointF(-250, 0 ))
        node.setColor(QtGui.QColor(200, 200, 200, 255))
        graph.addNode(node)


        text = fileContent.splitlines()
        lineList = [line.split() for line in text]
        
        myCamerasList = []
        myMaterialsList = []
        myMeshesList = []
        mySpotLightsList = []

        for line in lineList:
            # print line
            # GETS MESH NODES
            if line[0] == "createNode" and line[1] == "mesh":
                # print "My MESH Line"
                lineLength = len(line) - 1
                meshNodeName = line[lineLength]
                meshNodeNameBroken = meshNodeName.split("\"")
                meshNodeNameClean = meshNodeNameBroken[1]
                myMeshesList.append(meshNodeNameClean)

            # GETS MATERIAL NODES
            elif line[0] == "createNode" and line[1] == "lambert":
                # print "My MAT Line"
                lineLength = len(line) - 1
                matNodeName = line[lineLength]
                matNodeNameBroken = matNodeName.split("\"")
                matNodeNameClean = matNodeNameBroken[1]
                myMaterialsList.append(matNodeNameClean)
            
            # GETS CAMERA NODES
            elif line[0] == "createNode" and line[1] == "camera":
                # print "My MAT Line"
                lineLength = len(line) - 1
                matNodeName = line[lineLength]
                matNodeNameBroken = matNodeName.split("\"")
                cameraNodeNameClean = matNodeNameBroken[1]
                myCamerasList.append(cameraNodeNameClean)

            # GETS SPOTLIGHT NODES
            elif line[0] == "createNode" and line[1] == "spotLight":
                # print "My MAT Line"
                lineLength = len(line) - 1
                matNodeName = line[lineLength]
                matNodeNameBroken = matNodeName.split("\"")
                spotLightNodeNameClean = matNodeNameBroken[1]
                mySpotLightsList.append(spotLightNodeNameClean)

        # print myMeshesList

        x1 = len(myMeshesList)
        x2 = len(myMaterialsList)
        x3 = len(myCamerasList)
        x4 = len(mySpotLightsList)
        # print x

        # ADDIND NODE TYPES
        for meshNodeSpawn in range(x1):
            node = Node(graph, myMeshesList[meshNodeSpawn])
            node.addPort(InputPort(node, graph, 'In    ', QtGui.QColor(243, 207, 139), 'MyDataX'))
            node.addPort(OutputPort(node, graph, '    Out', QtGui.QColor(243, 207, 139), 'MyDataY'))
            node.setGraphPos(QtCore.QPointF(0, meshNodeSpawn * 80 ))
            node.setColor(QtGui.QColor(92, 204, 146, 255))
            graph.addNode(node)

        for materialNodeSpawn in range(x2):
            node = Node(graph, myMaterialsList[materialNodeSpawn])
            node.addPort(InputPort(node, graph, 'In    ', QtGui.QColor(243, 207, 139), 'MyDataX'))
            node.addPort(OutputPort(node, graph, '    Out', QtGui.QColor(243, 207, 139), 'MyDataY'))
            node.setGraphPos(QtCore.QPointF(150, materialNodeSpawn * 80 ))
            node.setColor(QtGui.QColor(215, 140, 255, 255))
            graph.addNode(node)

        for cameraNodeSpawn in range(x3):
            node = Node(graph, myCamerasList[cameraNodeSpawn])
            node.addPort(InputPort(node, graph, 'In    ', QtGui.QColor(243, 207, 139), 'MyDataX'))
            node.addPort(OutputPort(node, graph, '    Out', QtGui.QColor(243, 207, 139), 'MyDataY'))
            node.setGraphPos(QtCore.QPointF(300, cameraNodeSpawn * 80 ))
            node.setColor(QtGui.QColor(243, 207, 139))
            graph.addNode(node)

        for spotLightNodeSpawn in range(x4):
            node = Node(graph, mySpotLightsList[spotLightNodeSpawn])
            node.addPort(InputPort(node, graph, 'In    ', QtGui.QColor(243, 207, 139), 'MyDataX'))
            node.addPort(OutputPort(node, graph, '    Out', QtGui.QColor(243, 207, 139), 'MyDataY'))
            node.setGraphPos(QtCore.QPointF(450, spotLightNodeSpawn * 80 ))
            node.setColor(QtGui.QColor(79, 170, 204, 255))
            graph.addNode(node)


def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())
    
run()