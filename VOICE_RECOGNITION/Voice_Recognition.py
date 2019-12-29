import speech_recognition as sr

r=sr.Recognizer()

with sr.Microphone() as source:
    print('Say Something ! :')
    audio=r.listen(source)

    try:
        text=r.recognize_google(audio)
        print('here is what u said : {}'.format(text))
    except:
        print('SORRY COULD NOT HEAR WHAT YOU SAID !')
