import speech_recognition as sr

r=sr.Recognizer()

with sr.Microphone() as source:
    print('say something: ')
    audio=r.listen(source)

try:
    text = r.recognize_google(audio)
    print('you said: ', text)
except:
    print('tranlate failed')

with open('waveaudio.wav','wb') as f:
    f.write(audio.get_wav_data())
