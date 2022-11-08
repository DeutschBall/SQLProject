from my_util.mysql import *
def sqlAddHotel(location,price,numRooms,numAvail):
    sql="insert into HOTELS(location,price,numRooms) values('%s',%d,%d)"%(location,price,numRooms,numAvail)
    result=sqlExecutor(sql)
    return result
def sqlgetAllHotel():
    sql="select * from HOTELS"
    result=sqlGetTable(sql)
    return result

def sqlQueryHotelAt(location):
    sql="select * from HOTELS where location='%s'"%location
    result=sqlGetTable(sql)
    return result
def sqlReserveHotelAt(location):
    sql="update HOTEL set numAvail=numAvail-1 where location='%s'"%location
    result=sqlExecutor(sql)
    return result
