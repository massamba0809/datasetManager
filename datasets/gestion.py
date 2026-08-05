# ----- Partie 4 : Tuple des domaines autorises -----
DOMAINES_AUTORISES = ("Sante", "Finance", "Agriculture", "Transport", "Education")

# ----- Partie 5 : Liste des datasets -----
datasets = []


def ajouter_dataset():
    """Ajoute un nouveau dataset a la liste"""
    print("\n--- Ajout d'un dataset ---")
    nom = input("Nom du dataset : ")
    domaine = input("Domaine : ")
    while domaine not in DOMAINES_AUTORISES:
        print(f"Domaine invalide. Domaines autorises : {DOMAINES_AUTORISES}")
        domaine = input("Domaine : ")

    try:
        lignes = int(input("Nombre de lignes : "))
        colonnes = int(input("Nombre de colonnes : "))
        taille = float(input("Taille en Mo : "))
    except ValueError:
        print("\nErreur : veuillez saisir uniquement des nombres pour les lignes, colonnes et la taille.")
        return

    format_fichier = input("Format (csv ou json) : ")
    public_str = input("Public (true ou false) : ")
    public = public_str.strip().lower() == "true"

    dataset = {
        "nom": nom,
        "domaine": domaine,
        "lignes": lignes,
        "colonnes": colonnes,
        "taille": taille,
        "format": format_fichier.upper(),
        "public": public
    }

    datasets.append(dataset)
    print(f"\nDataset '{nom}' ajoute avec succes.")


def rechercher_dataset():
    """Recherche un dataset par son nom"""
    nom_recherche = input("\nNom du dataset a rechercher : ")
    try:
        resultat = next(d for d in datasets if d["nom"].lower() == nom_recherche.lower())
        print(f"\nDataset trouve :")
        for key, value in resultat.items():
            print(f"  {key}: {value}")
    except StopIteration:
        print(f"\nAucun dataset nomme '{nom_recherche}' trouve.")


def trier_dataset():
    """Trie les datasets par nom"""
    if not datasets:
        print("\nAucun dataset a trier.")
    else:
        datasets.sort(key=lambda d: d["nom"])
        print("\nDatasets tries par nom avec succes.")


def modifier_dataset():
    """Modifie un dataset existant"""
    nom_modif = input("\nNom du dataset a modifier : ")
    trouve = False
    for d in datasets:
        if d["nom"].lower() == nom_modif.lower():
            print(f"Dataset actuel :")
            for key, value in d.items():
                print(f"  {key}: {value}")

            nouveau_nom = input(f"\nNouveau nom (laisser vide pour garder '{d['nom']}') : ")
            if nouveau_nom.strip() != "":
                d["nom"] = nouveau_nom

            nouveau_domaine = input(f"Nouveau domaine (laisser vide pour garder '{d['domaine']}') : ")
            if nouveau_domaine.strip() != "":
                if nouveau_domaine in DOMAINES_AUTORISES:
                    d["domaine"] = nouveau_domaine
                else:
                    print(f"Domaine invalide. Domaines autorises : {DOMAINES_AUTORISES}")

            try:
                nouvelles_lignes = input(f"Nouveau nombre de lignes (laisser vide pour garder {d['lignes']}) : ")
                if nouvelles_lignes.strip() != "":
                    d["lignes"] = int(nouvelles_lignes)

                nouvelles_colonnes = input(f"Nouveau nombre de colonnes (laisser vide pour garder {d['colonnes']}) : ")
                if nouvelles_colonnes.strip() != "":
                    d["colonnes"] = int(nouvelles_colonnes)

                nouvelle_taille = input(f"Nouvelle taille (laisser vide pour garder {d['taille']}) : ")
                if nouvelle_taille.strip() != "":
                    d["taille"] = float(nouvelle_taille)
            except ValueError:
                print("Erreur : saisie numerique invalide. Les modifications numeriques sont annulees.")

            print("\nDataset modifie avec succes.")
            trouve = True
            break

    if not trouve:
        print(f"\nAucun dataset nomme '{nom_modif}' trouve.")


def supprimer_dataset():
    """Supprime un dataset"""
    nom_suppr = input("\nNom du dataset a supprimer : ")

    confirmation = input(f"Confirmer la suppression de '{nom_suppr}' ? (o/N) : ")
    if confirmation.lower() != 'o':
        print("Suppression annulee.")
        return

    trouve = False
    for d in datasets:
        if d["nom"].lower() == nom_suppr.lower():
            datasets.remove(d)
            print(f"Dataset '{nom_suppr}' supprime avec succes.")
            trouve = True
            break

    if not trouve:
        print(f"\nAucun dataset nomme '{nom_suppr}' trouve.")
