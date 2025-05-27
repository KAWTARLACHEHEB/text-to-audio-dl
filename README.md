<div>
  <img src="https://github.com/user-attachments/assets/0c269e33-fbba-4fb3-8313-564803d0c2e6">
</div>

# text-to-audio-dl
# Text-to-Audio - End-to-End Deep Learning Project

Ce projet présente un système complet de synthèse vocale basé sur un réseau de neurones artificiels entraîné à partir de zéro.  
L’objectif est de convertir une phrase textuelle en signal audio en apprenant à mapper les représentations textuelles vers des MFCCs (features audio), puis à reconstruire le son.

---

## Objectif du projet

- Créer un pipeline **texte → MFCC → audio**
- Utiliser le dataset **LJSpeech 1.1** contenant des fichiers `.wav` et leurs transcriptions
- Entraîner un petit **modèle ANN avec TensorFlow/Keras**
- Déployer une interface via **Streamlit**

---

## Dataset utilisé

- **Nom** : LJSpeech-1.1  
- **Source** : https://keithito.com/LJ-Speech-Dataset/  
- **Taille** : 13 100 phrases lues par une voix féminine
- Utilisé ici : **sous-ensemble de 500 exemples**

---

##  Technologies utilisées

- Python 3.9
- TensorFlow / Keras
- Librosa (extraction MFCC + reconstruction audio)
- Matplotlib
- Jupyter Notebook
- Streamlit

---

## Étapes du projet

1. **Chargement du dataset** `metadata.csv` + fichiers `.wav`
2. **Prétraitement du texte** (tokenisation, encodage)
3. **Extraction des MFCCs** à partir des fichiers audio
4. **Entraînement d’un modèle ANN**
5. **Génération audio prédite** via les MFCCs
6. **Interface utilisateur Streamlit (à venir)**

---

## Lancer le projet

### 1. Installer les dépendances
```bash
pip install tensorflow librosa matplotlib pandas scikit-learn streamlit
