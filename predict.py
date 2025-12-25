import sys

try:
    with open("thetas.txt", "r") as f:
        theta0 = float(f.readline().strip())
        theta1 = float(f.readline().strip())
except FileNotFoundError:
    print("Erreur : le fichier 'thetas.txt' est introuvable. Lance d'abord train.py.")
    sys.exit()
except ValueError:
    print("Erreur : contenu du fichier 'thetas.txt' invalide.")
    sys.exit()

def estimate_price(x):
    return theta0 + theta1 * x

try:
    x = float(input("Entrez le kilométrage : "))
except ValueError:
    print("Erreur : veuillez entrer un nombre.")
    sys.exit()

price_estimate = estimate_price(x)
print(f"Prix estimé : {price_estimate:.2f}")