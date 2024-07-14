from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os

from time import sleep
block_footer = (By.CLASS_NAME, 'sbisru-Footer__container')

list_footer = (By.CLASS_NAME, 'sbisru-Footer__link')

block_download = (By.CLASS_NAME, 'sbis_ru-DownloadNew-block.sbis_ru-DownloadNew-flex')
text_download = (By.CLASS_NAME, 'sbis_ru-DownloadNew-h3')
button_download = (By.CLASS_NAME, 'sbis_ru-DownloadNew-loadLink__link.js-link')
element_download = (By.CLASS_NAME, '')

class DownloadPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
    
    def go_to_download(self):
        self.browser.get('https://sbis.ru/')
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.presence_of_element_located(block_footer))
        footer_block = self.find(block_footer)
        footer_elements = self.find_elements_from_block(footer_block, list_footer)
        for el in footer_elements:
            if el.text == 'Скачать локальные версии':
                el.click()
                break
        sleep(5)

    def download_web_installer(self):
        self.go_to_download()
        elements_footer =  self.find_elements_from_block(self.browser, block_download)
        for el in elements_footer:
            current_el = self.find_element_from_block(el, text_download)
            if current_el.text == 'Веб-установщик':
                finded_el = self.find_element_from_block(el, button_download)
                print(finded_el.text)
                finded_el.click()
        sleep(15)
        return
    # def test_download_web_installer(self):
        self.download_web_installer()
        files = os.listdir(self.download_dir)
        assert len(files) > 0, "Файл не был загружен"
        downloaded_file = os.path.join(self.download_dir, files[0])
        expected_size = 123456  # Ожидаемый размер файла в байтах
        actual_size = os.path.getsize(downloaded_file)
        assert actual_size == expected_size, f"Размер файла не соответствует. Ожидалось: {expected_size}, Получено: {actual_size}"



    

