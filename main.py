from interface.menu import afficher_menu
from interface.affichage import afficher_datasets
from datasets.gestion import (
    datasets,
    ajouter_dataset,
    rechercher_dataset,
    trier_dataset,
    modifier_dataset,
    supprimer_dataset
)
from datasets.statistiques import statistiques
from stockage.csv_manager import sauvegarder, recharger


def main():
    print("\n" + "=" * 50)
    print("APPLICATION DE GESTION DE DATASETS")
    print("=" * 50)
    print("Bienvenue dans l'application de gestion de datasets.")
    print("=" * 50)

    while True:
        afficher_menu()
        choix = input("Votre choix : ")

        if choix == "1":
            ajouter_dataset()
        elif choix == "2":
            afficher_datasets(datasets)
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


if __name__ == "__main__":
    main()
