from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.common.exceptions import NoSuchElementException
import time
import getpass

#Prompts user to enter username and password
userid= input("Enter your phone number")
pwd = getpass.getpass()


#Open  FB 
print("Opening Firefox...")
driver= webdriver.Firefox(executable_path = '/Users/karloman/Downloads/geckodriver') 
wait = WebDriverWait(driver, 10)
driver.get("https://facebook.com")
time.sleep(5)
print('Entering Username and Password')

#Login to FB
emailelement = driver.find_element_by_xpath('//*[@id="email"]')
emailelement.send_keys(userid)
passwordfield = driver.find_element_by_xpath('//*[@id="pass"]')
passwordfield.send_keys(pwd)
button = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]')
button.click()

print("Login successful")

# Navigate to birthdays page on Facebook
driver.get('https://www.facebook.com/events/birthdays')
time.sleep(5)

birthdays = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[1]/div/div/div/div[2]")
# print(birthdays)

#Grab Container for all of the birthdays today
containers = birthdays.find_elements_by_css_selector("[class='tvmbv18p s1tcr66n']")
print(f'There are {len(containers)} birthdays today')

# Loop through the birthdays today and grab the text box element
for b in containers:
    text_area = b.find_element_by_css_selector("[class='notranslate _5rpu']")
    text_area.send_keys("Happy Birthday!")

# Pause for dramatic effect 
time.sleep(5)

# Click on profile pic
profile = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/span')
profile.click()
time.sleep(2)

# Click Log out
log_out_button = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div[3]/div/div[4]/div/div[1]/div[2]/div/div/div/div/span')
log_out_button.click()
print("Logged out of Facebook")