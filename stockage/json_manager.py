import json
from datasets.gestion import datasets


def sauvegarder_json():
    """Sauvegarde les datasets dans un fichier JSON (bonus)"""
    if not datasets:
        print("\nAucun dataset a sauvegarder.")
        return

    with open("data/datasets.json", "w", encoding="utf-8") as fichier:
        json.dump(datasets, fichier, indent=4, ensure_ascii=False)

    print(f"\n{len(datasets)} dataset(s) sauvegarde(s) dans data/datasets.json")


def recharger_json():
    """Recharge les datasets depuis un fichier JSON (bonus)"""
    try:
        with open("data/datasets.json", "r", encoding="utf-8") as fichier:
            datasets_charges = json.load(fichier)

        if not datasets_charges:
            print("\nLe fichier data/datasets.json est vide.")
        else:
            datasets.clear()
            datasets.extend(datasets_charges)
            print(f"\n{len(datasets)} dataset(s) recharge(s) depuis data/datasets.json")

    except FileNotFoundError:
        print("\nErreur : le fichier data/datasets.json n'existe pas.")
    except json.JSONDecodeError:
        print("\nErreur : le fichier data/datasets.json est corrompu ou mal forme.")
