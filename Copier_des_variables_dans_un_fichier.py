a = 5
b = 2.83
c = 67
f = open('test.txt', 'w')
f.write(str(a)) # Pour ecrire un entier converti en string
f.write(str(b))
f.write(str(c))
f.close()
#tous les nombres sont sur une meme ligne en mode caracteres

f = open('test.txt', 'r')
print(f.read()) #lire tout le document
f.close()

import pickle # Pour importer un module permettant conserver le type des variables
f = open('Monfichier', 'wb') # ouverture d’un fichier binaire
pickle.dump(a, f) # Pour enregistrer dans le fichier
pickle.dump(b, f) # equivalent a write mais en conservant le type de b
pickle.dump(c, f)
f.close()

f = open('Monfichier', 'rb')
print(f.read())
f.close()

f = open('Monfichier', 'rb')
t = pickle.load(f) # Operation inverse de dump
print(t, type(t))
t = pickle.load(f) # Equivalent a read mais en conservant le type de b
print(t, type(t))
t = pickle.load(f)
print(t, type(t))
f.close()