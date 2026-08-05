import csv

# ----- Partie 4 : Tuples -----
DOMAINES_AUTORISES = ("Sante", "Finance", "Agriculture", "Transport", "Education")

# ----- Partie 5 : Listes -----
datasets = []


# PARTIE 9 : FONCTIONS

def afficher_menu():
    """Affiche le menu principal"""
    print("\n========================")
    print("1. Ajouter un dataset")
    print("2. Afficher les datasets")
    print("3. Rechercher un dataset")
    print("4. Trier les datasets")
    print("5. Modifier un dataset")
    print("6. Supprimer un dataset")
    print("7. Statistiques")
    print("8. Sauvegarder dans un fichier CSV")
    print("9. Recharger depuis le fichier CSV")
    print("10. Quitter")
    print("========================")


def ajouter_dataset():
    """Ajoute un nouveau dataset a la liste"""
    print("\n--- Ajout d'un dataset ---")

    # ----- Partie 1 : Saisie -----
    nom = input("Nom du dataset : ")

    # Validation du domaine (Partie 4)
    domaine = input("Domaine : ")
    while domaine not in DOMAINES_AUTORISES:
        print(f"Domaine invalide. Domaines autorises : {DOMAINES_AUTORISES}")
        domaine = input("Domaine : ")

    # ----- Partie 8 : Gestion des exceptions-----
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

    # Ajout a la liste
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
    # ----- Partie 8 : Recherche avec gestion d'exception -----
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

            # Modification du nom
            nouveau_nom = input(f"\nNouveau nom (laisser vide pour garder '{d['nom']}') : ")
            if nouveau_nom.strip() != "":
                d["nom"] = nouveau_nom

            # Modification des autres champs
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

            nouveau_format = input(f"Nouveau format (laisser vide pour garder '{d['format']}') : ")
            if nouveau_format.strip() != "":
                d["format"] = nouveau_format.upper()

            nouveau_public = input(f"Public (true/false, laisser vide pour garder {d['public']}) : ")
            if nouveau_public.strip() != "":
                d["public"] = nouveau_public.strip().lower() == "true"

            print("Dataset modifie avec succes.")
            trouve = True
            break

    if not trouve:
        print(f"\nAucun dataset nomme '{nom_modif}' trouve.")


def supprimer_dataset():
    """Supprime un dataset"""
    nom_suppr = input("\nNom du dataset a supprimer : ")
    trouve = False

    # Confirmation de suppression
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


def statistiques():
    """Calcule et affiche les statistiques (Partie 6)"""
    if not datasets:
        print("\nAucun dataset enregistre pour calculer des statistiques.")
        return

    # ----- Partie 6 : Statistiques (comprehensions) -----
    nb_datasets = len(datasets)
    total_lignes = sum(d["lignes"] for d in datasets)
    moyenne_colonnes = sum(d["colonnes"] for d in datasets) / nb_datasets
    nb_publics = sum(1 for d in datasets if d["public"])
    nb_prives = nb_datasets - nb_publics
    nb_csv = sum(1 for d in datasets if d["format"] == "CSV")
    nb_json = sum(1 for d in datasets if d["format"] == "JSON")

    # Repartition par domaine (dictionnaire en comprehension)
    repartition_domaines = {
        dom: sum(1 for d in datasets if d["domaine"] == dom)
        for dom in DOMAINES_AUTORISES
        if any(d["domaine"] == dom for d in datasets)
    }

    print("\n--- Statistiques ---")
    print(f"Nombre de datasets       : {nb_datasets}")
    print(f"Nombre total de lignes   : {total_lignes:,}")
    print(f"Nombre moyen de colonnes : {moyenne_colonnes:.0f}")
    print(f"Datasets publics         : {nb_publics}")
    print(f"Datasets prives          : {nb_prives}")
    print(f"Format CSV               : {nb_csv}")
    print(f"Format JSON              : {nb_json}")
    print("Repartition par domaine :")
    for dom, count in repartition_domaines.items():
        print(f"  {dom} : {count}")


def sauvegarder():
    """Sauvegarde les datasets dans un fichier CSV (Partie 7)"""
    if not datasets:
        print("\nAucun dataset a sauvegarder.")
        return

    # ----- Partie 7 : Sauvegarde dans un fichier CSV -----
    with open("datasets.csv", "w", newline="", encoding="utf-8") as fichier:
        colonnes_csv = ["nom", "domaine", "lignes", "colonnes", "taille", "format", "public"]
        writer = csv.DictWriter(fichier, fieldnames=colonnes_csv)
        writer.writeheader()
        for d in datasets:
            writer.writerow(d)
    print(f"\n{len(datasets)} dataset(s) sauvegarde(s) dans datasets.csv")


def recharger():
    """Recharge les datasets depuis un fichier CSV (Partie 7 et 8)"""
    global datasets

    # ----- Partie 7 et 8 : Rechargement avec gestion des exceptions -----
    try:
        with open("datasets.csv", "r", encoding="utf-8") as fichier:
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
            print("\nLe fichier datasets.csv est vide.")
        else:
            datasets = datasets_charges
            print(f"\n{len(datasets)} dataset(s) recharge(s) depuis datasets.csv")
            for i, d in enumerate(datasets, start=1):
                print(f"[{i}] {d['nom']} - {d['domaine']}")

    except FileNotFoundError:
        print("\nErreur : le fichier datasets.csv n'existe pas. Faites d'abord une sauvegarde (option 8).")
    except Exception as e:
        print(f"\nErreur inattendue lors du rechargement : {e}")


def main():
    """Point d'entree principal de l'application"""
    print("\n" + "=" * 50)
    print("APPLICATION DE GESTION DE DATASETS")
    print("=" * 50)
    print("Bienvenue dans l'application de gestion de datasets.")
    print("=" * 50)

    # ----- Partie 2 : Menu interactif -----
    while True:
        afficher_menu()
        choix = input("Votre choix : ")

        if choix == "1":
            ajouter_dataset()
        elif choix == "2":
            afficher_datasets()
        elif choix == "3":
            rechercher_dataset()
        elif choix == "4":
            trier_dataset()
        elif choix == "5":
            modifier_dataset()
        elif choix == "6":
            supprimer_dataset()
        elif choix == "7":
            statistiques()
        elif choix == "8":
            sauvegarder()
        elif choix == "9":
            recharger()
        elif choix == "10":
            print("\nFermeture de l'application. A bientot !")
            break
        else:
            print("\nChoix invalide, veuillez reessayer.")



# POINT D'ENTREE DE L'APPLICATION

if __name__ == "__main__":
    main()