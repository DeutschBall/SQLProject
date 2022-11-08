from my_util.mysql import *


def sqlAdminAddBus(location,price,numBus):
    sql="insert into BUS(location,price,numBus,numAvail) values('%s',%d,%d)"%(location,price,numBus,numBus)
    result=(sql)
    return result

def sqlCustomerViewAllBus():
    sql="select * from BUS"
    result=sqlGetPrettyTable(sql)
    return result

def sqlCustomerQueryAllBus():
    sql="select * from BUS"
    result=sqlGetPrettyTable(sql)
    # print(result)
    return result


def sqlQueryBusAt(location):
    sql="select * from BUS where location='%s'"%location;
    result=sqlGetTable(sql)
    # print(result)
    return result


def sqlReserveBusAt(location):
    sql="update BUS set numAvail=numAvail-1 where location='%s'"%location;
    result=sqlGetTable(sql)
    return result



def sqlShowAvailAt(location):
    sql="select numAvail from BUS where location=%s"%location;
    result=sqlGetTable(sql)[0][0]
    return result

def sqlExistBusAt(location):
    sql="select * from BUS where location=%s"%location;
    result=sqlExecutor(sql)[0][0]
    return result