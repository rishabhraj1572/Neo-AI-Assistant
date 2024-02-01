import g4f
import re

messages = [
            {"role": "system",
             "content": "use modules like webbrowser, pyautogui, time,pyperclip,random,mouse,wikipedia,keyboard,datetime,tkinter,PyQt5 etc"},
            {"role": "system",
                "content": "don't use input function ad subprocess in python code"},
            {"role": "system", "content": "*always use default paths in python code*"},
            {
            "role": "system",
            "content": "When user say 'show image,' use the following code to display the image :\n```python\nfrom PIL import Image\n\nimage_path = r'C:\\Users\\subed\\OneDrive\\Desktop\\code\\AI TUTORIAL\\output\\0.jpeg'\nimage = Image.open(image_path)\nimage.show()\n```\nIf you want to show another image, let me know."
            },

            {
            "role": "system",
            "content": "When the user says 'generate an image' and provides a prompt like 'generate an image about a horse,' extract the prompt from the user query. Then, give this code to the user:\n```python\nfrom cookies.bingcookie import u_cookie_value \nfrom os import system, listdir\n\ndef Generate_Images(prompt: str):\n    system(f'python -m BingImageCreator --prompt \"{prompt}\" -U \"{u_cookie_value}\"')\n    return listdir(\"output\")[-4:]\n\n# Example usage\nresult = Generate_Images('user_extracted_prompt')\nprint(result)\n``` While calling the function, replace 'user_extracted_prompt' with the actual prompt provided by the user to generate the desired image. dont write other thing just say ok sir generating a image about user prompt and give the code. also dont write other things like heres the code. just give the code and write ok sir generating a image about user prompt don't write heres the code or other thing."},

            {"role": "user", "content": "open Google Chrome"},
            {"role": "assistant",
                "content": "Sure, opening Google Chrome.```python\nimport webbrowser\nwebbrowser.open('https://www.google.com')```"},

            {"role":"user","content": "open the screenshot.png"},
            {"role":"system","content":"Sure, here's the code to open the screenshot.png file using Python```python\nfrom PIL import Image\nimage_path = 'screenshot.png'\nimage = Image.open(image_path)\nimage.show()\n```"},
            
            {"role":"user","content": "open the captured_image.jpeg"},
            {"role":"system","content":"Sure, here's the code to open the screenshot.png file using Python```python\nfrom PIL import Image\nimage_path = 'captured_image.jpeg'\nimage = Image.open(image_path)\nimage.show()\n```"},

            {"role":"user","content":"Date"},
            {"role":"system","content":"```python\nfrom datetime import date\ncurrent_date = date.today()\nprint(current_date)\n```"},
            {"role":"user","content":"close current tab"},
            {"role":"system","content":"```python\nimport pyautogui\nimport time\npyautogui.hotkey('ctrl', 'w')\ntime.sleep(1)\n```"},
            {"role":"user","content":"search for ms dhoni"},
            {"role":"system","content":"```python\nimport webbrowser\nsearch_query = 'MS Dhoni'\nurl = f'https://www.google.com/search?q=ms%20dhoni'\nwebbrowser.open(url)\n```"},
            {"role":"user","content":"open google and search for ms dhoni"},
            {"role":"system","content":"```python\nimport webbrowser\nsearch_query = 'MS Dhoni'\nurl = f'https://www.google.com/search?q=ms%20dhoni'\nwebbrowser.open(url)\n```"},
                    {"role":"user","content":"take screenshot"},
            {"role":"system","content":"```python\nimport pyautogui\nscreenshot = pyautogui.screenshot()\nscreenshot.save('screenshot.png')```"},
            {"role":"user","content":"what is your name"},
            {"role":"system","content":"I am Neo not ChatGPT, I am an AI Assistant"},
            {"role":"user","content":"send whatsapp message to +917079110310"},
            {"role":"system","content":"sending message \n```python\nimport webbrowser\nsearch_query = '+917079110310'\nurl = f'https://wa.me/917079110310'\nwebbrowser.open(url)\n```"}
            ,
            {"role":"system","content":"whenever users asks for any information about anything provide in 15 words only"}


            ]


def GPT(*args):

    global messages
    assert args != ()

    message = ''
    for i in args:
        message += i

    messages.append({'role': 'user', "content": message})

    response = g4f.ChatCompletion.create(
        model="gpt-4-32k-0613",
        provider=g4f.Provider.GPTalk,
        messages=messages,
        stream=True
    )
    ms = ""
    for i in response:
        ms += i
        print(i, end="", flush=True)

    messages.append({'role': 'assistant', "content": ms})
    return ms


def find_code(text):
    pattern = r'```python(.*?)```'
    matches = re.findall(pattern, text, re.DOTALL)
    if matches:
        code = matches[0].strip()
        return code
    else:
        print('no code found')


# query = take_command()
# if query != '-':
#             print('user: ' + query)
#             response = GPT(query)
#             python_code = find_code(response)

#             if python_code:
#                 response = response.replace(python_code, '').replace(
#                     'python', '').replace('```', '')
#                 speak(response)
#                 exec(python_code)
#             else:
#                 speak(response)
# else:
#             pass


"""

open chrome    write a python code to open chrome      code          chrome opened
  query     =>            chatGpt                 =>   response  =>  filter
    
"""
