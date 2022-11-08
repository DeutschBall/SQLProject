from email import message
# import os
from admin.admin import *

def main():
    message='''welcome administrator'''
    print(message)
    menu='''
    [1] to add new flight
    [2] to add new hotel
    [3] to add new bus
    [4] to view all informations
    [5] to interactive with the database
    [6] to exit
    '''
    while(1):
        cmdPrompt(menu)
        choice=input()
        if(choice not in['1','2','3','4','5','6']):
            error("invalid choice")
            continue;
        if(choice=='1'):
                
            newFlight()
        elif(choice=='2'):
            newHotel()
        elif(choice=='3'):
            newBus()
        elif(choice=='4'):
            viewAllService()
        elif(choice=='5'):
            sqlInteractive()
        else:
            return 0


# sqlInteractive()
# viewAllService()
# newFlight()
# showAllFlight()
# input()
main()