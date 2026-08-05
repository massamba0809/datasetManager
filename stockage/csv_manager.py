import csv
from datasets.gestion import datasets


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
            # On modifie la liste en place (clear + extend) pour que la
            # reference partagee avec les autres modules reste valide.
            datasets.clear()
            datasets.extend(datasets_charges)
            print(f"\n{len(datasets)} dataset(s) recharge(s) depuis data/datasets.csv")
            for i, d in enumerate(datasets, start=1):
                print(f"[{i}] {d['nom']} - {d['domaine']}")

    except FileNotFoundError:
        print("\nErreur : le fichier data/datasets.csv n'existe pas. Faites d'abord une sauvegarde (option 8).")
    except Exception as e:
        print(f"\nErreur inattendue lors du rechargement : {e}")
