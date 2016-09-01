# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editor.ui'
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

class Ui_Editor(object):
    def setupUi(self, Editor):
        Editor.setObjectName(_fromUtf8("Editor"))
        Editor.resize(622, 488)
        self.Editor_button = QtGui.QDialogButtonBox(Editor)
        self.Editor_button.setGeometry(QtCore.QRect(450, 450, 161, 32))
        self.Editor_button.setOrientation(QtCore.Qt.Horizontal)
        self.Editor_button.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.Editor_button.setObjectName(_fromUtf8("Editor_button"))
        self.formLayoutWidget = QtGui.QWidget(Editor)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 491, 125))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_cate = QtGui.QLabel(self.formLayoutWidget)
        self.label_cate.setObjectName(_fromUtf8("label_cate"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_cate)
        self.Category = QtGui.QComboBox(self.formLayoutWidget)
        self.Category.setObjectName(_fromUtf8("Category"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.Category)
        self.label_name = QtGui.QLabel(self.formLayoutWidget)
        self.label_name.setObjectName(_fromUtf8("label_name"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_name)
        self.Name = QtGui.QLineEdit(self.formLayoutWidget)
        self.Name.setObjectName(_fromUtf8("Name"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.Name)
        self.label_url = QtGui.QLabel(self.formLayoutWidget)
        self.label_url.setObjectName(_fromUtf8("label_url"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_url)
        self.URL = QtGui.QTextEdit(self.formLayoutWidget)
        self.URL.setObjectName(_fromUtf8("URL"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.URL)
        self.Get = QtGui.QCheckBox(Editor)
        self.Get.setGeometry(QtCore.QRect(510, 10, 61, 21))
        self.Get.setObjectName(_fromUtf8("Get"))
        self.Put_param = QtGui.QToolButton(Editor)
        self.Put_param.setGeometry(QtCore.QRect(570, 70, 37, 18))
        self.Put_param.setObjectName(_fromUtf8("Put_param"))
        self.Post = QtGui.QCheckBox(Editor)
        self.Post.setGeometry(QtCore.QRect(510, 40, 61, 21))
        self.Post.setObjectName(_fromUtf8("Post"))
        self.Get_param = QtGui.QToolButton(Editor)
        self.Get_param.setGeometry(QtCore.QRect(570, 10, 37, 18))
        self.Get_param.setObjectName(_fromUtf8("Get_param"))
        self.Post_param = QtGui.QToolButton(Editor)
        self.Post_param.setGeometry(QtCore.QRect(570, 40, 37, 18))
        self.Post_param.setObjectName(_fromUtf8("Post_param"))
        self.Put = QtGui.QCheckBox(Editor)
        self.Put.setGeometry(QtCore.QRect(510, 70, 61, 21))
        self.Put.setObjectName(_fromUtf8("Put"))
        self.toolButton_3 = QtGui.QToolButton(Editor)
        self.toolButton_3.setGeometry(QtCore.QRect(570, 100, 37, 18))
        self.toolButton_3.setObjectName(_fromUtf8("toolButton_3"))
        self.Delete = QtGui.QCheckBox(Editor)
        self.Delete.setGeometry(QtCore.QRect(510, 100, 61, 21))
        self.Delete.setObjectName(_fromUtf8("Delete"))
        self.groupBox = QtGui.QGroupBox(Editor)
        self.groupBox.setGeometry(QtCore.QRect(10, 150, 601, 291))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.Parameters = QtGui.QTableWidget(self.groupBox)
        self.Parameters.setGeometry(QtCore.QRect(10, 20, 541, 261))
        self.Parameters.setObjectName(_fromUtf8("Parameters"))
        self.Parameters.setColumnCount(3)
        self.Parameters.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.Parameters.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.Parameters.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.Parameters.setHorizontalHeaderItem(2, item)
        self.Parameters.horizontalHeader().setDefaultSectionSize(200)
        self.Parameters.horizontalHeader().setStretchLastSection(True)
        self.Add_param = QtGui.QPushButton(self.groupBox)
        self.Add_param.setGeometry(QtCore.QRect(560, 20, 31, 31))
        self.Add_param.setText(_fromUtf8(""))
        self.Add_param.setObjectName(_fromUtf8("Add_param"))
        self.Del_param = QtGui.QPushButton(self.groupBox)
        self.Del_param.setGeometry(QtCore.QRect(560, 60, 31, 31))
        self.Del_param.setText(_fromUtf8(""))
        self.Del_param.setObjectName(_fromUtf8("Del_param"))

        self.retranslateUi(Editor)
        QtCore.QObject.connect(self.Editor_button, QtCore.SIGNAL(_fromUtf8("accepted()")), Editor.accept)
        QtCore.QObject.connect(self.Editor_button, QtCore.SIGNAL(_fromUtf8("rejected()")), Editor.reject)
        QtCore.QMetaObject.connectSlotsByName(Editor)

    def retranslateUi(self, Editor):
        Editor.setWindowTitle(_translate("Editor", "Edit", None))
        self.label_cate.setText(_translate("Editor", "Category", None))
        self.label_name.setText(_translate("Editor", "Interface Name", None))
        self.label_url.setText(_translate("Editor", "URL", None))
        self.Get.setText(_translate("Editor", "Get", None))
        self.Put_param.setText(_translate("Editor", "...", None))
        self.Post.setText(_translate("Editor", "Post", None))
        self.Get_param.setText(_translate("Editor", "...", None))
        self.Post_param.setText(_translate("Editor", "...", None))
        self.Put.setText(_translate("Editor", "Put", None))
        self.toolButton_3.setText(_translate("Editor", "...", None))
        self.Delete.setText(_translate("Editor", "Delete", None))
        self.groupBox.setTitle(_translate("Editor", "Parameters", None))
        item = self.Parameters.horizontalHeaderItem(0)
        item.setText(_translate("Editor", "Name", None))
        item = self.Parameters.horizontalHeaderItem(1)
        item.setText(_translate("Editor", "Default", None))
        item = self.Parameters.horizontalHeaderItem(2)
        item.setText(_translate("Editor", "Location", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Editor = QtGui.QDialog()
    ui = Ui_Editor()
    ui.setupUi(Editor)
    Editor.show()
    sys.exit(app.exec_())

