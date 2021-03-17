import ast
dat = open('dat.txt','r')
besedilo = dat.read()
slovar = ast.literal_eval(besedilo)
dat.close()
