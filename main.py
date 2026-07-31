
nom = input("Nom du dataset : ")
domaine = input("Domaine : ")
lignes = int(input("Nombre de lignes : "))
colonnes = int(input("Nombre de colonnes : "))
taille = float(input("Taille en Mo : "))
format_fichier = input("Format (csv ou json) : ")
public_str = input("Public (true ou false) : ")

public = public_str.strip().lower() == "true"

print("\n========== RÉSUMÉ DU DATASET ==========")
print(f"Nom       : {nom}")
print(f"Domaine   : {domaine}")
print(f"Lignes    : {lignes}")
print(f"Colonnes  : {colonnes}")
print(f"Taille    : {taille} Mo")
print(f"Format    : {format_fichier.upper()}")
print(f"Public    : {'Oui' if public else 'Non'}")
print("========================================")