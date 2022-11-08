from my_util.mysql import *
from my_util.console import *
from prettytable import *
from service.bus import *

# create table if not exists FLIGHTS(
#     flightNum varchar(255) unique,
#     price int,
#     numSeats int,
#     numAvail int default 0,
#     FromCity varchar(255),
#     ArivCity varchar(255),
#     primary key(flightNum)
# );
def newFlight():
    cmdPrompt("flightNum:")
    flightNum=input()
    cmdPrompt("price per seat:")
    price=int(input())
    cmdPrompt("numSeats:")
    numSeats=int(input())
    cmdPrompt("FromCity:")
    FromCity=input()
    cmdPrompt("ArivCity:")
    ArivCity=input()
    sql="insert into FLIGHTS(flightNum,price,numSeats,numAvail,FromCity,ArivCity) values('%s',%d,%d,%d,'%s','%s')"%(flightNum,price,numSeats,numSeats,FromCity,ArivCity)
    result=sqlInsert(sql)
    if(result==None):
        error("add new Flight failed")
        return -1
    success("add new Flight succeed")
    return 1


def newBus():
    cmdPrompt("location:")
    location=input()
    cmdPrompt("price:")
    price=int(input())
    cmdPrompt("numBus:")
    numBus=int(input())
    sql="insert into BUS(location,price,numBus,numAvail) values('%s',%d,%d,%d)"%(location,price,numBus,numBus)
    result=sqlInsert(sql)
    if(result==None):
        error("add new bus failed")
        return -1
    success("add new bus succeed")
    return 1

def newHotel():
    cmdPrompt("location:")
    location=input()
    cmdPrompt("price:")
    price=int(input())
    cmdPrompt("numRooms:")
    numRooms=int(input())
    sql="insert into HOTELS(location,price,numRooms,numAvail)values('%s',%d,%d,%d)"%(location,price,numRooms,numRooms)
    result=sqlInsert(sql)
    if(result==None):
        error("add new Hotel failed")
        return -1
    success("add new hotel succeed")
    return 1




def viewAllService():
    sql="select * from FLIGHTS"
    allFlight=sqlGetPrettyTable(sql)

    sql="select * from HOTELS"
    allHotel=sqlGetPrettyTable(sql)

    sql="select * from BUS"
    allBus=sqlGetPrettyTable(sql)

    sql="select * from CUSTOMERS"
    allCustomers=sqlGetPrettyTable(sql)

    sql="select * from RESERVATIONS"
    allReserve=sqlGetPrettyTable(sql)

    print(allFlight)
    print(allHotel)
    print(allBus)
    print(allCustomers)
    print(allReserve)

def sqlInteractive():
    
    while(1):
        cmdPrompt("[q] to quit:")
        sql=input()
        if(sql=='Q'):
            return 0
        result=sqlGetPrettyTable(sql)
        if(result==None):
            error("you fool!what did you imput?")
        else:
            print(result)
    return 1