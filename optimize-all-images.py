from PIL import Image
import os

ruta = './listings/'

alto = 800 # Aquí puedes cambiar la altura que desees
ancho = 1200 # Aquí puedes cambiar el ancho que desees

for root, dirs, files in os.walk(ruta):
    for filename in files:
        if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
            img_path = os.path.join(root, filename)
            with Image.open(img_path) as img:
                img_resized = img.resize((ancho, alto))
                img_resized.save(img_path)