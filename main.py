import text_to_speech

text_to_speech.speak("Welcome to Dhrashti - Vision for Blind")
text_to_speech.speak("Getting your device ready - Please Wait")

import config
import speech_recognition as sr
import image_capture
import image_detection
import currency_detection

r=sr.Recognizer()

text_to_speech.speak("Your Device is Ready")

MyText=""
while(MyText!="stop"):
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Start Speak")
            audio=r.listen(source,phrase_time_limit=5)
            print("End Speak")

            MyText=r.recognize_google(audio)
            MyText=MyText.lower()
            
            if(MyText=="image"):
                text_to_speech.speak("Capturing Image")
                image_capture.capture()
                output=image_detection.image_detection()
                print(output)
                text_to_speech.speak(output)
            elif(MyText=="currency"):
                text_to_speech.speak("Capturing Image")
                image_capture.capture()
                output=currency_detection.currency_detection()
                print(output)
                text_to_speech.speak(output)
            elif(MyText!="stop"):
                text_to_speech.speak("Wrong input, can you please speak again?")
    except sr.RequestError as request_error:
        text_to_speech.speak("Internet is not working.")
    except sr.UnknownValueError as unknown_value_error:
        print("Unknown Error Occured")

text_to_speech.speak("Thank You")
text_to_speech.speak("Restart to use your device again")