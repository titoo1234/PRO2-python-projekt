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
        try:
            datum_rojstva = re.findall(r'<b>Date of birth:</b>.+<sup>.+</sup>.+<br /><b>Nationality:', podatki[0])
            dan, mesec_leto = datum_rojstva[0].split("<sup>")[:2]
            dan = dan[22:]
            mesec,leto,starost = mesec_leto[9:-21].split(' ')
            datum_rojstva = dan + ". " + prevod_mesev[mesec]+' ' + leto +starost
            if '<br/><span><b>P' in datum_rojstva:
                datum_rojstva = datum_rojstva.replace('<br/><span><b>P','')
            
        except:
            self.d_rojstva = 'neznano'
        
        try:
            drzava = re.findall(r'</span><a class="black" href="nation/.+">.+</a><br />', podatki[0])[0]
            drzava = drzava.split('">')[1][:-10]
            drzava = prevod_drzav[drzava.split("</a><br />")[0]]
        except:
            self.nacionalnost = 'neznano'
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
        if datum_rojstva == []:
                datum_rojstva = 'neznano'
        self.d_rojstva = datum_rojstva
        self.nacionalnost = drzava
        self.link_ime = ime
        self.starti_tour = 0 #kolikorat je začel dirko po Franciji
        self.koncal_tour = 0 #kolikokrat je končal tour(pogleš končni GC)
        self.starti_etap = 0 #kolikokrat je začel etapo
        self.uvrstitve_etap = []
        self.etapne_zmage = 0
        self.gc_uvrstitve = []
        
    def leta(self):
        sl = dict()
        for uvrstitev in self.uvrstitve_etap:
            if uvrstitev[1] not in sl:
                sl[uvrstitev[1]] = [uvrstitev]
            else:
                sl[uvrstitev[1]].append(uvrstitev)
        return sl
        
    def __str__(self):
        return "{:>15} | {:s}\n{:>15} | {:s}\n{:>15} | {:s}\n{:>15} | {:s}\n{:>15} | {:s}\n".format("Ime",self.ime, "Datum rojstva", self.d_rojstva, "Država", self.nacionalnost, "Teža", self.teza, "Višina", self.visina) # self.ekipa!!!
    
    def __repr__(self):
        return "Kolesar({})".format(self.link_ime)
    
    def dosezki(self):
        '''izpiše statistične vrenosti kolesarja, kot so zmage, starti..'''
        return '{:>15} | {:}\n{:>15} | {:}\n{:>15} | {:}\n{:>15} | {:}'.format("Start dirke",self.starti_tour,"Končane dirke",self.koncal_tour,"Start etap",self.starti_etap,"Etapne zmage",self.etapne_zmage) #\nUvrstitve:{} self.uvrstitve_etap
                
    def skupna_dolzina(self):
        vsota = 0
        for rezultat in self.uvrstitve_etap:
            dol = float(rezultat[-1].split(" ")[-2])
            vsota += dol
        return vsota
    
    def dolzina_toura(self, leto):
        vsota = 0
        for rezultat in self.uvrstitve_etap:
            if rezultat[-2] == leto:
                dol = float(rezultat[-1].split(" ")[-2])
                vsota += dol
        return round(vsota, 2)
    
    def kolikokrat_zmagal(self):
        vsota = 0
        for _,uvrstitev in self.gc_uvrstitve:
            if uvrstitev == 1:
                vsota += 1
        return "{:>15} | {:}".format("Skupne zmage", vsota)
    
    def najbolse_uvrstitve(self):
        '''vrne seznam uvrstitev glede na mesto'''
        tab = sorted(self.uvrstitve_etap, key = lambda x: x[0])
        return tab
                
    

            

class Drzava:
    def __init__(self, ime):
        self.ime = ime
        self.tekmovalci = set()
        
    def dodaj_tekmovalca(self, kolesar):
        self.tekmovalci.add(kolesar)
    def __repr__(self):
        return "Drzava({})".format(self.ime)
    def __str__(self):
        return "{:>15} | {:}".format("Država", self.ime)
    
    
    def doloceno_leto(self, leto):
        mn_k = set()
        st_etapnih_z = 0
        koncali = 0
        for kolesar in self.tekmovalci:
            if leto in kolesar.leta():
                mn_k.add(kolesar)
                st_etapnih_z += sum([1 for x in kolesar.leta()[leto] if x[0] == 1])
                koncali += sum([1 for x in kolesar.gc_uvrstitve if x[0] == leto])
        return mn_k, st_etapnih_z, len(mn_k), koncali
    
    def zmaga_leto(self, leto):
        for kolesar in self.tekmovalci:
            for uvr in kolesar.gc_uvrstitve:
                if uvr[0] == leto and uvr[1] == 1:
                    return True
        return False
    
    def skupne_zmage(self):
        vsota = 0
        for kolesar in self.tekmovalci:
            vsota += int(kolesar.kolikokrat_zmagal().split()[-1])
        return "{:>15} | {:}".format("Skupne zmage", vsota)
    
    @staticmethod
    def najuspesnejse_drzave(leto,slovar):
        '''vrne tabelo dvojic, kjer je leva vrednost država, desna pa število zmag'''
        tab = []
        for drzava in slovar:    
            tab.append((slovar[drzava].ime,slovar[drzava].doloceno_leto(leto)[1]))
            nova = sorted(tab,key = lambda x: x[1])[::-1]
        return nova
    
    
    def st_startov_tour(self):
        return sum([kolesar.starti_tour for kolesar in self.tekmovalci])
    
    def st_starti_etap(self):
        return "{:>15} | {:}".format("Start etap", sum([kolesar.starti_etap for kolesar in self.tekmovalci]))
    
    def st_etapnih_zmag(self):
        return "{:>15} | {:}".format("Etapne zmage", sum([kolesar.etapne_zmage for kolesar in self.tekmovalci]))
    
    #def st_etapnih_zmag(self):
        #return sum([kolesar.etapne_zmage for kolesar in self.tekmovalci])
    
    def st_tekmovalcev(self):
        return len(self.tekmovalci)
    

    
    

# ime = "primoz-roglic"
# kol = Kolesar(ime)
# print(kol)
# print(kol.dosežki())

