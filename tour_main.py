import orodja
import branje_txt
from razred import *
import difflib
from orodja import *

import pickle
link = 'https://www.procyclingstats.com/race/tour-de-france'
datoteka = 'vse.txt'

slovar_imen = branje_txt.branje_ustvarjanje(datoteka)
# slovar_objektov_brez = branje_txt.ustvarjanje_objektov(slovar_imen)
# slovar_objektov =  branje_txt.zamenjava_kljucev(slovar_objektov_brez)

  
# #Step 1
# with open('slovar_objektov_brez_datoteka', 'wb') as datoteka:
#     pickle.dump(slovar_objektov_ne_prava_imena, datoteka)

# with open('slovar_objektov_datoteka', 'wb') as datoteka:
#     pickle.dump(slovar_objektov, datoteka)
                    



# #step 2
with open('slovar_objektov_ne_prava_imena', 'rb') as datoteka:
    slovar_kolesarjev_brez_pravih_imen = pickle.load(datoteka)
 
with open('slovar_objektov_datoteka', 'rb') as datoteka:
    slovar_kolesarjev_prava_imena = pickle.load(datoteka)
    
sl_drzav = dict()

for kolesar in slovar_kolesarjev_brez_pravih_imen:
    d = slovar_kolesarjev_brez_pravih_imen[kolesar].nacionalnost
    if d not in sl_drzav:
        trenutna_d = Drzava(d)
        sl_drzav[d] = trenutna_d
        sl_drzav[d].dodaj_tekmovalca(slovar_kolesarjev_brez_pravih_imen[kolesar])
    else:
        sl_drzav[d].dodaj_tekmovalca(slovar_kolesarjev_brez_pravih_imen[kolesar])
        
        

#print(mn_drzav["Slovenija"].zmaga(2020))
kolesarji = list(slovar_kolesarjev_prava_imena.keys())
        
print("Pozdravljeni v analizi Dirke po Franciji!")
print("")
print("Na voljo so različni podatki, izberi med naslednjimi tako, da vpišeš željeno številko.")
print("1.) Določen kolesar")
print("2.) Določeno leto")
print("3.) Določena država")
print("4.) Splošni podatki")
print("5.) Informacije")
print("6.) Končaj")

#stevka = int(input())

while True:
    stevka = int(input())
    if stevka == 1:
        print("Vnesi ime željenega kolesarja oblike ime-priimek!")
        kolesar = input()
        #print(difflib.get_close_matches(a, kolesarji))
        if kolesar in slovar_kolesarjev_prava_imena:
            print(slovar_kolesarjev_prava_imena[kolesar])
            print(slovar_kolesarjev_prava_imena[kolesar].dosezki())
            print(slovar_kolesarjev_prava_imena[kolesar].kolikokrat_zmagal())
        elif len(difflib.get_close_matches(kolesar, kolesarji)) > 0:
            print("Ste morda mislili katerega od naslednjiih kolesarjev?")
            print(", ".join(difflib.get_close_matches(kolesar, kolesarji)))
        else:
            print("Napačen vnos, poskusite znova!")
            
    elif stevka == 2:
        print("Vnesi ime željenega leta")
        leto = int(input())
        if leto not in vsa_leta(link):
            print("Neveljavno leto, poskusite znova!")
        else:
            for x in slovar_imen[leto]["ETAPE"]:
                prva_etapa = x
                break
            
            print("Število tekmovalcev na startu dirke: " + str(len(slovar_imen[leto]["ETAPE"][prva_etapa])))
            print("Število tekmovalcev na koncu dirke " + str(len(slovar_imen[leto]["GC"])))
            print("Dolžina dirke " + str(slovar_kolesarjev_brez_pravih_imen[slovar_imen[leto]["GC"][0]].dolzina_toura(leto)))
            print("Zmagovalec dirke: " + slovar_kolesarjev_brez_pravih_imen[slovar_imen[leto]["GC"][0]].ime)
            try: 
                print("Zmagovalec točkovanja za zeleno majico: " + slovar_kolesarjev_brez_pravih_imen[slovar_imen[leto]["ZELENA"][0]].ime)
            except:
                print("Točkovanja za zeleno majico ni bilo")
            try: 
                print("Zmagovalec točkovanja za pikčasto majico: " + slovar_kolesarjev_brez_pravih_imen[slovar_imen[leto]["PIK"][0]].ime)
            except:
                print("Točkovanja za pikčasto majico ni bilo")
            try: 
                print("Najboljši mladi kolesar (dobitnik bele majice): " + slovar_kolesarjev_brez_pravih_imen[slovar_imen[leto]["BELA"][0]].ime)
            except:
                print('Bele majice to leto niso podeljevali.')
            print('Država z največ etapnimi zmagami: ' + orodja.najuspesnejse_drzave(leto,sl_drzav)[0][0] +': '+ str(orodja.najuspesnejse_drzave(leto,sl_drzav)[0][1]) )
                
                      
                
    elif stevka == 3:
        print("Vnesi ime željene države v slovenščini")
        drzava = input()
        if drzava in sl_drzav:
            print(sl_drzav[drzava])
            print(sl_drzav[drzava].st_starti_etap())
            print(sl_drzav[drzava].st_etapnih_zmag())
            print(sl_drzav[drzava].skupne_zmage())
        elif len(difflib.get_close_matches(drzava, sl_drzav)) > 0:
            print("Ste morda mislili katero od naslednjiih držav?")
            print(", ".join(difflib.get_close_matches(drzava, sl_drzav)))
        else:
            print("Napačen vnos, poskusite znova!")
    
    elif stevka == 4:
        pass
    
    elif stevka == 5:
        pass
    
    elif stevka == 6:
        break
