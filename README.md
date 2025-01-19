# TimeBased_Attack

## Contexte:

Plusieurs variables peuvent être modifées afin d'accélérer l'attaque ou bien de la rendre plus précises

Elles se trouvent au meme endroit que le mot de passe à retrouver
Ces paramettres se situent en haut des fichiers check_string_methods.py et time_based_attack.py

check_string_methods.py:

    SECRET = "aligotSo6"

time_based_attack.py 

    nombre_essai = 500
    nombre_echantillon = 500

## Fonctionnement:

Pour executer l'attaque il faut lancer le fichier time_based_attack.py

    python .\time_based_attack.py

Si des messages d'erreurs apparaissent et sont en lien avec les imports il faut installer les dépendances

    pip install -r requirements.txt

## Contenu

Le projet permet de démontrer une attaque basée sur le temps

Pour empecher ce genre d'attaque une solution possible est de hasher les valeurs saisies dans la fonction
(Il existe plein de possibilité pour contrer cette attaque comme utiliser des fonctions de comparaison en temps constant)

Pour tester cette fonction il faut modifier la derniere ligne du script time_based_attack.py

    print(perform_attack()) -> print(perform_attack(True))