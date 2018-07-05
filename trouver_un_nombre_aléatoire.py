from random import randint
#Afficher l'interface :
# print("-----------------\n" +
# "| Devinez un nombre |\n" +
# "-----------------\n" +
# "Level choice:\n" +
# "1 - Entre 0 et 100\n" +
# "2 - Entre 0 et 1000\n" +
# "3 - Entre 0 et 10000\n" +
# "4 - Entre 0 et 100000")

#Laisser le choix de la difficulté à l'utilisateur :
# level = input("Choose your level? : ")
# while (level != "1" and level != "2" and level != "3" and level != "4") : 
#     print("Veuillez entrer quelque chose de correct !") 
#     level = input()

#Initialiser les variables :
nb_coup = 0
#Générer un nombre aléatoire :
# if level == "1" : 
nb_ordi = randint(0, 100)
# elif level == "2" :
#     nb_ordi = randint(0, 1000) 
# elif level == "3" : 
#     nb_ordi = randint(0, 10000)
# else :
#     nb_ordi = randint(0, 100000)
    
print("Mon choix :  =", nb_ordi) #afficher la valeur donnér par l'ordinateur   

#Indiquer que le jeu à commencé :
print("Le jeu commence !")

# Boucle principale :
while True : 
    nb_user = input("Votre nombre ? : ") # 1 ; &
    while isinstance (nb_user, int) == False :
        try : 
            nb_user = int(nb_user)
        except : 
            print("Il semble que vous n'avez pas saisi un nombre entier")
            nb_user = input("Votre nombre ? : ")

    nb_coup += 1

    if (nb_user != nb_ordi) : 
        if (nb_user > nb_ordi) :
            print('Votre nb est trop grand !')
        elif (nb_user < nb_ordi) :   
            print('Votre nb est trop petit !')
    else : 
        print ('Bingo !')
        print('Vous avez gagné en {} coup(s) !'.format(nb_coup))
        break
