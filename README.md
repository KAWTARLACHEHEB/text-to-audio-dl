<div align="center">
  <img src="https://github.com/user-attachments/assets/0c269e33-fbba-4fb3-8313-564803d0c2e6"width=800>
</div>
# 🗣️ Text-to-Speech (TTS) Demo with PyTorch & Streamlit

This is a web-based Text-to-Speech (TTS) demo built using **PyTorch**, **Streamlit**, and pre-trained models saved in the Hugging Face-compatible format. Users can input English text and generate realistic synthetic speech.

---

## 🚀 Features

- Convert English text into speech
- Simple, interactive web interface using Streamlit
- Uses a pre-trained TTS model and vocoder
- Models are saved and loaded using Hugging Face’s `save_pretrained` / `from_pretrained`

---

## 📁 Project Structure
tts-demo/
├── saved_tts_model/
│ ├── config.json
│ ├── pytorch_model.bin
│ ├── tokenizer_config.json
│ └── vocoder/
│ ├── config.json
│ └── pytorch_model.bin
├── streamlit_app.py
├── requirements.txt
└── README.md

## 🛠️ Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/tts-demo.git
cd tts-demo
Install dependencies

bash
Copier
Modifier
pip install -r requirements.txt
Verify your models are saved in saved_tts_model/
Make sure you saved them like this:

python
Copier
Modifier
processor.save_pretrained(output_dir)
model.save_pretrained(output_dir)
vocoder.save_pretrained(os.path.join(output_dir, "vocoder"))

## ▶️ Run the Application
bash
Copier
Modifier
streamlit run streamlit_app.py
Open the Streamlit app in your browser and type any text to hear the generated audio.


## 🧠 Model Loading
To reload the saved models in your code:

python
Copier
Modifier
from transformers import AutoProcessor
from your_model_file import YourModelClass
from your_vocoder_file import YourVocoderClass

processor = AutoProcessor.from_pretrained("saved_tts_model")
model = YourModelClass.from_pretrained("saved_tts_model")
vocoder = YourVocoderClass.from_pretrained("saved_tts_model/vocoder")


✅ Replace YourModelClass and YourVocoderClass with the actual class names used during training/saving.
---


💡 How It Works
Text is entered by the user.

The processor/tokenizer prepares the input.

The TTS model outputs a mel spectrogram.

The vocoder converts the spectrogram to audio.

The app plays the audio output in real time.

## 📦 Requirements

torch

torchaudio

transformers

streamlit

numpy

unidecode

Install all with:

bash
Copier
Modifier
pip install -r requirements.txt
🧪 Example
text
Copier
Modifier
Input: "Hello, how are you today?"
Output: [Audio is played using the vocoder]
📄 License
This project is licensed under the MIT License.

## 👤 Author
Kawtar
Master's student in Informatique & Télécommunications
AI & Deep Learning enthusiast | Morocco 🇲🇦

🌐 Demo
https://huggingface.co/spaces/123456KAWTAr/speech_app
---

