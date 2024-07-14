from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


button_contact = (By.CLASS_NAME, 'sbisru-Header__menu-item.sbisru-Header__menu-item-1.mh-8.s-Grid--hide-sm')
button_tensor = (By.CLASS_NAME, "sbisru-Contacts__logo-tensor.mb-12")
button_about = (By.CLASS_NAME, 'tensor_ru-link.tensor_ru-Index__link')

block_power_of_people = (By.CLASS_NAME, 'tensor_ru-Index__block4-content.tensor_ru-Index__card')
block_about = (By.CLASS_NAME, 'tensor_ru-Index__block4-content.tensor_ru-Index__card')
block_work = (By.CLASS_NAME, 'tensor_ru-container.tensor_ru-section.tensor_ru-About__block3')

block_images = (By.CLASS_NAME, 's-Grid-container')
block_images1 = (By.CLASS_NAME, 's-Grid-col.s-Grid-col--3.tensor_ru-About--col-md6.tensor_ru-About__block3--col-sm12')
block_images2 = (By.CLASS_NAME, 'tensor_ru-About__block3-image.new_lazy')

class StartPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self, link):
        self.browser.get(link)

    def button_contacts(self):
        return self.find(button_contact)
    
    def button_contacts_click(self):
        return self.button_contacts().click()
    
    def button_tenzor_link(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.presence_of_element_located(button_tensor))
        return self.find(button_tensor)
    
    def link_tenzor_click(self):
        link_tenzor = self.button_tenzor_link()
        return link_tenzor.get_attribute('href')
    
    def go_to_tenzor(self):
        self.open('https://sbis.ru/')
        self.button_contacts_click()
        self.open(self.link_tenzor_click())

    def block_power_of_people_is_displayed(self):
        block_is_displayed = self.find(block_power_of_people)
        return block_is_displayed.is_displayed()
    
    def check_width_hight(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.presence_of_element_located(block_about))
        find_block_about = self.find(block_about)
        click_block_about = self.find_element_from_block(find_block_about, button_about)
        self.browser.execute_script("arguments[0].click();", click_block_about)
        
        wait.until(EC.presence_of_element_located(block_work))
        find_block_work = self.find(block_work)
        all_images = self.find_element_from_block(find_block_work, block_images)
        all_images = self.find_elements_from_block(all_images, block_images1)
        first_image = self.find_element_from_block(all_images[0], block_images2)
        for image in all_images: 
            image_size = self.find_element_from_block(image, block_images2)
            image_width = image_size.size['width']
            image_height = image_size.size['height']
            print(image_width)
            print(image_height)
            if image_width != first_image.size['width'] or image_height != first_image.size['height']:
                return False
        else:
            return True

        
    