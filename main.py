from menu import afficher_menu
from gestion import (
    ajouter_dataset,
    afficher_datasets,
    rechercher_dataset,
    trier_dataset,
    modifier_dataset,
    supprimer_dataset,
    sauvegarder,
    recharger
)
from statistiques import statistiques


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


if __name__ == "__main__":
    main()