from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://demoqa.com/')

browser.find_element_by_class_name('card-body').click()
browser.find_element_by_id('item-0').click()

data = {
    'userName': 'Ivan Ivanov',
    'userEmail': 'test@test.com',
    'currentAddress': 'Moscow, 22, Lobovs',
    'permanentAddress': 'Moscow, 33, Kirilovsk'
}

for selector, person in data.items():
    browser.find_element_by_id(selector).send_keys(person)

browser.find_element_by_id('submit').click()
browser.quit()