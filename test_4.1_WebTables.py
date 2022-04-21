from argparse import Action
from platform import architecture
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
browser.get('https://demoqa.com/')

browser.find_element(By.CLASS_NAME, 'card-body').click()
browser.find_element(By.ID, 'item-3').click()


number_of_users = 0

persons = {
    'firstName': "Egor",
    'lastName': "Petrov",
    'userEmail': "egorik@mail.ru",
    'age': "19",
    'salary': "20000",
    'department': "AutoDesker"
}
while number_of_users != 50:
    browser.find_element(By.ID, "addNewRecordButton").click()

    for selector, person in persons.items():
        browser.find_element(By.ID, selector).send_keys(person)
    
    browser.find_element(By.CSS_SELECTOR, "#submit").click()
    number_of_users += 1
    print(number_of_users)

Select(browser.find_element(By.CSS_SELECTOR, '[aria-label="rows per page"]')).select_by_value("50")
