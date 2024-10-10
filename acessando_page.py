from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 1 - utilizando o WebDriver
browser = webdriver.Chrome()

#2 - Acessando a página
browser.get('https://www.amazon.com.br')


#3 - Acessando elemento em uma página
elem = browser.find_element(By.ID, 'twotabsearchtextbox')
elem.send_keys('ps5')
elem.send_keys(Keys.ENTER)

# browser.quit()
