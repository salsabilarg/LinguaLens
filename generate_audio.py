# Membuat file MP3 untuk setiap kata di words.json
# Jalankan sekali:  pip install gTTS   lalu   python generate_audio.py
import json
import os
from gtts import gTTS

with open("words.json", encoding="utf-8") as f:
    words = json.load(f)

for label, langs in words.items():
    label = "_".join(label.lower().split())   # nama file selalu huruf kecil
    for lang, text in langs.items():
        folder = os.path.join("audio", lang)
        os.makedirs(folder, exist_ok=True)
        path = os.path.join(folder, f"{label}.mp3")
        if os.path.exists(path):
            print("lewati (sudah ada):", path)
            continue
        gTTS(text=text, lang=lang).save(path)
        print("dibuat:", path)

print("Selesai.")