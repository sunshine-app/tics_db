# -*- coding: utf-8 -*-
# @Time    : 2020/1/15 10:55
# @Author  : shine
# @File    : manage_target_impurity.py


class ManageTargetImpurity:

    def __init__(self, connect, cursor, exec_sql):
        self.connect = connect
        self.cursor = cursor
        self.exec_sql = exec_sql
        self.create_target_impurity()

    def create_target_impurity(self):
        target_impurity_sql = '''CREATE TABLE IF NOT EXISTS target_impurity
                                               (RequestID VARCHAR(36) PRIMARY KEY  NOT NULL,
                                                ProcessID VARCHAR(36)  NOT NULL,
                                                PositionCode BIGINT  NOT NULL,
                                                Type VARCHAR(255)  NOT NULL,
                                                Probability FLOAT  NOT NULL,
                                                WX FLOAT  NOT NULL,
                                                WY FLOAT  NOT NULL,
                                                WZ FLOAT  NOT NULL,
                                                CX FLOAT  NOT NULL,
                                                CY FLOAT  NOT NULL,
                                                Width FLOAT  NOT NULL,
                                                Height FLOAT  NOT NULL);'''
        self.exec_sql(target_impurity_sql)

    def select_target_impurity(self):
        sql = ""