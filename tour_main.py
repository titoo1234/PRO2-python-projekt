import orodja
import branje_txt
from razred import *
import difflib
from orodja import *
# import grafi
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



    while True:
        try:
            stevka = int(input())
            break
        except:
            print('Napačen vnos. Vnesti morate število med 1 in 6.')
            
        
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
                print('{:25} {}'.format('Najboljše etapne uvrstitve:',orodja.izpisi_lepo(oseba.najbolse_uvrstitve()[0])) )
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
                # grafi.graf_zmage_drzav(Drzava.najuspesnejse_drzave(leto,sl_drzav))
                print("")
                # print("{:>10s} | '{:s}'".format("Genre", movie['Genre']))
                print("{:>50s} | {:s}".format("Število tekmovalcev na startu dirke: ", str(len(slovar_imen[leto]["ETAPE"][prva_etapa]))))
                print("{:>50s} | {:s}".format("Število tekmovalcev na koncu dirke ", str(len(slovar_imen[leto]["GC"]))))
                print("{:>50s} | {:s}".format("Dolžina dirke " , str(slovar_kolesarjev_brez_pravih_imen[slovar_imen[leto]["GC"][0]].dolzina_toura(leto))))
                print("{:>50s} | {:s}".format("Zmagovalec dirke: " , slovar_kolesarjev_brez_pravih_imen[slovar_imen[leto]["GC"][0]].ime))
                try: 
                    print("{:>50s} | {:s}".format("Zmagovalec točkovanja za zeleno majico" , slovar_kolesarjev_brez_pravih_imen[slovar_imen[leto]["ZELENA"][0]].ime))
                except:
                    print("{:>50s} | {:s}".format("Zmagovalec točkovanja za zeleno majico","Točkovanja za zeleno majico ni bilo"))
                try: 
                    print("{:>50s} | {:s}".format("Zmagovalec točkovanja za pikčasto majico" , slovar_kolesarjev_brez_pravih_imen[slovar_imen[leto]["PIK"][0]].ime))
                except:
                    print("{:>50s} | {:s}".format("Zmagovalec točkovanja za pikčasto majico","Točkovanja za pikčasto majico ni bilo"))
                try: 
                    print("{:>50s} | {:s}".format("Najboljši mladi kolesar (dobitnik bele majice)" , slovar_kolesarjev_brez_pravih_imen[slovar_imen[leto]["BELA"][0]].ime))
                except:
                    print("{:>50s} | {:s}".format("Najboljši mladi kolesar (dobitnik bele majice)",'Bele majice to leto niso podeljevali.'))
                        
                print("{:>50s} | {:s}".format('Država z največ etapnimi zmagami ' , Drzava.najuspesnejse_drzave(leto,sl_drzav)[0][0] +' ('+ str(Drzava.najuspesnejse_drzave(leto,sl_drzav)[0][1]) + ")"))
                for i in range(1, 100):
                    if Drzava.najuspesnejse_drzave(leto,sl_drzav)[0][1] == Drzava.najuspesnejse_drzave(leto,sl_drzav)[i][1]:
                        print("{:>50s} | {:s}".format(' ' , Drzava.najuspesnejse_drzave(leto,sl_drzav)[i][0] +' ('+ str(Drzava.najuspesnejse_drzave(leto,sl_drzav)[i][1]) + ")"))
                    else:
                        break
                vnos = input('Želite pogledati še rezultate posamičnih etap? da/ne ')
                if vnos == 'da':
                    print()
                    print('To leto je bilo izvedenih ' +str(len(slovar_imen[leto]['ETAPE'])) +' etap:')
                    etape = list(slovar_imen[leto]['ETAPE'].keys())
                    for i in range(1,len(slovar_imen[leto]['ETAPE']) + 1):
                        print("{:>20s}  {:s}".format(str(i)+') ' , etape[i-1]))
                    print('Izberite etapo, katere rezultate bi si želeli pogledati.')
                    while True:
                
                        vnos = input('Vnesite številko: ')
                        
                        if vnos not in [str(i) for i in range(1,(len(slovar_imen[leto]['ETAPE'])+1))]:
                            print('Neveljaven vnos ali leto. Izbirati morate med številom 1 in ' + str(len(slovar_imen[leto]['ETAPE'])+1))
                        else:
                            print()
                            rezultat = slovar_imen[leto]['ETAPE'][etape[int(vnos)-1]]
                            for i in range(1,11):
                                try:
                               
                                    print("{:>20s}   {:s}".format(str(i) +'. mesto: ', slovar_kolesarjev_brez_pravih_imen[rezultat[i-1]].ime ))
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
        print('Do sedaj je bilo izvedenih ' + str(len(slovar_imen))+' izvedb Dirke po Franciji.')
        ni_izvedeno = []
        for leto in range(1903,2021):
            if leto not in slovar_imen:
                ni_izvedeno.append(leto)
        print('Do sedaj se je zgodilo ' + str(len(ni_izvedeno)) +'x da je Dirka odpadla.')
        print('To je bilo v letih: ' + ', '.join([str(i) for i in ni_izvedeno]) +'.')
        etape = []
        for leto in vsa_leta(link):
            for etapa in  slovar_imen[leto]['ETAPE']:
                etape.append(etapa + ' ' + str(leto))
        najdalse = sorted(etape, key=lambda x: float(x.split()[-3]))
        print("{:>40s} | {:}".format('Število vseh etap', len(najdalse)) )
        print("{:>40s} | {:s}".format('Najdalša etapa',najdalse[-1]))
        print("{:>40s} | {:s}".format('Najkrajša etapa',najdalse[1])) #ena etapa je bila odpovedana
        naj = round(sum([float(x.split()[-3]) for x in najdalse])/len(najdalse),2)
        print("{:>40s} | {:} {}".format('Povprečna dolžina etape ',naj,'km'))
        z = zmagovalci(slovar_imen,slovar_kolesarjev_brez_pravih_imen)
        dolzine = sorted([(kolesar[0].dolzina_toura(kolesar[1]),kolesar[1]) for kolesar in z],key=lambda x: x[0])
        # print(dolzine)
        print("{:>40s} | {:}".format('Najdalša dolžina celotne Dirke',dolzine[-1][0]))
        print("{:>40s} | {:}".format('Najkrajša dolžina celotne Dirke',dolzine[0][0]))
        povp = round(sum([x[0] for x in dolzine])/len(dolzine),2)
        print("{:>40s} | {:}".format('Povprečna dolžina celotne Dirke',povp))
        najkolesar_etape = max([(kolesar.etapne_zmage, kolesar.ime) for kolesar in slovar_kolesarjev_prava_imena.values()])
        najkolesar_skupno = max([(kolesar.kolikokrat_zmagal().split()[-1], kolesar.ime) for kolesar in slovar_kolesarjev_prava_imena.values()])
        print("{:>40s} | {:} ({})".format('Kolesar z največ etapnimi zmagami',najkolesar_etape[1], najkolesar_etape[0]))
        print("{:>40s} | {:} ({})".format('Kolesar z največ skupnimi zmagami',najkolesar_skupno[1], najkolesar_skupno[0]))
        najkolesar_razmerje = max([(kolesar.razmerje(), kolesar.ime) for kolesar in slovar_kolesarjev_prava_imena.values()])
        print("{:>40s} | {:} ({})".format('Najboljše razmerje etapne zmage/končane etape',najkolesar_razmerje[1], najkolesar_razmerje[0]))

        #največje število etpanih zmag na enem touru kolesar
        # največje število etapnih zmag na enem touru država
        #največje število zmaganih tourov dražva
        #
        print('Najuspešnjejše države:')
        #histogram,fr. kolač
        
        
    
    elif stevka == 5:
        pass
    
    elif stevka == 6:
        break
    
