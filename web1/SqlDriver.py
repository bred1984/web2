import psycopg2
from psycopg2.extras import RealDictCursor
# from sql_db import *
from web1.sql_db import *



class SqlDriver:
    con:None
    cur:None
    data:None
    result:None
    sql:None
    @staticmethod
    def connect(f,data=0):
        # self.data=data
        SqlDriver.con = psycopg2.connect(host='localhost',
                                         user='postgres',
                                         password='postgres',
                                         dbname="socnetwork",
                                         port="5432")
        SqlDriver.data=data
        res=0
        with SqlDriver.con:
            # создаем объект для запуска sql запросов
            SqlDriver.cur = SqlDriver.con.cursor(cursor_factory=RealDictCursor)
            res=f()
            # print(res)
            SqlDriver.cur.close()
        # print('curclose')
        return res

    @staticmethod
    def Insert_db():
        # db={'name': 'users', 'sql': "insert into users (fio, age, pasport) values('Иванов',31,'qwertytuy')"}
        # sql=f"insert into photo (name, href, ) values('{SqlDriver.data['name'].name}',{SqlDriver.data['href']}')"
        # print(SqlDriver.sql)
        SqlDriver.cur.execute(SqlDriver.sql)

    @staticmethod
    def Show():
        # if SqlDriver.data==0:
        #     sql="select * from users"
        # else:
        #     sql=f"select * from users where fio = '{SqlDriver.data}'"
        # sql = f"select id from {SqlDriver.data['zapros']}"
        # print(sql)
        SqlDriver.cur.execute(SqlDriver.sql)
        return SqlDriver.cur.fetchall()
    @staticmethod
    def ShowUser():
        SqlDriver.cur.execute(SqlDriver.sql)
        return SqlDriver.cur.fetchall()
    @staticmethod
    def CreateDB():
        for s in sql_create_table:
            SqlDriver.cur.execute(s['sql'])

