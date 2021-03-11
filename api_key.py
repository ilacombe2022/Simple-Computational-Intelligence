from selenium import webdriver

# Location of web driver
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# Need a free API key, driver will prompt to Google Chrome once the program runs
driver.get("https://www.wolframalpha.com/")
print(driver.title)