from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
browser.get('https://demoqa.com/')

browser.find_element(By.CLASS_NAME, 'card-body').click()
browser.find_element(By.ID, 'item-3').click()
browser.find_element(By.ID, "addNewRecordButton").click()

persons = {
    'firstName': "Egor",
    'lastName': "Petrov",
    'userEmail': "egorik@mail.ru",
    'age': "19",
    'salary': "20000",
    'department': "AutoDesker"
}

for selector, person in persons.items():
    browser.find_element(By.ID, selector).send_keys(person)

browser.find_element(By.CSS_SELECTOR, "#submit").click()
browser.find_element(By.CSS_SELECTOR, "#searchBox").send_keys("egor")
browser.find_element(By.ID, "delete-record-4").click()
Select(browser.find_element(By.CSS_SELECTOR, '[aria-label="rows per page"]')).select_by_value("50")

browser.quit()