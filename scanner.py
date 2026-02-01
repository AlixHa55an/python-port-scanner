import socket
import threading
import datetime

SERVICES = {
21: "FTP",
22: "SSH",
23: "Telnet",
25: "SMTP",
53: "DNS",
80: "HTTP",
110: "POP3",
143: "IMAP",
443: "HTTPS",
3306: "MySQL",
3389: "RDP"
}

print_lock = threading.Lock()

def port_scan(ip,port,open_port):

    try:
       print(f"Scanning...IP{ip} on port{port}")
       sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
       sock.settimeout(1)

       result = sock.connect_ex((ip,port))

       if result == 0:
        services = SERVICES.get(port,"Unknown Service")

        with print_lock:
            print(f"[OPEN] port{port},({services})") 
            open_port.append((port,services))
        
       sock.close()  
    except:
       pass     


def main():
   print("=== FAST MULTI-THREADED PORT SCANNER ===")

   IP = input("Enter your IP address :\n")

   try:
        start_port = int(input("Enter the start port : \n"))
        end_port = int(input("Enter the end port :\n"))
   except ValueError:
        print("Ports must be valid numbers !!")
        return
   

   print(f"\nScanning {IP} from port {start_port} to {end_port}\n")

   start_time = datetime.datetime.now()

   open_port = []
   Threads = []

   for port in range(start_port, end_port + 1):
    
      thread = threading.Thread(
        target=port_scan,
        args=(IP, port, open_port)
       )
      Threads.append(thread)
      thread.start()

   for Thread in Threads:
      thread.join()   

   end_time = datetime.datetime.now()

   Total_time = end_time - start_time

   print("\n=== Scan Complete ===")
   print(f"Open ports found: {len(open_port)}")
   print(f"Time taken: {Total_time}")


   if open_port:
    print("\nOpen Ports List:")
    for port, service in open_port:
       print(f" - Port {port} ({service})")  


if __name__ == "__main__":
   main()
        
   
   


