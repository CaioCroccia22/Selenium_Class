from selenium import webdriver

# utilizando o WebDriver
browser = webdriver.Firefox()
print(browser)

browser.get('https://www.amazon.com.br')
browser.quit()
