from docx import Document

# ChatGPT

def detectar_listas(documento):
    doc = Document(documento)
    listas = []

    for paragraph in doc.paragraphs:
        if paragraph.style.name.startswith('List'):
            listas.append(paragraph.text)

    return listas

# Uso del ejemplo:
listas_encontradas = detectar_listas('nombre_documento.docx')
for lista in listas_encontradas:
    print(lista)
