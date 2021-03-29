import orodja
import branje_txt
from razred import *

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
    
mn_drzav = dict()

for kolesar in slovar_kolesarjev_brez_pravih_imen:
    d = slovar_kolesarjev_brez_pravih_imen[kolesar].nacionalnost
    if d not in mn_drzav:
        trenutna_d = Drzava(d)
        mn_drzav[d] = trenutna_d
        mn_drzav[d].dodaj_tekmovalca(slovar_kolesarjev_brez_pravih_imen[kolesar])
    else:
        mn_drzav[d].dodaj_tekmovalca(slovar_kolesarjev_brez_pravih_imen[kolesar])
        
        

print(mn_drzav["Slovenija"].zmaga(2020))

