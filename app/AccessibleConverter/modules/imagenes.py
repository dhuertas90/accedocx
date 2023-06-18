from docx.shared import Inches
import os, os.path
from PIL import Image
from pathlib import Path

def path_actual():
    raiz = Path(__file__).resolve().parents[1]
    return raiz

def verificar_extension(path):
    extension = ".png"
    for f in os.listdir(path):
        nom = os.path.splitext(f)[0]
        ext = os.path.splitext(f)[1]
        if ext.lower() != extension:

            # Path de la imagen: Nombre sin extension
            nom_imagen = f'{path}\{nom}'

            imagen = Image.open(rf'{nom_imagen}{ext}')
            imagen.save(rf'{nom_imagen}.png')
            os.remove(rf'{nom_imagen}{ext}')

def create_url_image(img_path, num):
    """Genera url completa de la imagen

    Args:
        img_path (string): ubicacion de la carpeta contenedora de imágenes
        num (int): numero correspondiente al nombre de la imagen

    Returns:
        string: url completa de la imagen
    """
    # DIR = Path(__file__).resolve().parents[1]
    # parent = os.path.dirname(DIR)
    # real = os.path.join(DIR,'img_folder')

    image_complete = '{}{}{}.png'.format(img_path,'\image',num)
    return image_complete

def insertar_imagen(doc, img_path, num):
    """ Agrega una imagen al documento

    Args:
        doc (Document): Objeto Documento
        img_path (String): ubicacion de la carpeta contenedora de imágenes
        num (int): numero correspondiente al nombre de la imagen

    img_path : path\img_folder
    num : int
    
    """
    image_complete = create_url_image(img_path, num)

    doc.add_picture(image_complete, width=Inches(4))
