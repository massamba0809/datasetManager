# main.py

# ----- Partie 4 : Tuples -----

domaines_autorises = ("Santé", "Finance", "Agriculture", "Transport", "Education")

# ----- Partie 5 : Listes -----

datasets = []

# ----- Partie 2 : Structures de contrôle

while True:
    print("\n========================")
    print("1. Ajouter un dataset")
    print("2. Afficher les datasets")
    print("3. Rechercher")
    print("4. Trier les datasets")
    print("5. Modifier un dataset")
    print("6. Supprimer un dataset")
    print("7. Quitter")
    print("========================")

    choix = input("Votre choix : ")

    if choix == "1":
        # ----- Partie 1 : Saisie -----
        nom = input("Nom du dataset : ")

        domaine = input("Domaine : ")
        while domaine not in domaines_autorises:
            print(f"Domaine invalide. Domaines autorisés : {domaines_autorises}")
            domaine = input("Domaine : ")

        lignes = int(input("Nombre de lignes : "))
        colonnes = int(input("Nombre de colonnes : "))
        taille = float(input("Taille en Mo : "))
        format_fichier = input("Format (csv ou json) : ")
        public_str = input("Public (true ou false) : ")
        public = public_str.strip().lower() == "true"

        # ----- Partie 3 : Dictionnaire -----
        dataset = {
            "nom": nom,
            "domaine": domaine,
            "lignes": lignes,
            "colonnes": colonnes,
            "taille": taille,
            "format": format_fichier.upper(),
            "public": public
        }

        # Ajout à la liste
        datasets.append(dataset)
        print(f"\n Dataset '{nom}' ajouté avec succès !")

    elif choix == "2":
        # ----- Affichage -----
        if not datasets:
            print("\nAucun dataset enregistré.")
        else:
            print(f"\n--- {len(datasets)} dataset(s) enregistré(s) ---")
            for i, d in enumerate(datasets, start=1):
                print(f"\n[{i}] {d['nom']}")
                print(f"    Domaine   : {d['domaine']}")
                print(f"    Lignes    : {d['lignes']}")
                print(f"    Colonnes  : {d['colonnes']}")
                print(f"    Taille    : {d['taille']} Mo")
                print(f"    Format    : {d['format']}")
                print(f"    Public    : {'Oui' if d['public'] else 'Non'}")

    elif choix == "3":
        # ----- Recherche -----
        nom_recherche = input("Nom du dataset à rechercher : ")
        trouve = False
        for d in datasets:
            if d["nom"].lower() == nom_recherche.lower():
                print(f"\n Dataset trouvé : {d}")
                trouve = True
                break
        if not trouve:
            print(f"\n Aucun dataset nommé '{nom_recherche}' trouvé.")

    elif choix == "4":
        # ----- Tri -----
        if not datasets:
            print("\nAucun dataset à trier.")
        else:
            datasets.sort(key=lambda d: d["nom"])
            print("\n Datasets triés par nom.")

    elif choix == "5":
        # ----- Modification -----
        nom_modif = input("Nom du dataset à modifier : ")
        trouve = False
        for d in datasets:
            if d["nom"].lower() == nom_modif.lower():
                print(f"Dataset actuel : {d}")
                nouveau_nom = input(f"Nouveau nom (laisser vide pour garder '{d['nom']}') : ")
                if nouveau_nom.strip() != "":
                    d["nom"] = nouveau_nom
                print(" Dataset modifié avec succès.")
                trouve = True
                break
        if not trouve:
            print(f"\n Aucun dataset nommé '{nom_modif}' trouvé.")

    elif choix == "6":
        # ----- Suppression -----
        nom_suppr = input("Nom du dataset à supprimer : ")
        trouve = False
        for d in datasets:
            if d["nom"].lower() == nom_suppr.lower():
                datasets.remove(d)
                print(f" Dataset '{nom_suppr}' supprimé.")
                trouve = True
                break
        if not trouve:
            print(f"\n Aucun dataset nommé '{nom_suppr}' trouvé.")

    elif choix == "7":
        print("Fermeture de l'application")
        break

    else:
        print("Choix invalide, veuillez réessayer.")