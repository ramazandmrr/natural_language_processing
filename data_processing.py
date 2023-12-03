import nltk
from nltk.tokenize import sent_tokenize
import re 

def veri_duzenleme(girendata,cikandata):
    try:
        with open(girendata,'r',encoding='utf-8') as file:
            veri = file.read()

        veri = veri.lower()

        veri = re.sub(r'\d','',veri)  # nümerik ifadlereden arındırma
        
       
        veri = re.sub(r'\.', '',veri)

        veri = re.sub(r'[^\w\s.]', '',veri) # özel karakter ve noktalama kaldırma
        
        gereksiz_kelimeler = ['ve','ama','veya','.','..','...'] #gereksiz kelimeler
        veri = ' '.join([kelime for kelime in veri.split() if kelime not in gereksiz_kelimeler])

        cümleler = sent_tokenize(veri)
        
        with open(cikandata,'w',encoding='utf-8') as output_file:
            for i, cümle in enumerate(cümleler,start=1):
                output_file.write(f"{cümle.strip()}")        

    except FileNotFoundError:
        print(f"{girendata} dosya bulunamadı...")


veri_duzenleme('iphonese.txt','islenmis_veri_iphonese.txt')        