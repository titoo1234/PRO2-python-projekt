#koda za pridobitev imen za nek seštevek
#treba še mal uredit imena 
import time
link = 'https://www.procyclingstats.com/race/tour-de-france'
import requests
import re
def imena_vseh(link,leto):
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
    slovar['ETAPE'] = etape(link,leto)     
        
    return slovar
def imena_etapa(link):
    '''vrne seznam imen kolesarjev glede na posamezne razvrstitve'''
   
    req = requests.get(link).text    
    tab = req.split('<table class="basic')[1]                                                    
    osebe = re.findall(r'data-nation=".+">.+class="showIfMobile', tab)
    #osebe, ki niso začele etape, ne dam v tabelo
    imena = [oseba.split('href="rider/')[1] for oseba in osebe if ('DNS' not in oseba and 'DNF' not in oseba and 'OTL' not in oseba)]
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
        slovar[leto] = imena_vseh(link + '/'+str(leto),leto)
    return slovar

def linki_etap(link):
    '''vrne tabelo linkov do posameznih etap v nekem letu'''
    req = requests.get(link).text
    ime_etap = re.findall(r'max-width: 250px; width: 100%;  "><select style="" onChange="window.location.href=this.value;.+">.+</option><option', req)
    ime_etap = ime_etap[0].split(' |')
    nov =[etapa.split('option value="')[1] for etapa in ime_etap]
    nov =['https://www.procyclingstats.com/'+ etapa.split('"')[0] for etapa in nov]
    
    return nov[:-1]
def etape(link,leto):
    
    '''vrne slovar, ključi so katera etapa, vrednosti pa seznam kolesarjev'''
    slovar = dict()
    link2='https://www.procyclingstats.com/race/tour-de-france'+ '/' + str(leto)
    
    for etapa in linki_etap(link2):
        razrez = etapa.split('https://www.procyclingstats.com/race/tour-de-france/')[1].split('/')[1]
        req = requests.get(etapa).text
        #dodal bom še dolžino etape lahko dodama tud drugače
        najdi = re.findall(r'<li><div>Distance:.+', req)[0][31:].split('<')[0]
        if req.count('TTT') > 3:
            slovar[razrez[6:] + '. etapa' + ' (TTT): ' +najdi]= imena_etapa(etapa)
        else:
            if 'pro' in razrez:
                slovar['prolog: '+ najdi]= imena_etapa(etapa)
            else:slovar[razrez[6:] +'. etapa: '+ najdi]= imena_etapa(etapa)
    return slovar
def ime_za_link(ime):
    '''iz Ime Priimek naredi ime-priimek'''
    nov = ime.lower()
    nov = nov.replace(' ','-')
    return nov
def prevod_drzav():
    '''naredi ang-slo slovar prevodov držav'''
    link = 'https://www.101languages.net/slovenian/country-names-slovenian/'
    req = requests.get(link).text
    tab = req.split('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp')
    nova = [i.split('<td>')[-1] for i in tab][:-1]
    sl_drzav = {nova[i]: nova[i + 1] for i in range(0, len(nova), 2)}
    
    
    for kl,vr in sl_drzav.items():
        if '&#269' in vr:
            sl_drzav[kl] = vr.replace('&#269;','č')
        if '&#268' in vr:
            sl_drzav[kl] = vr.replace('&#268;','č')
            
    sl_drzav['United States'] = 'Združene države Amerike'
    sl_drzav['Great Britain'] = 'Velika Britanija'
    return sl_drzav


# for kl,vr in b.items():
#     print(vr)
    
# c = time.time()
# a= pridobivanje_vseh_let(link,2020)
# dat = open('proba.txt','w',encoding='utf-8')
# print(a,file = dat)
# dat.close()
# print(abs(c- time.time()))