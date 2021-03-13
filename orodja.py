#koda za pridobitev imen za nek seštevek
#treba še mal uredit imena 

import requests
import re
def imena(link):
    '''vrne slovar imen kolesarjev glede na posamezne razvrstitve'''
    # dat2 = open('dat2.txt','w',encoding='utf-8')
    slovar = dict()
    req = requests.get(link).text
    
    tabela = req.split('<table class="basic') #tuki sam spremeni indeks in boš dobu imena za drugo
                                                 #točkovanje(2=GC,3=ZELENA,4=PIKČASTA) 
                                                    
    for i in range(2,5):
        tab = tabela[i]
        osebe = re.findall(r'href="rider/.+">.+class="showIfMobile', tab)
        imena = [re.sub(r'href="rider/', '', oseba) for oseba in osebe]
        imena = [uredi_ime(oseba.split('"')[0]) for oseba in imena]
        if i == 2:
            slovar['GC'] = imena
        elif i == 3:
            slovar['ZELENA'] = imena
        else:
            slovar['PIK'] = imena
            
        
    return slovar


def uredi_ime(niz):
    '''uredi ime oblike ime-priimek v obliko Ime priimek'''
    razcep = niz.split('-')
    vrni = ' '.join([ime.capitalize() for ime in razcep])
    return vrni
        
