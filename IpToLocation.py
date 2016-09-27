#Marcin Cherek
import requests
import sys
import re
import socket

'''
Module for getting geoData of a Ip
Adress.
'''


def rightIpPattern(ip):
    '''
    Checks for the right ipv4 pattern.
    '''
    return re.match("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$",ip)!=None

def hasInternetConnection(host="8.8.8.8", port=53, timeout=3):
    '''
    Checks if it's possible to connect with a google sever.
    '''
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except Exception as ex:
        print(ex)
        return False

def getData(ip,what='country_name'):
    '''
    Returns the Location datas of the given Ip
    what can be:
    *region_code
    *ip
    *time_zone
    *city
    *country_code
    *region_name
    *country_name
    *metro_code
    *latitude
    *longtitude
    '''
    if(hasInternetConnection() and rightIpPattern(ip)):
        response = requests.get("http://freegeoip.net/json/"+ip)
        json = response.json()
        if(what!="everything"):
            return json[what]
        else:
            return json
    else:
        print("Fail, check Ip adress and you internet connection")

if __name__== "__main__":
    print(getData(sys.argv[1],sys.argv[2]))
