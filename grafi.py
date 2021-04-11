import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from orodja import *

def kolac_drzave_zmage_skupno(tabela):
    '''
       Nariše frekvenčni kolač glede na število skupnih zmag za države 
    '''
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
    '''
       Nariše frekvenčni kolač glede na število etapnih zmag za določeno leto
    '''
    kratice = kratice_drzav()
    sl = dict()
    for drzava in tabela:
        if drzava[1] != 0:
            sl[kratice[drzava[0]]] = drzava[1]
    fig1, ax1 = plt.subplots()
    plt.title('Razmerje etapnih zmag po državah')
    ax1.pie(list(sl.values()), labels=list(sl.keys()), autopct=lambda p : '{:.1f}% ({:,.0f})'.format(p,p * sum(sl.values())/100),shadow=True, startangle=90)
    plt.show()

    
def graf_zmage_drzav_test(tabela):
    '''
        Iz tabele (elementi so (leto, st etapnih zmag, st tekmovalcev)), naredi linijski diagram za določeno državo
    '''
    #najprej iz tabele razvrsti imena in št. zmag
    fig = plt.figure(figsize = [9, 6])
    plt.plot([leto[0] for leto in tabela], [zmage[1] for zmage in tabela], marker = 'o', markersize = 3, c = [0,0,1], label="Etapne zmage")
    plt.plot([leto[0] for leto in tabela], [tekmovalci[2] for tekmovalci in tabela], marker = '*', markersize = 3, c = [1,0.66,0], label ="Št. tekmovalcev")
    plt.legend(loc = 'upper left', fontsize = 13)
    plt.title("Etapne zmage skozi leta", fontsize = 21, fontweight = 'bold')
    plt.ylabel("Število zmag & tekmovalcev", fontsize = 18)
    plt.xlabel("Leto", fontsize = 15)
    plt.show()
    
    
def graf_kolesar(kolesar):
    '''
        Nariše linijski diagram za kolesarjeve etapne zmage (če etapne zmage nima, diagrama ne nariše)
    '''
    slovar = kolesar.st_etapne_zmage_leto()
    if len(slovar) == 0: # kolesar nima nobene etapne zmage, zato grafa ne nariše
        return None
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
    

