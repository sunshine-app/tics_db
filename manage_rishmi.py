# -*- coding: utf-8 -*-
# @Time    : 2020/1/15 10:16
# @Author  : shine
# @File    : manage_rishmi.py
import sqlite3
import pymysql

from tics_db.manage_position_code import ManagePositionCode
from tics_db.manage_recog_impurity import ManageRecogImpurity
from tics_db.manage_target_impurity import ManageTargetImpurity
from tics_db.manage_catch_result import ManageCatchResult


class ManageLiteDb(ManagePositionCode, ManageRecogImpurity, ManageTargetImpurity, ManageCatchResult):
    def __init__(self, *args, **kwargs):
        try:
            if args[0] == "mysql":
                self.connect = pymysql.connect(host=kwargs["host"],
                                               port=kwargs["port"],
                                               user=kwargs["user"],
                                               password=kwargs["password"],
                                               db=kwargs["database"],
                                               use_unicode=True,
                                               charset="utf8",
                                               cursorclass=pymysql.cursors.DictCursor)
                self.cursor = self.connect.cursor()
            else:
                self.connect = sqlite3.connect(kwargs["db_path"])
                self.cursor = self.connect.cursor()
            ManagePositionCode.__init__(self, self.connect, self.cursor, self.execute_sql)
            ManageRecogImpurity.__init__(self, self.connect, self.cursor, self.execute_sql)
            ManageTargetImpurity.__init__(self, self.connect, self.cursor, self.execute_sql)
            ManageCatchResult.__init__(self, self.connect, self.cursor, self.execute_sql)
        except Exception as ex:
            print("Sqlite数据库连接失败：{error}".format(error=ex))

    def execute_sql(self, sql, date_list=None):
        if date_list is None:
            self.cursor.execute(sql)
        else:
            self.cursor.executemany(sql, date_list)
        self.connect.commit()

    def close_db(self):
        self.connect.close()


if __name__ == "__main__":
    # manageLiteDb = ManageLiteDb("sqlite3", db_path="E:\\shineLoverDesktop\\rishmi.sqlite")
    manageLiteDb = ManageLiteDb("mysql", host="127.0.0.1", port=3306,
                                user="shinelover", password="123456", database="rishmi")
    manageLiteDb.select_catch_result()
    manageLiteDb.close_db()
