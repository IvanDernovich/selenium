import unittest
from selenium import webdriver
from POMObject.Pages.onlinerMainPage import onlinerMainPage
from POMObject.Pages.onlinerSearchFrame import onlinerSearchFrame


class SearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='E://chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_page(self):
        #
        # initialize driver and open URL
        #
        driver = self.driver
        driver.get(onlinerMainPage.URL)
        #
        # assert page title
        #
        self.assertIn(onlinerMainPage.ASSERT_TITLE, driver.title)
        #
        # insert TEXT find element
        #
        searchBox = onlinerMainPage(driver)
        searchBox.enter_text_search_bar(onlinerMainPage.ENTER_TEXT)
        #
        # iframe switch
        #
        frame_identify = onlinerSearchFrame(driver)
        frame_identify.goto_search_frame()
        #
        # collect massive of result page
        #
        # selectedElement = onlinerSearchFrame(driver)
        # selectedElement.result_of_search(0)
        massiveSearchResult = driver.find_elements_by_xpath('//*[@class="result__item result__item_product"]')

        #        if len(massiveSearchResult) > 0:
        link = massiveSearchResult[0].find_element_by_xpath('.//*[@class="product__title"]').click()
        #        else:
        #            print('No one obj found')
        # self.assertIn(OnlinerMainPages.ASSERT_PAGE_SOURCE, OnlinerMainPages.check_assertion_source())
        assert "Apple iPhone 11 64GB (черный)" in driver.page_source

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test teardown')


if __name__ == '__main__':
    unittest.main()
