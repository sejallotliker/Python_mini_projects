import googletrans
import speech_recognition as sr
import gtts
import playsound

recognizer= sr.Recognizer()
translator = googletrans.Translator()

lang_input ="en-IN"
lang_output ="hi"

try:
    with sr.Microphone() as source:
        print("You can start speaking now....")
        voice =recognizer.listen(source)
        text= recognizer.recognize_google(voice, language= lang_input)
        print(text)

except:
    pass

translated = translator.translate(text, dest=lang_output)
print(translated.text)
converted_audio = gtts.gTTS(translated.text, lang=lang_output)

converted_audio.save("holi.mp3")
playsound.playsound('holi.mp3')

