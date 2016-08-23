# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_HubaoTestToolkit(object):
    def setupUi(self, HubaoTestToolkit):
        HubaoTestToolkit.setObjectName(_fromUtf8("HubaoTestToolkit"))
        HubaoTestToolkit.resize(890, 723)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        HubaoTestToolkit.setFont(font)
        self.Display_panel = QtGui.QTextBrowser(HubaoTestToolkit)
        self.Display_panel.setGeometry(QtCore.QRect(500, 10, 381, 701))
        self.Display_panel.setObjectName(_fromUtf8("Display_panel"))
        self.Condition = QtGui.QComboBox(HubaoTestToolkit)
        self.Condition.setGeometry(QtCore.QRect(40, 10, 101, 21))
        self.Condition.setObjectName(_fromUtf8("Condition"))
        self.Condition.addItem(_fromUtf8(""))
        self.Condition.addItem(_fromUtf8(""))
        self.Condition.addItem(_fromUtf8(""))
        self.Condition.addItem(_fromUtf8(""))
        self.Label = QtGui.QLabel(HubaoTestToolkit)
        self.Label.setGeometry(QtCore.QRect(10, 10, 21, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.Label.setFont(font)
        self.Label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Label.setAcceptDrops(True)
        self.Label.setObjectName(_fromUtf8("Label"))
        self.Query = QtGui.QPushButton(HubaoTestToolkit)
        self.Query.setGeometry(QtCore.QRect(420, 10, 75, 23))
        self.Query.setObjectName(_fromUtf8("Query"))
        self.Request = QtGui.QPushButton(HubaoTestToolkit)
        self.Request.setGeometry(QtCore.QRect(10, 380, 71, 23))
        self.Request.setObjectName(_fromUtf8("Request"))
        self.Condition_value = QtGui.QLineEdit(HubaoTestToolkit)
        self.Condition_value.setGeometry(QtCore.QRect(150, 10, 261, 21))
        self.Condition_value.setObjectName(_fromUtf8("Condition_value"))
        self.Api_list = QtGui.QTableWidget(HubaoTestToolkit)
        self.Api_list.setGeometry(QtCore.QRect(10, 90, 481, 281))
        self.Api_list.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.Api_list.setObjectName(_fromUtf8("Api_list"))
        self.Api_list.setColumnCount(2)
        self.Api_list.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.Api_list.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.Api_list.setHorizontalHeaderItem(1, item)
        self.Api_list.horizontalHeader().setVisible(True)
        self.Api_list.horizontalHeader().setCascadingSectionResizes(False)
        self.Api_list.horizontalHeader().setDefaultSectionSize(200)
        self.Api_list.horizontalHeader().setStretchLastSection(True)
        self.Category = QtGui.QComboBox(HubaoTestToolkit)
        self.Category.setGeometry(QtCore.QRect(10, 60, 201, 22))
        self.Category.setObjectName(_fromUtf8("Category"))
        self.Category.addItem(_fromUtf8(""))
        self.Category.addItem(_fromUtf8(""))
        self.Category.addItem(_fromUtf8(""))
        self.Category.addItem(_fromUtf8(""))
        self.Category.addItem(_fromUtf8(""))
        self.Category.addItem(_fromUtf8(""))
        self.Category.addItem(_fromUtf8(""))
        self.Category.addItem(_fromUtf8(""))
        self.Category.addItem(_fromUtf8(""))
        self.Add_api = QtGui.QPushButton(HubaoTestToolkit)
        self.Add_api.setGeometry(QtCore.QRect(410, 380, 81, 23))
        self.Add_api.setObjectName(_fromUtf8("Add_api"))
        self.Add_category = QtGui.QPushButton(HubaoTestToolkit)
        self.Add_category.setGeometry(QtCore.QRect(220, 60, 81, 23))
        self.Add_category.setObjectName(_fromUtf8("Add_category"))
        self.Remove_api = QtGui.QPushButton(HubaoTestToolkit)
        self.Remove_api.setGeometry(QtCore.QRect(410, 410, 81, 23))
        self.Remove_api.setObjectName(_fromUtf8("Remove_api"))

        self.retranslateUi(HubaoTestToolkit)
        QtCore.QMetaObject.connectSlotsByName(HubaoTestToolkit)

    def retranslateUi(self, HubaoTestToolkit):
        HubaoTestToolkit.setWindowTitle(_translate("HubaoTestToolkit", "HubaoTestToolkit", None))
        self.Condition.setItemText(0, _translate("HubaoTestToolkit", "user_id", None))
        self.Condition.setItemText(1, _translate("HubaoTestToolkit", "user_id (int)", None))
        self.Condition.setItemText(2, _translate("HubaoTestToolkit", "room_id", None))
        self.Condition.setItemText(3, _translate("HubaoTestToolkit", "nickname", None))
        self.Label.setText(_translate("HubaoTestToolkit", "KEY", None))
        self.Query.setText(_translate("HubaoTestToolkit", "Query", None))
        self.Request.setText(_translate("HubaoTestToolkit", "Request", None))
        item = self.Api_list.horizontalHeaderItem(0)
        item.setText(_translate("HubaoTestToolkit", "Interface", None))
        item = self.Api_list.horizontalHeaderItem(1)
        item.setText(_translate("HubaoTestToolkit", "URL", None))
        self.Category.setItemText(0, _translate("HubaoTestToolkit", "Common", None))
        self.Category.setItemText(1, _translate("HubaoTestToolkit", "Compere", None))
        self.Category.setItemText(2, _translate("HubaoTestToolkit", "Content", None))
        self.Category.setItemText(3, _translate("HubaoTestToolkit", "Mate", None))
        self.Category.setItemText(4, _translate("HubaoTestToolkit", "Payment", None))
        self.Category.setItemText(5, _translate("HubaoTestToolkit", "Property", None))
        self.Category.setItemText(6, _translate("HubaoTestToolkit", "Room", None))
        self.Category.setItemText(7, _translate("HubaoTestToolkit", "Support", None))
        self.Category.setItemText(8, _translate("HubaoTestToolkit", "User", None))
        self.Add_api.setText(_translate("HubaoTestToolkit", "Add", None))
        self.Add_category.setText(_translate("HubaoTestToolkit", "Add", None))
        self.Remove_api.setText(_translate("HubaoTestToolkit", "Remove", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    HubaoTestToolkit = QtGui.QWidget()
    ui = Ui_HubaoTestToolkit()
    ui.setupUi(HubaoTestToolkit)
    HubaoTestToolkit.show()
    sys.exit(app.exec_())

