import streamlit as st
import torch
import re
import torchaudio
from unidecode import unidecode
import numpy as np
import tempfile
import os

# 🔥 Importer les bons modules de transformers
from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, SpeechT5HifiGan

# ========== Traitement du texte ==========
def clean_text(text):
    text = unidecode(text.lower())
    text = re.sub(r"[^a-z' ]+", "", text)
    return text

# ========== Charger le modèle ==========
@st.cache_resource
def load_model():
    output_dir = os.path.join(os.path.dirname(_file_), "saved_tts_model")
    processor = SpeechT5Processor.from_pretrained(output_dir)
    model = SpeechT5ForTextToSpeech.from_pretrained(output_dir)
    vocoder = SpeechT5HifiGan.from_pretrained(os.path.join(output_dir, "vocoder"))
    return processor, model, vocoder

# ========== Interface Streamlit ==========
st.title("🗣 Text-to-Speech (TTS) avec PyTorch")

text_input = st.text_input("Entrez votre texte en anglais 👇", "hello world")

if st.button("Convertir en audio 🎧"):
    with st.spinner("Génération de la voix en cours..."):
        # Charger les modèles
        processor, model, vocoder = load_model()

        # Nettoyer et encoder le texte
        cleaned = clean_text(text_input)
        inputs = processor(text=cleaned, return_tensors="pt")

        # Générer un speaker embedding aléatoire (tu peux charger un vrai speaker si tu veux)
        speaker_embeddings = torch.randn((1, 512))

        # Générer le spectrogramme
        with torch.no_grad():
            speech = model.generate_speech(inputs["input_ids"], speaker_embeddings, vocoder=vocoder)

        # Sauvegarder temporairement l'audio
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
            torchaudio.save(f.name, speech.unsqueeze(0), 16000)
            st.audio(f.name)

        os.unlink(f.name)
