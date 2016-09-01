# -*- coding: utf-8 -*-
import json
import re
from collections import OrderedDict
import psycopg2
import psycopg2.extensions
from psycopg2.extras import DictCursor
from PyQt4 import QtGui, QtCore
from jinja2 import Template

from layout import Ui_HubaoTestToolkit, _fromUtf8, _translate
from editor import Ui_Editor
from dbconfig import *
from Requester import Requester

psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)

class HubaoTest(QtGui.QWidget):
    def __init__(self):
        super(HubaoTest, self).__init__()
        self.ui = Ui_HubaoTestToolkit()
        self.ui.setupUi(self)
        self.ui.Query.clicked.connect(self.show_auth_info)
        self.ui.Condition_value.returnPressed.connect(self.show_auth_info)
        self.ui.Add_api.clicked.connect(self.open_editor)
        self.ui.Edit_api.clicked.connect(self.open_editor)
        self.ui.Category.currentIndexChanged.connect(self.setup_api_table)
        self.ui.Api_list.itemSelectionChanged.connect(self.api_selected)
        self.ui.Visitor.stateChanged.connect(lambda : self.setup_condition(self.ui.Visitor.isChecked()))
        self.ui.Request.clicked.connect(self.request)

        self.load_config()
        self.setup_category()
        self.setup_method_group()
        self.setup_condition(self.ui.Visitor.isChecked())

        self.selected_api = None

    def load_config(self):
        self.config = json.load(open("APIs.json"))

    def setup_condition(self, is_visitor):
        self.ui.Condition.clear()
        if is_visitor:
            self.ui.Condition.addItem(_fromUtf8(""))
            self.ui.Condition.setItemText(0, _translate("HubaoTestToolkit", "udid", None))
        else:
            self.ui.Condition.addItem(_fromUtf8(""))
            self.ui.Condition.addItem(_fromUtf8(""))
            self.ui.Condition.addItem(_fromUtf8(""))
            self.ui.Condition.addItem(_fromUtf8(""))
            self.ui.Condition.addItem(_fromUtf8(""))
            self.ui.Condition.setItemText(0, _translate("HubaoTestToolkit", "user_id", None))
            self.ui.Condition.setItemText(1, _translate("HubaoTestToolkit", "user_id (int)", None))
            self.ui.Condition.setItemText(2, _translate("HubaoTestToolkit", "room_id", None))
            self.ui.Condition.setItemText(3, _translate("HubaoTestToolkit", "nickname", None))
            self.ui.Condition.setItemText(4, _translate("HubaoTestToolkit", "udid", None))

    def setup_method_group(self):
        self.Method_group = QtGui.QButtonGroup(self)
        self.Method_group.addButton(self.ui.Get_button)
        self.Method_group.addButton(self.ui.Post_button)
        self.Method_group.addButton(self.ui.Put_button)
        self.Method_group.addButton(self.ui.Delete_button)

        self.Method_group.buttonClicked.connect(self.show_param)

    def setup_category(self):
        for i, key in enumerate(sorted(self.config.keys())):
            self.ui.Category.addItem(_fromUtf8(""))
            self.ui.Category.setItemText(i, _translate("HubaoTestToolkit", key, None))

    def setup_api_table(self):
        self.ui.Api_list.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.ResizeToContents)

        # clear table
        for row in range(self.ui.Api_list.rowCount()):
            self.ui.Api_list.removeRow(0)

        api_list = self.config.get(str(self.ui.Category.currentText()), [])
        for i, item in enumerate(api_list):
            self.ui.Api_list.insertRow(i)
            self.ui.Api_list.setItem(i, 0, QtGui.QTableWidgetItem(item["name"]))
            self.ui.Api_list.setItem(i, 1, QtGui.QTableWidgetItem(item["url"]))

        if self.ui.Api_list.size().width() - self.ui.Api_list.columnWidth(0) - 2 > self.ui.Api_list.columnWidth(1):
            self.ui.Api_list.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.Stretch)

        self.ui.Api_list.selectRow(0)

    def api_selected(self):
        cate = str(self.ui.Category.currentText())
        selected = self.ui.Api_list.selectedIndexes()
        if selected:
            index = selected[0].row()
            self.selected_api = self.config.get(cate, [])[index]
            self.show_param()

    def show_param(self):
        # clear parameter table
        for row in range(self.ui.Param_table.rowCount()):
            self.ui.Param_table.removeRow(0)

        method = str(self.Method_group.checkedButton().text())
        info = self.selected_api["method"].get(method.lower())
        if info:
            params = info.get("url_param", []) + info.get("body_param", [])
            for i, param in enumerate(params):
                self.ui.Param_table.insertRow(i)
                tItem = QtGui.QTableWidgetItem(param.get("name"))
                tItem.setFlags(tItem.flags() & ~QtCore.Qt.ItemIsEditable)
                self.ui.Param_table.setItem(i, 0, tItem)
                default = "{}".format(param.get("default"))
                self.ui.Param_table.setItem(i, 1, QtGui.QTableWidgetItem(default))

    def show_auth_info(self):
        output = json.dumps(self.query_auth_info(), indent=2, ensure_ascii=False)
        self.ui.Display_panel.setText(output)

    def query_auth_info(self):
        query = "select u.uid, u.uuid, d.udid, uc.token, uc.nickname, r.rid " \
                "from users u inner join device d on u.active_device=d.did " \
                "inner join user_certs uc on u.uid=uc.uid " \
                "inner join room r on u.uid=r.uid " \
                "where {0}={1}"

        condition = {
            "user_id": "u.uuid",
            "user_id (int)": "u.uid",
            "nickname": "uc.nickname",
            "room_id": "r.rid",
            "udid": "d.udid"
        }.get(str(self.ui.Condition.currentText()))
        con_value = unicode(self.ui.Condition_value.text())

        if not con_value.strip():
            self.warning("Empty input!")
            return {}

        with psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD,
                              host=HOST, port=PORT) as conn:
            cur = conn.cursor(cursor_factory=DictCursor)

            result = OrderedDict({})
            try:
                cur.execute(query.format(condition, "%s"), (con_value,))
                r = cur.fetchone()
                result.update([
                    ("uuid", r["uuid"].replace("-", "")),
                    ("udid", r["udid"].replace("-", "")),
                    ("token", r["token"].split(".")[0]),
                    ("nickname", r["nickname"]),
                    ("user_id", r["uid"]),
                    ("room_id", r["rid"])
                ]) if r else {}
            except psycopg2.DataError:
                conn.rollback()
                self.warning("Query error! Please check your input")
            except Exception as e:
                conn.rollback()
                self.warning("Query error!")

            return result

    def open_editor(self):
        self.editor = Editor()
        self.editor.exec_()

    def warning(self, msg=None):
        msgbox = QtGui.QMessageBox()
        msgbox.setWindowTitle("Error")
        msgbox.setText(msg or "Wrong input!")
        msgbox.exec_()

    def request(self):
        if self.ui.Visitor.isChecked():
            is_visitor = True
            requester = Requester(udid=str(self.ui.Condition_value.text()))
        else:
            is_visitor = False
            auth_info = self.query_auth_info()
            requester = Requester(user_id=auth_info["uuid"], udid=auth_info["udid"], access_token=auth_info["token"])

        input_param = {}
        for i in range(self.ui.Param_table.rowCount()):
            input_param.update({
                str(self.ui.Param_table.item(i, 0).text()): str(self.ui.Param_table.item(i, 1).text())
            })

        ctype = str(self.ui.ContentType.currentText())
        method = str(self.Method_group.checkedButton().text()).lower()
        api_url = self.selected_api["url"]

        params = re.findall("<(.+?)>", api_url)
        for p in params:
            api_url = api_url.replace("<{}>".format(p), input_param.pop(p))

        if method in ("post", "put"):
            url_params = self.selected_api["method"][method].get("url_param", [])
            args = [(k["name"], input_param.pop(k["name"])) for k in url_params if input_param.get(k["name"])]
            api_url += "?" + "&".join(["{0}={1}".format(*a) for a in args])

        urls = []
        if self.ui.Localhost.isChecked():
            urls.append("http://localhost:" + str(self.ui.Localhost_port.text()) + api_url)
        if self.ui.Testnode1.isChecked():
            urls.append("http://test-node1.hubao.tv" + api_url)

        self.ui.Display_panel.clear()
        for url in urls:
            try:
                result = requester.request(url=url,
                                           method=method,
                                           data=input_param if input_param else None,
                                           content_type=ctype,
                                           visitor=is_visitor)
            except Exception as e:
                result = {}
                self.warning("{0}: {1}".format(type(e), e.message))
            self.ui.Display_panel.append(result.get("content", ""))


class Editor(QtGui.QDialog):
    def __init__(self, action="add", data=None):
        super(Editor, self).__init__()
        self.ui = Ui_Editor()
        self.ui.setupUi(self)

        if action == "add":
            self.ui.Editor_button.button(self.ui.Editor_button.Ok).setText("Add")
        else:
            self.ui.Editor_button.button(self.ui.Editor_button.Ok).setText("Save")

        self.ui.Add_param.setIcon(QtGui.QIcon("images/add.png"))
        self.ui.Add_param.clicked.connect(self.add_param)
        self.ui.Del_param.setIcon(QtGui.QIcon("images/delete.png"))
        self.ui.Del_param.clicked.connect(self.del_param)

    def load_config(self):
        self.config = json.load(open("APIs.json"))

    def save_config(self, data=None):
        d = data or self.config
        with open("APIs.json", "w") as f:
            json.dump(d, f, indent=2)

    def set_param_table(self):
        pass

    def add_param(self):
        pass

    def del_param(self):
        pass



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    test = HubaoTest()
    test.show()
    sys.exit(app.exec_())