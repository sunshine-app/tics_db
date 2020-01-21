# -*- coding: utf-8 -*-
# @Time    : 2020/1/15 10:54
# @Author  : shine
# @File    : manage_recog_impurity.py


class ManageRecogImpurity:

    def __init__(self, connect, cursor, exec_sql):
        self.connect = connect
        self.cursor = cursor
        self.exec_sql = exec_sql
        self.create_recog_impurity()

    def create_recog_impurity(self):
        recog_impurity_sql = '''CREATE TABLE IF NOT EXISTS recog_impurity
                                                       (RequestID VARCHAR(36) PRIMARY KEY  NOT NULL,
                                                        ProcessID VARCHAR(36)  NOT NULL,
                                                        ResponseID VARCHAR(36)  NOT NULL,
                                                        PositionCode BIGINT  NOT NULL,
                                                        TimestampSec BIGINT  NOT NULL,
                                                        TimestampMSec BIGINT  NOT NULL,
                                                        Result INT  NOT NULL,
                                                        Photo TEXT  NOT NULL,
                                                        ImpurityNum INT  NOT NULL);'''
        self.exec_sql(recog_impurity_sql)

    def select_recog_impurity(self):
        sql = ""