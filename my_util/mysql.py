import pymysql
import my_util.config as config
from prettytable import *

def sqlGetPrettyTable(sql):
    db=pymysql.connect(host=config.hostName,user=config.DataBaseUser,password=config.DataBasePassword,database=config.DataBaseName)
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        result=from_db_cursor(cursor)
        return result
    except:
        pass
    db.close()
    return None

def sqlGetAllTuples(sql):#获取满足sql条件的所有记录,每个记录一个元组,返回二维元组
    db=pymysql.connect(host=config.hostName,user=config.DataBaseUser,password=config.DataBasePassword,database=config.DataBaseName)
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    try:
        cursor.execute(sql)
        db.commit()
        result = cursor.fetchall();
        # return result
        if(result==()):
            return None;
        else:
            return result
    except:
        pass
    db.close()
    return None

def sqlGetOneTuple(sql):#获取满足sql条件的第一条记录,以元组形式返回
    db=pymysql.connect(host=config.hostName,user=config.DataBaseUser,password=config.DataBasePassword,database=config.DataBaseName)
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    try:
        cursor.execute(sql)
        db.commit()
        result = cursor.fetchone();
        return result
    except:
        pass
    db.close()
    return None


def sqlInsert(sql):
    db=pymysql.connect(host=config.hostName,user=config.DataBaseUser,password=config.DataBasePassword,database=config.DataBaseName)
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    try:
        result=cursor.execute(sql)
        db.commit()
        return result
    except:
        pass
    db.close()
    return None

def sqlUpdate(sql):
    db=pymysql.connect(host=config.hostName,user=config.DataBaseUser,password=config.DataBasePassword,database=config.DataBaseName)
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    try:
        result=cursor.execute(sql)
        db.commit()
        return result
    except:
        pass
    db.close()
    return None

# def sqlUpdate(sql):


if __name__=='__main__':
    pass