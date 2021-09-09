from datetime import datetime
import sqlite3


class DataOutputMgr:
    """
    manage ways how to save datas to databases
    """

    def __init__(self, dbname="sqlite_test.db") -> None:
        self.con = sqlite3.connect(dbname)
        self.creatTable()

    def creatTable(self):
        cur = self.con.cursor()
        cur.execute(
            'create table if not exists airinfo (id INTEGER PRIMARY KEY, city text, time text, temp text, note text)')
        self.con.commit()

    def upsert(self, row):
        # if city_name and datetime is equal, then just update existing one. if not, insert new one
        city_name, datetimeobj, temp, note = tuple(row)
        datetimeobjstr = '\'' + datetimeobj.strftime('%d.%m.%Y %H:%M') + '\''
        temp = str(temp) if temp is not None else "null"
        idx = str(hash(city_name + datetimeobjstr)).replace('-', '')
        city_name = '\'' + city_name + '\''
        note = ('\'' + note + '\'') if note is not None else "null"
        sql_str = 'INSERT OR REPLACE INTO airinfo (id, city, time, temp, note) VALUES(' + \
            idx + ', ' + city_name + ', ' + datetimeobjstr + \
            ', ' + temp + ',' + note + ')'
        cur = self.con.cursor()
        cur.execute(sql_str)

    def commit(self):
        self.con.commit()
