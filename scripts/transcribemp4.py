import os
import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence

def transcribe_audio_chunk(recognizer, chunk):
    try:
        return recognizer.recognize_google(chunk)
    except sr.UnknownValueError:
        return ""
    except sr.RequestError as e:
        print(f"API unavailable or unresponsive: {e}")
        return ""

def transcribe_large_audio(path):
    sound = AudioSegment.from_wav(path)
    chunks = split_on_silence(sound, min_silence_len=500, silence_thresh=sound.dBFS-14, keep_silence=500)
    
    folder_name = "audio-chunks"
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    
    whole_text = ""
    recognizer = sr.Recognizer()
    
    for i, chunk in enumerate(chunks, start=1):
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        chunk.export(chunk_filename, format="wav")
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = recognizer.record(source)
            try:
                text = transcribe_audio_chunk(recognizer, audio_listened)
            except sr.RequestError as e:
                print(f"Could not request results: {e}")
                continue
        whole_text += text + " "
    
    return whole_text

if __name__ == '__main__':
    # Prompt the user to enter the MP4 file path
    mp4_file = input("Enter the path to the MP4 file: ")
    
    try:
        # Extract the audio from the MP4 file
        print("Extracting audio from MP4...")
        audio = AudioSegment.from_file(mp4_file, format="mp4")
        audio_file = "audio.wav"
        audio.export(audio_file, format="wav")
        
        print("Transcribing audio...")
        text = transcribe_large_audio(audio_file)
        
        print("Transcription:")
        print(text)
        
        # Save the transcript to a text file
        with open("transcript.txt", "w") as file:
            file.write(text)
        print("Transcript saved to transcript.txt")
    
    except FileNotFoundError:
        print(f"Error: The file '{mp4_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        # Clean up temporary files
        if os.path.exists("audio.wav"):
            os.remove("audio.wav")
        if os.path.exists("audio-chunks"):
            for file in os.listdir("audio-chunks"):
                os.remove(os.path.join("audio-chunks", file))
            os.rmdir("audio-chunks")