import time
import requests
import re
import orodja
#import orodja
link = "https://www.procyclingstats.com/rider"
prevod_drzav = orodja.prevod_drzav()
prevod_mesev = {'January': 'janunar', 'February': 'februar', 'March': 'marec','April':'april', 'May':'maj', 'June':'junij','July':'julij', 'August' :'avgust', 'September':'september', 'October':'oktober', 'November':'november', 'December':'december'}
class Kolesar:
    def __init__(self, ime):
        req = requests.get(link + "/" + ime).text
        podatki = re.findall(r'</span><h1 class="">.+<div class=""></div>', req, re.DOTALL)
        polno_ime = re.findall(r'<h1 class="">.+</h1>', podatki[0])[0][13:-5].replace("  ", " ")
        #ekipa = re.findall(r'hideIfMobile">.+</span></div><div class="sub">', podatki[0])[0][14:-30]
        datum_rojstva = re.findall(r'<b>Date of birth:</b>.+<sup>.+</sup>.+<br /><b>Nationality:', podatki[0])
        dan, mesec_leto = datum_rojstva[0].split("<sup>")[:2]
        dan = dan[22:]
        mesec,leto,starost = mesec_leto[9:-21].split(' ')
        
        datum_rojstva = dan + ". " + prevod_mesev[mesec]+' ' + leto +starost
        drzava = re.findall(r'</span><a class="black" href="nation/.+">.+</a><br />', podatki[0])[0]
        drzava = drzava.split('">')[1][:-10]
        drzava = prevod_drzav[drzava.split("</a><br />")[0]]
        try:
            teza = re.findall(r'Weight:</b>.+&nbsp; <span><b>Height:', podatki[0])[0][12:-24]
            visina = re.findall(r'Height:</b>.+m<br /><b>', podatki[0])[0][12:-9]
            self.teza = teza
            self.visina = visina
        except:
            self.teza = "neznano"
            self.visina = "neznano"
        
        self.ime = polno_ime
        #self.ekipa = ekipa
        self.d_rojstva = datum_rojstva
        self.nacionalnost = drzava
        self.link_ime = ime
        self.starti_tour = 0 #kolikorat je začel dirko po Franciji
        self.koncal_tour = 0 #kolikokrat je končal tour(pogleš končni GC)
        self.starti_etap = 0 #kolikokrat je začel etapo
        self.uvrstitve_etap = []
        self.etapne_zmage = 0
        
    def __str__(self):
        return "Ime: {:>2}\nDatum rojstva: {:>}\nDržava: {:>}\nTeža: {:}\nVišina: {:}\n".format(self.ime, self.d_rojstva, self.nacionalnost, self.teza, self.visina) # self.ekipa!!!
    
    def __repr__(self):
        return "Kolesar({})".format(self.link_ime)
    
    def dosežki(self):
        '''izpiše statistične vrenosti kolesarja, kot so zmage, starti..'''
        return 'Start dirke: {}\nKončane dirke: {}\nStart etap:{}\nEtapne zmage: {}\nUvrstitve:{}'.format(self.starti_tour,self.koncal_tour,self.starti_etap,self.etapne_zmage, self.uvrstitve_etap) 
                
    def skupna_dolzina(self):
        vsota = 0
        for rezultat in self.uvrstitve_etap:
            dol = float(rezultat[-1].split(" ")[-2])
            vsota += dol
        return vsota
            

class Drzava:
    def __init__(self, ime):
        self.ime = ime
        self.tekmovalci = set()
        
    def dodaj_tekmovalca(self, kolesar):
        self.tekmovalci.add(kolesar)
        
    
    def st_startov_tour(self):
        return sum([kolesar.starti_tour for kolesar in self.tekmovalci])
    
    def st_starti_etap(self):
        return sum([kolesar.starti_tour for kolesar in self.tekmovalci])
    
    def st_etapnih_zmag(self):
        return sum([kolesar.etapne_zmage for kolesar in self.tekmovalci])
    
    def st_etapnih_zmag(self):
        return sum([kolesar.etapne_zmage for kolesar in self.tekmovalci])
    
    def st_tekmovalcev(self):
        return len(self.tekmovalci)
    
    

# ime = "primoz-roglic"
# kol = Kolesar(ime)
# print(kol)
# print(kol.dosežki())

