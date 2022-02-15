from __future__ import  unicode_literals
from django.db import models
from django.db import connection    #使用原生sql

class cal(models.Model):
    value_a = models.CharField(max_length=10)
    value_b = models.FloatField(max_length=10)
    result = models.CharField(max_length=10)

class MYSQL():
    def sql(self,sql):
        cursor = connection.cursor()    #获取游标
        cursor.execute(sql)  #执行原生sql
        #cursor.execute("select name from login_selenium where type = '1'")
        row = cursor.fetchall()
        return row


    # def create_table(self,DATABASE):
    #     '''创建一个新表'''
    #     create_table_sql = "create table {} (id int primary key auto_increment,title varchar(10),uname varchar(50),ukey varchar(50),delete_state int(1),value1 varchar(50),value2 varchar(50),value3 varchar(50),value4 varchar(50),value5 varchar(50),value6 varchar(50),value7 varchar(50),value8 varchar(50),value9 varchar(50),value10 varchar(50));".format(DATABASE)
    #     return create_table_sql

    def drop_table(self,table):
        '''删除table表'''
        drop_table_sql = "drop table {};".format(table)
        return  drop_table_sql

    def select(self,table):
        '''查询table表中未被删除的内容'''
        select_sql = "SELECT * from {} where delete_state is null;".format(table)
        return select_sql

    def insert_into(self,table,*args):
        '''在table表中插入一行数据'''
        str_args = str(args)
        insert_sql = "insert into " + table + " values" + str_args + ";"
        return insert_sql

    def update(self,table,list_name,list_value,id_value):
        '''修改table表中id为id_value的list_name列'''
        update_sql = "update {} set {} = {} where id = {}".format(table,list_name,list_value,id_value)
        return update_sql

    def delate(self,table,id_value):
        delate_sql = "update {} set delete_state = 1 where id = {};".format(table,id_value)
        return delate_sql



