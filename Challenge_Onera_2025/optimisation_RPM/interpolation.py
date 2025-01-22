import numpy as np
import matplotlib.pyplot as plt

# Hélice 3 pales
points_3pales = [(8000, 21.4), (5000, 6.72), (3000, 0.85)]
x_3pales, y_3pales = zip(*points_3pales)

coefficients_3pales = np.polyfit(x_3pales, y_3pales, 2)
polynomial_3pales = np.poly1d(coefficients_3pales)

x_range_3pales = np.linspace(min(x_3pales) - 1, max(x_3pales) + 1, 500)
y_range_3pales = polynomial_3pales(x_range_3pales)

# Hélice 2 pales
points_2pales = [(3000, 0.92), (5000, 3.447), (8000, 9.67)]
x_2pales, y_2pales = zip(*points_2pales)

coefficients_2pales = np.polyfit(x_2pales, y_2pales, 2)
polynomial_2pales = np.poly1d(coefficients_2pales)

x_range_2pales = np.linspace(min(x_2pales) - 1, max(x_2pales) + 1, 500)
y_range_2pales = polynomial_2pales(x_range_2pales)


portance_target = 4.5


rpm_3pales = np.roots(polynomial_3pales - portance_target)  # Résolution de P(x) = 4.5
rpm_2pales = np.roots(polynomial_2pales - portance_target)  # Résolution de P(x) = 4.5


rpm_3pales = [rpm for rpm in rpm_3pales if np.isreal(rpm) and min(x_3pales) <= rpm <= max(x_3pales)]
rpm_2pales = [rpm for rpm in rpm_2pales if np.isreal(rpm) and min(x_2pales) <= rpm <= max(x_2pales)]


print(f"RPM pour l'hélice 3 pales à une portance de 4.5 N : {np.real(rpm_3pales)}")
print(f"RPM pour l'hélice 2 pales à une portance de 4.5 N : {np.real(rpm_2pales)}")


plt.figure(figsize=(10, 6))

# Tracé de l'hélice 3 pales
plt.plot(x_range_3pales, y_range_3pales, label="Hélice 3 pales", color="blue")
plt.scatter(x_3pales, y_3pales, color="blue", label="Points 3 pales", zorder=5)

# Tracé de l'hélice 2 pales
plt.plot(x_range_2pales, y_range_2pales, label="Hélice 2 pales", color="green")
plt.scatter(x_2pales, y_2pales, color="green", label="Points 2 pales", zorder=5)

# Ajout des lignes pointillées pour chaque courbe
for rpm in rpm_3pales:
    plt.plot([rpm, rpm], [0, portance_target], linestyle="--", color="blue", alpha=0.7)
    plt.scatter(rpm, portance_target, color="blue", zorder=10)

for rpm in rpm_2pales:
    plt.plot([rpm, rpm], [0, portance_target], linestyle="--", color="green", alpha=0.7)
    plt.scatter(rpm, portance_target, color="green", zorder=10)

# Ligne horizontale pour portance = 4.5 N
plt.axhline(y=portance_target, xmin=0, xmax=1, linestyle="--", color="gray", alpha=0.8, label="Portance cible = 4.0 N")


plt.axhline(0, color="black", linewidth=0.5, linestyle="--")
plt.axvline(0, color="black", linewidth=0.5, linestyle="--")
plt.title("Comparaison des portances en fonction des RPM")
plt.xlabel("RPM")
plt.ylabel("Portance (N)")
plt.legend()
plt.grid(True)


plt.show()



