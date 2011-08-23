from PyQt4 import QtGui, QtDesigner
from labelListView import *
from labelListModel import *

class PyLabelListViewPlugin(QtDesigner.QPyDesignerCustomWidgetPlugin):

    def __init__(self, parent = None):
    
        QtDesigner.QPyDesignerCustomWidgetPlugin.__init__(self)

        self.initialized = False
        
    def initialize(self, core):

        if self.initialized:
            return

        self.initialized = True

    def isInitialized(self):

        return self.initialized
    
    def createWidget(self, parent):
        red   = QColor(255,0,0)
        green = QColor(0,255,0)
        blue  = QColor(0,0,255)
        model = LabelListModel([Label("Label 1", red), Label("Label 2", green), Label("Label 3", blue)])
        
        a=LabelListView(parent)
        a.setModel(model)
        
        return a
    
    def name(self):
        return "LabelListView"

    def group(self):
        return "ilastik widgets"
    
    def isContainer(self):
        return False
    
    def domXml(self):
        return (
               '<widget class="LabelListView" name=\"labelListView\">\n'
               " <property name=\"toolTip\" >\n"
               "  <string>The current time</string>\n"
               " </property>\n"
               " <property name=\"whatsThis\" >\n"
               "  <string>The analog clock widget displays "
               "the current time.</string>\n"
               " </property>\n"
               "</widget>\n"
               )
    
    def includeFile(self):
        return "labelListView"
    
    