from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
import time


# set up Firefox options
firefox_options = Options()
firefox_options.headless = False # True does not open a window and runs in background instead
firefox_options.add_argument('-disable-extensions')
firefox_options.set_preference('javascript.enabled', True) 
service = Service(GeckoDriverManager().install())
firefox_options.binary_location = 'C:/Program Files/Mozilla Firefox/firefox.exe' 

# start web driver
driver = webdriver.Firefox(service=service, options=firefox_options)

# open 2048 
driver.get("https://play2048.co/")

# wait for the cookie consent button to be clickable and click it
wait = WebDriverWait(driver, 10)
try:
    # wait for up to 10 seconds for the button to be clickable
    cookie_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ez-accept-all"]')))
    cookie_button.click()
    print("Cookie consent button clicked.")
except Exception as e:
    print("Cookie consent button not found or could not be clicked:", e)


    
# find the div element and ensure the div element is focusable. not useful in this case bc we just send the keystrokes to the entire body of the page and dont need to focus any element
# div_element = driver.find_element(By.CSS_SELECTOR, 'div#div_id')
# driver.execute_script("arguments[0].setAttribute('tabindex', '0');", div_element)
# driver.execute_script("arguments[0].focus();", div_element)

body = driver.find_element(By.TAG_NAME, 'body')


# keep sending keystrokes until the retry button appears
def playGame():
    for nthgame in range(1000): #play 1000 games 
        print(f"Game {nthgame} is starting...")
        # continue playing the game
        while True:
            try:
                # look for the retry button 
                retry_button = WebDriverWait(driver, 0.001).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/div[1]/div/a[2]")))
                print("Button appeared!")
                break  
            except Exception as _:
                # send keystrokes if the retry button hasn't appeared
                body.send_keys(Keys.UP)
                time.sleep(0.001)
                body.send_keys(Keys.RIGHT)
                time.sleep(0.001)
                body.send_keys(Keys.DOWN)
                time.sleep(0.001)
                body.send_keys(Keys.LEFT)
                time.sleep(0.001)

        # click the restart button found earlier to restart the game
        # by going back into the nested infinite loop
        score = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[1]")
        best = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[2]")

        print(f"Retry button clicked! Game restarting...\nScore achieved: {score.text}\nBest: {best.text}")
        retry_button.click()

playGame()

input ("Press Enter to close the program")

driver.quit()
