from selenium import webdriver
from PIL import Image
from io import BytesIO
#browser exposes an executable file
#Through Selenium test we will invoke the executable file which will then
#invoke actual browser
driver = webdriver.Chrome(executable_path="chromedriver.exe")
# to maximize the browser window
from time import sleep

driver.get('https://www.python.org')
sleep(1)

driver.get_screenshot_as_file("screenshot.png")
driver.quit()
print("end...")