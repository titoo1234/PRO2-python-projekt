import razred
import ast
import orodja
import pickle

def branje_ustvarjanje(datoteka):
    '''
        Iz datoteke 'datoteka' naredi slovar, ki je zapisan v datoteki
    '''
    dat = open(datoteka,'r')
    besedilo = dat.read()
    slovar_vseh_let = ast.literal_eval(besedilo)
    dat.close()
    return slovar_vseh_let

def zamenjava_kljucev(slovar):
    '''
        Iz slovarja 'slovar' naredi nov slovar, 
        ki ima spremenjene 'ključe' vrednosti pa so iste
        (Iz Primoz Roglic naredi Primož roglič...)
    '''
    nov = dict()
    for _, kolesar in slovar.items():
        nov[kolesar.ime] = kolesar
    return nov

def ustvarjanje_objektov(slovar):
    '''
        Iz slovarja, kjer so shranjeni rezultati za vsa leta,
        naredi nov slovar, ki ima ključ: ime kolesarja, vrednost pa je 
        objekt tipa Kolesar. Vedno, ko pride do novega kolesarja naredi nov objekt,
        sicer pa že obstoječemu objektu spremeni vrednosti atributov
    '''
    slovar_kolesarjev = dict()
    mn_kolesarjev = set()
    
    #najprej gremo skozi etapne uvrstitve
    for leto in slovar:
        mn_etap = slovar[leto]['ETAPE']    
        št_etap = 1
        for etapa in mn_etap:
            rezultati = slovar[leto]['ETAPE'][etapa]
            pozicija = 1
            for kolesar in rezultati:
                if kolesar not in mn_kolesarjev:#še ni prišel do kolesarja, zato naredi objekt
                    slovar_kolesarjev[kolesar] = razred.Kolesar(orodja.ime_za_link(kolesar))
                    mn_kolesarjev.add(kolesar)
                oseba = slovar_kolesarjev[kolesar]
                
                if št_etap == 1: #Pojavil se je na 1. etapi
                    oseba.starti_tour += 1  #kolikorat je začel dirko po Franciji              
                if pozicija == 1:#zmagal je etapo
                    oseba.etapne_zmage += 1
                #Kolesarju dodamo še uvrstitev in povečamo št. startov za 1
                oseba.uvrstitve_etap.append([pozicija,leto,etapa])
                oseba.starti_etap += 1
                
                pozicija += 1
            št_etap += 1
    #sedaj gremo še skozi skupne uvrstitve
    for leto in slovar:
        gc_razvrstitev = slovar[leto]['GC']
        pozicija = 1
        for kolesar in gc_razvrstitev:
            oseba = slovar_kolesarjev[kolesar]
            oseba.gc_uvrstitve.append([leto, pozicija])
            oseba.koncal_tour += 1
            pozicija += 1
    return slovar_kolesarjev





                    