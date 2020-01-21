# -*- coding: utf-8 -*-
# @Time    : 2020/1/15 10:55
# @Author  : shine
# @File    : manage_catch_result.py


class ManageCatchResult:

    def __init__(self, connect, cursor, exec_sql):
        self.connect = connect
        self.cursor = cursor
        self.exec_sql = exec_sql
        self.create_catch_result()

    def create_catch_result(self):
        catch_result_sql = '''CREATE TABLE IF NOT EXISTS catch_result
                               (RequestID VARCHAR(36) PRIMARY KEY  NOT NULL,
                                ProcessID VARCHAR(36)  NOT NULL,
                                MsgType INT  NOT NULL,
                                MsgResult INT  NOT NULL);'''
        self.exec_sql(catch_result_sql)

    def select_catch_result(self):
        sql = "SELECT ProcessID, MsgType, MsgResult from catch_result"
        self.cursor.execute(sql)
        for row in self.cursor.fetchall():
            print(row)
        print("查询完成")

    def count_catch_result(self):
        sql = "SELECT count(RequestID) as ProcessCount from catch_result"

    def insert_catch_result(self, request_id, process_id, msg_type, msg_result):
        sql = "INSERT INTO catch_result VALUES('%s', '%s', '%s', '%s')" \
              % (request_id, process_id, msg_type, msg_result)
        self.exec_sql(sql)
