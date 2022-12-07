met = float(input('Escreva uma metragem: '))
dm = met*10
cm = met*100
mm = met*1000
dam = met*0.1
hm = met*0.01
km = met*0.001
print('{} metro(s) equivale a {} decimetros {} centimetros e {} milimetros'.format(met, dm, cm, mm))
print('{} metro(s) equivale a {} 57decamentros, {} hectometros e {} kilometros'.format(met, dam, hm, km))