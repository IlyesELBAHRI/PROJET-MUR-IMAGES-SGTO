# PROJET-MUR-IMAGES-SGTO

## Description du projet
---
Le contexte de ce projet est de développer un système de mur d'images pour la serre géodésique de Polytech. Ce système doit permettre aux personnes passant par le hall du bâtiment Esclangon de visualiser les données de la serre ainsi que d'autres informations utiles telles que les horaires des bus et la météo. Le but serait de rendre le hall plus vivant et d’ajouter un sentiment d’appartenance à l’école.
Cependant, dans le cadre d'une stratégie de développement durable, il est important d'intégrer une dimension environnementale pour le projet par le biais de récupérations notamment ou encore de panneaux solaires.

## Auteurs - Etudiants EISE4
---
- **Walid BOUCHICHIT** - [Walid_Bouchichit](https://github.com/KCwalid)
- **Baptiste CAMON** - [Baptiste_Camon](https://github.com/baptiste-cn)
- **Louis DUBARLE** - [Louis_Dubarle](https://github.com/louisdbrle)
- **Ilyes EL BAHRI** - [Ilyes_El_Bahri](https://github.com/IlyesELBAHRI)

## Documentation
---
La documentation du projet est disponible à la racine du projet.  
Les codes sources utilisés pour le projet sont disponibles dans leur dossier respectif.  

## Structure du projet
---
Le projet est organisé en plusieurs dossiers :

- **/Jetson_nano** : contient le code source de l'application godot pour afficher différentes trames d'images/vidéos et informations ratp/météo.
- **/Jetson_Xavier** : contient tous les codes de la carte mère qui sert de serveur. Il y a le code de l'application web, les codes des APIs, les codes de traitements d'images/vidéos pour la matrice d'écrans ou pour les écrans secondaires et le code enet qui n'a finalement pas été retenu mais peut être exploité si besoin dans le futur.
- **/Scripts_python** : contient des scripts utiles pour le développement et le déploiement du projet.

