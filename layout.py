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
        HubaoTestToolkit.setWindowModality(QtCore.Qt.WindowModal)
        HubaoTestToolkit.resize(890, 751)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        HubaoTestToolkit.setFont(font)
        self.Display_panel = QtGui.QTextBrowser(HubaoTestToolkit)
        self.Display_panel.setGeometry(QtCore.QRect(500, 10, 381, 731))
        self.Display_panel.setObjectName(_fromUtf8("Display_panel"))
        self.Condition = QtGui.QComboBox(HubaoTestToolkit)
        self.Condition.setGeometry(QtCore.QRect(40, 10, 101, 21))
        self.Condition.setObjectName(_fromUtf8("Condition"))
        self.Label = QtGui.QLabel(HubaoTestToolkit)
        self.Label.setGeometry(QtCore.QRect(10, 10, 21, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.Label.setFont(font)
        self.Label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Label.setAcceptDrops(False)
        self.Label.setObjectName(_fromUtf8("Label"))
        self.Query = QtGui.QPushButton(HubaoTestToolkit)
        self.Query.setGeometry(QtCore.QRect(420, 10, 75, 23))
        self.Query.setObjectName(_fromUtf8("Query"))
        self.Request = QtGui.QPushButton(HubaoTestToolkit)
        self.Request.setGeometry(QtCore.QRect(410, 660, 81, 41))
        self.Request.setObjectName(_fromUtf8("Request"))
        self.Condition_value = QtGui.QLineEdit(HubaoTestToolkit)
        self.Condition_value.setGeometry(QtCore.QRect(150, 10, 261, 21))
        self.Condition_value.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Condition_value.setObjectName(_fromUtf8("Condition_value"))
        self.Api_list = QtGui.QTableWidget(HubaoTestToolkit)
        self.Api_list.setGeometry(QtCore.QRect(10, 100, 481, 281))
        self.Api_list.setLineWidth(1)
        self.Api_list.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.Api_list.setAutoScroll(True)
        self.Api_list.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.Api_list.setProperty("showDropIndicator", False)
        self.Api_list.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.Api_list.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerItem)
        self.Api_list.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.Api_list.setObjectName(_fromUtf8("Api_list"))
        self.Api_list.setColumnCount(2)
        self.Api_list.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.Api_list.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.Api_list.setHorizontalHeaderItem(1, item)
        self.Api_list.horizontalHeader().setVisible(True)
        self.Api_list.horizontalHeader().setCascadingSectionResizes(True)
        self.Api_list.horizontalHeader().setDefaultSectionSize(180)
        self.Api_list.horizontalHeader().setSortIndicatorShown(False)
        self.Api_list.horizontalHeader().setStretchLastSection(False)
        self.Api_list.verticalHeader().setVisible(False)
        self.Api_list.verticalHeader().setSortIndicatorShown(False)
        self.Category = QtGui.QComboBox(HubaoTestToolkit)
        self.Category.setGeometry(QtCore.QRect(10, 70, 201, 22))
        self.Category.setObjectName(_fromUtf8("Category"))
        self.Add_api = QtGui.QPushButton(HubaoTestToolkit)
        self.Add_api.setGeometry(QtCore.QRect(230, 390, 81, 23))
        self.Add_api.setObjectName(_fromUtf8("Add_api"))
        self.Edit_category = QtGui.QPushButton(HubaoTestToolkit)
        self.Edit_category.setGeometry(QtCore.QRect(220, 70, 81, 23))
        self.Edit_category.setObjectName(_fromUtf8("Edit_category"))
        self.Remove_api = QtGui.QPushButton(HubaoTestToolkit)
        self.Remove_api.setGeometry(QtCore.QRect(410, 390, 81, 23))
        self.Remove_api.setAutoDefault(False)
        self.Remove_api.setDefault(False)
        self.Remove_api.setFlat(False)
        self.Remove_api.setObjectName(_fromUtf8("Remove_api"))
        self.Edit_api = QtGui.QPushButton(HubaoTestToolkit)
        self.Edit_api.setGeometry(QtCore.QRect(320, 390, 81, 23))
        self.Edit_api.setObjectName(_fromUtf8("Edit_api"))
        self.Parameter = QtGui.QGroupBox(HubaoTestToolkit)
        self.Parameter.setGeometry(QtCore.QRect(10, 420, 481, 231))
        self.Parameter.setObjectName(_fromUtf8("Parameter"))
        self.Param_table = QtGui.QTableWidget(self.Parameter)
        self.Param_table.setGeometry(QtCore.QRect(10, 20, 461, 201))
        self.Param_table.setEditTriggers(QtGui.QAbstractItemView.DoubleClicked|QtGui.QAbstractItemView.EditKeyPressed)
        self.Param_table.setDragEnabled(True)
        self.Param_table.setDragDropOverwriteMode(False)
        self.Param_table.setObjectName(_fromUtf8("Param_table"))
        self.Param_table.setColumnCount(2)
        self.Param_table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.Param_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.Param_table.setHorizontalHeaderItem(1, item)
        self.Param_table.horizontalHeader().setDefaultSectionSize(150)
        self.Param_table.horizontalHeader().setStretchLastSection(True)
        self.Param_table.verticalHeader().setVisible(False)
        self.Method = QtGui.QGroupBox(HubaoTestToolkit)
        self.Method.setGeometry(QtCore.QRect(10, 660, 121, 80))
        self.Method.setObjectName(_fromUtf8("Method"))
        self.Get_button = QtGui.QRadioButton(self.Method)
        self.Get_button.setGeometry(QtCore.QRect(10, 20, 61, 16))
        self.Get_button.setChecked(True)
        self.Get_button.setObjectName(_fromUtf8("Get_button"))
        self.Put_button = QtGui.QRadioButton(self.Method)
        self.Put_button.setGeometry(QtCore.QRect(10, 50, 61, 16))
        self.Put_button.setObjectName(_fromUtf8("Put_button"))
        self.Delete_button = QtGui.QRadioButton(self.Method)
        self.Delete_button.setGeometry(QtCore.QRect(60, 50, 61, 16))
        self.Delete_button.setObjectName(_fromUtf8("Delete_button"))
        self.Post_button = QtGui.QRadioButton(self.Method)
        self.Post_button.setGeometry(QtCore.QRect(60, 20, 61, 16))
        self.Post_button.setAutoExclusive(True)
        self.Post_button.setObjectName(_fromUtf8("Post_button"))
        self.Localhost = QtGui.QCheckBox(HubaoTestToolkit)
        self.Localhost.setGeometry(QtCore.QRect(140, 690, 71, 21))
        self.Localhost.setObjectName(_fromUtf8("Localhost"))
        self.Testnode1 = QtGui.QCheckBox(HubaoTestToolkit)
        self.Testnode1.setGeometry(QtCore.QRect(140, 720, 81, 21))
        self.Testnode1.setChecked(True)
        self.Testnode1.setObjectName(_fromUtf8("Testnode1"))
        self.ContentType = QtGui.QComboBox(HubaoTestToolkit)
        self.ContentType.setGeometry(QtCore.QRect(140, 660, 241, 22))
        self.ContentType.setObjectName(_fromUtf8("ContentType"))
        self.ContentType.addItem(_fromUtf8(""))
        self.ContentType.addItem(_fromUtf8(""))
        self.Localhost_port = QtGui.QLineEdit(HubaoTestToolkit)
        self.Localhost_port.setGeometry(QtCore.QRect(220, 690, 51, 20))
        self.Localhost_port.setObjectName(_fromUtf8("Localhost_port"))
        self.Visitor = QtGui.QCheckBox(HubaoTestToolkit)
        self.Visitor.setGeometry(QtCore.QRect(40, 40, 71, 16))
        self.Visitor.setObjectName(_fromUtf8("Visitor"))

        self.retranslateUi(HubaoTestToolkit)
        QtCore.QMetaObject.connectSlotsByName(HubaoTestToolkit)

    def retranslateUi(self, HubaoTestToolkit):
        HubaoTestToolkit.setWindowTitle(_translate("HubaoTestToolkit", "HubaoTestToolkit", None))
        self.Label.setText(_translate("HubaoTestToolkit", "KEY", None))
        self.Query.setText(_translate("HubaoTestToolkit", "Query", None))
        self.Request.setText(_translate("HubaoTestToolkit", "Request", None))
        item = self.Api_list.horizontalHeaderItem(0)
        item.setText(_translate("HubaoTestToolkit", "Interface", None))
        item = self.Api_list.horizontalHeaderItem(1)
        item.setText(_translate("HubaoTestToolkit", "URL", None))
        self.Add_api.setText(_translate("HubaoTestToolkit", "Add", None))
        self.Edit_category.setText(_translate("HubaoTestToolkit", "Edit", None))
        self.Remove_api.setText(_translate("HubaoTestToolkit", "Remove", None))
        self.Edit_api.setText(_translate("HubaoTestToolkit", "Edit", None))
        self.Parameter.setTitle(_translate("HubaoTestToolkit", "Parameter", None))
        item = self.Param_table.horizontalHeaderItem(0)
        item.setText(_translate("HubaoTestToolkit", "Parameter", None))
        item = self.Param_table.horizontalHeaderItem(1)
        item.setText(_translate("HubaoTestToolkit", "Value", None))
        self.Method.setTitle(_translate("HubaoTestToolkit", "Method", None))
        self.Get_button.setText(_translate("HubaoTestToolkit", "Get", None))
        self.Put_button.setText(_translate("HubaoTestToolkit", "Put", None))
        self.Delete_button.setText(_translate("HubaoTestToolkit", "Delete", None))
        self.Post_button.setText(_translate("HubaoTestToolkit", "Post", None))
        self.Localhost.setText(_translate("HubaoTestToolkit", "localhost", None))
        self.Testnode1.setText(_translate("HubaoTestToolkit", "test_node1", None))
        self.ContentType.setItemText(0, _translate("HubaoTestToolkit", "application/x-www-form-urlencoded", None))
        self.ContentType.setItemText(1, _translate("HubaoTestToolkit", "application/json", None))
        self.Localhost_port.setText(_translate("HubaoTestToolkit", "5011", None))
        self.Visitor.setText(_translate("HubaoTestToolkit", "Visitor", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    HubaoTestToolkit = QtGui.QWidget()
    ui = Ui_HubaoTestToolkit()
    ui.setupUi(HubaoTestToolkit)
    HubaoTestToolkit.show()
    sys.exit(app.exec_())

