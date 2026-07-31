
nom = input("Nom du dataset : ")
domaine = input("Domaine : ")
lignes = int(input("Nombre de lignes : "))
colonnes = int(input("Nombre de colonnes : "))
taille = float(input("Taille en Mo : "))
format_fichier = input("Format (csv ou json) : ")
public_str = input("Public (true ou false) : ")

public = public_str.strip().lower() == "true"

print("\n========== RÉSUMÉ DU DATASET ==========")
print(f"Nom       : {nom}")
print(f"Domaine   : {domaine}")
print(f"Lignes    : {lignes}")
print(f"Colonnes  : {colonnes}")
print(f"Taille    : {taille} Mo")
print(f"Format    : {format_fichier.upper()}")
print(f"Public    : {'Oui' if public else 'Non'}")
print("========================================")


# ----- Partie 2 : Structures de contrôle (menu interactif) -----

while True:
    print("\n========================")
    print("1. Ajouter un dataset")
    print("2. Afficher les datasets")
    print("3. Rechercher")
    print("4. Quitter")
    print("========================")

    choix = input("Votre choix : ")

    if choix == "1":
        print("→ Ajout d'un dataset ")
    elif choix == "2":
        print("→ Affichage des datasets ")
    elif choix == "3":
        print("→ Recherche d'un dataset ")
    elif choix == "4":
        print("Fermeture de l'application. À bientôt !")
        break
    else:
        print("Choix invalide, veuillez réessayer.")


# ----- Partie 3 : Dictionnaires -----

dataset = {
    "nom": nom,
    "domaine": domaine,
    "lignes": lignes,
    "colonnes": colonnes,
    "taille": taille,
    "format": format_fichier.upper(),
    "public": public
}

print("\n--- Dictionnaire du dataset ---")
print(dataset)

print(f"\nAccès direct : le dataset '{dataset['nom']}' contient {dataset['lignes']} lignes.")