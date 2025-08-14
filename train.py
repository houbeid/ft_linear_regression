import csv

#initialisation

theta0 = 0
theta1 = 0
alpha = 0.01
max_iteration = 10000
epsilon = 1e-6

x = []
y = []

try:
    with open("data.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)  # ignorer l'en-tête
        for row in reader:
            x.append(float(row[0]))
            y.append(float(row[1]))
except FileNotFoundError:
    print("Erreur : fichier 'data.csv' introuvable.")
    exit()

m = len(x)
if m == 0:
    print("dataset vide")
    exit


#normalisation
x_max = max(x)
y_max = max(y)

x = [val / x_max for val in x]
y = [val / y_max for val in y]

def estimatePrice(val_x) :
    return theta0 + theta1 * val_x

def comput_cost():
    total_error = 0
    for i in range(m):
        total_error += (estimatePrice(x[i]) - y[i]) ** 2
    return (total_error / m)
# descente du gradient
ex_cost = comput_cost()
for iteration in range(max_iteration):
    temp_theta0 = 0
    temp_theta1 = 0
    for i in range(m):
        temp_theta0 += (estimatePrice(x[i]) - y[i])
        temp_theta1 += (estimatePrice(x[i]) - y[i]) * x[i]
    temp_theta0 = theta0 - alpha * temp_theta0 / m
    temp_theta1 = theta1 - alpha * (temp_theta1) / m
    theta0 , theta1 = temp_theta0, temp_theta1
    cost = comput_cost()
    if abs(cost - ex_cost) < epsilon :
        print(f" Convergence atteinte à l'itération {iteration+1}")
        break;
    ex_cost = cost
#denormalisation
theta1 = theta1 * (y_max / x_max)
theta0 = theta0 * y_max

# ---------- Sauvegarde ----------
with open("thetas.txt", "w") as f:
    f.write(f"{theta0}\n{theta1}")

print(f" Training terminé : theta0 = {theta0:.4f}, theta1 = {theta1:.4f}")