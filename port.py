import pyfiglet
import sys
import socket
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

#defining a target 
if len(sys.argv) == 2:
    print("-" *50)
    target = input("INPUT THE target ip:")
else:
    print("Invalid ammount of Argument")
    
#add banner
print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at: " + str(datetime.now())
print("-" * 50)

try:
    #Scanning port between 1 to 65535
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        
        #returns an error indicator
        result = s.conner_ex((target,port))
        if result == 0:
            print("Port {} is open",format(port))
        s.close()
        
except KeyboardInteruppt:
    print("\n Extting Program...")
    sys.exit()
except socket.error:
    print("\n Server not responding...")
    sys.exit()
