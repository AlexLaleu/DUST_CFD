import matplotlib.pyplot as plt
import numpy as np
import os

filename1 = r'C:/Users/laleu/OneDrive/Documents/2A/DUST-CFD/Casalino/Hover_LL_3_donnees_Boqiao/Hover_LL_3_tableau3/resultats_8000RPM/TUD_blade1_Fz.dat'
filename2 = r'C:/Users/laleu/OneDrive/Documents/2A/DUST-CFD/Casalino/Hover_LL_3_donnees_Boqiao/Hover_LL_3_tableau3/resultats_8000RPM/TUD_blade2_Fz.dat'
filename3 = r'C:/Users/laleu/OneDrive/Documents/2A/DUST-CFD/Casalino/Hover_LL_3_donnees_Boqiao/Hover_LL_3_tableau3/resultats_8000RPM/TUD_blade3_Fz.dat'
dt = 0.0002
nb_iterations = 150

def process_dat_file(filename):
    results = []
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Lire la deuxième ligne (y_span)
    line = lines[3]
    list_span = line.split()
    n_sec = len(list_span)
    span = [float(value) for value in list_span]
    if len(span) != n_sec:
         raise ValueError("La ligne contenant les valeurs L ne contient pas exactement 56 éléments.")

    # Lire les lignes contenant les données temporelles (portance ou moments par section)
    data_lines = lines[5:nb_iterations+5]

    # Sommer la portance, pondérée par y_span sur chacune des sections
    for data_line in data_lines:
        load_i = list(map(float, data_line.split()))
        if len(load_i) < n_sec:
            raise ValueError(f"Une ligne de sectional load contient moins de 91 valeurs : {data_line}")
        result = sum(load_i[j] * span[j] for j in range(n_sec))
        results.append(result)

    return results

def create_time_list(dt, num_points):
    return

results_blade1 = process_dat_file(filename1)
results_blade2 = process_dat_file(filename2)
results_blade3 = process_dat_file(filename3)
#on somme la portance des deux hélices
results = []
for i in range(len(results_blade1)):
    results.append(results_blade1[i]+results_blade2[i]+results_blade3[i])

temps = [i * dt for i in range(len(results))]

#on trace
fig, axs = plt.subplots(2, 1, figsize=(10, 12))


axs[0].plot(temps, results_blade1, marker='o', linestyle='-', color='r', label='Portance hélice 1')
axs[0].plot(temps, results_blade2, marker='o', linestyle='-', color='b', label='Portance hélice 2')
axs[0].plot(temps, results_blade3, marker='o', linestyle='-', color='g', label='Portance hélice 3')
axs[0].set_title("Portance des hélices 1, 2 et 3 en fonction du temps (8000RPM)", fontsize=14)
axs[0].set_xlabel("Temps (s)", fontsize=12)
axs[0].set_ylabel("Fz (N)", fontsize=12)
axs[0].legend()
axs[0].grid(True)


axs[1].plot(temps, results, marker='o', linestyle='-', color='g', label='Portance totale')
axs[1].set_xlabel("Temps (s)", fontsize=12)
axs[1].set_ylabel("Fz (N)", fontsize=12)
axs[1].legend()
axs[1].grid(True)

plt.show()