from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from . import translator

from django.conf import settings

from webapp.models import PDFFile
from .forms import PDFFileForm
import os,json

def file_upload_view(request):
   if request.method == 'POST':
        file = request.FILES['file']
        fname , fsize, ftype = file.name, file.size, file.content_type
        form = PDFFileForm(request.POST, request.FILES)
        data = {
            "file_name" : f"media/pdfs/{pdf.file}",
            "new_file_name" : new_file_name,
            "from" : request.POST['from'],
            "to" : request.POST['to']
        }
        new_file_name = f"{str(pdf.file).split('.pdf')[0]}_{request.POST['from']}_{request.POST['to']}.pdf"
        # print(request.POST['from'])
        # print(request.POST['to'])
        
        if form.is_valid():
            pdf = form.save(commit=False) 
            # place = PDFFile.objects.get(file=f'pdfs/{fname}')
            new_file_name = f"{str(pdf.file).split('.pdf')[0]}_{request.POST['from']}_{request.POST['to']}.html"
            pdf.translated_file = f"/htmlfiles/{new_file_name}"
            print(pdf.unique_tag)
            print(pdf.file , round(fsize/1048576, 2),"mb", ftype)
            pdf.save()

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
        response = HttpResponse(pdf_record.file, content_type='application/pdf')
        print(pdf_record.translated_file.name)
        print(pdf_record.file.name)
        response['Content-Disposition'] = f'attachment; filename="{pdf_record.translated_file.name}"'
        return response
    except PDFFile.DoesNotExist:
        return JsonResponse({'error': 'File not found'}, status=404)