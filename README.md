<div align="center">
  <img src="https://github.com/user-attachments/assets/0c269e33-fbba-4fb3-8313-564803d0c2e6"width=800>
</div>
# 🗣️ Text-to-Speech (TTS) Demo with PyTorch & Streamlit

# Text-to-Speech Training Notebook

## Présentation

Ce notebook permet d'entraîner un modèle de synthèse vocale (Text-to-Speech, TTS) à partir de données textuelles et audio. Il est conçu pour être exécuté sur Google Colab avec un GPU, ce qui facilite l'entraînement même pour les utilisateurs ne disposant pas de ressources matérielles puissantes. À la fin de l'entraînement, le modèle peut être exporté et téléchargé pour un déploiement ultérieur, par exemple via une application Streamlit ou Hugging Face Spaces.

---

## Fonctionnalités

- **Installation automatique des dépendances nécessaires**
- **Téléchargement et préparation du jeu de données**
- **Entraînement d'un modèle TTS (par exemple, Tacotron2 sur LJSpeech)**
- **Sauvegarde du modèle entraîné sur Google Drive**
- **Téléchargement facile du modèle pour une utilisation future**
- **Déploiement facile sur Streamlit ou Hugging Face Spaces**

---

## Prérequis

- Un compte Google pour utiliser Google Colab et Google Drive
- Connaissances de base en Python et Machine Learning (optionnel, mais recommandé)
- Jeu de données compatible (par défaut, LJSpeech)

---

## Utilisation

### 1. Ouvrir le notebook sur Google Colab

Téléchargez ou ouvrez le notebook `texttospeechlaaastttt.ipynb` sur Google Colab.

### 2. Installer les dépendances

Les premières cellules installent toutes les bibliothèques nécessaires, notamment :
- [TTS](https://github.com/coqui-ai/TTS)
- `numpy` (version compatible)
- Autres dépendances audio

### 3. Préparer les données

Le notebook télécharge et extrait automatiquement le jeu de données LJSpeech. Vous pouvez modifier cette étape pour utiliser vos propres données.

### 4. Entraîner le modèle

L'entraînement se fait via la bibliothèque TTS. Les paramètres (nombre d'époques, batch size, etc.) sont configurables selon vos besoins et la puissance du GPU disponible.

### 5. Sauvegarder et télécharger le modèle

À la fin de l'entraînement, le modèle est sauvegardé sur Google Drive puis compressé pour être téléchargé localement.

### 6. Déploiement

Le modèle téléchargé peut être intégré dans une application Streamlit, ou être déployé facilement sur Hugging Face Spaces.

---

## Exemple de déploiement

### Sur Hugging Face Spaces

Une démo du modèle est également disponible en ligne sur Hugging Face Spaces :  
👉 [Accéder à la démo Hugging Face](https://huggingface.co/spaces/123456KAWTAr/speech_app)

Vous pouvez tester le modèle directement via cette interface web sans installation supplémentaire.

---

## Conseils

- Pensez à ajuster la version de `numpy` si vous rencontrez des erreurs de compatibilité.
- Utilisez un GPU Colab pour accélérer l'entraînement.
- Sauvegardez régulièrement votre travail sur Google Drive.

---

## Auteurs

Notebook adapté pour un usage pédagogique et pratique en synthèse vocale automatique.




