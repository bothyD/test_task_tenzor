from pages.tenzor_page import StartPage
import pytest

@pytest.mark.promt1
def test_power_people_exist(browser):
    start_page = StartPage(browser)
    start_page.go_to_tenzor()
    assert start_page.block_power_of_people_is_displayed()

@pytest.mark.promt1
def test_check_width_hight(browser):
    start_page = StartPage(browser)
    start_page.go_to_tenzor()
    assert start_page.check_width_hight()

