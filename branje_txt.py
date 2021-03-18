import razred
import ast
import orodja
def branje_ustvarjanje():
    # slovar_kolesarjev = dict()
    dat = open('dat.txt','r')
    besedilo = dat.read()
    slovar_vseh_let = ast.literal_eval(besedilo)
    dat.close()
    mn_kolesarjev = []
    for leto in slovar_vseh_let:
        for etapa in slovar_vseh_let[leto]['ETAPE']:
            for kolesar in slovar_vseh_let[leto]['ETAPE'][etapa]:
                if kolesar in mn_kolesarjev:
                    continue
                else:
                    yield razred.Kolesar(orodja.ime_za_link(kolesar))
                    # slovar_kolesarjev[kolesar] = (razred.Kolesar(orodja.ime_za_link(kolesar)))
                    mn_kolesarjev.append(kolesar)
    # return slovar_kolesarjev
   
#dat = open("kolesarji.txt", "w", encoding="utf-8")
# for kolesar in branje_ustvarjanje():
#     print(kolesar)
    
#dat.close()
# tab=[i for i in branje_ustvarjanje()]
# dat = open("kolesarji.txt", "w", encoding="utf-8")
# print(slo,file=dat)
    
# dat.close()
