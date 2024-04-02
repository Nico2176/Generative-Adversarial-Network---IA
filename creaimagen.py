from PIL import Image
import matplotlib.pyplot as plt
import os

# Ruta al directorio que contiene las imágenes
ruta_directorio = './Animales generados/Caballos'

# Listar todos los archivos en el directorio
archivos = os.listdir(ruta_directorio)

# Filtrar solo los archivos de imagen (por ejemplo, en formato PNG)
archivos_imagenes = [archivo for archivo in archivos if archivo.endswith('.png')]

# Lista para almacenar las imágenes
imagenes = []

# Cargar las imágenes y almacenarlas en la lista
for nombre_archivo in archivos_imagenes:
    ruta_imagen = os.path.join(ruta_directorio, nombre_archivo)
    imagen = Image.open(ruta_imagen)
    imagenes.append(imagen)

# Crear una figura para mostrar las imágenes en una fila
fig, axs = plt.subplots(1, len(imagenes), figsize=(15, 3))  # Cambia el tamaño según sea necesario

# Iterar sobre las imágenes y mostrarlas en fila
for i, imagen in enumerate(imagenes):
    axs[i].imshow(imagen)
    axs[i].axis('off')

plt.tight_layout()
plt.show()