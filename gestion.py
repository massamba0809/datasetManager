import csv

# ----- Partie 4 : Tuple des domaines autorisés -----
DOMAINES_AUTORISES = ("Santé", "Finance", "Agriculture", "Transport", "Education")

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


def afficher_datasets():
    """Affiche tous les datasets enregistres"""
    if not datasets:
        print("\nAucun dataset enregistre.")
    else:
        print(f"\n--- {len(datasets)} dataset(s) enregistre(s) ---")
        for i, d in enumerate(datasets, start=1):
            print(f"\n[{i}] {d['nom']}")
            print(f"    Domaine   : {d['domaine']}")
            print(f"    Lignes    : {d['lignes']}")
            print(f"    Colonnes  : {d['colonnes']}")
            print(f"    Taille    : {d['taille']} Mo")
            print(f"    Format    : {d['format']}")
            print(f"    Public    : {'Oui' if d['public'] else 'Non'}")


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
    trouve = False

    confirmation = input(f"Confirmer la suppression de '{nom_suppr}' ? (o/N) : ")
    if confirmation.lower() != 'o':
        print("Suppression annulee.")
        return

    for d in datasets:
        if d["nom"].lower() == nom_suppr.lower():
            datasets.remove(d)
            print(f"Dataset '{nom_suppr}' supprime avec succes.")
            trouve = True
            break

    if not trouve:
        print(f"\nAucun dataset nomme '{nom_suppr}' trouve.")


def sauvegarder():
    """Sauvegarde les datasets dans un fichier CSV (Partie 7)"""
    if not datasets:
        print("\nAucun dataset a sauvegarder.")
        return

    with open("data/datasets.csv", "w", newline="", encoding="utf-8") as fichier:
        colonnes_csv = ["nom", "domaine", "lignes", "colonnes", "taille", "format", "public"]
        writer = csv.DictWriter(fichier, fieldnames=colonnes_csv)
        writer.writeheader()
        for d in datasets:
            writer.writerow(d)

    print(f"\n{len(datasets)} dataset(s) sauvegarde(s) dans data/datasets.csv")


def recharger():
    """Recharge les datasets depuis un fichier CSV (Partie 7 et 8)"""
    global datasets

    try:
        with open("data/datasets.csv", "r", encoding="utf-8") as fichier:
            reader = csv.DictReader(fichier)
            datasets_charges = []
            for ligne in reader:
                try:
                    ligne["lignes"] = int(ligne["lignes"])
                    ligne["colonnes"] = int(ligne["colonnes"])
                    ligne["taille"] = float(ligne["taille"])
                    ligne["public"] = ligne["public"] == "True"
                    datasets_charges.append(ligne)
                except (ValueError, KeyError) as e:
                    print(f"Erreur de conversion pour une ligne : {e}")
                    continue

        if not datasets_charges:
            print("\nLe fichier data/datasets.csv est vide.")
        else:
            datasets = datasets_charges
            print(f"\n{len(datasets)} dataset(s) recharge(s) depuis data/datasets.csv")
            for i, d in enumerate(datasets, start=1):
                print(f"[{i}] {d['nom']} - {d['domaine']}")

    except FileNotFoundError:
        print("\nErreur : le fichier data/datasets.csv n'existe pas. Faites d'abord une sauvegarde (option 8).")
    except Exception as e:
        print(f"\nErreur inattendue lors du rechargement : {e}")