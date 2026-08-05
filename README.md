# datasetManager

Application console Python permettant de gérer un catalogue de jeux de données (datasets) : ajout, recherche, tri, modification, suppression, statistiques, sauvegarde et rechargement.

## Contexte

Ce projet a été développé dans le cadre d'une formation Python, pour une entreprise fictive spécialisée en Intelligence Artificielle. Les Data Scientists de cette entreprise manipulent quotidiennement des centaines de datasets (CSV et JSON) ; l'application permet de cataloguer et gérer leurs caractéristiques avant tout traitement avec Pandas.

## Fonctionnalités

- Ajouter un dataset (nom, domaine, nombre de lignes, nombre de colonnes, taille, format, visibilité)
- Afficher la liste des datasets enregistrés
- Rechercher un dataset par son nom
- Trier les datasets par nom
- Modifier un dataset existant
- Supprimer un dataset (avec confirmation)
- Afficher des statistiques globales (nombre total, répartition par domaine, par format, etc.)
- Sauvegarder les datasets dans un fichier CSV
- Recharger les datasets depuis le fichier CSV
- Gestion des erreurs de saisie et de fichier (le programme ne plante jamais)

## Structure du projet

```
datasetManager/
├── main.py                  # Point d'entree de l'application
├── datasets/
│   ├── __init__.py
│   ├── gestion.py           # Logique metier : ajout, recherche, tri, modification, suppression
│   └── statistiques.py      # Calcul des statistiques
├── interface/
│   ├── __init__.py
│   ├── menu.py               # Affichage du menu
│   └── affichage.py         # Affichage de la liste des datasets
├── stockage/
│   ├── __init__.py
│   ├── csv_manager.py       # Sauvegarde / rechargement CSV
│   └── json_manager.py      # Sauvegarde / rechargement JSON (bonus)
├── data/
│   ├── datasets.csv         # Genere automatiquement lors d'une sauvegarde
│   └── datasets.json        # Genere automatiquement (bonus)
└── README.md
```

## Prérequis

- Python 3.10 ou supérieur
- Aucune dépendance externe (uniquement la bibliothèque standard : `csv`, `json`)

## Installation

```bash
git clone https://github.com/massamba0809/datasetManager.git
cd datasetManager
```

## Utilisation

Lancer l'application depuis la racine du projet :

```bash
python main.py
```

Un menu interactif s'affiche :

```
========================
1. Ajouter un dataset
2. Afficher les datasets
3. Rechercher un dataset
4. Trier les datasets
5. Modifier un dataset
6. Supprimer un dataset
7. Statistiques
8. Sauvegarder dans un fichier CSV
9. Recharger depuis le fichier CSV
10. Quitter
========================
```

Saisis le numéro de l'action souhaitée et suis les instructions à l'écran.

### Exemple d'ajout de dataset

```
Nom du dataset : Titanic
Domaine : Transport
Nombre de lignes : 891
Nombre de colonnes : 12
Taille en Mo : 48
Format (csv ou json) : csv
Public (true ou false) : true
```

### Domaines autorisés

Le domaine saisi doit obligatoirement appartenir à la liste suivante :

`Santé`, `Finance`, `Agriculture`, `Transport`, `Education`

## Gestion des erreurs

L'application gère les cas d'erreur suivants sans jamais s'arrêter brutalement :

- Saisie d'un texte à la place d'un nombre (lignes, colonnes, taille)
- Fichier `data/datasets.csv` absent lors d'un rechargement
- Fichier `data/datasets.csv` vide
- Dataset recherché, modifié ou supprimé introuvable

## Auteur

Massamba

## Licence

Projet réalisé dans un cadre pédagogique.