import random



nb_equipes = int(input("Combien d'equipes participent ? : "))
test_parite = nb_equipes % 2
nb_journees = nb_equipes + test_parite - 1
nb_match = int(nb_equipes/2) + test_parite

liste_equipe=[]
for i in range (0, nb_equipes):
    eq = input ((str("Entrez le nom de l'equipe numero "))+str(i+1)+" : ")
    liste_equipe.append(eq)
if test_parite == 1:
	liste_equipe.append("exempt")
random.shuffle(liste_equipe)

print (liste_equipe)	
print(liste_equipe[0])
print (nb_match)
print (test_parite)
for j in range (0,nb_journees):
	print ('******')
	idx = 0
	for i in range (0, nb_match):
		print (liste_equipe[idx]," - ",liste_equipe[idx+1])
		idx = idx+2
	liste_equipe_new=[]
	liste_equipe_new.append(liste_equipe[0])	
	for k in range (1, nb_equipes):
		if k == nb_equipes-1:
			r = 1
		else:
			r = k+1
		liste_equipe_new.append(liste_equipe[r])
	print(liste_equipe_new)	
	liste_equipe=liste_equipe_new	
