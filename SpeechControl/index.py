import os
from pygame import mixer
import speech_recognition as sr
import music
import pyttsx3


def ConvertSpeech():
    """
    converts speech -> string-> Music commands
    :return:
    """
    engine = pyttsx3.init()
    r = sr.Recognizer()
    recog_text = ""
    mus = music.Music()
    '''
    end or finish - to end the speech
    '''
    # engine.say(f"Welcome to Voisic")
    # engine.runAndWait()
    # engine.say(f"Say play music name to play a song")
    # engine.runAndWait()
    # engine.say(f"Say random to shuffle your playlist")
    # engine.runAndWait()
    # engine.say(f"Say finish or end to end the voisic process")
    # engine.runAndWait()
    # engine.stop()
    while recog_text != "finish" and recog_text != "end":
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.2)
                audio = r.listen(source)
                recog_text = r.recognize_google(audio)
                recog_text = recog_text.lower()
                print(recog_text)
                """
                the main control function
                """
                if "random" in recog_text:
                    mus.random_play()
                elif "play" in recog_text:
                    song_text = recog_text.replace("play ", "")
                    engine.say(f"playing {song_text}")
                    engine.runAndWait()
                    engine.stop()
                    song = song_text+".mp3"
                    print(song)
                    mus.play_one_song(song)
                elif "stop" in recog_text:
                    mus.stop()
                elif "resume" in recog_text:
                    mus.resume()
                elif "increase volume" in recog_text:
                    volume_word = ''.join(x for x in recog_text if x.isdigit())
                    volume = 1 if volume_word == "" else int(volume_word)
                    print(volume)
                elif "decrease volume" in recog_text or "reduce volume" in recog_text:
                    volume_word = ''.join(x for x in recog_text if x.isdigit())
                    volume = 1 if volume_word == "" else int(volume_word)
                    print(volume)
                elif "next" in recog_text:
                    mus.random_next()
                elif "previous" in recog_text:
                    mus.random_prev()

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("unknown error")


ConvertSpeech()
