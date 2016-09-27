#Marcin Cherek
#version 1.0
#Python 3.4

import os
import sys
import re

'''
<PrefixManager Module>

In the case you are writing a command line tool, this package can
be usefull for you. It is able to manage arguemts. So you can check
if your argument is existing or has it the right data typ or lenght.
You can even check if it has the right pattern.
It is ofcorse possible just to return the plain data, or with
a short report if you wish.
Please read the getDataFromPrefix docString for more
information about the method itself.
Usage:
getDataFromPrefix(pref,args,.....)
Return:
onlydata : data
rep: [boolean(Succesfull),Data,WhatChecked]
'''

def doesPrefixExist(pref,args)->bool:
    '''
    Return's True if the prefix
    exists
    '''
    return pref in args

def getDataType(data):
    '''
    Returns the type of the datas.
    '''
    if(str(data).isdigit()):return int
    elif(len(data)==1):return chr
    elif(data in ["True","False"]):return bool
    else:return str

def __isRightDataTypeofPrefix(data,typ)->bool:
    '''
    Looks if datas have the correct datatype.
    '''
    return getDataType(data)==typ

def __isRightSizeOfData(data,size)->bool:
    '''
    Looks if datas have the right lenght.
    '''
    return len(data)-size

def doesMatchPattern(pat,data)->bool:
    '''
    Looks if data's match the given pattern.
    '''
    return re.match(pat,data)==None

def areArgsOk(args)->bool:
    '''
    Looks if the given arguments can be used.
    '''
    if(isinstance(args,list)!=True):
        return [False," Args should be a list"]
    if(len(args)<1):
        return [False," to fiew args"]
    return [True,""]

def getDataFromPrefix(pref:str, args:list, length:int=-1, typ=None, report:bool = True, pattern:str=None ,multiDim:bool=False, moreThanOne:bool=False,onlydata=False):
    '''
    Searches for the prefix and returns
    the data from it.
    * pref <str>: The prefix , ex: -p
    * args <list>: you commandline Arguments.
    * length <int>: The length the data should be of.
    * typ <type>: The type the data should be of (str,int,chr,bool)
    * report <bool>: Give me the report back.
    * pattern <str>: Maybe the argument should have a pattern?
    * multiDim <bool>: Like this -a dat1 dat2
    * moreThanOne <bool>: returns every data of the same prefix.
    * onlydata <bool>: Just returns the needed data without evaluation of correctness.
    '''
    rep=[]
    ret = areArgsOk(args)
    if(ret[0]==False):return ret
    if(doesPrefixExist(pref,args)==False):
        return [False,"Prefix does not exist"]
    data = [None]
    for i in range(0,len(args)):
        if(args[i].strip()==pref):
           data[0] = args[i+1]
    if(onlydata):return data[0]
    if(typ!=None):
        rep.append("DataType:should be "+str(typ))
        rep.append(__isRightDataTypeofPrefix(data[0],typ))
    if(length!=-1):
        rep.append("DataLenght:should be "+str(length))
        rep.apppend(abs(__isRightSizeOfData(data[0],length))-length==0)
    if(pattern!=None):
        rep.append("DataPattern:should be "+str(pattern))
        rep.append(doesMatchPattern(pattern,data[0]))
    final = [False not in rep]
    if(report):
        data.extend(rep)
        final.extend(data)
        return final
    else:
        return final
