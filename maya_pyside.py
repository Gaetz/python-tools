""" 1

from PySide2 import QtCore
from PySide2 import QtWidgets
from shiboken2 import wrapInstance

import maya.OpenMayaUI as omui


class TestDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(TestDialog, self).__init__(parent)

d = TestDialog()
d.show()

"""

# window get behing maya main's window, so we want our dialog to become chil of the main window


""" 2

from PySide2 import QtCore
from PySide2 import QtWidgets
from shiboken2 import wrapInstance

import maya.OpenMayaUI as omui


def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)

class TestDialog(QtWidgets.QDialog):
    def __init__(self, parent=maya_main_window()):
        super(TestDialog, self).__init__(parent)
        self.setWindowTitle("Test Dialog")
        self.setMinimumWidth(200)
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)

d = TestDialog()
d.show()


"""

from PySide2 import QtCore
from PySide2 import QtWidgets
from shiboken2 import wrapInstance

import maya.OpenMayaUI as omui
import pymel.core as pm


def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)

def select_all():
    pm.select(pm.ls())


class TestDialog(QtWidgets.QDialog):
    def __init__(self, parent=maya_main_window()):
        super(TestDialog, self).__init__(parent)
        self.setWindowTitle("Test Dialog")
        self.setMinimumWidth(200)
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        self.create_widgets()
        self.create_layouts()

    def create_widgets(self):
        self.line_edit = QtWidgets.QLineEdit()
        self.check_box1 = QtWidgets.QCheckBox("CheckBox1")
        self.check_box2 = QtWidgets.QCheckBox("CheckBox2")
        self.button1 = QtWidgets.QPushButton("Button1")
        self.button2 = QtWidgets.QPushButton("Button2")
        self.button1.clicked.connect(select_all)     

    def create_layouts(self):
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addWidget(self.line_edit)
        main_layout.addWidget(self.check_box1)
        main_layout.addWidget(self.check_box2)
        main_layout.addWidget(self.button1)
        main_layout.addWidget(self.button2)



d = TestDialog()
d.show()



# Save to shelve to create a tool