import time
import requests
import re
import orodja


link = "https://www.procyclingstats.com/rider"
prevod_drzav = orodja.prevod_drzav()
prevod_mesev = {'January': 'janunar', 'February': 'februar', 'March': 'marec','April':'april', 'May':'maj', 'June':'junij','July':'julij', 'August' :'avgust', 'September':'september', 'October':'oktober', 'November':'november', 'December':'december'}
class Kolesar:
    def __init__(self, ime):
        #pridobivanje podatkov iz spleta
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
            self.d_rojstva = datum_rojstva
            
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
        #v nekaterih primerih ni bilo datuma
        if self.d_rojstva == []:
            self.d_rojstva = 'neznano'
        #self.d_rojstva = datum_rojstva
        self.nacionalnost = drzava
        self.link_ime = ime
        self.starti_tour = 0 #kolikorat je začel dirko po Franciji
        self.koncal_tour = 0 #kolikokrat je končal tour(pogleš končni GC)
        self.starti_etap = 0 #kolikokrat je začel etapo
        self.uvrstitve_etap = [] #elementi v tabeli so oblike: [mesto,leto,etapa]
        self.etapne_zmage = 0
        self.gc_uvrstitve = [] #elementi v tabeli so oblike: [leto,mesto]
        
    def leta(self):
        '''
            vrne slovar, kjer so ključi leta, vrednosti pa seznam etap,
            katerih se je udeležil v danem letu
        '''
        sl = dict()
        for uvrstitev in self.uvrstitve_etap:
            if uvrstitev[1] not in sl:
                sl[uvrstitev[1]] = [uvrstitev]
            else:
                sl[uvrstitev[1]].append(uvrstitev)
        return sl
        
    def __str__(self):
        return "{:>40s} | {:s}\n{:>40s} | {:s}\n{:>40s} | {:s}\n{:>40s} | {:s}\n{:>40s} | {:s}".format("Ime",self.ime, "Datum rojstva", self.d_rojstva, "Država", self.nacionalnost, "Teža", self.teza, "Višina", self.visina) # self.ekipa!!!
    
    def __repr__(self):
        return "Kolesar({})".format(self.link_ime)
    
    def dosezki(self):
        '''
            izpiše statistične vrenosti kolesarja, kot so zmage, starti..
        '''
        return '{:>40s} | {:}\n{:>40s} | {:}\n{:>40s} | {:}\n{:>40s} | {:}'.format("Start dirke",self.starti_tour,"Končane dirke",self.koncal_tour,"Start etap",self.starti_etap,"Etapne zmage",self.etapne_zmage) #\nUvrstitve:{} self.uvrstitve_etap
                
    def skupna_dolzina(self):
        '''
            Vrne skupno dolžino, ki jo je kolesar prevozil na vseh etapah
        '''
        vsota = 0
        for rezultat in self.uvrstitve_etap:
            dol = float(rezultat[-1].split(" ")[-2])
            vsota += dol
        return vsota
    
    def dolzina_toura(self, leto):
        '''
            Vrne skupno dolžino, ki jo je kolesar prevozil na vseh etapah v določenem letu
        '''
        vsota = 0
        for rezultat in self.uvrstitve_etap:
            if rezultat[-2] == leto:
                dol = float(rezultat[-1].split(" ")[-2])
                vsota += dol
        return round(vsota, 2)
    
    def kolikokrat_zmagal(self):
        '''
            Vrne število skupnih zmag, ki jih je osvojil kolesar 
        '''
        vsota = 0
        for _,uvrstitev in self.gc_uvrstitve:
            if uvrstitev == 1:
                vsota += 1
        return vsota
    
    def najbolse_uvrstitve(self):
        '''
            Vrne seznam uvrstitev glede na mesto
        '''
        tab = sorted(self.uvrstitve_etap, key = lambda x: x[0])
        return tab
                
    def razmerje(self):
        """
            Vrne razmerje etapnih zmag in koncanih etap
        """
        return round(self.etapne_zmage/self.starti_etap, 3)
    
    def etapne_zmage_leto(self):
        '''
            Vrne največje število zmag v enem letu in leto v katerem se je to zgodilo (št. zmag, leto)
        '''
        sl = {}
        for uvrstitev in self.najbolse_uvrstitve():
            #ko pride do mesta, ki ni več prvo, lahko konča
            if uvrstitev[0] != 1:
                break
            else:
                leto = uvrstitev[1]
                if leto in sl:
                    
                    sl[leto] +=1
                else:
                    sl[leto] = 1
        naj_leto = 0    
        naj = 0
        for leto,st in sl.items():
            if st >= naj:
                naj = st
                naj_leto = leto
        return (naj,naj_leto)
    
    
    
    def st_etapne_zmage_leto(self):
        sl = {}
        for uvrstitev in self.najbolse_uvrstitve():
            #ko pride do mesta, ki ni več prvo, lahko konča
            if uvrstitev[0] != 1:
                break
            else:
                leto = uvrstitev[1]
                if leto in sl:
                    
                    sl[leto] +=1
                else:
                    sl[leto] = 1
        return sl

            

class Drzava:
    def __init__(self, ime):
        self.ime = ime
        self.tekmovalci = set()
        
    def dodaj_tekmovalca(self, kolesar):
        self.tekmovalci.add(kolesar)
        
    def __repr__(self):
        return "Drzava({})".format(self.ime)
    
    def __str__(self):
        return "{:>50s} | {:}".format("Država", self.ime)
    
    
    def doloceno_leto(self, leto):
        ''' Za določeno leto vrne množico kolesarjev, ki so sodelovai na Dirki iz dane države,
            število etapnih zmag, število vseh kolesarjev,ki so sodelovai na Dirki iz dane države,
            in število kolesarjev, ki so končali Dirko
        '''
        mn_k = set()
        st_etapnih_z = 0
        koncali = 0
        for kolesar in self.tekmovalci:
            if leto in kolesar.leta():
                mn_k.add(kolesar)
                st_etapnih_z += sum([1 for x in kolesar.leta()[leto] if x[0] == 1])
                koncali += sum([1 for x in kolesar.gc_uvrstitve if x[0] == leto])
        return mn_k, st_etapnih_z, len(mn_k), koncali
    
    def etapne_zmage_skozi_leta(self):
        ''' vrne tabelo parov (leto,št_etapnih_zmag_v_tem_letu)
            urejeno glede na število zmag v tem letu
        '''
        tab = []
        for leto in orodja.vsa_leta('https://www.procyclingstats.com/race/tour-de-france'):
            tab.append((leto,self.doloceno_leto(leto)[1]))
        nov = sorted(tab,key=lambda x: x[1])[::-1]
        return nov
    
    
    def zmaga_leto(self, leto):
        '''
            pove ali tekmovalec iz te države zmagal Dirko v nekem letu
        '''
        for kolesar in self.tekmovalci:
            for uvr in kolesar.gc_uvrstitve:
                if uvr[0] == leto and uvr[1] == 1:
                    return True
        return False
    
    def skupne_zmage(self):
        '''
            Vrne število skupnih zmag od vseh kolesarjev v državi
        '''
        vsota = 0
        for kolesar in self.tekmovalci:
            vsota += int(kolesar.kolikokrat_zmagal())
        return "{:>50s} | {:}".format("Skupne zmage", vsota)
    
    @staticmethod
    def najuspesnejse_drzave(leto,slovar):
        '''
            Vrne tabelo dvojic, kjer je leva vrednost država, desna pa število zmag,
            urejeno po velikosti
        '''
        tab = []
        for drzava in slovar:    
            tab.append((slovar[drzava].ime,slovar[drzava].doloceno_leto(leto)[1]))
            nova = sorted(tab,key = lambda x: x[1])[::-1]
        return nova
    
    @staticmethod
    def najuspesnejse_drzave_vsa_leta(slovar):
        '''
            Vrne slovar, kjer so ključi ime države, vrednost pa število etapnih zmag
            skozi vsa leta
        '''
        sl = {}
        for leto in orodja.vsa_leta('https://www.procyclingstats.com/race/tour-de-france'):
            for drzava,zmage in Drzava.najuspesnejse_drzave(leto,slovar):
                if drzava not in sl:
                    sl[drzava] = 0
                sl[drzava] += zmage
        return sl

    
    def st_startov_tour(self):
        '''
            Izpiše vsoto vseh startov na Dirki(1.etapa) od vseh kolesarjev iz dane države
        '''
        return sum([kolesar.starti_tour for kolesar in self.tekmovalci])
    
    def st_starti_etap(self):
        '''
            Izpiše vsoto vseh startov na Dirki(vse etape) od vseh kolesarjev iz dane države
        '''
        return "{:>50s} | {:}".format("Start etap", sum([kolesar.starti_etap for kolesar in self.tekmovalci]))
    
    def st_etapnih_zmag(self):
        '''
            Izpiše vsoto vseh zmag, ki so jo dosegli kolesarji iz države
        '''
        return "{:>50s} | {:}".format("Etapne zmage", sum([kolesar.etapne_zmage for kolesar in self.tekmovalci]))
    
    def st_tekmovalcev(self):
        return len(self.tekmovalci)
    
    def st_zmaganih_tourov(self):
        '''
            Izpiše vsoto vseh zmaganih dirk, ki so jo osvojili kolesarji iz te države
        '''
        vsota = 0
        for tekmovalec in self.tekmovalci:
            vsota += tekmovalec.kolikokrat_zmagal()
        return vsota
    
    @staticmethod
    def najuspesnejse_drzave_vsa_leta_gc(slovar_drazav):
        '''
            Vrne tabelo parov, oblike (drzava, število zmaganih tourov),
            urejeno po številu zmaganih tourov
        '''
        tab = []
        for drzava_ime,drzava in slovar_drazav.items():
            tab.append((drzava_ime,drzava.st_zmaganih_tourov()))
            nov = sorted(tab,key=lambda x: x[1])[::-1]
        return nov
