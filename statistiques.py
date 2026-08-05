from gestion import datasets, DOMAINES_AUTORISES


def statistiques():
    """Calcule et affiche les statistiques (Partie 6)"""
    if not datasets:
        print("\nAucun dataset enregistre pour calculer des statistiques.")
        return

    nb_datasets = len(datasets)
    total_lignes = sum(d["lignes"] for d in datasets)
    moyenne_colonnes = sum(d["colonnes"] for d in datasets) / nb_datasets
    nb_publics = sum(1 for d in datasets if d["public"])
    nb_prives = nb_datasets - nb_publics
    nb_csv = sum(1 for d in datasets if d["format"] == "CSV")
    nb_json = sum(1 for d in datasets if d["format"] == "JSON")

    repartition_domaines = {
        dom: sum(1 for d in datasets if d["domaine"] == dom)
        for dom in DOMAINES_AUTORISES
        if any(d["domaine"] == dom for d in datasets)
    }

    print("\n--- Statistiques ---")
    print(f"Nombre de datasets        : {nb_datasets}")
    print(f"Nombre total de lignes    : {total_lignes:,}")
    print(f"Nombre moyen de colonnes  : {moyenne_colonnes:.0f}")
    print(f"Datasets publics          : {nb_publics}")
    print(f"Datasets prives           : {nb_prives}")
    print(f"Format CSV                : {nb_csv}")
    print(f"Format JSON               : {nb_json}")
    print("Repartition par domaine :")
    for dom, count in repartition_domaines.items():
        print(f"  {dom} : {count}")