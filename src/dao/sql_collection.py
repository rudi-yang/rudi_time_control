class SqlCollection():
    SQL_CREATE_TABLE_TIME_CONTROL = """
    create table if not exists time_control
    (
       id integer primary key  autoincrement,
       action text not null,
       cate text not null,
       detail text not null,
       start_timestamp datetime,
       end_timestamp datetime,
       ds int,
       duration float
    );"""

    SQL_INSERT_TIME_CONTRL = """
    insert into time_control(action, cate,  detail, start_timestamp, end_timestamp, ds,duration)
                values ('{0}', '{1}', '{2}', '{3}', '{4}','{5}','{6}');
    """

    SQL_DROP_TABLE_TIME_CONTROL = """
    drop table if exists time_control;
    """

    SQL_DROP_TIME_CONTROL_BY_ID = """
    delete from time_control where id='{0}';
    """

    SQL_CHECK_CONFILCT = """
    select * from time_control where ('{0}' > start_timestamp and '{0}' <end_timestamp) or ('{1}' > start_timestamp and '{1}' <end_timestamp);
    """
