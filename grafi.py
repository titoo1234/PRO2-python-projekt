import matplotlib.pyplot as plt
import numpy as np


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
    return plt.bar(list(sl.keys()), list(sl.values()))
    
        
graf_zmage_drzav(a)
# print('asd')
def kolac_drazave_zmage(tabela):
    sl = dict()
    for drzava in tabela:
        if drzava[1] != 0:
            
            sl[drzava[0]] = drzava[1] 
    fig1, ax1 = plt.subplots()
    ax1.pie(list(sl.values()), labels=list(sl.keys()), autopct='%1.1f%%',shadow=True, startangle=90)
    
kolac_drazave_zmage(a)
    
