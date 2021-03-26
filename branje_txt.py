import razred
import ast
import orodja

import pickle
 

  
  
  
def branje_ustvarjanje(datoteka):
    '''iz datoteke prebere slovar in ga naredi'''
    
    dat = open(datoteka,'r')#sicer je 'dat.txt'
    besedilo = dat.read()
    slovar_vseh_let = ast.literal_eval(besedilo)
    dat.close()
    return slovar_vseh_let

def zamenjava_kljucev(slovar):
    nov = dict()
    for _, kolesar in slovar.items():
        nov[kolesar.ime] = kolesar
    return nov

def ustvarjanje_objektov(slovar):
    '''iz slovarja prebere vsa imena kolesarjev,
        naredi objekte in jih shrani v nov slovar
    '''
    slovar_kolesarjev = dict()
    mn_kolesarjev = set()
    for leto in slovar:
        mn_etap = slovar[leto]['ETAPE']
        
        št_etap = 1
        for etapa in mn_etap:
            # if št_etap == 3: #to sam zanenkrat da ne čakama predougo
            #     break
            rezultati = slovar[leto]['ETAPE'][etapa]
            pozicija = 1
            for kolesar in rezultati:
                # if pozicija == 20: #to sam zanenkrat da ne čakama predougo
                #     break
                if kolesar not in mn_kolesarjev:
                    slovar_kolesarjev[kolesar] = (razred.Kolesar(orodja.ime_za_link(kolesar)))
                    mn_kolesarjev.add(kolesar)
                oseba = slovar_kolesarjev[kolesar]
                
                if št_etap == 1:
                    oseba.starti_tour += 1  #kolikorat je začel dirko po Franciji              
                if pozicija == 1:
                    oseba.etapne_zmage += 1
                oseba.uvrstitve_etap.append([pozicija,leto,etapa])
                oseba.starti_etap += 1
                
                
                
                pozicija += 1
            št_etap += 1
    for leto in slovar:
        gc_razvrstitev = slovar[leto]['GC']
        pozicija = 1
        for kolesar in gc_razvrstitev:
            oseba = slovar_kolesarjev[kolesar]
            oseba.gc_uvrstitve.append([leto, pozicija])
            oseba.koncal_tour += 1
            pozicija += 1
    return slovar_kolesarjev





                    