import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
import random
from orodja import *
b = [('Francija', 715), ('Belgija', 480), ('Italija', 266), ('Nizozemska', 170), ('Španija', 127), ('Nemčija', 92), ('Velika britanija', 72), ('Luksemburg', 68), ('Švica', 58), ('Združene države amerike', 39), ('Avstralija', 38), ('Kolumbija', 24), ('Danska', 22), ('Norveška', 20), ('Portugalska', 14), ('Irska', 14), ('Slovaška', 12), ('Rusija', 10), ('Uzbekistan', 9), ('Poljska', 7), ('Kazahstan', 7), ('Slovenija', 6), ('Avstrija', 4), ('Češka', 4), ('Ukrajina', 4), ('Estonija', 4), ('Kanada', 2), ('Mehika', 2), ('Latvija', 2), ('Južna afrika', 2), ('Švedska', 1), ('Brazilija', 1), ('Litva', 1), ('Alžirija', 0), ('Tunizija', 0), ('Monako', 0), ('Nova zelandija', 0), ('Jugoslavija', 0), ('Romunija', 0), ('Maroko', 0), ('Lihtenštajn', 0), ('Venezuela', 0), ('Japonska', 0), ('Finska', 0), ('Moldavija', 0), ('Hrvaška', 0), ('Belorusija', 0), ('Kostarika', 0), ('Argentina', 0), ('Kitajska', 0), ('Eritreja', 0), ('Etiopija', 0), ('Ekvador', 0), ('Izrael', 0)]



a = [('Slovenija', 4), ('Kolumbija', 2), ('Irska', 2), ('Avstralija', 2), ('Danska', 2), ('Belgija', 2), ('Francija', 2), ('Kazahstan', 1), ('Norveška', 1), ('Poljska', 1), ('Nemčija', 1), ('Švica', 1), ('Izrael', 0), ('Ekvador', 0), ('Etiopija', 0), ('Eritreja', 0), ('Kitajska', 0), ('Argentina', 0), ('Kostarika', 0), ('Belorusija', 0), ('Hrvaška', 0), ('Moldavija', 0), ('Južna Afrika', 0), ('Finska', 0), ('Japonska', 0), ('Estonija', 0), ('Venezuela', 0), ('Litva', 0), ('Latvija', 0), ('Ukrajina', 0), ('Uzbekistan', 0), ('Rusija', 0), ('češka', 0), ('Slovaška', 0), ('Brazilija', 0), ('Mehika', 0), ('Kanada', 0), ('Združene države Amerike', 0), ('Švedska', 0), ('Portugalska', 0), ('Lihtenštajn', 0), ('Maroko', 0), ('Velika Britanija', 0), ('Romunija', 0), ('Yugoslavia', 0), ('Nizozemska', 0), ('Avstrija', 0), ('Nova Zelandija', 0), ('Monako', 0), ('Španija', 0), ('Tunizija', 0), ('Alžirija', 0), ('Luksemburg', 0), ('Italija', 0)]

# Compute frequency and bins
# frequency, bins = np.histogram(x, bins=10, range=[0, 100])
# plt.rcParams.update({'figure.figsize':(7,5), 'figure.dpi':100})

# Plot Histogram on x
# x = ['asd','aasdasd','bg']
# plt.hist(x, [1,2,3])
# plt.gca().set(title='Frequency Histogram', ylabel='Frequency')
# fig, axes = plt.subplots(figsize=(7,5), dpi=100)
# plt.bar([1,2,3], [1,2,3])

def graf_zmage_drzav(tabela):
    '''iz tabele "najuspešnejše_države" naredi histogram'''
    #najprej iz tabele razvrsti imena in št. zmag
    sl = dict()
    for drzava in tabela:
        if drzava[1] != 0:
            
            sl[drzava[0]] = drzava[1] 
    fig, axes = plt.subplots(figsize=(7,5), dpi=100)
    plt.bar(list(sl.keys()), list(sl.values()))
    plt.show()
    
        
#graf_zmage_drzav(a)
# print('asd')
def kolac_drzave_zmage(tabela):
    kratice = kratice_drzav()
    sl = dict()
    sl["Ostalo"] = 0
    for drzava in tabela:
        if drzava[1] != 0:
            if drzava[1] > 6:
                sl[kratice[drzava[0]]] = drzava[1]
            else:
                sl["Ostalo"] += drzava[1]
    fig1, ax1 = plt.subplots()
    plt.title('Razmerje skupnih zmag po državah')
    ax1.pie(list(sl.values()), labels=list(sl.keys()), autopct=lambda p : '{:.1f}% ({:,.0f})'.format(p,p * sum(sl.values())/100),shadow=True, startangle=90)
    plt.show()
    
#kolac_drzave_zmage(a)
    
def graf_zmage_drzav_test(tabela):
    '''iz tabele (elementi so (leto, st etapnih zmag, st tekmovalcev)), naredi linijski diagram'''
    #najprej iz tabele razvrsti imena in št. zmag
    fig = plt.figure(figsize = [9, 6])
    plt.plot([leto[0] for leto in tabela], [zmage[1] for zmage in tabela], marker = 'o', markersize = 3, c = [0,0,1], label="Etapne zmage")
    plt.plot([leto[0] for leto in tabela], [tekmovalci[2] for tekmovalci in tabela], marker = '*', markersize = 3, c = [0.66,0.66,0.66], label ="Št. tekmovalcev")
    plt.legend(loc = 'upper left', fontsize = 13)
    plt.title("Etapne zmage skozi leta", fontsize = 21, fontweight = 'bold')
    plt.ylabel("Število zmag & tekmovalcev", fontsize = 18)
    plt.xlabel("Leto", fontsize = 15)
    plt.show()
    
    
def vse_drzave_zmage(slovar):
    drzave=[]
    zmage = []
    for drzava in slovar:
        dr,zmaga= drzava
        #v histogram dam države z 5 ali več zmagami
        if zmaga > 4:
            drzave.append(dr)
            zmage.append(zmaga)
    fig, axes = plt.subplots(figsize=(7,5), dpi=100)
    

    
    plt.bar(drzave, zmage)
    plt.show()
    
    
def graf_kolesar(kolesar):
    slovar = kolesar.st_etapne_zmage_leto()
    # dodam 0 za tista vmesna leta ko ni nastopil npr nastopil 2017, 2018 in 2020, dodam 0 za 2019 in še kako leto prej
    for leto in range(min(list(slovar.keys())) - 5, 2021):
        if leto not in slovar:
            slovar[leto] = 0
            
    pravi_sl = dict() # uredim slovar
    for kljuc in sorted(slovar):
        pravi_sl[kljuc] = slovar[kljuc]
        
    plt.plot(list(pravi_sl.keys()), list(pravi_sl.values()), marker = 'o', markersize = 3, c = [0,0,1], label="Število etapnih zmag")
    plt.legend(loc = 'upper left', fontsize = 13)
    plt.title("Etapne in skupne zmage skozi leta", fontsize = 21, fontweight = 'bold')
    plt.ylabel("Število zmag", fontsize = 18)
    plt.xlabel("Leto", fontsize = 15)
    plt.show()
    
    
    
    
# vse_drzave_zmage(b)  

