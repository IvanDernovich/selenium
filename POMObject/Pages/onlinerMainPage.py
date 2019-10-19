class onlinerMainPage():
    ASSERT_TITLE = 'Onliner'
    URL = 'https://www.onliner.by'
    ENTER_TEXT = 'iPhone'
    ASSERT_PAGE_SOURCE = 'Apple iPhone 11 64GB (черный)'

    def __init__(self, driver):
        self.driver = driver
        self.search_bar = 'fast-search__input'
        self.assertion_of_page_title = driver.title
        self.assertion_of_page_source = driver.page_source

    def enter_text_search_bar(self, ENTER_TEXT):
        self.driver.find_element_by_class_name(self.search_bar).clear()
        self.driver.find_element_by_class_name(self.search_bar).send_keys(ENTER_TEXT)

    def check_assertion(self):
        msg = self.assertion_of_page_title
        return msg

    def check_assertion_source(self):
        assertion_page_source = self.assertion_of_page_source
        return assertion_page_source
