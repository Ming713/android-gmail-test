from common.driver_manager import DriverManager

# some initialized activities or methods can be organized here before entering each page object.

class BasicPage:

    def __init__(self, driver=None):
        if driver is None:
            driver = DriverManager.start_appium_in_local()
        self.driver = driver

    def quit(self):
        self.driver.quit()

