from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep
                                        
def main():
    browser = webdriver.Chrome()

    browser.get(' https://sbis.ru/')
    wait = WebDriverWait(browser, 10)
    click_contact = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'sbisru-Header__menu-item.sbisru-Header__menu-item-1.mh-8.s-Grid--hide-sm')))
    click_contact.click()
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'sbisru-Contacts__logo-tensor.mb-12')))
    # Получаем URL изображения
    click_tenzor = browser.find_element(By.CLASS_NAME, "sbisru-Contacts__logo-tensor.mb-12")
    link_tenzor = click_tenzor.get_attribute('href')
    browser.get(link_tenzor)
    
    block_about = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'tensor_ru-Index__block4-content.tensor_ru-Index__card')))
    click_about = block_about.find_element(By.CLASS_NAME, 'tensor_ru-link.tensor_ru-Index__link')
    browser.execute_script("arguments[0].click();", click_about)
    
    block_work = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'tensor_ru-container.tensor_ru-section.tensor_ru-About__block3')))
    all_images = block_work.find_elements(By.CLASS_NAME, 'tensor_ru-About__block3-image.new_lazy.loaded')
    # for image in all_images:
    #     image_width = image.get_attribute('width')
    #     image_height = image.get_attribute('height')
    #     if image_height > image_width:
    #         sleep(15)
        
   

if __name__=="__main__":
    main()