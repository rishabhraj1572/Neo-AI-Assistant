from time import sleep 
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import warnings 
from selenium.webdriver.chrome.service import Service

warnings.simplefilter("ignore")
url = f'https://text-to-speech.online/'
chrome_driver_path = 'chromedriver.exe'
chrome_options = Options()
#chrome_options.add_argument("--headless=new")  # Enable headless mode (runs Chrome without GUI)
chrome_options.add_argument('--log-level=3')  # Set Chrome log level
service = Service(chrome_driver_path)
user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
chrome_options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.get(url)
sleep(3)

def select_voice():
    locale = driver.find_element(By.ID, 'locale').click()
    sleep(0.7)
    japnese_voice = driver.find_element(By.XPATH, '//*[@id="locale"]/option[72]').click()
    sleep(0.7)
    voice = driver.find_element(By.ID, 'voice').click()
    sleep(0.7)
    female_voice = driver.find_element(By.XPATH, '//*[@id="voice"]/option[2]').click()


def speak(text):
    driver.execute_script("document.querySelector('.cookiealert').style.display='none';")
    textarea = driver.find_element(By.ID, 'text')
    textarea.clear()
    textarea.send_keys(text)
    sleep(2)
    playBtn = driver.find_element(By.ID,'quick-play')
    playBtn.click()
    sleep(10)
    
    
select_voice()
# while 1:
#     speak(input('>> '))