README - Simulations CFD avec DUST : CASALINO

Le dossier "Casalino" contient mes premières simulations de mécanique des fluides numériques (CFD) réalisées avec le logiciel DUST.

Objectif des simulations :
Ces simulations visaient à analyser la portance et le moment générés par une hélice de référence, étudiée l'année précédente par un camarade. L'objectif était de reproduire des résultats similaires pour valider l'approche.

Remarque :
Le rotor utilisé dans ces simulations ne respecte aucun des critères imposés par le cadre du challenge ONERA 2025. De plus, les codes fournis ne sont sans doute pas parfaits et ne doivent pas être considérés comme une référence.

Contenu du dossier :
Le dossier "Casalino" contient deux approches distinctes pour effectuer les simulations.

Méthode Lifting Lines (dossier Hover_LL_3)
Méthode Vortex Lattice (dossier Hover_VL)
Voir dust_user_manual pour plus de précisions sur les méthodes.

Traitement des données :
Les résultats sont traités à l'aide de scripts Python disponibles dans le dossier visualisation_python. Ces scripts permettent de lire les fichiers .DAT générés par les simulations. Le temps en abscisse est la période définie par t_start et t_end dans "dust_post" (exemple : t_start = 300, t_end = 361, dt = 0.0002 donc l'intervalle traité par dust_post couvre 0.012s à partir de t_start).
Ces fichiers se trouvent dans les répertoires suivants :

postpro/ pour Hover_VL
resultats_2_helices/ et resultats_3_helices/ pour Hover_LL_3
Pour Hover_VL, j'ai testé de changer t_start et t_end pour vérifier que la convergence est atteinte.


Pour exécuter les simulations :
Ouvrir un terminal sous Ubuntu 22.05.4.
Naviguer jusqu'au répertoire contenant les codes.
Lancer successivement les commandes suivantes :
dust_pre
dust
dust_post
Les résultats seront enregistrés dans le dossier spécifié dans le fichier de configuration de dust_post.