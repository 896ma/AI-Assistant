import speech_recognition as aa
import pyttsx3
import pywhatkit
import datetime
import wikipedia

machine = pyttsx3.init()


def talk(text):
    machine.say(text)
    machine.runAndWait()


listener = aa.Recognizer()


def input_instruction():
    instruction = ""  # Initialize instruction variable

    try:
        with aa.Microphone() as origin:
            print("Listening for a command : )")
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()

            if "Eddy" in instruction:  # activation word
                instruction = instruction.replace('Eddy', "")
                print(instruction)

    except aa.UnknownValueError:
        print("Sorry, I couldn't understand the audio. Please repeat.")
        talk("Sorry, I couldn't understand the audio. Please repeat.")
    except aa.RequestError as e:
        print(f"Speech recognition request failed: {e}")
        talk("Sorry, there was an error with the speech recognition. Please try again later.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        talk("An unexpected error occurred. Please try again.")

    return instruction


def play_Eddy():
    instruction = input_instruction()
    print(instruction)

    # Adding conditional statements to implement functionalities
    if "play" in instruction:
        song = instruction.replace("play", "")
        talk("Playing " + song)
        pywhatkit.playonyt(song)

    elif 'time' in instruction:
        current_time = datetime.datetime.now().strftime('%I:%M:%p')
        talk('The current time is ' + current_time)

    elif 'date' in instruction:
        current_date = datetime.datetime.now().strftime('%dth of %m , %Y')
        talk("Today's date " + current_date)

    elif 'hello' in instruction:
        talk('Greetings Developer!')

    elif 'identify yourself' in instruction:
        print('My name is Eddy , A  high level AI Assistant, what can I do for you today :)')
        talk('My name is Eddy , A  high level AI Assistant, what can I do for you today ')

    elif 'search' in instruction:
        finder = instruction.replace('search', "")
        info = wikipedia.summary(finder, 1)
        print(info)
        talk(info)

    else:
        print("Sorry but I did not quite catch that. Please repeat :)")
        talk("Sorry but I did not quite catch that. Please repeat")


play_Eddy()
