from unittest import result
import pyfiglet
import sys
import socket
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("w 3 b r a 1 n")
print(ascii_banner)

target = input(str("IP or Domain: "))

print ("-" * 50)
print ("Scanning: " + target)
print (str(datetime.now()))
print("-" * 50)

try:
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        
        result = s.connect_ex((target,port))
        if result==0:
            print("[*] Port {} is open".format(port))
        
        s.close()
        
except KeyboardInterrupt:
    print("\n Exiting")
    sys.exit()
    
except socket.error:
    print("\ Host not responding")
    sys.exit