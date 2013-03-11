# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'quickfind.ui'
#
# Created: Mon Mar 11 21:05:49 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_QuickFind(object):
    def setupUi(self, QuickFind):
        QuickFind.setObjectName(_fromUtf8("QuickFind"))
        QuickFind.resize(610, 500)
        self.verticalLayoutWidget = QtGui.QWidget(QuickFind)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 441, 51))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.queryBox = QtGui.QTextEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.queryBox.setFont(font)
        self.queryBox.setObjectName(_fromUtf8("queryBox"))
        self.verticalLayout.addWidget(self.queryBox)
        self.verticalLayoutWidget_2 = QtGui.QWidget(QuickFind)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(460, 10, 141, 51))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.queryButton = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.queryButton.setMinimumSize(QtCore.QSize(139, 23))
        self.queryButton.setMaximumSize(QtCore.QSize(135, 75))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.queryButton.setFont(font)
        self.queryButton.setObjectName(_fromUtf8("queryButton"))
        self.verticalLayout_2.addWidget(self.queryButton)
        self.verticalLayoutWidget_3 = QtGui.QWidget(QuickFind)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 70, 591, 421))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.exampleBrowser = QtGui.QTextBrowser(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.exampleBrowser.setFont(font)
        self.exampleBrowser.setObjectName(_fromUtf8("exampleBrowser"))
        self.verticalLayout_3.addWidget(self.exampleBrowser)

        self.retranslateUi(QuickFind)
        QtCore.QMetaObject.connectSlotsByName(QuickFind)

    def retranslateUi(self, QuickFind):
        QuickFind.setWindowTitle(_translate("QuickFind", "例句速查", None))
        self.queryButton.setText(_translate("QuickFind", "查询", None))

