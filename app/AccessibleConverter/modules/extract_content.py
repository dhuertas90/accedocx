import os
import docx
import docx2txt
from docx.opc.constants import RELATIONSHIP_TYPE as RT

""" Module extract content
+ Input: file docx
+ Detect content: img, para, hyper
+ Output: file txt

"""

def processing_file(file, image_path):
    """
    Abre el documento, extrae las imágenes, procesa el texto.
    Si es una imagen, guarda el id.
    Si es un hipervinculo, guarda cada dato del mismo.
    """    
    # Extraer imagenes hacia carpeta img_folder/
    docx2txt.process(file, image_path)
  
    # Abrir documento.
    doc = docx.Document(file)

    rels = {}
    for r in doc.part.rels.values():
        if isinstance(r._target, docx.parts.image.ImagePart):
            rels[r.rId] = os.path.basename(r._target.partname)
                
    # Procesar el texto
    dic_content = {}
    numPara = 1

    for paragraph in doc.paragraphs:
        # Si se encuentra una imagen.
        if 'Graphic' in paragraph._p.xml:
            # Obtener rId de la imagen
            for rId in rels:
                if rId in paragraph._p.xml:
                    # Recordar, ubicacion en os.path.join(img_path, rels[rId])
                    content = rId
        elif paragraph.style.name.startswith('List'):
            # if paragraph.style.name == 'List Bullet':
            #     list_type = 'List Bullet'
            # else:
            list_type = 'List Bullet'
            content = f"rList-{paragraph.text}-{list_type}"
        else:
            # No es una imagen
            # Busco hyperlink
            if bool(paragraph._element.xpath(".//w:hyperlink")):
                for link in paragraph._element.xpath(".//w:hyperlink"):
                    inner_run = link.xpath("w:r", namespaces=link.nsmap)[0]
                    h_text = inner_run.text
                    h_rId = link.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id")
                    h_url = doc._part.rels[h_rId]._target
                    text = paragraph.text + "\n" + h_text + ": " + h_url
            else:
                text = paragraph.text
            content = text
        dic_content[numPara] = content
        numPara+=1
    with open("AccessibleConverter/contenido.txt", 'w', encoding='utf-8') as f:
        for key, value in dic_content.items():
            f.write("%s\n" % value)