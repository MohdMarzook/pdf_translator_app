from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from . import translator

from django.conf import settings
import threading
from webapp.models import PDFFile
from .forms import PDFFileForm
import os,json

def file_upload_view(request):
   if request.method == 'POST':
        file = request.FILES['file']
        fname , fsize, ftype = file.name, file.size, file.content_type

        form = PDFFileForm(request.POST, request.FILES)
        
        if form.is_valid():
            pdf = form.save(commit=False) 
            # place = PDFFile.objects.get(file=f'pdfs/{fname}')
            # print(pdf.unique_tag)
            pdf.save()
            new_file_name = f"{str(pdf.file)[5:-4]}_{request.POST['from']}_{request.POST['to']}.html"
            pdf.translated_html = f"./htmlfiles/{new_file_name}"
            data = {
                "file_name" : f"media/{pdf.file}",
                "new_file_name" : new_file_name,
                "from" : request.POST['from'],
                "to" : request.POST['to']
            }
            pdf.save()
            print(pdf.file , round(fsize/1048576, 2),"mb", ftype)
            translator.initializer(data)

            print("file saved") 

            return JsonResponse({'unique_tag': str(pdf.unique_tag)})
        
        return JsonResponse({'error': 'Invalid form'}, status=400)

def index(request):
    with open(os.path.join(settings.BASE_DIR, 'static/json/lang.json')) as file:
        data_file = json.load(file)
    form = PDFFileForm()
    context = {
        'form' : form,
        'langs' : data_file
        }
    return render(request, 'webapp/home.html', context)

def download_file(request, unique_tag):
    try:
        pdf_record = PDFFile.objects.get(unique_tag=unique_tag)
        # print(pdf_record)
        # print(pdf_record.file)
        response = HttpResponse(pdf_record.translated_html, content_type='text/html')
        # print(pdf_record.translated_file.name)
        # print(pdf_record.file.name)
        response['Content-Disposition'] = f'attachment; filename="{pdf_record.translated_html.name}"'
        return response
    except PDFFile.DoesNotExist:
        return JsonResponse({'error': 'File not found'}, status=404)