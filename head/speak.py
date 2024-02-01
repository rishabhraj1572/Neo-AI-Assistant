import pygame,os

def speak(text):
    voice = "en-US-ChristopherNeural"

    command = f'edge-tts --voice "{voice}" --text "{text}" --write-media "audio/output.mp3"'

    os.system(command)

    pygame.init()
    pygame.mixer.init()

    try:
        pygame.mixer.music.load("audio/output.mp3")

        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        print(e)

    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()


# speak('hello')
# speak('hello')
# import pygame
# print(edge-tts.__file__)
