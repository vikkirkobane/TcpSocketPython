import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 10000

#create a socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind to address and ip
server.bind((bind_ip, bind_port))

#server listening to tcp connection
server.listen(5)

print("[*] Listening on %s: %d" % (bind_ip, bind_port))

#client-handling thread
def handle_client(client_socket):
    #print out what client sends
    request = client_socket.recv(1024)
    
    print("[*] Received: %s" % request)
    
    #send back a packet
    client_socket.send("ACK!".encode(encoding='utf-8'))
    
    client_socket.close()

while True:
    client,addr = server.accept()
    
    print("[*] Accepted connection from: %s:%d" % (addr[0],addr[1]))
    
    #client thread to handle incoming data
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()

request.decode()

#close server connection
server.close()