from PIL import Image

#Carga imagen
imagen = Image.open('comida_indu.png')
#Convertir a escala de grises
imagen_escala_de_grises = Image.open('comida_indu.png').convert('L')
