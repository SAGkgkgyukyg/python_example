import os
import socket

udp_ip = "Your IP"
udp_port = 8888
MESSAGE = '{"From":"Jack","Message":"Hello World"}'
sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP
sock.sendto(MESSAGE.encode('utf-8'), (udp_ip, udp_port))

def send_splunk(Message):
    sock.sendto(Message.encode('utf-8'), (udp_ip, udp_port))

