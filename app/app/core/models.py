from django.db import models


class Documento(models.Model):
    titulo = models.CharField(max_length=100, null=False)
    autor = models.CharField(max_length=100, null=False)
    doc = models.FileField(upload_to='documentos/docs/', null=False)
    nombre_accesible = models.CharField(default='', max_length=100)
    
    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.doc.delete()
        super().delete(*args, **kwargs)
    
    def get_titulo(self):
        return self.titulo

    def get_author(self):
        return self.autor
    
    def get_doc(self):
        return self.doc
    
    def get_nombreAccesible(self):
        return self.nombre_accesible