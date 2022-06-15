from selenium import webdriver

browser=webdriver.Firefox(executable_path=r'/usr/local/bin/geckodriver')
browser.get("http://127.0.0.1:8000")

header_text = browser.find_element(value='h1').text

assert 'Lista do zrobienia' in browser.title
assert 'Zadanie numer 3' in header_text