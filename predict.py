
# ---------- Chargement des paramètres ----------
try:
    with open("thetas.txt", "r") as f:
        theta0 = float(f.readline())
        theta1 = float(f.readline())
except FileNotFoundError:
    print("Erreur : le fichier 'thetas.txt' est introuvable. Lance d'abord train.py.")
    exit()

# ---------- Fonction de prédiction ----------
def estimate_price(x):
    return theta0 + theta1 * x

# ---------- Interaction utilisateur ----------
try:
    x = float(input("Entrez le kilométrage : "))
except ValueError:
    print("Erreur : veuillez entrer un nombre.")
    exit()

price_estimate = estimate_price(x)
print(f" Prix estimé : {price_estimate:.2f}")
