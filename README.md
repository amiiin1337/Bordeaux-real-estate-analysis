# 🏠 Bordeaux Real Estate Analysis

**Analyse et Visualisation de l'Immobilier à Bordeaux (2020-2025)**

Un projet d'analyse de données immobilières basé sur les données DVF (Demandes de Valeurs Foncières) du gouvernement français, avec un focus sur la métropole bordelaise.

## 🎯 Objectifs du Projet

- Analyser l'évolution des prix immobiliers dans la région bordelaise
- Identifier les tendances par quartier et par type de bien
- Créer des visualisations claires et informatives
- Pratiquer le cycle complet d'un projet Data Science (de la donnée brute au résultat)

## 📊 Source des Données

Les données proviennent de la base officielle **DVF (Demandes de Valeurs Foncières)** :
- Source : [data.gouv.fr](https://files.data.gouv.fr/geo-dvf/latest/csv/)
- Périmètre : Département de la Gironde (33)
- Période : 2020-2025

## 🚀 Installation et Utilisation

### Prérequis
```bash
python 3.8+
pandas
matplotlib
seaborn
```

### Installation des dépendances
```bash
pip install pandas matplotlib seaborn jupyter
```

### Téléchargement des données
1. Aller sur https://files.data.gouv.fr/geo-dvf/latest/csv/
2. Télécharger le fichier le plus récent (ex: `2024.csv`)
3. Placer le fichier dans le dossier du projet

### Lancement de l'analyse
```bash
python analysis.py
```

## 📅 Roadmap

### ✅ Sprint 1 (Semaine 1-2) - EN COURS
- [x] Configuration du repository
- [x] Téléchargement des données DVF
- [x] Chargement et filtrage des données
- [x] Exploration initiale du dataset
- [x] **Résultat** : 11,660 transactions immobilières à Bordeaux chargées
- [ ] Nettoyage des données (filtrer Ventes, Maison/Appartement)
- [ ] Feature engineering (prix au m²)
- [ ] Gestion des outliers

### 📋 Sprint 2 (Semaine 3-4)
- [ ] Nettoyage des données
- [ ] Création de visualisations
- [ ] Analyse des prix par quartier

### 🎨 Sprint 3 (Mois 2)
- [ ] Dashboard interactif
- [ ] Documentation finale
- [ ] Déploiement

## 👨‍💻 Auteur

Projet réalisé dans le cadre du Master Informatique parcours IA - Université de Bordeaux

## 📝 License

Ce projet utilise des données publiques du gouvernement français.