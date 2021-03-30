import orodja
import branje_txt
from razred import *
import difflib
from orodja import *

import pickle
link = 'https://www.procyclingstats.com/race/tour-de-france'
datoteka = 'vse.txt'

#NA NOVO SE MORAJO NAREDITI OBJEKTI!!!!!!
#NA NOVO SE MORAJO NAREDITI OBJEKTI!!!!!!
#NA NOVO SE MORAJO NAREDITI OBJEKTI!!!!!!
#NA NOVO SE MORAJO NAREDITI OBJEKTI!!!!!!


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
while True:
    print("")
    print("Na voljo so različni podatki, izberi med naslednjimi tako, da vpišeš željeno številko.")
    print("1.) Določen kolesar")
    print("2.) Določeno leto")
    print("3.) Določena država")
    print("4.) Splošni podatki")
    print("5.) Informacije")
    print("6.) Končaj")

    #stevka = int(input())


    stevka = int(input())
    if stevka == 1:
        print("Vnesi ime željenega kolesarja oblike ime-priimek!")
        while True:
            kolesar = input("Kolesar: ")
            #print(difflib.get_close_matches(a, kolesarji))
            if kolesar in slovar_kolesarjev_prava_imena:
                oseba = slovar_kolesarjev_prava_imena[kolesar]
                print(oseba)
                print(oseba.dosezki())
                print(oseba.kolikokrat_zmagal())
                print('Najboljše etapne uvrstitve: ' + orodja.izpisi_lepo(oseba.najbolse_uvrstitve()[0]) )
                for i in range(1,11):
                    try:
                        print('                            ' + orodja.izpisi_lepo(oseba.najbolse_uvrstitve()[i]))
                    except:
                        pass
                
                
                print()
                vnos = input("Želite nadaljevati? (da/ne) ")
                if vnos != "da":
                    break
            elif len(difflib.get_close_matches(kolesar, kolesarji)) > 0:
                print("Ste morda mislili katerega od naslednjiih kolesarjev?")
                print(", ".join(difflib.get_close_matches(kolesar, kolesarji)))
            else:
                print("Napačen vnos, poskusite znova!")
            
    elif stevka == 2:
        while True:
            try:
                leto = int(input("Vnesi ime željenega leta: "))
                if leto not in vsa_leta(link):
                    print("Neveljavno leto, poskusite znova!")
                    #leto = int(input("Vnesi ime željenega leta: "))
            except:
                print("Neveljaven vnos, poskusite znova!")
                continue
                
            
            if leto in vsa_leta(link):
                for x in slovar_imen[leto]["ETAPE"]:
                    prva_etapa = x
                    break
                
                print("")
                print("Število tekmovalcev na startu dirke: "+ str(len(slovar_imen[leto]["ETAPE"][prva_etapa])))
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
                        
                print('Država z največ etapnimi zmagami: ' + Drzava.najuspesnejse_drzave(leto,sl_drzav)[0][0] +' ('+ str(Drzava.najuspesnejse_drzave(leto,sl_drzav)[0][1]) + ")")
                for i in range(1, 100):
                    if Drzava.najuspesnejse_drzave(leto,sl_drzav)[0][1] == Drzava.najuspesnejse_drzave(leto,sl_drzav)[i][1]:
                        print('                                  ' + Drzava.najuspesnejse_drzave(leto,sl_drzav)[i][0] +' ('+ str(Drzava.najuspesnejse_drzave(leto,sl_drzav)[i][1]) + ")")
                    else:
                        break
                vnos = input('Želite pogledati še rezultate posamičnih etap? da/ne ')
                if vnos == 'da':
                    print()
                    print('To leto je bilo izvedenih ' +str(len(slovar_imen[leto]['ETAPE'])) +' etap:')
                    etape = list(slovar_imen[leto]['ETAPE'].keys())
                    for i in range(1,len(slovar_imen[leto]['ETAPE']) + 1):
                        print(str(i)+') ' + etape[i-1])
                    print('Izberite etapo, katere rezultate bi si želeli pogledati.')
                    while True:
                
                        vnos = input('Vnesite številko: ')
                        
                        if vnos not in [str(i) for i in range(1,(len(slovar_imen[leto]['ETAPE'])))]:
                            print('Neveljaven vnos ali leto. Izbirati morate med številom 1 in ' + str(len(slovar_imen[leto]['ETAPE'])+1))
                        else:
                            print()
                            rezultat = slovar_imen[leto]['ETAPE'][etape[int(vnos)-1]]
                            for i in range(1,11):
                                try:
                               
                                    print(str(i) +'. mesto: '+ slovar_kolesarjev_brez_pravih_imen[rezultat[i-1]].ime )
                                except:
                                    pass
                            vnos = input('Želite izvedeti še rezultate za druge etape? da/ne ')
                            if vnos != 'da':
                                
                                break
                            
                        
                        
                        
                    
                print("")
                #frekvenčni kolač
                vnos = input("Želite nadaljevati s kakšnim drugim letom? (da/ne) ")
                if vnos != "da":
                    break
                      
                
    elif stevka == 3:
        while True:
            drzava = input("Vnesi ime željene države v slovenščini: ")
            try:
                drzava = drzava[0].capitalize() + drzava[1:]
            except:
                print("Napačen vnos, poskusite znova!")
                continue
            if drzava in sl_drzav:
                print(sl_drzav[drzava])
                print("Število tekmovalcev skozi leta: " + str(sl_drzav[drzava].st_tekmovalcev()))
                print(sl_drzav[drzava].st_starti_etap())
                print(sl_drzav[drzava].st_etapnih_zmag())
                print(sl_drzav[drzava].skupne_zmage())
                #linijski diagram
                print("")
                vnos = input("Želite nadaljevati? (da/ne) ")
                if vnos != "da":
                    break
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
    
