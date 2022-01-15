import speech_recognition as sr

engine = sr.Recognizer()
mic = sr.Microphone()
hasil = ""

with mic as source:
    print("Silahkan mulai bicara")
    rekaman = engine.listen(source)
    print("Waktu habis")
    
    try:
        hasil = engine.recognize_google(rekaman, language = "id-ID")
        print(hasil)
    except engine.UnknownValueError:
        print("Maaf suara anda tidak terdeteksi, mohon coba lagi")
    except Exception as e:
        print(e) 