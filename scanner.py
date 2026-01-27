import socket

def port_scan(ip,port):

    print(f"Scanning...IP{ip} on port{port}")
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((ip,port))

    if result == 0:
        print(f"[OPEN] port{port}")
    else:
        print(f"[CLOSED] port{port}")   

    sock.close()    

ip = input("Enter your IP Address :\n")
port = int(input("Enter your Port : \n")) 

port_scan(ip,port)

