#coding: utf-8

annie = [format(annie) for annie in range(30000, 100000)]

anne = ["{:05d}".format(anne) for anne in range(0, 18000)]

print(annie, anne)

### Bonne solution!
### Afficher deux listes successivement ne permet cependant pas d'utiliser le numéro de permis dans un script comme je l'ai montré en classe au début du cours du 15 février.
### Pour pouvoir le faire, il faudrait mettre en commentaire ta ligne 7 et ajouter les lignes suivantes:

mds = annie + anne
for md in mds:
	print(md)