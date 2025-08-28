# 📊 Analyse Simplifiée des Quartiers "Bad" (MAE Élevée)

## 🎯 Objectif

Cette analyse refactorisée et simplifiée identifie les quartiers ayant une erreur de prédiction élevée (MAE) et analyse les caractéristiques qui expliquent cette performance dégradée du modèle.

## 🏗️ Structure

L'analyse est organisée en **5 cellules distinctes** pour faciliter la compréhension et le refactoring :

### 1️⃣ Contexte et préparation
- **Objectif** : Chargement des données et définition des groupes de comparaison
- **Fonctionnalités** :
  - Entraînement d'un modèle RandomForest simple
  - Calcul de la MAE globale et par quartier
  - Identification des quartiers "bad" (MAE > percentile 75)
  - Création du flag `__is_bad__` pour l'analyse comparative

### 2️⃣ Métriques simples (ΔMAE) et tableaux récap
- **Objectif** : Calcul des MAE pour toutes les caractéristiques numériques et catégorielles
- **Fonctionnalités** :
  - Prédiction "naïve" basée sur les médianes par quartile (variables numériques)
  - Prédiction "naïve" basée sur les moyennes par modalité (variables catégorielles)
  - Calcul du ΔMAE = MAE(quartiers_bad) - MAE(quartiers_good)
  - Tableaux récapitulatifs triés par impact

### 3️⃣ Graphiques lisibles pour les TOP_K features (numériques)
- **Objectif** : Visualisation des médianes de SalePrice par quantile
- **Fonctionnalités** :
  - Grille compacte de 6 sous-graphiques (2x3)
  - Comparaison côte à côte quartiers "Good" vs "Bad"
  - Annotations automatiques des valeurs
  - Affichage du ΔMAE dans le titre de chaque graphique

### 4️⃣ Graphiques lisibles pour les TOP_K features (catégorielles)
- **Objectif** : Visualisation des moyennes de SalePrice par modalité
- **Fonctionnalités** :
  - Graphiques en barres pour chaque feature catégorielle
  - Tri par différence pour meilleure lisibilité
  - Annotations des écarts importants (>20k$)
  - Filtrage des modalités avec peu de données

### 5️⃣ Pistes d'action, par quartier "bad"
- **Objectif** : Rapport textuel sur les caractéristiques qui pénalisent la MAE
- **Fonctionnalités** :
  - Analyse détaillée par quartier problématique
  - Identification des features les plus impactantes
  - Recommandations spécifiques et actionables
  - Résumé global des actions prioritaires

## 🔧 Améliorations techniques

### Robustesse
- Gestion des erreurs pour les features à peu de valeurs uniques (`duplicates='drop'`)
- Fonction MAE corrigée avec gestion des cas limites
- Validation des données avant visualisation

### Lisibilité
- **Commentaires en français** comme demandé
- **Emojis et formatage** pour une navigation claire
- **Structure modulaire** en cellules séparées
- **Graphiques compacts** et informatifs

### Performance  
- Utilisation de méthodes vectorisées NumPy/Pandas
- Filtrage intelligent des données peu représentatives
- Optimisation des calculs de MAE

## 📈 Résultats types

L'analyse identifie automatiquement :
- **Quartiers problématiques** : Ceux avec MAE > percentile 75
- **Features numériques critiques** : Ex. GrLivArea (ΔMAE: +57k$)
- **Features catégorielles critiques** : Ex. KitchenQual (ΔMAE: +47k$)
- **Recommandations prioritaires** par quartier

## 🎨 Visualisations

### Graphiques numériques
- **Format** : Barres côte à côte (Good vs Bad)
- **Métrique** : Prix médian par quartile de feature
- **Annotations** : Valeurs automatiques + ΔMAE

### Graphiques catégorielles  
- **Format** : Barres par modalité
- **Métrique** : Prix moyen par modalité
- **Annotations** : Écarts significatifs (Δ>20k$)

## 🚀 Utilisation

1. **Exécuter la cellule 1** pour préparer les données et identifier les quartiers "bad"
2. **Exécuter la cellule 2** pour calculer les métriques ΔMAE
3. **Exécuter la cellule 3** pour visualiser les features numériques problématiques
4. **Exécuter la cellule 4** pour visualiser les features catégorielles problématiques  
5. **Exécuter la cellule 5** pour générer le rapport d'actions

## 💡 Insights typiques

- **Features numériques** : Les quartiers "bad" ont souvent des patterns non-linéaires
- **Features catégorielles** : Mêmes modalités, prix différents selon quartier
- **Recommandations** : Modèles spécialisés, interactions quartier-specific, collecte de données

## 📋 Prochaines étapes

1. **Implémenter** les interactions spécifiques aux quartiers identifiés
2. **Collecter** plus de données pour les quartiers sous-représentés  
3. **Développer** des modèles spécialisés pour les quartiers à haute variabilité
4. **Tester** l'encodage spécifique aux quartiers pour les features catégorielles