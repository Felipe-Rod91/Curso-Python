# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('\033[031mSite do pudim não está acessível no momento.\033[m')
else:
    print('\033[032mSite do pudim está acessível.\033[m')
