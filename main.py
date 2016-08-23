# -*- coding: utf-8 -*-
import json
from collections import OrderedDict
import psycopg2
import psycopg2.extensions
from psycopg2.extras import DictCursor
from PyQt4 import QtGui, QtCore

from layout import Ui_HubaoTestToolkit
from dbconfig import *

psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)

class HubaoTest(QtGui.QWidget):
    def __init__(self):
        super(HubaoTest, self).__init__()
        self.ui = Ui_HubaoTestToolkit()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.Query, QtCore.SIGNAL("clicked()"), self.get_auth_info)
        QtCore.QObject.connect(self.ui.Condition_value, QtCore.SIGNAL("returnPressed()"), self.get_auth_info)
        QtCore.QObject.connect(self.ui.Add_api, QtCore.SIGNAL("clicked()"), self.get_auth_info)

    def get_auth_info(self):
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
            "room_id": "r.rid"
        }.get(str(self.ui.Condition.currentText()))
        con_value = unicode(self.ui.Condition_value.text())

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
                self.warning()
            except Exception as e:
                conn.rollback()
                self.warning("Error!")

            return result

    def warning(self, msg=None):
        msgbox = QtGui.QMessageBox()
        msgbox.setWindowTitle("Error")
        msgbox.setText(msg or "Wrong input!")
        msgbox.exec_()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    test = HubaoTest()
    test.show()
    sys.exit(app.exec_())