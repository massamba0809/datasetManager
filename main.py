import csv

# ----- Partie 4 : Tuples -----

domaines_autorises = ("Santé", "Finance", "Agriculture", "Transport", "Education")

# ----- Partie 5 : Listes -----

datasets = []

# ----- Partie 2 : Structures de contrôle (menu interactif) -----

while True:
    print("\n========================")
    print("1. Ajouter un dataset")
    print("2. Afficher les datasets")
    print("3. Rechercher")
    print("4. Trier les datasets")
    print("5. Modifier un dataset")
    print("6. Supprimer un dataset")
    print("7. Statistiques")
    print("8. Sauvegarder dans un fichier CSV")
    print("9. Recharger depuis le fichier CSV")
    print("10. Quitter")
    print("========================")

    choix = input("Votre choix : ")

    if choix == "1":
        # ----- Partie 1 : Saisie -----
        nom = input("Nom du dataset : ")

        domaine = input("Domaine : ")
        while domaine not in domaines_autorises:
            print(f"Domaine invalide. Domaines autorisés : {domaines_autorises}")
            domaine = input("Domaine : ")

        # ----- Partie 8 : Gestion des exceptions (saisie numérique) -----
        try:
            lignes = int(input("Nombre de lignes : "))
            colonnes = int(input("Nombre de colonnes : "))
            taille = float(input("Taille en Mo : "))
        except ValueError:
            print("\nErreur : veuillez saisir uniquement des nombres pour les lignes, colonnes et la taille.")
            continue

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
        print(f"\nDataset '{nom}' ajouté avec succès.")

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
        # ----- Partie 8 : Recherche avec gestion d'exception -----
        nom_recherche = input("Nom du dataset à rechercher : ")
        try:
            resultat = next(d for d in datasets if d["nom"].lower() == nom_recherche.lower())
            print(f"\nDataset trouvé : {resultat}")
        except StopIteration:
            print(f"\nAucun dataset nommé '{nom_recherche}' trouvé.")

    elif choix == "4":
        # ----- Tri -----
        if not datasets:
            print("\nAucun dataset à trier.")
        else:
            datasets.sort(key=lambda d: d["nom"])
            print("\nDatasets triés par nom.")

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
                print("Dataset modifié avec succès.")
                trouve = True
                break
        if not trouve:
            print(f"\nAucun dataset nommé '{nom_modif}' trouvé.")

    elif choix == "6":
        # ----- Suppression -----
        nom_suppr = input("Nom du dataset à supprimer : ")
        trouve = False
        for d in datasets:
            if d["nom"].lower() == nom_suppr.lower():
                datasets.remove(d)
                print(f"Dataset '{nom_suppr}' supprimé.")
                trouve = True
                break
        if not trouve:
            print(f"\nAucun dataset nommé '{nom_suppr}' trouvé.")

    elif choix == "7":
        # ----- Partie 6 : Statistiques (compréhensions) -----
        if not datasets:
            print("\nAucun dataset enregistré pour calculer des statistiques.")
        else:
            nb_datasets = len(datasets)
            total_lignes = sum(d["lignes"] for d in datasets)
            moyenne_colonnes = sum(d["colonnes"] for d in datasets) / nb_datasets
            nb_publics = sum(1 for d in datasets if d["public"])
            nb_prives = nb_datasets - nb_publics
            nb_csv = sum(1 for d in datasets if d["format"] == "CSV")
            nb_json = sum(1 for d in datasets if d["format"] == "JSON")

            # Répartition par domaine (dictionnaire en compréhension)
            repartition_domaines = {
                dom: sum(1 for d in datasets if d["domaine"] == dom)
                for dom in domaines_autorises
                if any(d["domaine"] == dom for d in datasets)
            }

            print("\n--- Statistiques ---")
            print(f"Nombre de datasets       : {nb_datasets}")
            print(f"Nombre total de lignes    : {total_lignes}")
            print(f"Nombre moyen de colonnes  : {moyenne_colonnes:.0f}")
            print(f"Datasets publics          : {nb_publics}")
            print(f"Datasets privés           : {nb_prives}")
            print(f"Format CSV                : {nb_csv}")
            print(f"Format JSON               : {nb_json}")
            print("Répartition par domaine :")
            for dom, count in repartition_domaines.items():
                print(f"  {dom} : {count}")

    elif choix == "8":
        # ----- Partie 7 : Sauvegarde dans un fichier CSV -----
        if not datasets:
            print("\nAucun dataset à sauvegarder.")
        else:
            with open("datasets.csv", "w", newline="", encoding="utf-8") as fichier:
                colonnes_csv = ["nom", "domaine", "lignes", "colonnes", "taille", "format", "public"]
                writer = csv.DictWriter(fichier, fieldnames=colonnes_csv)
                writer.writeheader()
                for d in datasets:
                    writer.writerow(d)
            print(f"\n{len(datasets)} dataset(s) sauvegardé(s) dans datasets.csv")

    elif choix == "9":
        # ----- Partie 7 et 8 : Rechargement depuis le fichier CSV avec gestion des exceptions -----
        try:
            with open("datasets.csv", "r", encoding="utf-8") as fichier:
                reader = csv.DictReader(fichier)
                datasets_charges = []
                for ligne in reader:
                    ligne["lignes"] = int(ligne["lignes"])
                    ligne["colonnes"] = int(ligne["colonnes"])
                    ligne["taille"] = float(ligne["taille"])
                    ligne["public"] = ligne["public"] == "True"
                    datasets_charges.append(ligne)

            if not datasets_charges:
                print("\nLe fichier datasets.csv est vide.")
            else:
                datasets = datasets_charges
                print(f"\n{len(datasets)} dataset(s) rechargé(s) depuis datasets.csv")
                for i, d in enumerate(datasets, start=1):
                    print(f"[{i}] {d}")

        except FileNotFoundError:
            print("\nErreur : le fichier datasets.csv n'existe pas. Faites d'abord une sauvegarde (option 8).")

    elif choix == "10":
        print("Fermeture de l'application. À bientôt !")
        break

    else:
        print("Choix invalide, veuillez réessayer.")