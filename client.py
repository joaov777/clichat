#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import select
import socket
import sys


# How to run: python3 client.py [SERVER_PORT] [SERVER_HOST]
# How to run from a remote machine: ssh [SERVER_HOST] "python3 ~/Documents/repos/clichat/client.py [SERVER_PORT] [SERVER_HOST]"
# ssh operador@192.168.17.2 -t 'bash -ci' runclient

if __name__ == "__main__":

	if len(sys.argv) == 1:
		HOST = ("localhost", 10000)
	elif len(sys.argv) == 2:
		HOST = ("localhost", int(sys.argv[1]))
	else:
		HOST = (sys.argv[2], int(sys.argv[1]))

	main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	try:
		main_socket.connect(HOST)
		sys_msg = "Connected to {} : {}".format(HOST[0],HOST[1])
		#sys_msg,'yellow',attrs=['bold']
		#sys.stdout.write("Connected to " + HOST[0] + ":" + str(HOST[1]) + '\n')
		sys.stdout.flush()
	except:
		sys_msg = "Unable to connect to {} : {}".format(HOST[0],HOST[1])
		#sys_msg,'red',attrs=['bold']
		sys.stdout.flush()
		exit(2)

	nick = None
	while not nick:
		nick = input("Choose a nick: ")
	print("Hello, {}. Press [ENTER] to start. ".format(nick))
	#print("")

	# manda uma mensagem de boas vindas pro server
	send_msg = "[[>> {} joined!! <<]]\n".format(nick)
	main_socket.send( send_msg.encode() )

	while True:
		prompt = "{}> ".format(nick)
		#print(prompt)
		msg = None
		read_buffers = [sys.stdin, main_socket]
		try:
			read_list, write_list, error_list = select.select(read_buffers, [], [])

			for sock in read_list:
				if sock == main_socket:
					data = sock.recv(4096)
					if data:
						data = data.decode()
						sys.stdout.write(data)
						sys.stdout.flush()
					else:
						print("Disconnected from server!")
						exit(2)
				else:
					msg = sys.stdin.readline()
					send_msg = "{}{}".format(prompt, msg)
					#sys.stdout.write("You> " + msg)
					#sys.stdout.flush()
					main_socket.send( send_msg.encode() )

		except KeyboardInterrupt:
			print("Disconnected from server!")
			exit(1)
