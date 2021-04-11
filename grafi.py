import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
import random
from orodja import *

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
def kolac_drzave_zmage_skupno(tabela):
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
    
    
def kolac_drzave_zmage(tabela):
    kratice = kratice_drzav()
    sl = dict()
    for drzava in tabela:
        if drzava[1] != 0:
            sl[kratice[drzava[0]]] = drzava[1]
    fig1, ax1 = plt.subplots()
    plt.title('Razmerje etapnih zmag po državah')
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
    for leto in range(min(list(slovar.keys())) - 5, min(max(list(slovar.keys()))+5,2021)):
        if leto not in slovar:
            slovar[leto] = 0
            
    pravi_sl = dict() # uredim slovar
    for kljuc in sorted(slovar):
        pravi_sl[kljuc] = slovar[kljuc]
        
    plt.plot(list(pravi_sl.keys()), list(pravi_sl.values()), marker = 'o', markersize = 5, c = [0,0,1], label="Število etapnih zmag")
    plt.legend(loc = 'upper left', fontsize = 13)
    plt.title("Etapne zmage skozi leta", fontsize = 21, fontweight = 'bold')
    plt.ylabel("Število zmag", fontsize = 18)
    plt.xlabel("Leto", fontsize = 15)
    plt.ylim(0, 10)
    plt.show()
    

