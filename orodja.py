#koda za pridobitev imen za nek seštevek
#treba še mal uredit imena 
link = 'https://www.procyclingstats.com/race/tour-de-france/2012'
import requests
import re
def imena_vseh(link):
    '''vrne slovar imen kolesarjev glede na posamezne razvrstitve'''
    # dat2 = open('dat2.txt','w',encoding='utf-8')
    slovar = dict()
    req = requests.get(link).text
    
    tabela = req.split('<table class="basic') #tuki sam spremeni indeks in boš dobu imena za drugo
                                                 #točkovanje(2=GC,3=ZELENA,4=PIKČASTA) 
                                                    
    for i in [2,3,5]:#4 je bela majica lahk dodama...
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
def imena_etapa(link):
    '''vrne seznam imen kolesarjev glede na posamezne razvrstitve'''
    # dat2 = open('dat2.txt','w',encoding='utf-8')
    
    req = requests.get(link).text
    
    tabela = req.split('<table class="basic')
    #tuki sam spremeni indeks in boš dobu imena za drugo
    #točkovanje(2=GC,3=ZELENA,4=PIKČASTA) a
                                                    
    for i in [1]:#4 je bela majica lahk dodama...
        tab = tabela[i]
        osebe = re.findall(r'href="rider/.+">.+class="showIfMobile', tab)
        imena = [re.sub(r'href="rider/', '', oseba) for oseba in osebe]
        imena = [uredi_ime(oseba.split('"')[0]) for oseba in imena]
        
            
        
    return imena

def uredi_ime(niz):
    '''uredi ime oblike ime-priimek v obliko Ime priimek'''
    razcep = niz.split('-')
    vrni = ' '.join([ime.capitalize() for ime in razcep])
    return vrni

#nevem če boma to rabla ampak ok :)
def zapis(tabela):
    '''izpiše imena iz tabele vsako v svoji vrsti'''
    st = 1
    for ime in tabela:
        print('{:10}. {}'.format(st,ime))
        st += 1
def pridobivanje_vseh_let(link, od_leta): #link = https://www.procyclingstats.com/race/tour-de-france
    '''naredi slovar slovarjev slovar[leto] = slovar_imena_vseh'''
    slovar = dict()
    for leto in range(od_leta,2021):
        slovar[leto] = imena_vseh(link + '/'+str(leto))
    return slovar

def naslov_etap(link):
    '''vrne tabelo kratic etap, da bom jih lahko uporabu za funkcijo etape'''
    tab = []
    req = requests.get(link).text
    ime_etap = re.findall(r'max-width: 250px; width: 100%;  "><select style="" onChange="window.location.href=this.value;.+">.+</option><option', req)
    ime_etap = ime_etap[0].split(' |')
    nov =[etapa.split('>')[-1] for etapa in ime_etap]
    
    return ime_etap
def etape(link,leto):
    '''vrne slovar, ključi so katera etapa, vrednosti pa seznam kolesarjev'''
    slovar = dict()
    for etapa in range(1,22):
        slovar[str(etapa)+'. etapa']= imena_etapa(link+ '/'+str(leto) +'/'+'stage-'+str(etapa) + '/'+'result'+'/'+'result')
    return slovar
    
      
print(naslov_etap(link))