# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_api.ui'
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

class Ui_Edit(object):
    def setupUi(self, Edit):
        Edit.setObjectName(_fromUtf8("Edit"))
        Edit.resize(563, 463)
        Edit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.formLayoutWidget = QtGui.QWidget(Edit)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 541, 111))
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
        self.groupBox = QtGui.QGroupBox(Edit)
        self.groupBox.setGeometry(QtCore.QRect(10, 130, 541, 291))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.Parameters = QtGui.QTableView(self.groupBox)
        self.Parameters.setGeometry(QtCore.QRect(10, 20, 521, 261))
        self.Parameters.setObjectName(_fromUtf8("Parameters"))
        self.Save = QtGui.QPushButton(Edit)
        self.Save.setGeometry(QtCore.QRect(360, 430, 91, 23))
        self.Save.setObjectName(_fromUtf8("Save"))
        self.Cancel = QtGui.QPushButton(Edit)
        self.Cancel.setGeometry(QtCore.QRect(460, 430, 91, 23))
        self.Cancel.setObjectName(_fromUtf8("Cancel"))

        self.retranslateUi(Edit)
        QtCore.QMetaObject.connectSlotsByName(Edit)

    def retranslateUi(self, Edit):
        Edit.setWindowTitle(_translate("Edit", "Edit", None))
        self.label_cate.setText(_translate("Edit", "Category", None))
        self.label_name.setText(_translate("Edit", "Interface Name", None))
        self.label_url.setText(_translate("Edit", "URL", None))
        self.groupBox.setTitle(_translate("Edit", "Parameters", None))
        self.Save.setText(_translate("Edit", "Save", None))
        self.Cancel.setText(_translate("Edit", "Cancel", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Edit = QtGui.QWidget()
    ui = Ui_Edit()
    ui.setupUi(Edit)
    Edit.show()
    sys.exit(app.exec_())

