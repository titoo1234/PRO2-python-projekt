#import razred
import ast
dat = open('dat.txt','r')
besedilo = dat.read()
slovar_vseh_let = ast.literal_eval(besedilo)
dat.close()
for leto in slovar_vseh_let:
    print(leto)
    