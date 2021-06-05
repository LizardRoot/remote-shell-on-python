import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 3333
s.bind((host, port))
s.listen(1)
conn, addr = s.accept()
print(addr)

while True:
	cmd = input('#> ')
	conn.send(cmd.encode())

	cmd_process = conn.recv(5000)
	cmd_process = str(cmd_process, "cp866")
	print(cmd_process)
