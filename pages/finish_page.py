from stepik_autotest_project.base.base_class import Base


class FinishPage(Base):
    base_url = 'https://www.saucedemo.com/checkout-complete.html'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_driver(self):
        return self.driver

    # Locators

    # Getters

    # Actions

    # Methods

    def check_finish(self):
        """Check finish page"""
        self.get_current_url()
        self.assert_url(self.base_url)
        self.make_screenshot()
