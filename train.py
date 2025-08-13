import csv

# ---------- Paramètres ----------
learning_rate = 0.01
max_iterations = 10000
epsilon = 1e-6  # seuil pour arrêter si l'erreur change peu
theta0 = 0.0
theta1 = 0.0

# ---------- Lecture du dataset ----------
mileage = []
price = []

try:
    with open("data.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)  # ignorer l'en-tête
        for row in reader:
            mileage.append(float(row[0]))
            price.append(float(row[1]))
except FileNotFoundError:
    print("Erreur : fichier 'data.csv' introuvable.")
    exit()

m = len(mileage)
if m == 0:
    print("Erreur : dataset vide.")
    exit()

# ---------- Normalisation ----------
max_mileage = max(mileage)
max_price = max(price)
mileage = [x / max_mileage for x in mileage]
price = [y / max_price for y in price]

# ---------- Fonction de prédiction ----------
def estimate_price(mil):
    return theta0 + theta1 * mil

# ---------- Fonction coût (MSE) ----------
def compute_cost():
    total_error = 0
    for i in range(m):
        total_error += (estimate_price(mileage[i]) - price[i]) ** 2
    return total_error / m

# ---------- Descente de gradient ----------
prev_cost = compute_cost()

for iteration in range(max_iterations):
    sum_error_theta0 = 0
    sum_error_theta1 = 0
    for i in range(m):
        error = estimate_price(mileage[i]) - price[i]
        sum_error_theta0 += error
        sum_error_theta1 += error * mileage[i]
    
    tmp_theta0 = theta0 - learning_rate * (sum_error_theta0 / m)
    tmp_theta1 = theta1 - learning_rate * (sum_error_theta1 / m)
    
    theta0, theta1 = tmp_theta0, tmp_theta1

    # Calcul du nouveau coût
    current_cost = compute_cost()
    cost_diff = abs(prev_cost - current_cost)

    print(f"Iteration {iteration+1}: cost = {current_cost:.8f}, diff = {cost_diff:.8f}")

    # Critère d'arrêt
    if cost_diff < epsilon:
        print(f" Convergence atteinte à l'itération {iteration+1}")
        break
    
    prev_cost = current_cost

# ---------- Dénormalisation ----------
theta1 = theta1 * (max_price / max_mileage)
theta0 = theta0 * max_price

# ---------- Sauvegarde ----------
with open("thetas.txt", "w") as f:
    f.write(f"{theta0}\n{theta1}")

print(f" Training terminé : theta0 = {theta0:.4f}, theta1 = {theta1:.4f}")
