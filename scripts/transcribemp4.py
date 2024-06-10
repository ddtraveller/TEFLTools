import os
import speech_recognition as sr
from pydub import AudioSegment

# Specify the path to the MP4 file
mp4_file = "girl_complains_about_price_of_ice_cream.mp4"

# Extract the audio from the MP4 file
audio = AudioSegment.from_file(mp4_file, format="mp4")
audio_file = "audio.wav"
audio.export(audio_file, format="wav")

# Create a recognizer object
recognizer = sr.Recognizer()

# Load the audio file
with sr.AudioFile(audio_file) as source:
    # Read the audio data
    audio = recognizer.record(source)

# Perform speech recognition using Google Speech Recognition
try:
    text = recognizer.recognize_google(audio)
    print("Transcription:")
    print(text)

    # Save the transcript to a text file
    with open("transcript.txt", "w") as file:
        file.write(text)

    print("Transcript saved to transcript.txt")

except sr.UnknownValueError:
    print("Speech recognition could not understand the audio")

except sr.RequestError as e:
    print("Could not request results from the speech recognition service; {0}".format(e))

# Remove the temporary audio file
os.remove(audio_file)