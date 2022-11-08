from my_util.mysql import *
def sqlAddFlight(flightNum,price,numSeats,FromCity,ArivCity):
    sql="insert into FLIGHTS(flightNum,price,numSeats,numAvail,FromCity,ArivCity) values('%s',%d,%d,'%s','%s')"%(flightNum,price,numSeats,numSeats,FromCity,ArivCity)
    result=sqlExecutor(sql)
    return result
def sqlgetAllFlight():
    sql="select * from FLIGHTS"
    result=sqlGetTable(sql)
    return result
def sqlQueryFlightNum(flightNum):
    sql="select * from FLIGHTS where flightNum='%s'"%flightNum
    result=sqlGetTable(sql)
    return result

def sqlReserveFlightNum(flightNum):
    sql="update FLIGHTS set numAvail=numAvail-1 where flightNum='%s'"%flightNum
    result=sqlExecutor(sql)
    return result
