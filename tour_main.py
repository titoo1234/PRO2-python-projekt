import orodja
import branje_txt

import pickle
link = 'https://www.procyclingstats.com/race/tour-de-france'
datoteka = 'proba.txt'

# slovar_imen = branje_txt.branje_ustvarjanje(datoteka)
# slovar_objektov = ustvarjanje_objektov(slovar_imen)
# for kolesar in slovar_objektov:
#     print(kolesarji[kolesar])
#     print(kolesarji[kolesar].dosežki())


a= orodja.pridobivanje_vseh_let(link,2017)
slovar_objektov = branje_txt.ustvarjanje_objektov(a)

 
 
# Step 2
with open('test', 'wb') as config_dictionary_file:
 
  # Step 3
    pickle.dump(slovar_objektov, config_dictionary_file)
                    
#                 else:
#                     yield razred.Kolesar(orodja.ime_za_link(kolesar))


# Step 2
with open('test', 'rb') as config_dictionary_file:
 
    # Step 3
    slovar_kolesarjev = pickle.load(config_dictionary_file)
 
    # After config_dictionary is read from file
    print(slovar_kolesarjev)





# slovar = orodja.pridobivanje_vseh_let('https://www.procyclingstats.com/race/tour-de-france',2015)
# kaj = input('Kaj želiš vedeti iz Toura leta 2020? Vrstni red skupne razvrstitve(GC) ali ....')
# input('zaenkrat boš mogu bit zadovoljen samo z naslednjim pritisne magično tipko ENTER')
# if neki neki
# orodja.zapis(slovar[2020]['PIK'])
