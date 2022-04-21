from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://demoqa.com/')

browser.find_element_by_class_name('card-body').click()
browser.find_element_by_id('item-1').click()

actions = [
    "[aria-label='Toggle']", 
    "#tree-node > ol > li > ol > li:nth-child(2) > span > button", 
    "#tree-node > ol > li > ol > li:nth-child(2) > ol > li:nth-child(2) > span > button",
    "[for='tree-node-general']",
    "[aria-label='Collapse all']"
    ]

for action in actions:
    browser.find_element_by_css_selector(action).click()
