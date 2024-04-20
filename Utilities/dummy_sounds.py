from gtts import gTTS
import os

folder_name = "audio_files"  # Global variable for folder name

def text_to_speech(input_file):
    # Create folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    with open(input_file, 'r') as f:
        lines = f.readlines()

    for line in lines:
        if line.startswith("sound"):
            words = line.split()[1:]
            text = ' '.join(words)
            tts = gTTS(text)
            tts.save(os.path.join(folder_name, f"{text}.wav"))

if __name__ == "__main__":
    input_file = "dummy_sounds.txt"  # Change this to the path of your input file
    text_to_speech(input_file)
