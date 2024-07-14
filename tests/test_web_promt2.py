from pages.sbis_page import SibsPage

def test_check_current_region(browser):
    sibsPage = SibsPage(browser)
    current_region = sibsPage.check_region()
    assert current_region == "Новосибирская обл."

def test_check_partners(browser):
    sibsPage = SibsPage(browser)
    assert sibsPage.check_list_partners()

def test_check_title_after_change_region(browser):
    sibsPage = SibsPage(browser)
    assert sibsPage.check_title() == 'СБИС Контакты — Камчатский край'

def test_check_url_after_change_region(browser):
    sibsPage = SibsPage(browser)
    assert sibsPage.check_url() == 'https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients'

def test_check_region_after_change_region(browser):
    sibsPage = SibsPage(browser)
    assert sibsPage.check_new_region() == "Камчатский край"

def test_check_partners_after_change_region(browser):
    sibsPage = SibsPage(browser)
    assert sibsPage.check_new_partners()