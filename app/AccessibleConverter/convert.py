from docx import Document
from modules.functions import writeParagraph
from modules.imagenes import insertar_imagen
from modules.extract_content import *

def convert(content, name, author):
    """Recibe un diccionario con el contenido del formulario

    Args:
        obj_doc (Book Object): Documento alojado en el servidor    
        content (List): 
            Contenido del formulario para ser procesado
            [('header', 'si', 'h1'), ('image', '1', 'desc'), ...]
    """
    document = Document()
    core_properties = document.core_properties
    core_properties.author = author

    path_project = os.getcwd()
    path_docs_folder = f"{os.path.join(path_project, 'media','documentos', 'docs','')}"
    # Ubicacion carpeta imagenes a guardar
    images_folder = os.path.join(path_project, 'app', 'static', 'images')
    # Abrir archivo txt con el contenido del documento origen
    filename = os.path.join(path_project, 'AccessibleConverter', 'contenido.txt')

    with open(filename, 'r', encoding='utf-8') as f:
        # Contador de las imagenes existentes, usado para el nombre completo.
        img_number = 1

        for line in f.readlines():
            # Quitar quiebres de lineas.
            c_line = line.rstrip('\n') 
            # Quitar renglones vacíos
            whitespace_line = c_line.replace(" ", "")
            if whitespace_line == '':
                pass
            else:
                if c_line.startswith("rId"):
                    # Deteccion de imagenes
                    # Cargar imagen e insertar en el documento.
                    insertar_imagen(document, images_folder, img_number)
                    img_number += 1
                    # Obtener descripcion
                    for elem in content:
                        if elem[0] == 'image':
                            description = elem[2] + '\n'
                            content.remove(elem)
                            break
                    writeParagraph(document, description)
                elif c_line.startswith("rList"):
                    # Es un elemento de un listado
                    infoList = c_line.split("-")
                    itemList = infoList[1]
                    typeList = infoList[2]
                    writeParagraph(document, itemList, style=typeList, indentation=1)
                elif len(c_line) <= 40 and not any(map(c_line.__contains__, ["http","www.",".com",".org"])):
                    is_header = False
                    print(f"CONTENIDO formulario: \n{content}.")
                    for elem in content:
                        print("*"*15)
                        print(f"Contenido de elem:\n{elem}")
                        if elem[0] == 'header':
                            print("...Detectado como posible header...")
                            if elem[1] == "no":
                                print(f"No es header (debería ser NO): {elem[1]}.\nTexto: {c_line}.")
                                writeParagraph(document, c_line)
                                content.remove(elem)
                                print("*"*15)
                            else:
                                print(f"Es un header (debería ser SI): {elem[1]}.\nTexto: {c_line}.\nNivel será: {elem[2]}.")
                                is_header=True
                                h_level = elem[2]
                                content.remove(elem)
                            break
                    if is_header:
                        print(f"Encabezado: {c_line}.\nEs header (si): {elem[1]}. Nivel: {h_level}.")
                        # Agregar encabezado
                        document.add_heading(c_line+"\n", level=int(h_level))
                        print("*"*15)
                else:
                    writeParagraph(document, c_line)
    url_doc = path_docs_folder + name + '.docx'
    core_properties.title = name
    core_properties.language = 'es-AR'
    document.save(url_doc)
    return url_doc
