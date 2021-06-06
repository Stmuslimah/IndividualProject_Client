import socket
import time

c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = '192.168.56.103'
port = 8888

c.connect((host,port))

print('\n***_DOMAIN NAME RESOLVER APPLICATION_***\n')

file = open('Details.txt','w')
while True:
	msg = input('\nEnter a Domain / details / \'end\' to exit: ')
	c.sendto(msg.encode('utf-8'),(host,port))

	if msg == "end":
		print('\nConnection ended...')
		False
		time.sleep(1)
		break

	if msg != 'details' and msg != '':
		data, addr  = c.recvfrom(1024)

		if data.decode('utf-8') != 'Not a proper domain':
			print('Resolve to : ', data.decode('utf-8'))
			file.write(msg + ' resolve to ' + data.decode('utf-8') + '\n')
		else:
			print(data.decode('utf-8'))

	elif msg == 'details':
		print('\n*****Previous Details*****')
		file = open('Details.txt','r')
		print(file.read())
		file = open('Details.txt','a')

file.close()
c.close()
