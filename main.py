import pyfiglet
import sys
import socket
from datetime import datetime
 
def check_ports(ports):
    if len(ports) > 1:
        start = ports[0]
        end = ports[1]
    else:
        start = ports[0]
        end = ports[0]+1
        
    try:
        for port in range(start,end):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1e-2)

            # returns an error indicator
            result = s.connect_ex((target,port))
            if result ==0:
                print("Port {} is open".format(port))                
            s.close()
            
    except KeyboardInterrupt:
            print("\n Exiting Program !!!!")
            sys.exit()
    except socket.gaierror:
            print("\n Hostname Could Not Be Resolved !!!!")
            sys.exit()
    except socket.error:
            print("\ Server not responding !!!!")
            sys.exit()    

def create_banner(target):
    # Add Banner
    print("-" * 50)
    print("Scanning Target: " + target)
    print("Scanning started at:" + str(datetime.now()))
    print("-" * 50)
    

if __name__ == "__main__":  
    ascii_banner = pyfiglet.figlet_format("Python\nPort Scanner")
    print(ascii_banner)
    
    # Defining a target
    host = input("Enter the target ip or the start ip and end ip of a network (use , as separator): ").split(",")
    ports = input("Enter the target port or a range of ports (use , as separator): ").split(",")
    
    if len(host) > 1:
        while 1:
            None
    else:
        # translate hostname to IPv4
        target = socket.gethostbyname(host[0])

        create_banner(target)
        check_ports([int(x) for x in ports])
                    



# Project inspired by https://www.geeksforgeeks.org/port-scanner-using-python/

