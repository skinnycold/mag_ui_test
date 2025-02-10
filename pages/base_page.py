from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    current_page = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self):
        if self.current_page:
            self.driver.get(self.base_url + self.current_page)
        else:
            raise NotImplementedError('Current page is empty')

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)