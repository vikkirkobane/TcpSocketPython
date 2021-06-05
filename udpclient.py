import socket

target_host = "127.0.0.1"
target_port = 80

#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#bind to address and ip
client.bind((target_host, target_port))

print("UDP server up and listening")

#send some data
client.sendto("KIRKOBANE".encode(encoding='utf-8'), (target_host, target_port))

#receive some data
data, addr = client.recvfrom(4069)

msg = ("Message from server %s : %d" % data, addr)
print(msg)

client.close()