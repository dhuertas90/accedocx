from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage

from .forms import DocumentoForm
from .models import Documento
from .converter import converterPDF, converterDOCX
from pathlib import Path
from datetime import datetime

import os
import sys

script_dir = os.path.dirname( __file__ )
mymodule_dir = os.path.join( script_dir, '..','..','AccessibleConverter' )
sys.path.append( mymodule_dir )

import process, convert

class Home(TemplateView):
    template_name = 'home.html'

def documentos(request):
    documentos = Documento.objects.all()
    return render(request, 'documentos.html', {
        'documentos': documentos
    })

def seccion_subir_documento(request):
    # retorna la página para subir dos tipos de documentos, el doc y el pdf
    return render(request, 'seccion_subir_documento.html')

def seccion_convertir_pdf(request):
    return render(request, 'seccion_convertir_documento_pdf.html')
    
def convert_to_docx(request):
    return render(request, 'convert_to_docx.html')

def upload(request):
    context = {}
    uploaded_file = request.FILES['doc']
    fs = FileSystemStorage()
    context['name'] = fs.save(uploaded_file.name, uploaded_file)
    return context
    
def realizar_conversion(request):
    """ 
    Convierte documento PDF a documento DOCX
    Construye el path origen del archivo PDF y el path destino.
    Ejecuta la funcion converterPDF.
    """
    if request.method == 'POST':
        context = upload(request)   # aca esta el problema, no hay que subirlo
        app_folder = os.getcwd()
        input_path = os.path.join(app_folder,'media', context['name'])
        output_path = os.path.join(app_folder,'media', 'convertidos')
        if not os.path.exists(output_path):
            os.mkdir(output_path)
        
        dirname = datetime.now().strftime('%Y.%m.%d.%H.%M.%S') #2010.08.09.12.08.45
        new_doc = os.path.join(app_folder, 'media', 'convertidos', dirname,'')
        os.mkdir(new_doc)
        new_filename = Path(context['name']).stem

        filename = rf"{new_doc}{new_filename}.docx"
        with open(filename, 'w', encoding='utf-8') as f:
            # f = open(rf"{new_doc}{new_filename}.docx", 'w')
            pass
        output_path = new_doc + new_filename + '.docx'

        converterPDF(input_path, output_path)

        # form = DocumentoForm(request.POST, request.FILES)
        # if form.is_valid():
        #     form.save()
        #     return redirect('documentos')
        # else:
        #     form = DocumentoForm()
    return redirect('documentos')

def upload_documento(request):
    # realiza el guardado real
    if request.method == 'POST':       
        form = DocumentoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('documentos')
    else:
        form = DocumentoForm()
    return render(request, 'subir_doc.html', {
        'form': form
    })

def delete_documento(request, pk):
    if request.method == 'POST':
        documento = Documento.objects.get(pk=pk)
        documento.delete()
    return redirect('documentos')

def get_documento(request, pk):
    """Captura la petición, botón Accesibilizar

    Args:
        request (Request): Method Post
        pk (integer): Numero del documento

    Returns:
        dic: dictionary
        document: Object book
        pk: entero
    """
    if request.method == 'POST':
        documento = Documento.objects.get(pk=pk)

    # dicccionario{
    #  0: ('msg_heading', 'Qué es un archivo'),
    #  1: ('msg_image', 'PATH\\AccessibleConverter\\img_folder\\image1.png', 1),
    # }

    # Abrir el documento del servidor y obtener un diccionario para desplegar en la página "Accesibilizando"
    dict_content = process.process(documento)

    return render(request, 'accesibilizando.html', {
        'dict' : dict_content,
        'document' : documento,
        'pk' : pk,
    })

def convertir(request):
    """Captura la petición, botón Convertir (Accesibilizando),
    obtiene el documento en el sistema y  convierte el doc en un doc accesible

    Args:
        request (Request): Method Post

    Returns:
        url: /documentos  
    """
    contenido = []
    if request.method == 'POST':
        items = request.POST.items()
        next(items)
        for elem in items:
            if elem[0] == 'pk': pass
            elif elem[0] == 'titulo': nombre = elem[1]
            elif elem[0].startswith("encabezado"):
                if elem[0].startswith("encabezado-select"):
                    res = elem[1]
                else:
                    contenido.append(('header',res, elem[1]))
                    res = ''
            elif elem[0].startswith("imagen"):
                if elem[0].startswith("imagen-desc"):
                    desc = elem[1]
                else:
                    contenido.append(('image',elem[1], desc))
                    desc = ''
            else:
                pass
    else:
        pass
    pk=int(request.POST['pk'])
    obj_doc = Documento.objects.get(pk=pk) # obtiene el documento en el sistema
    convert.convert(contenido, nombre, obj_doc.autor) # convierte el doc en un doc accesible
    obj_doc.nombre_accesible = nombre + '.docx'
    obj_doc.save()
    return redirect('/documentos/')

def convert_to_pdf(request, pk):
    # Implementación futura
    if request.method == 'POST':
        documento = Documento.objects.get(pk=pk)
        doc_path = documento.doc.path
        doc_name = documento.titulo
        converterDOCX(doc_name + '.pdf',doc_path)
    return redirect('/documentos/')