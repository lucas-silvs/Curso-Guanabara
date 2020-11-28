import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://classroom.google.com/u/0/h')
except:
    print('Deu algum erro')
else:
    print('O site é acessivel')

