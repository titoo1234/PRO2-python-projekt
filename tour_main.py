import orodja
#pridobivanje podatkov








slovar = orodja.pridobivanje_vseh_let('https://www.procyclingstats.com/race/tour-de-france',2019)
# kaj = input('Kaj želiš vedeti iz Toura leta 2020? Vrstni red skupne razvrstitve(GC) ali ....')
# input('zaenkrat boš mogu bit zadovoljen samo z naslednjim pritisne magično tipko ENTER')
# if neki neki
orodja.zapis(slovar[2020]['PIK'])
