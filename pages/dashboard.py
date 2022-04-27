from selenium.webdriver.common.by import By
from datetime import date


class Dashboard:
    register_buildings_by_xpath = "(//img[@alt='mylogo'])[2]"
    register_homes_by_xpath = "(//img[@alt='mylogo'])[6]"
    invite_home_owners_by_xpath = "(//img[@alt='mylogo'])[4]"
    connect_hubs_to_homes_xpath = "(//img[@alt='mylogo'])[8]"
    water_text_by_xpath = "//p[normalize-space()='Water']"
    alarm_text_by_xpath = "//p[normalize-space()='Alarm']"
    fire_text_by_xpath = "//p[normalize-space()='Fire']"
    hub_text_by_xpath = "//p[normalize-space()='Hub']"
    current_date_xpath = "//h3[normalize-space()='"

    def __init__(self, driver):
        self.driver = driver

    def click_on_connect_hubs_to_homes(self):
        self.driver.find_element(By.XPATH, self.connect_hubs_to_homes_xpath).click()

    def click_on_register_buildings(self):
        self.driver.find_element(By.XPATH, self.register_buildings_by_xpath).click()

    def click_on_invite_home_owners(self):
        self.driver.find_element(By.XPATH, self.invite_home_owners_by_xpath).click()

    def click_on_register_homes(self):
        self.driver.find_element(By.XPATH, self.register_homes_by_xpath).click()

    def check_water_text(self):
        return self.driver.find_element(By.XPATH, self.water_text_by_xpath).text

    def check_alarm_text(self):
        return self.driver.find_element(By.XPATH, self.alarm_text_by_xpath).text

    def check_fire_text(self):
        return self.driver.find_element(By.XPATH, self.fire_text_by_xpath).text

    def check_hub_text(self):
        return self.driver.find_element(By.XPATH, self.hub_text_by_xpath).text

    def check_current_date(self):
        today = date.today()
        current_date = today.strftime("%d %B %Y").lstrip("0").replace(" 0", " ")
        return self.driver.find_element(By.XPATH, self.current_date_xpath + current_date + "']").text, current_date
