README - Simulations CFD avec DUST : Challenge ONERA 2025

Ce dossier constitue mon travail à proprement dit pour le Challenge Onera 2025. J'avais pour mission de comparer la relation portance/RPM pour deux rotors différents, un composé de deux pales, l'autre de trois.
Leur géométrie (codée dans ll_wing) avait été définie grâce à un code d'optimisation dont je ne me suis pas occupé.

Pour ce faire j'ai décidé de lancer trois simulations pour trois RPM différents et ensuite interpoler les points par un polynôme pour en déduire le RPM optimal nous permettant d'atteindre la portance visée dans le cadre du challenge (4,5N).

J'ai ici utilisé la méthode Lifting_Lines.
 
Contenu :
Hover_LL_3_tableau1 contient les simulations pour le rotor 2 pales.
Hover_LL_3_tableau3 contient les simulations pour le rotor 3 pales.
optimisation_RPM contient l'interpolation des points.

Traitement des données :
Les résultats sont traités à l'aide de scripts Python disponibles dans le dossier python pour chaque tableau. Ces scripts permettent de lire les fichiers .DAT générés par les simulations. Le temps en abscisse est la période définie par t_start et t_end dans "dust_post" (exemple : t_start = 300, t_end = 361, dt = 0.0002 donc l'intervalle traité par dust_post couvre 0.012s à partir de t_start).

Pour exécuter les simulations :
Ouvrir un terminal sous Ubuntu 22.05.4.
Naviguer jusqu'au répertoire contenant les codes.
Lancer successivement les commandes suivantes :
dust_pre
dust
dust_post
Les résultats seront enregistrés dans le dossier spécifié dans le fichier de configuration de dust_post.

Remarque : 
Mes codes ne sont sans doute pas parfait et il semble que nous n'atteignons pas de convergence dans certains cas. Mes résultats ne doivent pas être pris pour référence.