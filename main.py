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
            service = ""
            try:
                service = socket.getservbyport(port, "tcp")
            except:
                None
                
            if result ==0:
                print("Port {}/{} is open".format(port,service))                
            s.close()
            
    except KeyboardInterrupt:
            print("\n Exiting Program !!!!")
            sys.exit()
    except socket.gaierror:
            print("\n Hostname Could Not Be Resolved !!!!")
            sys.exit()
    except socket.error:
            print("\n Server not responding !!!!")
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
    hosts = input("Enter the target ip or the start ip and end ip of a network (use , as separator): ").split(",")
    
    if input("Just check the well know ports(yes/no):") != "yes":
        ports = input("Enter the target port or a range of ports (use , as separator): ").split(",")
    else:
        ports = ["1","1024"]
    
        
    if len(hosts) > 1:
        for host in hosts:
            target = socket.gethostbyname(host)
            create_banner(target)
            check_ports([int(x) for x in ports])
            print("\n")

    else:
        # translate hostname to IPv4
        target = socket.gethostbyname(hosts[0])

        create_banner(target)
        check_ports([int(x) for x in ports])

        
                    



# Project inspired by https://www.geeksforgeeks.org/port-scanner-using-python/


