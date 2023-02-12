from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
url = 'https://www.placardefutebol.com.br/'
driver.get(url)

livescore = driver.find_element(By.ID, 'livescore')
container = livescore.find_elements(By.CLASS_NAME, 'container content trending-box')
if container:
    data = container.find_elements(By.CLASS_NAME, 'row align-items-center content')
    for n in data:
        jogo = n.find_elements(By.CLASS_NAME, 'w-25 p-1 status text-center')
        for j in jogo:
            span = j.find_element(By.CLASS_NAME, 'badge badge-danger status-name')
            print(span)
            if span:
                link = container.find_element(By.TAG_NAME, 'a')
                print('oii')
                print(link.get_attribute('href'))

driver.quit()