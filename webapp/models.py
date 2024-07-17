from django.db import models
import uuid

class PDFFile(models.Model):
    file = models.FileField(upload_to='pdfs/')
    translated_file = models.FileField(upload_to='translated_pdfs/', null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    unique_tag = models.CharField(max_length=100, unique=True, default=uuid.uuid4)

