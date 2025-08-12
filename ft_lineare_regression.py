# ========================
# 1. Données d'entraînement
# ========================
mileage = [10, 20, 30]  # kilométrage en milliers
price = [25, 20, 15]    # prix en milliers d'euros
m = len(mileage)

# Normalisation (optionnelle mais recommandée)
max_mileage = max(mileage)
max_price = max(price)
mileage = [x / max_mileage for x in mileage]
price = [y / max_price for y in price]

# ========================
# 2. Paramètres initiaux
# ========================
theta0 = 0.0
theta1 = 0.0
learning_rate = 0.01  # peut être réduit à 0.001 si besoin
iterations = 1000

# ========================
# 3. Descente de gradient
# ========================
for _ in range(iterations):
    sum_error0 = 0.0
    sum_error1 = 0.0
    
    for i in range(m):
        prediction = theta0 + theta1 * mileage[i]
        error = prediction - price[i]
        sum_error0 += error
        sum_error1 += error * mileage[i]
    
    theta0 -= (learning_rate * (1/m) * sum_error0)
    theta1 -= (learning_rate * (1/m) * sum_error1)

# ========================
# 4. Affichage résultats
# ========================
print(f"theta0 = {theta0:.4f}, theta1 = {theta1:.4f}")

# ========================
# 5. Utilisation du modèle
# ========================
km = 15 / max_mileage  # on normalise aussi l'entrée
predicted_price = theta0 + theta1 * km
predicted_price *= max_price  # on remet à l'échelle d'origine
print(f"Prix estimé pour 15000 km : {predicted_price:.2f} milliers d'euros")
