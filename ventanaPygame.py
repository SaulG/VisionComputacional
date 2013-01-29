#Libreria pygame
import pygame

#ancho
width = 640
#altura
height = 480

#Se llama a la funcion init(), esto nos ayuda a inicializar pygame
#para poder usar submodulos de la misma
pygame.init() 

#Se crea la ventana con el ancho y la altura correspondiente
ventana = pygame.display.set_mode((width, height))

#Se colorea en blanco la ventana
ventana.fill(pygame.Color(255, 255, 255))

#Loop infinito
while True:
    #Se agrega el evento de cerrar en la ventana;
    #Si este llega a ser usado esta ventana se cierra
    # es por eso que esta break
    if pygame.QUIT in [e.type for e in pygame.event.get()]:
        break
