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
    if leto in range(1903,1930) or leto == 1931:
        for i in [2]:
            tab = tabela[i]
            osebe = re.findall(r'href="rider/.+">.+class="showIfMobile', tab)
            imena = [re.sub(r'href="rider/', '', oseba) for oseba in osebe]
            imena = [uredi_ime(oseba.split('"')[0]) for oseba in imena]
            slovar['GC'] = imena

        
    elif leto in [1930,1932]:
        for i in [2]:
            tab = tabela[i]
            osebe = re.findall(r'href="rider/.+">.+class="showIfMobile', tab)
            imena = [re.sub(r'href="rider/', '', oseba) for oseba in osebe]
            imena = [uredi_ime(oseba.split('"')[0]) for oseba in imena]
            slovar['GC'] = imena

    elif leto in range(1933,1953):
        if leto == 1939:
            for i in [2,3,7]:
                tab = tabela[i]
                osebe = re.findall(r'href="rider/.+">.+class="showIfMobile', tab)
                imena = [re.sub(r'href="rider/', '', oseba) for oseba in osebe]
                imena = [uredi_ime(oseba.split('"')[0]) for oseba in imena]
                if i == 2:
                    slovar['GC'] = imena
                elif i == 3:
                    slovar['ZeLENA'] = imena
                else:
                    slovar['PIK'] = imena
        else: 
            for i in [2,3]:
                tab = tabela[i]
                osebe = re.findall(r'href="rider/.+">.+class="showIfMobile', tab)
                imena = [re.sub(r'href="rider/', '', oseba) for oseba in osebe]
                imena = [uredi_ime(oseba.split('"')[0]) for oseba in imena]
                if i == 2:
                    slovar['GC'] = imena
                else:
                    slovar['PIK'] = imena
    elif leto in [1953,1954,1958,1965]:
        for i in [2,3,4]:
            tab = tabela[i]
            osebe = re.findall(r'href="rider/.+">.+class="showIfMobile', tab)
            imena = [re.sub(r'href="rider/', '', oseba) for oseba in osebe]
            imena = [uredi_ime(oseba.split('"')[0]) for oseba in imena]
            if i == 2:
                slovar['GC'] = imena
            elif i == 3:
                slovar['PIK'] = imena
            else:
                slovar['ZELENA'] = imena
    elif leto in [1955,1956,1957,1959,1960,1961,1962,1963,1964,1966,1967,1968,1969,1970,1971,1972,1973,1974]:
        for i in [2,3,4]:
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
    elif leto in [1975,1993,2000,2007]:
        for i in [2,3,5,6]:
            tab = tabela[i]
            osebe = re.findall(r'href="rider/.+">.+class="showIfMobile', tab)
            imena = [re.sub(r'href="rider/', '', oseba) for oseba in osebe]
            imena = [uredi_ime(oseba.split('"')[0]) for oseba in imena]
            if i == 2:
                slovar['GC'] = imena
            elif i == 3:
                slovar['ZELENA'] = imena
            elif i == 6:
                slovar['BELA'] = imena     
            else:
                slovar['PIK'] = imena
    elif leto in [1976,1978,1986,2003,2018,2019,2020]:
        for i in [2,3,4,5]:
            tab = tabela[i]
            osebe = re.findall(r'href="rider/.+">.+class="showIfMobile', tab)
            imena = [re.sub(r'href="rider/', '', oseba) for oseba in osebe]
            imena = [uredi_ime(oseba.split('"')[0]) for oseba in imena]
            if i == 2:
                slovar['GC'] = imena
            elif i == 3:
                slovar['ZELENA'] = imena
            elif i == 4:
                slovar['BELA'] = imena
            else:
                slovar['PIK'] = imena
                
    elif  leto == 1987:     
        for i in [3,4,5,6]:
            tab = tabela[i]
            osebe = re.findall(r'href="rider/.+">.+class="showIfMobile', tab)
            imena = [re.sub(r'href="rider/', '', oseba) for oseba in osebe]
            imena = [uredi_ime(oseba.split('"')[0]) for oseba in imena]
            if i == 3:
                slovar['GC'] = imena
            elif i == 4:
                slovar['ZELENA'] = imena
            elif i == 6:
                slovar['BELA'] = imena
            else:
                slovar['PIK'] = imena
    else:    
        for i in [2,3,4,5]:
            tab = tabela[i]
            osebe = re.findall(r'href="rider/.+">.+class="showIfMobile', tab)
            imena = [re.sub(r'href="rider/', '', oseba) for oseba in osebe]
            imena = [uredi_ime(oseba.split('"')[0]) for oseba in imena]
            if i == 2:
                slovar['GC'] = imena
            elif i == 3:
                slovar['ZELENA'] = imena
            elif i == 5:
                slovar['BELA'] = imena
            else:
                slovar['PIK'] = imena
                
                
    slovar['ETAPE'] = etape(link,leto)
    return slovar
def imena_etapa(link):
    '''vrne seznam imen kolesarjev glede na posamezne razvrstitve'''
    
    req = requests.get(link).text   
    if link == 'https://www.procyclingstats.com/race/tour-de-france/1987/stage-25':#tuki je malo drugače...
        tab = req.split('<table class="basic')[2] 
    else:
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
    for leto in range(od_leta,1990): #vsa_leta(link): #
        slovar[leto] = imena_vseh(link + '/'+str(leto),leto)
    return slovar

def linki_etap(link):
    '''vrne tabelo linkov do posameznih etap v nekem letu'''
    req = requests.get(link).text
    ime_etap = re.findall(r'max-width: 250px; width: 100%;  "><select style="" onChange="window.location.href=this.value;.+">.+</option><option', req)
    ime_etap = ime_etap[0].split(' |')[:-1]
    nov =[etapa.split('>')[-2].replace('<option ','') for etapa in ime_etap]
    nov =['https://www.procyclingstats.com/' + etapa[:-1].replace('value="','')[:-1] for etapa in nov]
#     nov =['https://www.procyclingstats.com/'+ etapa.split('"')[0] for etapa in nov]
    
    return nov#nov[:-1]
    
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
    sl_drzav['Yugoslavia'] = 'Jugoslavija'
    nov = dict()
    for drzava in sl_drzav:
        nov[drzava] = sl_drzav[drzava].capitalize()
    
    return nov
def vsa_leta(link):
    '''vrne vsa leta, kjer se je pojavil tour'''
    req = requests.get(link).text
    najdi = re.findall(r'"><option value="race/tour-de-france/2021.+href="race/tour-de-', req)[0].split('value="race/tour-de-france/')[1:]
    leta = sorted([int(niz[:4]) for niz in najdi][:-22])[:-1]
    return leta

def izpisi_lepo(tab):
    '''[1, 2018, '19. etapa: 200.5 km'] izpiše na lep način'''
    return str(tab[0]) + '. mesto; leto: ' + str(tab[1]) +'; ' + tab[2]
def zmagovalci(slovar_imen,slovar_kolesarjev):
    '''vrne tabelo zmagovalcev toura'''
    zmagovalci = []
    for leto in slovar_imen:
        zmagovalec = slovar_imen[leto]['GC'][0]
        zmagovalci.append((slovar_kolesarjev[zmagovalec],leto))
    return zmagovalci

 



# for kl,vr in b.items():
#     print(vr)
    
# c = time.time()
# a= pridobivanje_vseh_let(link,1985)
# a[1987]['ETAPE']['25. etapa: 186 km'] = orodja.imena_etapa('https://www.procyclingstats.com/race/tour-de-france/1987/stage-25')
# dat = open('dat.txt','w',encoding='utf-8')
# print(a,file = dat)
# dat.close()
# print('konec')
# print(abs(c- time.time()))