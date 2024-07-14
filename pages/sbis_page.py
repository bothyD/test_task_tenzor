from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from time import sleep

button_contact = (By.CLASS_NAME, 'sbisru-Header__menu-item.sbisru-Header__menu-item-1.mh-8.s-Grid--hide-sm')

block_region = (By.CLASS_NAME, 's-Grid-container.s-Grid-container--alignBaseline.s-Grid-container--noGutter.pb-4.pb-xm-16.pr-16.pr-xm-0')
region_class = (By.CLASS_NAME, 'sbis_ru-Region-Chooser__text.sbis_ru-link')

block_partners = (By.CLASS_NAME, 'controls-BaseControl.controls_list_theme-sbisru.controls_toggle_theme-sbisru')

list_partners = (By.CLASS_NAME, 'controls-ListView__itemV-relative.controls-ListView__itemV.controls-ListView__item_default.controls-ListView__item_contentWrapper.js-controls-ListView__editingTarget.controls-ListView__itemV_cursor-pointer.controls-ListView__item_showActions.js-controls-ListView__measurableContainer.controls-ListView__item__unmarked_default.controls-ListView__item_highlightOnHover.controls-hover-background-default.controls-Tree__item')
block_regions = (By.CLASS_NAME, 'sbis_ru-Region-Panel__list-l')
lisst_regions = (By.CLASS_NAME, 'sbis_ru-Region-Panel__item')

class SibsPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self, link):
        self.browser.get(link)

    def button_contacts(self):
        return self.find(button_contact)
    
    def button_contacts_click(self):
        return self.button_contacts().click()

    def go_to_contacts(self):
        self.open('https://sbis.ru/')
        self.button_contacts_click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.presence_of_element_located(block_region))

    def change_region(self):
        self.go_to_contacts()
        currentRegion = self.find(block_region)
        self.find_element_from_block(currentRegion, region_class).click()
        regions = self.find(block_regions)
        all_regions = self.find_elements_from_block(regions, lisst_regions)
        for el in all_regions:
            if el.text == '41 Камчатский край':
                el.click()
                break
               

    def check_region(self):
        self.go_to_contacts()
        currentRegion = self.find(block_region)
        region = self.find_element_from_block(currentRegion, region_class)
        return region.text
    
    def check_list_partners(self):
        self.go_to_contacts()
        check_list = self.find(block_partners)
        result_list = self.find_elements_from_block(check_list, list_partners)
        print(result_list)
        if len(result_list) > 1:
            return True
        else:
            return False
        
    def check_title(self):
        self.change_region()
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.title_contains("Камчатский"))
        current_title = self.browser.title
        return current_title
    
    def check_url(self):
        self.change_region()
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.title_contains("Камчатский"))
        current_title = self.browser.current_url
        return current_title

    def check_new_region(self):
        self.change_region()
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.title_contains("Камчатский"))
        currentRegion = self.find(block_region)
        region = self.find_element_from_block(currentRegion, region_class)
        return region.text
    
    def check_new_partners(self):
        self.change_region()
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.title_contains("Камчатский"))
        check_list = self.find(block_partners)
        result_list = self.find_elements_from_block(check_list, list_partners)
        print(result_list)
        if len(result_list) > 1:
            return True
        else:
            return False
    

    