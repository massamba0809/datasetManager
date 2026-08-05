def afficher_datasets(datasets):
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
