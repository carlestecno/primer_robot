import socket
import pygame

# Configuració del client WiFi
SERVER_IP = '192.168.1.99'  # IP de la teva Raspberry Pi
PORT = 65432

# Crear socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, PORT))

# Inicialització de pygame
pygame.init()
screen = pygame.display.set_mode((100, 100))  # Necessari per inicialitzar l'entrada de teclat

try:
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    client_socket.sendall(b'w')
                elif event.key == pygame.K_s:
                    client_socket.sendall(b's')
                elif event.key == pygame.K_x:
                    client_socket.sendall(b'x')
finally:
    client_socket.close()
    pygame.quit()
