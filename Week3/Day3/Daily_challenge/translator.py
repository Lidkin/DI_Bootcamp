from translate import Translator as tr
from googletrans import Translator

def translator(french_words) :
    fr_en_dict = {}
    translator = tr(from_lang='fr', to_lang="en")
    for word in french_words:
        fr_en_dict[word] = translator.translate(word)
    print (fr_en_dict)    

def google_translator(french_words):
        fr_en_dict = {}
        translations = Translator().translate(french_words, dest='en', src='fr')
        for translation in translations:
           fr_en_dict[translation.origin] = translation.text
        print(fr_en_dict)   

french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 
translator(french_words)
google_translator(french_words)