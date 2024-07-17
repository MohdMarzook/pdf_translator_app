import os
import time
import subprocess
from bs4 import BeautifulSoup as bs
from pyhtml2pdf import converter
from googletrans import Translator


start = time.time()

def create_directory(directory):
    os.makedirs(directory, exist_ok=True)

def html2pdf_and_save(html_filename,new_file_name, og_name):
    output_filename = f"./media/translated_pdf/{new_file_name}"
                            

    # print_options = {
    #     'paperHeight': 11.69,
    #     'paperWidth': 8.27,
    #     'printBackground': True
    # }

    converter.convert(f'file:///code/htmlfiles/{og_name}', output_filename)
    print(f"done! The output file is saved in {output_filename}")

def translate_text(text, from_language, to_language):
    translator = Translator()
    try:
        translated_text = translator.translate(text,src= from_language, dest=to_language).text
    except:
        translated_text = text
    return translated_text

def process_multiclass(multidiv, soup, from_lang, to_lang):
    if multidiv.find('span'):
        spans = multidiv.find_all('span')
        for span in spans:
            if len(span.get('class')) >= 4:
                saved_span = soup.new_tag(name='span', attrs={'class': span.get('class')})
                saved_span.string = " "
                multidiv.string = translate_text(multidiv.get_text())
                multidiv.append(saved_span)
                return
        multidiv.string = translate_text(multidiv.get_text(), from_lang, to_lang)
    else:
        multidiv.string = translate_text(multidiv.get_text(), from_lang, to_lang)

def html_parser(html_filename, newfilename, og_name, to_lang, from_lang='auto' ):
    
    with open(html_filename, "r", encoding='utf-8') as file:
        html_content = file.read()

    soup = bs(html_content, 'html.parser')
    container = soup.find("div", {"id": "page-container"})
    pages = container.find_all("div", recursive=False)
    total_no_pages = len(pages)
    for current_page_no, page in enumerate(pages, start=1):
        page = page.find('div')
        for list_of_div in page.find_all('div', recursive=False):
            if not list_of_div.text.strip():
                continue
            if len(list_of_div.get('class')) > 5:
                process_multiclass(list_of_div, soup, from_lang, to_lang)
            else:
                for subdiv in list_of_div.find_all('div', recursive=False):
                    process_multiclass(subdiv, soup, from_lang, to_lang)
        # print(f"\rTranslated({current_page_no},{total_no_pages})  {time.time() - start:.2f}", end='', flush=True)
    create_directory('./media/translated_pdf')
    with open(html_filename, 'w', encoding='utf-8') as file:
        file.write(str(soup))
    print("\nSaving translated file")
    html2pdf_and_save(html_filename, newfilename, og_name)

def pdf2html(filename, newfilename):
    create_directory("./htmlfiles")
    input_file = f"./{filename}"
    # print("----------------------------------------------------------------------")
    # print("----------------------------------------------------------------------")
    output_file = f"./htmlfiles/{newfilename.split('.pdf')[0]}.html"
    #  pdf2htmlEX ./sample_pdfs/sample.pdf ./htmlfiles/newfile.html
    result = subprocess.run(['pdf2htmlEX', input_file, output_file], 
                        capture_output=True, text=True, check=True)
    og_html_filename = f"{newfilename.split('.pdf')[0]}.html"
    return output_file , og_html_filename


def initializer(data):
    html_file_name ,og_name = pdf2html(data["file_name"], data["new_file_name"])
    html_parser(html_file_name, data["new_file_name"], og_name ,  from_lang=data["from"], to_lang=data["to"]) 
    



print("preprocessing is started")
# docker_init(input_filename)
# print("translating is started")
# html_filename = f"./temp/{input_filename.split('.')[0]}.html"
# html_parser(html_filename,input_to_language)     


print(f"Translation completed in {time.time() - start:.2f}s")
