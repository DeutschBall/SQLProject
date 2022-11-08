from my_util.mysql import *
global currentCustID
currentCustID=0
global currentCustName
currentCustName=''


def sqlGetCustID(custName):
    sql="select custID from CUSTOMERS where custName= '%s' " % (custName)
    result=sqlGetOneTuple(sql)
    if(result==None):
        error("no such customer")
        return -1
    try:
        return result[0][0]
    except:
        return 0

def sqlExistCustName(custName):
    return sqlGetCustID(custName)

def sqlCheckIdentity(custName,cryptedPassword):
    sql="select custID from CUSTOMERS where custName='%s' and custPassword='%s' "%(custName,cryptedPassword);
    result=sqlExecutor(sql)
    try:
        return result[0][0]
    except:
        return 0

def sqlReigisterCust(custName,cryptedPassword):
    sql="insert into CUSTOMERS(custName,custPassword) values('%s','%s'); "%(custName,cryptedPassword)
    result=sqlExecutor(sql)
    return result        

def sqlgetAllCust():
    sql="select * from CUSTOMERS"
    result=sqlGetTable(sql)
    # print(result)
    return result