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


    def create_sql(self,DATABASE):
        '''创建一个新表'''
        create_table_sql = "create table {} (id int primary key auto_increment,title varchar(10),uname varchar(50),ukey varchar(50),delete_state int(1),value1 varchar(50),value2 varchar(50),value3 varchar(50),value4 varchar(50),value5 varchar(50),value6 varchar(50),value7 varchar(50),value8 varchar(50),value9 varchar(50),value10 varchar(50));".format(DATABASE)
        return create_table_sql

    def drop_table(self,table):
        '''删除table表'''
        drop_table_sql = "drop table {};".format(table)
        return  drop_table_sql

    def select(self,table):
        '''查询table表中未被删除的内容'''
        select_sql = "SELECT title,uname,ukey,value1,value2,value3,value4,value5,value6,value7,value8,value9,value10 from {} where delete_state is null;".format(table)
        return select_sql

    def insert_into(self,table,title,uname,ukey,value1,value2,value3,value4,value5,value6,value7,value8,value9,value10):
        '''在table表中插入一行数据'''
        if title == '':
            title = 'NUll'
        if uname == '':
            uname = 'NUll'
        if ukey == '':
            ukey = 'NUll'
        if value1 == '':
            value1 = 'NUll'
        if value2 == '':
            value2 = 'NUll'
        if value3 == '':
            value3 = 'NUll'
        if value4 == '':
            value4 = 'NUll'
        if value5 == '':
            value5 = 'NUll'
        if value6 == '':
            value6 = 'NUll'
        if value7 == '':
            value7 = 'NUll'
        if value8 == '':
            value8 = 'NUll'
        if value9 == '':
            value9 = 'NUll'
        if value10 == '':
            value10 = 'NUll'
        insert_sql = "insert into {0} values (NULL,{1},{2},{3},{4},1,{5},{6},{7},{8},{9},{10},{11},{12},{13});".format(table,title,uname,ukey,value1,value2,value3,value4,value5,value6,value7,value8,value9,value10)
        return insert_sql

    def update(self,table,list_name,list_value,id_value):
        '''修改table表中id为id_value的list_name列'''
        update_sql = "update {} set {} = {} where id = {}".format(table,list_name,list_value,id_value)
        return update_sql

    def delate(self,table,id_value):
        delate_sql = "update {} set delete_state = 1 where id = {};".format(table,id_value)
        return delate_sql


