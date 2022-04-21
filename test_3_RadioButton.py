from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://demoqa.com/')

browser.find_element_by_class_name('card-body').click()
browser.find_element_by_id('item-2').click()

clicks = ['[for="yesRadio"]', '[for="impressiveRadio"]']
for click in clicks:
    browser.find_element_by_css_selector(click).click()
