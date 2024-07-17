from googletrans import Translator
from deep_translator import GoogleTranslator

def translate_text(text, from_language, to_language):
    try:
        translator = GoogleTranslator(source=from_language, target=to_language)
        translated_text = translator.translate(text)
        return translated_text
    except:
        print("deep fails")
    try:
        translator = Translator()
        translated_text = translator.translate(text,src= from_language, dest=to_language).text
        return translated_text
    except:
        print("google fails")
    
    
    translated_text = text
    return translated_text

out = translate_text("A Simple PDF File" , "auto", "fr")
print(out)
