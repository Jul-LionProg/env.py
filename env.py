import argparse, socket
from datetime import dateti

MAX_BYTES = 65535

def servidor(porta):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Cria um socket simples 
    sock.bind(('127.0.0.1', porta)) # Solicita um endereço de rede UDP
        print('Servidor >> Escutando no IP e porta {}'.format(sock.getsockname()))
    while True: # Executa repetidamente recvfrom()
        
