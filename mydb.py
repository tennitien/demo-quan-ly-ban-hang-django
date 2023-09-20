import pymysql
from decouple import config


PASSWORD_MYSQL=config('PASSWORD_MYSQL')

db= pymysql.connect(
    host='localhost',
    user='root',
    passwd=PASSWORD_MYSQL,
)

cursorObj= db.cursor()

# create db
cursorObj.execute('CREATE DATABASE QLBH')
print('Create Database')