from gtts import gTTS
import os

folder_name = "audio_files"  # Global variable for folder name

def text_to_speech(input_file):
    """
    This is a simple script to do batch text to speech in the following format:

    In the same directory that this script is run create a file called sounds.txt.

    The text in the file should be in the following format:
    ```
    sound dcharge
    sound dfire
    sound reload
    ```
    Where `sound` is followed by a single space followed by the text that you want to be converted to speech. The converted speech will be saved in the same name. 

    EX:
    sound dcharge -> audio_files/dcharge.wav
    sound dfire -> audio_files/dfire.wav
    sound reload -> audio_files/reload.wav

    """
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
    input_file = "sounds.txt"  # Change this to the path of your input file
    text_to_speech(input_file)
