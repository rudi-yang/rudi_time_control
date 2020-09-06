import sqlite3

from src.dao.sql_collection import SqlCollection
from src.entity.entity_time_control import EntityTimeControl


class Dao():
    def __init__(self, conn):
        self.conn = conn

    def execute_sql(self, sql):
        c = self.conn.cursor()
        c.execute(sql)
        self.conn.commit()

    def execute_query(self, sql):
        c = self.conn.cursor()
        res = c.execute(sql)
        return res

    def create_table(self):
        self.execute_sql(SqlCollection.SQL_CREATE_TABLE_TIME_CONTROL)

    def insert_record(self, entity: EntityTimeControl):
        sql = SqlCollection.SQL_INSERT_TIME_CONTRL.format(
            entity.action,
            entity.cate,
            entity.detail,
            entity.start_timestamp,
            entity.end_timestamp,
            entity.ds,
            entity.duration
        )
        self.execute_sql(sql)

    def drop_table(self):
        sql = SqlCollection.SQL_DROP_TABLE_TIME_CONTROL
        self.execute_sql(sql)

    def drop_by_id(self, id):
        sql = SqlCollection.SQL_DROP_TIME_CONTROL_BY_ID.format(id)
        self.execute_sql(sql)

    def check_confilct(self, ts_start, ts_end):
        sql = SqlCollection.SQL_CHECK_CONFILCT.format(ts_start, ts_end)
        res = self.execute_query(sql)
        return res
