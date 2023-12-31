from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains



import time

# https://sites.google.com/chromium.org/driver/
# https://creditcards.chase.com/a1/southwest/AEP50kPlus1223?REF=FULLSITE&CELL=6PNF

# Set the user agent string for iPhone
iphone_user_agent = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15"
)

# Set the options for Chrome WebDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"user-agent={iphone_user_agent}")

# Set the path tothe ChromeDriver executable
chrome_driver_path = r'chromedriver.exe'  # Replace with the actual path

# Set the service options including executable path
service = Service(executable_path=chrome_driver_path)

# Create a Chrome WebDriver with the specified options and service
driver = webdriver.Chrome(service=service, options=chrome_options)

starturl=("https://bot.sannysoft.com/")
driver.get(starturl)



# Wait for the presence of the element with the specified href attribute
try:
    apply_now_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="cardInfo"]/div/header/div[3]/div[2]/div/div[2]/div[1]/div[1]/a')
        )
    )

    # Scroll to the element
    apply_now_button.location_once_scrolled_into_view
    # Click the element
    action = ActionChains(driver)
    action.move_to_element_with_offset(apply_now_button, 5, 5)
    action.click()
    action.perform()
    print("Will click it vi JS")
    #driver.execute_script("arguments[0].click();", apply_now_button)

    # Perform actions with the located element, for example, click on it
    newlink = apply_now_button.get_attribute("href")
    print(f"The href attribute is: {newlink}")
    time.sleep(5)
    #driver.get(newlink)

#    apply_now_button.click()
#    print("Element found and clicked!")
except TimeoutException:
    print("Timeout: Element not found within specified time.")

 

time.sleep(155) 

#driver.quit()