from django import forms
from .models import PDFFile

class PDFFileForm(forms.ModelForm):
    class Meta:
        model = PDFFile
        fields = ['file']
        widgets = {
            'file' : forms.FileInput(attrs={
                'class' : "nothing",
                "id" : "file_input",
                'onchange':"showsubmitbutton(this)",
                "onclick" : "this.value = null;"
            })
        }
    