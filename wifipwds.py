# This script dumps all wifi passwords saved in windows computer.
# Tested on: Windows 10 

from prettytable import PrettyTable
import os

options ={'es':['Perfiles de usuario','Perfil de todos los usuarios     :','Contenido de la clave  :'],
          'en':['User profiles','All User Profile     :','Key Content  :']}

def parse_ssid(text):
    wifinetworks = {}
    sp1 = text.split(options[LANGUAGE][0])
    sp2 = sp1[1].split(options[LANGUAGE][1])
    wifinetworks = {item: 'Not Found!' for item in sp2} 
    return wifinetworks

def get_pwd(access_points):
    ap = {}
    txt = options[LANGUAGE][2]
    for item in access_points.keys():
        ssid = item.replace(' ','').replace('\n','')
        cmd_reply= os.popen('netsh wlan show profile name='+ssid+' key=clear').read()
        if (cmd_reply != 'No se encuentra el perfil "'+ssid+'" en el sistema.\n') and (txt in cmd_reply):
            content = cmd_reply[cmd_reply.find(txt) + len(txt):].split('\n')
            ap[ssid] = content[0]
    return ap

def display(result,filename):
    
    line = 1
    with open(filename,'w') as file:
        file.write( '*'*60)
        file.write('\n*   W   i   f   i   -   P   a   s   s   w   o   r   d   s  *\n')
        file.write( '*'*60)
        file.write( '\n')

        t = PrettyTable(['#','BSSID', 'Password'])
        for (k,v) in result.items():
            t.add_row([line,k, v])
            line += 1  
        file.write('{0}\n'.format(t))
    file.close()

def get_language():
    lng = 'en'
    reply = os.popen('cmd').read()
    if 'Todos los derechos reservados.' in reply:
        lng = 'es'
    return lng

if __name__=='__main__':
    LANGUAGE = get_language()
    filename = 'wifi-credentials.txt'
    result = os.popen('netsh wlan show profile').read()
    wifissid = parse_ssid(result)
    credentials = get_pwd(wifissid)
    display(credentials,filename)
          
