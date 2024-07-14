from pages.download_page import DownloadPage
import pytest


@pytest.mark.skip('Not completed')
def test_check_size_downloaded_file(browser):
    downloadPage = DownloadPage(browser)
    downloadPage.download_web_installer()
    assert 1 == 2