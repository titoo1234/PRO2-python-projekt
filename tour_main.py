import orodja
import branje_txt
link = 'https://www.procyclingstats.com/race/tour-de-france'
datoteka = 'proba.txt'

# slovar_imen = branje_txt.branje_ustvarjanje(datoteka)
# slovar_objektov = ustvarjanje_objektov(slovar_imen)
# for kolesar in slovar_objektov:
#     print(kolesarji[kolesar])
#     print(kolesarji[kolesar].dosežki())


a= orodja.pridobivanje_vseh_let(link,2020)
slovar_objektov = branje_txt.ustvarjanje_objektov(a)








# slovar = orodja.pridobivanje_vseh_let('https://www.procyclingstats.com/race/tour-de-france',2015)
# kaj = input('Kaj želiš vedeti iz Toura leta 2020? Vrstni red skupne razvrstitve(GC) ali ....')
# input('zaenkrat boš mogu bit zadovoljen samo z naslednjim pritisne magično tipko ENTER')
# if neki neki
# orodja.zapis(slovar[2020]['PIK'])
