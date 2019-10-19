class onlinerSearchFrame():

    def __init__(self, driver):
        self.driver = driver

        self.changeFrame = '//iframe[@class="modal-iframe"]'
        self.findMassiveResult = '//*[@class="result__item result__item_product"]'
        self.selectMassiveElement = './/*[@class="product__title"]'

    def goto_search_frame(self):
        frameID = self.driver.find_element_by_xpath(self.changeFrame)
        self.driver.switch_to.frame(frameID)

    #def result_of_search(self, select_item):
    #   self.driver.find_elements_by_xpath(self.findMassiveResult)
    #   self.driver.find_elements_by_xpath(self.selectMassiveElement['select_item'])