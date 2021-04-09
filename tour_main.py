import orodja
import branje_txt
from razred import *
import difflib
from orodja import *
import pickle
from grafi import *
link = 'https://www.procyclingstats.com/race/tour-de-france'
datoteka = 'dat.txt'

#KODA ZA PRIDOBIVANJE PODATKOV 
slovar_imen = branje_txt.branje_ustvarjanje(datoteka)
# slovar_objektov_brez = branje_txt.ustvarjanje_objektov(slovar_imen)
# slovar_objektov =  branje_txt.zamenjava_kljucev(slovar_objektov_brez)
# 
#   
# # Korak 1
# #Slovar slovar_objektov_brez in slovar_objektov sva sharnila na dve datoteki,
#ker je časovno zelo dolgo trajalo, da je naredilo vse objekte.

# with open('slovar_objektov_brez_datoteka2', 'wb') as datoteka:
#     pickle.dump(slovar_objektov_ne_prava_imena, datoteka)

# with open('slovar_objektov_datoteka2', 'wb') as datoteka:
#     pickle.dump(slovar_objektov, datoteka)
                    



# Korak 2
#Iz datotek preberemo slovar vseh objektov. Slovarja sta oblike: 'Ime Priimek': Kolesar(Ime Priimek)
with open('slovar_objektov_brez_datoteka2', 'rb') as datoteka:
    slovar_kolesarjev_brez_pravih_imen = pickle.load(datoteka)
 
with open('slovar_objektov_datoteka2', 'rb') as datoteka:
    slovar_kolesarjev_prava_imena = pickle.load(datoteka)
    
# Naredimo še slovar_držav, t.j slovar, kjer so ključi ime države,
# vrednosti pa so objekti tipa Država 
sl_drzav = dict()
for kolesar in slovar_kolesarjev_brez_pravih_imen:
    d = slovar_kolesarjev_brez_pravih_imen[kolesar].nacionalnost
    if d not in sl_drzav:#še ni bilo te države, zato jo naredimo
        trenutna_d = Drzava(d)
        sl_drzav[d] = trenutna_d
        sl_drzav[d].dodaj_tekmovalca(slovar_kolesarjev_brez_pravih_imen[kolesar])
    else:
        sl_drzav[d].dodaj_tekmovalca(slovar_kolesarjev_brez_pravih_imen[kolesar])

kolesarji = list(slovar_kolesarjev_prava_imena.keys())
   

#KODA ZA UPORABNIKA
#==============================================================================

     
print("Pozdravljeni v analizi Dirke po Franciji!")
while True:
    print("")
    print("Na voljo so različni podatki, izberi med naslednjimi tako, da vpišeš željeno številko.")
    print("1.) Določen kolesar")
    print("2.) Določeno leto")
    print("3.) Določena država")
    print("4.) Splošni podatki")
    print("5.) Končaj")



    while True:
        try:
            stevka = int(input())
            break
        except:
            print('Napačen vnos. Vnesti morate število med 1 in 5.')
            
        
    if stevka == 1:
        print("Vnesi ime željenega kolesarja oblike Ime Priimek!")
        while True:
            kolesar = input("Kolesar: ")
            if kolesar in slovar_kolesarjev_prava_imena:
                oseba = slovar_kolesarjev_prava_imena[kolesar]
                
                print(oseba)
                print(oseba.dosezki())
                print("{:>40s} | {}".format('Razmerje:  Število zmag / Start etap', oseba.razmerje()))
                print("{:>40s} | {}".format('Skupaj prevoženih kilometrov', round(oseba.skupna_dolzina()),2))               
                print("{:>40s} | {}".format('Zmagal tour',oseba.kolikokrat_zmagal()))                                      
                print('{:>40}  {}'.format('Najboljše etapne uvrstitve:',orodja.izpisi_lepo(oseba.najbolse_uvrstitve()[0])))
                for i in range(1,11):
                    try:
                        print('{:>40s}  {}'.format(' ' , orodja.izpisi_lepo(oseba.najbolse_uvrstitve()[i])))
                    except:
                        pass
                    
                graf_kolesar(oseba)
                #relativna razvrstitev glede na število vseh tekmovalcev?
                #Posebni dosežki?
                
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
                    #izpiše katera leta?
            except:
                print("Neveljaven vnos, poskusite znova!")
                continue
                
            
            if leto in vsa_leta(link):
                if leto in [1905,1971,1988]:#Tukaj je prišlo do izjeme
                    števec = 0
                    for x in slovar_imen[leto]["ETAPE"]:
                        prva_etapa = x
                        if števec == 1:
                            break
                        števec += 1
                else:        
                    for x in slovar_imen[leto]["ETAPE"]:
                        prva_etapa = x
                        break
                # grafi.graf_zmage_drzav(Drzava.najuspesnejse_drzave(leto,sl_drzav))
                print("")
                print("{:>50s} | {:s}".format("leto",str(leto)))
                print("{:>50s} | {:s}".format("Število tekmovalcev na startu dirke ", str(len(slovar_imen[leto]["ETAPE"][prva_etapa]))))
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
                    print("{:>50s} | {:s}".format("Najboljši mladi kolesar (dobitnik bele majice)",'Bele majice to leto niso podeljevali'))
                    
                tabela = Drzava.najuspesnejse_drzave(leto,sl_drzav)
                        
                print("{:>50s} | {:s}".format('Država z največ etapnimi zmagami ' , tabela[0][0] +' ('+ str(tabela[0][1]) + ")"))
                for i in range(1, 100):
                    if tabela[0][1] == tabela[i][1]:
                        print("{:>50s} | {:s}".format(' ' , tabela[i][0] +' ('+ str(tabela[i][1]) + ")"))
                    else:
                        break
                #naredi graf
                kolac_drzave_zmage(tabela)
                
                
                vnos = input('Želite pogledati še rezultate posamičnih etap? da/ne ')
                if vnos == 'da':
                    print()
                    print('To leto je bilo izvedenih ' +str(len(slovar_imen[leto]['ETAPE'])) +' etap:')
                    etape = list(slovar_imen[leto]['ETAPE'].keys())
                    for i in range(1,len(slovar_imen[leto]['ETAPE']) + 1):
                        print("{:>20s}  {:s}".format(str(i)+') ' , etape[i-1]))
                    print('Izberite etapo, katere rezultate bi si želeli pogledati.')
                    while True:
                
                        vnos = input('Vnesite število: ')
                        
                        if vnos not in [str(i) for i in range(1,(len(slovar_imen[leto]['ETAPE'])+1))]:
                            print('Neveljaven vnos ali leto. Izbirati morate med številom 1 in ' + str(len(slovar_imen[leto]['ETAPE'])))
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
                dr = sl_drzav[drzava]
                zmage_skozi_leta = dr.etapne_zmage_skozi_leta()
                tab = []
                for leto in vsa_leta(link):
                    a, b = sl_drzav[drzava].doloceno_leto(leto)[1:3]
                    tab.append((leto, a, b))
                print(dr)
                print("{:>50s} | {:}".format("Število tekmovalcev skozi leta" , str(sl_drzav[drzava].st_tekmovalcev())))
                tab_kolesarjev = sorted([(kolesar.ime,kolesar.etapne_zmage) for kolesar in dr.tekmovalci],key = lambda x: x[1])[::-1]

                print("{:>50s} | {:} ({})".format('Najuspešnejši kolesarji glede na etapne zmage',tab_kolesarjev[0][0],tab_kolesarjev[0][1]))
                for i in range(1,5):
                    try:#lahko se zgodi, da je maanj kot 5 kolesarjev
                        if tab_kolesarjev[i][1] != 0:
                            print("{:>50s} | {:} ({})".format(' ',tab_kolesarjev[i][0],tab_kolesarjev[i][1]))
                    except:
                        continue
                print(dr.st_starti_etap())
                print(dr.st_etapnih_zmag())
                print(dr.skupne_zmage())
                
                if zmage_skozi_leta[0][1] == 0:
                    print("{:>50s} | {:}".format('Najuspešnejša leta',"-"))
                else:
                    print("{:>50s} | {:} ({})".format('Najuspešnejša leta',zmage_skozi_leta[0][0],zmage_skozi_leta[0][1]))
                for i in range(1,5):
                    try:
                        if zmage_skozi_leta[i][1] != 0:
                            print("{:>50s} | {:} ({})".format(' ',zmage_skozi_leta[i][0],zmage_skozi_leta[i][1]))
                
                    except:
                        continue
                #linijski diagram
                
                graf_zmage_drzav_test(tab)
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
        print(str(len(ni_izvedeno)) +'x je Dirka odpadla.')
        print('To je bilo v letih: ' + ', '.join([str(i) for i in ni_izvedeno]) +'.')
        etape = []
        for leto in vsa_leta(link):
            for etapa in  slovar_imen[leto]['ETAPE']:
                etape.append(etapa + ' ' + str(leto))
        najdalse = sorted(etape, key=lambda x: float(x.split()[-3]))
        print("{:>50s} | {:}".format('Število kolesarjev, ki je nastopilo v vseh letih', len(slovar_kolesarjev_brez_pravih_imen)) )
        
        print("{:>50s} | {:}".format('Število vseh etap', len(najdalse)) )
        print("{:>50s} | {:s}".format('Najdalša etapa',najdalse[-1]))
        print("{:>50s} | {:s}".format('Najkrajša etapa',najdalse[1])) #ena etapa je bila odpovedana
        naj = round(sum([float(x.split()[-3]) for x in najdalse])/len(najdalse),2)
        print("{:>50s} | {:} {}".format('Povprečna dolžina etape ',naj,'km'))
        z = zmagovalci(slovar_imen,slovar_kolesarjev_brez_pravih_imen)
        dolzine = sorted([(kolesar[0].dolzina_toura(kolesar[1]),kolesar[1]) for kolesar in z],key=lambda x: x[0])
        print("{:>50s} | {:}".format('Najdalša dolžina celotne Dirke',dolzine[-1][0]))
        print("{:>50s} | {:}".format('Najkrajša dolžina celotne Dirke',dolzine[0][0]))
        povp = round(sum([x[0] for x in dolzine])/len(dolzine),2)
        print("{:>50s} | {:}".format('Povprečna dolžina celotne Dirke',povp))
        najkolesar_etape = max([(kolesar.etapne_zmage, kolesar.ime) for kolesar in slovar_kolesarjev_prava_imena.values()])
        najkolesar_skupno = max([(kolesar.kolikokrat_zmagal(), kolesar.ime) for kolesar in slovar_kolesarjev_prava_imena.values()])
        print("{:>50s} | {:} ({})".format('Kolesar z največ etapnimi zmagami',najkolesar_etape[1], najkolesar_etape[0]))
        print("{:>50s} | {:} ({})".format('Kolesar z največ skupnimi zmagami',najkolesar_skupno[1], najkolesar_skupno[0]))
        najkolesar_razmerje = sorted([(kolesar.razmerje(), kolesar.ime) for kolesar in slovar_kolesarjev_prava_imena.values()])[::-1]
        print("{:>50s} | {:} ({})".format('Najboljše razmerje etapne zmage/končane etape', najkolesar_razmerje[0][1], najkolesar_razmerje[0][0]))
        print("{:>50s} | {:} ({})".format(' ', najkolesar_razmerje[1][1], najkolesar_razmerje[1][0]))
        print("{:>50s} | {:} ({})".format(' ', najkolesar_razmerje[2][1], najkolesar_razmerje[2][0]))
        najkolesar_etape_leto = [(kolesar.etapne_zmage_leto(), kolesar.ime) for kolesar in slovar_kolesarjev_prava_imena.values()]
        po_vrsti = sorted(najkolesar_etape_leto)[::-1]
    
        print("{:>50s} | {:} ({})".format('Kolesar z največ etapnimi zmagami v enem letu',max(najkolesar_etape_leto)[1],max(najkolesar_etape_leto)[0]))
        for i in range(1,5):
            print("{:>50s} | {:} ({})".format(' ',po_vrsti[i][1],po_vrsti[i][0]))
        najuspesnejse_drzave = slovar_tabela(Drzava.najuspesnejse_drzave_vsa_leta(sl_drzav))
        print("{:>50s} | {:} ({})".format('Države z njavečjim številom etapnih zmag',najuspesnejse_drzave[0][0],najuspesnejse_drzave[0][1]))
        for i in range(1,5):
            print("{:>50s} | {:} ({})".format(' ',najuspesnejse_drzave[i][0],najuspesnejse_drzave[i][1]))
        
        
        naj_drzave_gc = Drzava.najuspesnejse_drzave_vsa_leta_gc(sl_drzav)
        print("{:>50s} | {:} ({})".format('Države z njavečjim številom skupnih zmag',naj_drzave_gc[0][0],naj_drzave_gc[0][1]))
        for i in range(1,5):
            print("{:>50s} | {:} ({})".format(' ',naj_drzave_gc[i][0],naj_drzave_gc[i][1]))
        kolac_drzave_zmage_skupno(naj_drzave_gc)
        
        #histogram,fr. kolač
    
    elif stevka == 5:
        print("")
        print("Hvala!")
        break
    else:
        print('Vnesiti morate število med 1 in 5!')
    
# print(slovar_kolesarjev_prava_imena['Peter Sagan'].etapne_zmage_leto())
