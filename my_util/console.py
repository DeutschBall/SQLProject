import os
from prettytable import *
def cmdPrompt(str):
    # os.system("cls")
    print(str)
    print(">",end='')
def error(str):
    print("error:%s"%str)
def success(str):
    print("success:%s"%str)

