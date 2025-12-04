# =============================
# Audiobook Creator using gTTS
# =============================

# =============================
# Install : pip install gtts
# =============================

from gtts import gTTS

# Read text file
with open("abc.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Convert to audio
coding = gTTS(text = text, lang="en")

# Save audiobook
coding.save("audiobook.mp3")

print("Audiobook created: audiobook.mp3")

