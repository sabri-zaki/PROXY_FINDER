#!/usr/bin/env python
# -*- coding: utf-8 

Green="\033[1;33m"
Blue="\033[1;34m"
Grey="\033[1;30m"
Reset="\033[0m"
Red="\033[1;31m"
Purple="\033[0;35m"


print " "+Green+"   ############################"
print " "+Green+"   PROXY FINDER FOR 1001_ACCOUNT"
print " "+Green+"   ############################"
print " "+Green+"   [+]: Developer: SABRI ZAKI :[+]"
print " "+Green+"   ############################"
print ""
print " "+Grey+" █║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║█"
print "       "+Green+" 1001_ACCOUNT WAS HEAR"
print "           "+Blue+"" 

import time
import itertools
import threading
import sys

done = False
 
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rWAIT A MOMENT I WILL DO IT QUICKLY ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('')

t = threading.Thread(target=animate)
t.start()

 
done = True

print ""+Purple+"---> I FOUND THESE......."


print""+Blue+""


import requests
from bs4 import BeautifulSoup

proxyDomain = "https://free-proxy-list.net" 

system = requests.get(proxyDomain)

mranonymous_systemSoup = BeautifulSoup(system.content,'html.parser')

sosBlackhats = mranonymous_systemSoup.find('table',{"id" : "proxylisttable"})

for row in sosBlackhats.find_all('tr'):
    columns = row.find_all('td')
    try:
        print "%s:%s\t%-20s\t%-10s"  % (columns[0].get_text(),columns[1].get_text(),columns[3].get_text(),columns[4].get_text())
    except:
        pass

print" "+Grey+" JUST RUN ME ANYTIME, I WILL REFRESH PROXY LIST < join US on #1001_ACOOUNT GROUP= facebook >" 

    






 

