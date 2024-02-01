import cv2
from PIL import Image

email_addresses = {
    'myself': 'YOUR_EMAIL',
    }

phone_numbers = {
    'myself': 'YOUR_WHATSAPP_NUMBER',
    }

def run():
    import os
    import pygame
    import pyautogui
    import pywhatkit
    import speech_recognition as sr
    # from scrapper.bot_scrapper import *
    from datetime import datetime
    from head.listen import take_command

    from functions.emailsender import send_email
    from head.listen import take_command
    from head.speak import speak
    import subprocess
    from handcontrolling.main import hand_controlling
    sleep_mode = False

    speak('Hello sir, I am Neo and How can i help you today?')

    while True:
        query = take_command().lower()
        print('\nYou: ' + query)


        # if 'open' in query:
        #     app_name = query.replace('open', '')
        #     speak('opening ' + app_name)
        #     pyautogui.press('super')
        #     pyautogui.typewrite(app_name)
        #     pyautogui.sleep(1)
        #     pyautogui.press('enter')

        # if 'what is your name' in query or 'who are you' in query:
        #     speak("I am Neo and I am an AI Assistant ")

        if 'Hello' in query or 'hello' in query:
            speak('Hello! How can I assist you today?')

        elif 'write a note' in query or 'take a note' in query or 'take note' in query:
            write_note()
            # sleep_mode = True

        elif 'take picture' in query or 'take pictures' in query  or 'click pictures' in query or 'click picture' in query:
            speak('Taking Picture')
            speak('Smile Please')
            take_picture()
            speak('Done')
            speak('Do you want to see the image ?')
            y = take_command()
            if 'yes' in y:
                open_image()
            elif 'no' in y:
                pass
            else:
                pass

        elif 'weather' in query or 'temperature' in query:
            from weather import weather,get_ip_location
            print(get_ip_location(),":",weather(get_ip_location()))
            speak(f'current temperature in {get_ip_location()} is {weather(get_ip_location())}')
        
        elif 'show picture' in query or ' show image' in query or 'show pictures' in query or 'show my picture' in query:
            try:
                open_image()
            except:
                speak('No picture available')
            

        elif 'play' in query:
            song_name = query.replace('play', '')
            speak('Playing ' + song_name + ' in youtube')
            pywhatkit.playonyt(song_name)
            # sleep_mode = True

        elif 'switch tab' in query:
            pyautogui.hotkey('ctrl', 'tab')
            # sleep_mode = True

        elif 'close tab' in query:
            pyautogui.hotkey('ctrl', 'w')
            # sleep_mode = True

        elif 'close' in query:
            pyautogui.hotkey('alt', 'f4')
            speak('done sir')
            # sleep_mode = True

        elif 'time' in query:
            current_time = datetime.now().strftime('%H:%M %p')
            speak(f'Current time is {current_time}')
            # sleep_mode = True
        
        elif 'date' in query:
            current_date = datetime.now()
            formatted_date = current_date.strftime('%d %B, %Y')
            speak(f'Todays date is {formatted_date}')
            # sleep_mode = True

        elif 'sleep' in query:
            speak('Ok sir. I am going to sleep but you can call me any time just say wake up and i will be there for you.')
            sleep_mode = True
        elif 'good bye' in query or 'bye bye' in query or 'goodbye' in query or 'byebye' in query or 'bye' in query:
            speak('have a good day sir.')
            sleep_mode = True
            break

        elif 'write an email' in query or 'compose an email' in query or 'send an email' in query or 'send email' in query:
            from gpt4_free import GPT
            speak('Sure sir, Can you provide me the name of the user to whom you want to send email: ')
            name = take_command().lower()
            print(name)
            email_address = get_email_address_by_name(name)
            print(email_address)
            if email_address is not None:
                speak('What should be the subject of the email?')
                subject = take_command()
                print(subject)
                speak('What should be the content?')
                email_prompt = take_command()
                print(email_prompt)
                
                send_email(email_address, subject, email_prompt)
                
                speak(f'Done sir. Email sent successfully to {name}')
            else:
                try:
                    speak('Sorry, the provided name is not in the list. Please manually enter the email address.')
                    receiver = input('Enter the email address: ')
                    speak('What should be the subject of the email?')
                    subject = take_command()
                    print(subject)
                    speak('What should be the content?')
                    email_prompt = take_command()
                    print(email_prompt)
                    
                    send_email(receiver, subject, email_prompt)
                
                    speak(f'Done sir. Email sent successfully to {receiver}')
                except:
                    speak('Email not sent')
                    pass
            # sleep_mode = True

        elif 'send whatsapp message' in query or 'send whatsapp' in query or 'whatsapp message' in query:
            from send_whatsapp import send_whatsapp_message
            speak('Sure sir, Can you provide me the name of the user to whom you want to send whatsapp message: ')
            name = take_command().lower()
            print(name)
            phone_num = get_phone_num_by_name(name)
            print(phone_num)
            if phone_num is not None:
                speak('What should be the content?')
                msg = take_command()
                print(msg)
                
                send_whatsapp_message(phone_num, msg)
                
                speak(f'Done sir. message sent successfully to {name}')
            else:
                try:
                    speak('Sorry, the provided name is not in the list. Please manually enter the phone number')
                    receiver = input('Enter the phone number: ')
                    speak('What should be the content?')
                    email_prompt = take_command()
                    print(email_prompt)
                    send_email('91'+receiver, email_prompt)
                    speak(f'Done sir. message sent successfully to {receiver}')
                except:
                    speak('Message not sent')
                    pass
                
                
        elif 'identify the object' in query or 'what is this' in query or 'identify' in query:
            speak('Sure sir, show item in the camera')
            from identify import detect_object_from_image
            import cv2
            # speak(f'Detected Object is {identify.detect_object_from_camera()}')      

            # from object_detection import detect_object_from_image

            if __name__ == "__main__":
                cap = cv2.VideoCapture(0)
                ret, frame = cap.read()
                cv2.imwrite("captured_image.jpg", frame)
                cap.release()

                detected_item = detect_object_from_image("captured_image.jpg")

                if detected_item:
                    print(f"Detected Item: {detected_item}")
                    speak(f'Detected Object is {detected_item}')  
                else:
                    speak("No item detected.")  
                # sleep_mode = True  

        elif 'scroll using hands' in query or 'scroll' in query:
            speak('Starting process')
            speak('Now you can scroll using your hands')
            try:
                hand_controlling()
            except:
                hand_controlling()  
            # sleep_mode = True

        # elif 'stop scroll' in query or 'stop' in query:
        #     speak('Stopping scroll process')
        #     # sleep_mode = True
            
        elif query=='take screenshot' or query=='screenshot' or query== 'screen shot':
            speak('Taking Screenshot')
            print('Taking Screenshot...')
            screenshot = pyautogui.screenshot()
            screenshot.save('screenshot.png')
            speak('Screenshot Saved successfully')
            print('Screenshot saved successfully')
            speak('do you want to see thre screenshot?')
            q = take_command()
            if 'yes' in q:
                try:
                    from PIL import Image
                    speak('opening screenshot')
                    image_path = 'screenshot.png'

                    image = Image.open(image_path)

                    image.show()
                except:
                    speak('error in opening')
            # sleep_mode = True
    

        elif 'show screenshot' in query or 'showscreenshot' in query:
            try:
                from PIL import Image
                speak('opening screenshot')
                image_path = 'screenshot.png'

                image = Image.open(image_path)

                image.show()
            except:
                speak('error in opening')
            # sleep_mode = True

        else:
            from gpt4_free import GPT,find_code
            # res = GPT(query)
            # speak(res)

            print('user: ' + query)
            response = GPT(query)
            python_code = find_code(response)

            if python_code:
                response = response.replace(python_code, '').replace(
                    'python', '').replace('```', '')
                speak(response)
                exec(python_code)
            else:
                    speak(response)
            # sleep_mode = True

        while sleep_mode:
            query = take_command().lower()
            print(query)
            if 'wake up' in query:
                speak('How can i help  you sir.')
                sleep_mode = False
            elif 'neo' in query:
                sleep_mode = False
            elif 'good bye' in query or 'bye bye' in query or 'goodbye' in query or 'byebye' in query or 'bye' in query:
                speak('have a good day sir.')
                sleep_mode = True
                exit()

def get_email_address_by_name(name):
    return email_addresses.get(name, None)

def get_phone_num_by_name(name):
    return phone_numbers.get(name, None)

def write_note():
    speak("What would you like to write in the note?")
    
    
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = recognizer.listen(source, timeout=5)
            note_content = recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand what you said.")
            return
        except sr.RequestError:
            speak("Sorry, I'm having trouble accessing Mic.")
            return
    
    note_filename = "note.txt"
    with open(note_filename, "w") as note_file:
        note_file.write(note_content + "\n")
    
    speak("Note written successfully. Opening notepad.")
    
    subprocess.Popen(["notepad.exe", note_filename])

def take_picture(file_path='captured_image.jpg'):
    cap = cv2.VideoCapture(0)

    ret, frame = cap.read()

    cv2.imwrite(file_path, frame)

    cap.release()

    print(f"Picture taken and saved as {file_path}")

def open_image(file_path='captured_image.jpg'):
    image = Image.open(file_path)
    image.show()

run()
exit()
