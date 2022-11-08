
import cmd
import hashlib
from customer.identity import *

from my_util.mysql import *
from my_util.console import * 
from service.bus import *
from service.flight import *
from service.hotel import *

def default_menu():
    menu='''
    [1] to login
    [2] to register
    [3] to exit
    '''
    while(1):
        cmdPrompt(menu)
        choice=input()
        if(choice not in ['1','2','3']):
            error("invalid choice")
            continue;
        if(choice=='1'):
            flag=login()
            if(flag>0):
                customer_menu()
            else:
                error("login failed")
        elif(choice=='2'):
            register()
        else:
            return 



def customer_menu():
    message='''welcome customer'''
    print(message)
    menu='''
    [1] to reserve
    [2] to view information
    [3] to query route integrity
    [4] to logout
    '''
    while(1):
        cmdPrompt(menu)
        choice=input()
        if(choice not in ['1','2','3','4']):
            error("invalid choice")
            continue
        if(choice=='1'):
            reserve()
        elif(choice=='2'):
            print("all reserved:")
            viewReserved()
            print("route:")
            viewRoute()
        elif(choice=='3'):
            queryRouteIntegrity()
        else:
            logout()
            return 

def debuglogin():
    global currentCustID
    global currentCustName
    currentCustID=2
    currentCustName="sjh"

def login():
    global currentCustID
    global currentCustName
    cmdPrompt("username")
    custName=input()
    cmdPrompt("password")
    custPassword=input()
    cryptedPassword=hashlib.md5(custPassword.encode()).hexdigest()

    sql="select * from CUSTOMERS where custName='%s' and custPassword='%s' "%(custName,cryptedPassword)
    result=sqlGetOneTuple(sql)
    if(result==None):
        error("no such customer,login failed")
        return -1
    currentCustID=result['custID']
    currentCustName=result['custName']
    success("customer %s login successfully"%currentCustName)
    return 1

       
def register():
    cmdPrompt("username")
    custName=input()
    sql="select * from CUSTOMERS where custName= '%s' " % (custName)
    result=sqlGetOneTuple(sql)
    if(result!=None):
        error("customer %s already exists"%custName)
        return -1
    cmdPrompt("password")
    custPassword1=input()
    cmdPrompt("password again")
    custPassword2=input()
    if(custPassword1!=custPassword2):
        error("password is not consistent")
        return 0
    cryptedPassword=hashlib.md5(custPassword1.encode()).hexdigest()
    sql="insert into CUSTOMERS(custName,custPassword) values('%s','%s'); "%(custName,cryptedPassword)
    result=sqlInsert(sql)
    if(result==None):
        error("operation failed")
        return -1
    success("customer %s fully registered"%custName)
    return 1
    
def logout():
    global currentCustID
    global currentCustName
    if(currentCustID==0):
        error("no customer login")
        return -1
    cmdPrompt("enter [Yes] for logout")
    flag=input()
    if(flag=="Yes"):
        currentCustID=0
        currentCustName=""
        success("customer %s logout "%currentCustName)
        return 1
    error("invalid input logout canceled")
    return -1

def reserveBus():
    global currentCustName
    global currentCustID
    if(currentCustID==0):
        error("no customer login")
        return 0
    sql="select * from BUS"
    result=sqlGetPrettyTable(sql)
    print(result)

    cmdPrompt("input complete location that you want to reserve")
    location=input()
    sql="select * from BUS where location='%s'"%location
    result=sqlGetPrettyTable(sql)
    print(result)
    result=sqlGetOneTuple(sql)
    if(result==None):
        error("no such bus")
        return -1
    numAvail=result['numAvail']
    if(numAvail<=0):
        error("full seats")
        return -1
    cmdPrompt("%d seats left,[Sure] to ensure this reserve"%numAvail)
    ensure=input()
    if(ensure!='Sure'):
        error("reservation cancled")
        return -3
    sql="update BUS set numAvail=numAvail-1 where location='%s'"%location
   
    result=sqlUpdate(sql)
    if(result==None):
        error("operation1 failed")
        return -1
    sql="insert into reservations (resvKey,custName,resvType) values('%s','%s',%d)"%(location,currentCustName,3)
    
    result=sqlInsert(sql)
    if(result==None):
        error("operation2 failed")
        return -1
    success("successfully reserved")
    return 1

def reserveHotel():
    global currentCustName
    global currentCustID
    if(currentCustID==0):
        error("no customer login")
        return 0
    sql="select * from HOTELS";
    result=sqlGetPrettyTable(sql)
    print(result)

    cmdPrompt("input complete location of hotel that you want to reserve")
    location=input()
    sql="select * from HOTELS where location='%s'"%location
    result=sqlGetPrettyTable(sql)
    print(result)
    result=sqlGetOneTuple(sql)
    if(result==None):
        error("no such hotels")
        return -1
    
    cmdPrompt("[Sure] to ensure this reserve")
    ensure=input()
    if(ensure!='Sure'):
        error("reservation canceled")
        return -3
    sql="update HOTELS set numRooms=numRooms-1 where location='%s'"%location
    result=sqlUpdate(sql)
    if(result==None):
        error("operation failed")
        return -1
    sql="insert into reservation(resvKey,custName,resvType) values('%s','%s','%s')"%(location,currentCustName,2)
    result=sqlInsert(sql)
    if(result==None):
        error("operation failed")
        return -1
    success("successfully reserved")
    return 1


def reserveFlight():
    global currentCustName
    global currentCustID
    if(currentCustID==0):
        error("no customer login")
        return 0
    sql="select * from FLIGHTS"
    result=sqlGetPrettyTable(sql)
    print(result)

    cmdPrompt("input complete flightNum to reserve")
    flightNum=input()
    sql="select * from FLIGHTS where flightNum='%s'"%flightNum
    result=sqlGetPrettyTable(sql)
    print(result)
    result=sqlGetOneTuple(sql)
    if(result==None):
        error("input error or no flight avalible")
        return -1
    cmdPrompt("[Sure] to ensure this reserve")
    ensure=input()
    if(ensure!='Sure'):
        error("reservation canceled")
        return -3
    sql="updata FLIGHTS set numAvail=numAvail-1 where flightNum='%s'"%flightNum
    result=sqlUpdate(sql)
    if(result==None):
        error("operation failed")
        return -1
    sql="insert into reservations(resvKey,custName,resvType)values('%s','%s',%d)"%(flightNum,currentCustName,1)
    result=sqlInsert(sql)
    if(result==None):
        error("operation failed")
        return -1
    success("successfully reserved")
    return 1


def viewReserved():
    if(currentCustID==0):
        error("no customer failed")
        return -1
    sql="select * from reservations where custName='%s'"%currentCustName
    result=sqlGetPrettyTable(sql)
    print(result)
    return 1

def viewRoute():
    sql="select FromCity,ArivCity from reservations join flights on reservations.resvKey=flights.flightNum where custName='%s'"%currentCustName
    result=sqlGetPrettyTable(sql)
    print(result)
    return 1

def queryRouteIntegrity():
    cmdPrompt("input From city:")
    FromCity=input()
    cmdPrompt("input Arive City:")
    ArivCity=input()
    sql="select * from reservations join flights on reservations.resvKey=flights.flightNum where custName='%s' and FromCity='%s' and ArivCity='%s' "%(currentCustName,FromCity,ArivCity)
    result=sqlGetOneTuple(sql)
    if(result==None):
        error("no route reserved")
        return -1
    success("route exists")
    return 1


def reserve():
    global currentCustID
    global currentCustName
    if(currentCustID==0):
        error("no customer login")
        return 0
    reserveMenu='''
    [1] for reserve flight
    [2] for reserve hotel
    [3] for reserve bus
    '''
    cmdPrompt(reserveMenu)
    choice=input()
    if(choice not in ['1','2','3']):
        error("invalid choice")
        return 0
    result=0
    if(choice=='1'):
        result=reserveFlight()
    elif(choice=='2'):
        result=reserveHotel()
    else:
        result=reserveBus()
    if(result!=0):
        success("%s successfully reserved %s"%(currentCustName,result))
    
if __name__=='__main__':
    login()