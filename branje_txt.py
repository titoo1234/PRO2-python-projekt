#import razred
import ast
dat = open('dat.txt','r')
besedilo = dat.read()
slovar_vseh_let = ast.literal_eval(besedilo)
dat.close()
mn_kolesarjev = set()
for leto in slovar_vseh_let:
    for etapa in slovar_vseh_let[leto]['ETAPE']:
        for kolesar in slovar_vseh_let[leto]['ETAPE'][etapa]:
            if kolesar in mn_kolesarjev:
                continue
            else:
                #naredimo kolesarja
                mn_kolesarjev.add(kolesar)
                
    