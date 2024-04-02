from PIL import Image
import imageio
import os
import time

def cargar_imagenes():
    folder_path = './Animales generados/Vacas'  # Ruta al directorio que contiene las imágenes
    imagenes = []

    # Recorrer el directorio y cargar las imágenes
    for filename in os.listdir(folder_path):
        img_path = os.path.join(folder_path, filename)
        if os.path.isfile(img_path):
            img = Image.open(img_path)
            img = img.resize((128, 128))  # Ajusta el tamaño si es necesario
            imagenes.append(img)

    return imagenes

# Obtener las imágenes
imagenes = cargar_imagenes()

# Crear el GIF
with imageio.get_writer('output.gif', mode='I', duration=2) as writer:
    for img in imagenes:
        img.save('temp.gif')
        image = imageio.imread('temp.gif')
        writer.append_data(image)
        time.sleep(0.5)  # Esperar 0.5 segundos antes de pasar a la siguiente imagen

# Eliminar el archivo temporal
os.remove('temp.gif')