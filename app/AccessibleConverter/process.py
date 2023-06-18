from modules.extract_content import *
from modules.imagenes import create_url_image, verificar_extension


def process(obj_doc):
    """Procesa el documento del sistema y genera el contenido en un diccionario
    que devuelve a la pagina "Accesibilizando" para el formaulario

    Args:
        obj_doc (File): documento origen

    return:
        dict_content (Dict): diccionario del contenido
    """
    # Encontrar el directorio del documento guardado por la App web
    path_app = os.getcwd()
    path_folder_docs = f"{os.path.join(path_app, 'media','documentos', 'docs')}"
    doc_name = f"{obj_doc.doc.url.split('/')[-1]}"
    doc_path = os.path.join(path_folder_docs, doc_name)

    # Ubicacion carpeta imagenes a guardar
    script_dir = os.path.dirname( __file__ )
    images_folder = os.path.join(path_app, 'app','static','images')
    
    # Procesar documento origen
    processing_file(doc_path,images_folder)
    verificar_extension(images_folder)

    # Obtuve el contenido generado en un txt y las imágenes dentro de una carpeta
    ##################################################


    # Leer el contenido txt y generar el diccionario de contenidos.

    # Abrir archivo txt contenido procesado
    filename = os.path.join(script_dir, 'contenido.txt')
    with open(filename, 'r', encoding='utf-8') as f:
        # f = open(f"{os.path.join(script_dir, 'contenido.txt')}","r")

        # Diccionario que guarda Prints e Inputs
        dict_content = {}
        dict_key = 0
        
        # Contador imagenes
        img_count = 1

        for line in f.readlines():
            # Quitar quiebres de lineas.
            c_line = line.rstrip('\n') 
            # Detectar encabezados
            whitespace_line = c_line.replace(" ", "")
            if whitespace_line == '':
                pass
            else:
                if c_line.startswith("rId"):
                    # Deteccion de imagenes
                    # Obtener la url de la imagen
                    url_image = create_url_image(images_folder, img_count)
                    
                    # Solicitar descripcion (Template)
                    dict_content[dict_key] = ("msg_image", url_image, img_count)
                    dict_key += 1
                    img_count += 1
                elif c_line.startswith("rList"):
                    pass
                elif len(c_line) <= 40 and not any(map(c_line.__contains__, ["http","www.",".com",".org"])):
                    # Consultar nivel de encabezado (Template)
                    dict_content[dict_key] = ("msg_heading", c_line)
                    dict_key += 1
    return dict_content

