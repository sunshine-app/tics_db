# -*- coding: utf-8 -*-
# @Time    : 2020/1/15 10:54
# @Author  : shine
# @File    : manage_position_code.py


class ManagePositionCode:

    def __init__(self, connect, cursor, exec_sql):
        self.connect = connect
        self.cursor = cursor
        self.exec_sql = exec_sql
        self.create_position_code()

    def create_position_code(self):
        position_code_sql = '''CREATE TABLE IF NOT EXISTS posi_code
                                       (RequestID VARCHAR(36) PRIMARY KEY  NOT NULL,
                                        ProcessID VARCHAR(36)  NOT NULL,
                                        PositionCode BIGINT  NOT NULL,
                                        TimestampSec BIGINT  NOT NULL,
                                        TimestampMSec BIGINT  NOT NULL);'''
        self.exec_sql(position_code_sql)

    def select_position_code(self):
        sql = ""