import pytest
import time
from pages.dashboard import Dashboard
from utilities.utils import Utils
import allure
from allure_commons.types import AttachmentType


@pytest.mark.usefixtures("setup")
class TestDashboard:
    log = Utils.custom_logger()

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.dashboard = Dashboard(self.driver)

    def test_dashboard(self):
        self.log.info("Test dashboard Started")
        time.sleep(5)
        dashboard_title = self.driver.title
        print(dashboard_title)
        if dashboard_title == "Dashboard - Admin Panel | Abra Web Portal":
            assert True
        else:
            assert False
        self.log.info("Test dashboard completed")

    def test_dashboard_checking_water(self):
        self.log.info("Test dashboard using Checking water Text Started")
        water = self.dashboard.check_water_text()
        if water == "Water":
            assert True
        else:
            assert False
        self.log.info("Test dashboard using Checking water Text Completed")

    def test_dashboard_checking_alarm(self):
        self.log.info("Test dashboard using Checking alarm Text Started")
        alarm = self.dashboard.check_alarm_text()
        if alarm == "Alarm":
            assert True
        else:
            assert False
        self.log.info("Test dashboard using Checking alarm Text Completed")

    def test_dashboard_checking_fire(self):
        self.log.info("Test dashboard using Checking Fire Text Started")
        fire = self.dashboard.check_fire_text()
        if fire == "Fire":
            assert True
        else:
            assert False
        self.log.info("Test dashboard using Checking Fire Text Completed")

    def test_dashboard_checking_hub(self):
        self.log.info("Test dashboard using Checking Hub Text Started")
        hub = self.dashboard.check_hub_text()
        if hub == "Hub":
            assert True
        else:
            assert False
        self.log.info("Test dashboard using Checking Hub Text Completed")

    def test_dashboard_using_date(self):
        self.log.info("Test dashboard using Checking Date Started")
        exp_date, current_date = self.dashboard.check_current_date()
        if current_date == exp_date:
            assert True
        else:
            assert False
        self.log.info("Test dashboard using Checking Date Completed")

    def test_dashboard_clicking_connect_hubs_to_homes(self):
        self.log.info("Test dashboard By Clicking Connect Hubs to Homes Started")
        time.sleep(5)
        self.dashboard.click_on_connect_hubs_to_homes()
        dashboard_url_hubs_to_homes = self.driver.title
        if dashboard_url_hubs_to_homes == "Devices - Admin Panel | Abra Web Portal":
            assert True
        else:
            assert False
        self.log.info("Test dashboard By Clicking Connect Hubs to Homes Completed")

    def test_dashboard_using_invite_home_owners(self):
        self.log.info("Test dashboard By Clicking Invite Home Owners Started")
        time.sleep(5)
        self.driver.back()
        self.dashboard.click_on_invite_home_owners()
        dashboard_url_by_home_owners = self.driver.title
        if dashboard_url_by_home_owners == "Users - Admin Panel | Abra Web Portal":
            assert True
        else:
            assert False
        self.log.info("Test dashboard By Clicking Invite Home Owners Completed")

    def test_dashboard_using_register_buildings(self):
        self.log.info("Test dashboard By Clicking Register Buildings Started")
        time.sleep(5)
        self.driver.back()
        self.dashboard.click_on_register_buildings()
        add_buildings_url_by_register_buildings = self.driver.title
        if add_buildings_url_by_register_buildings == "Add Building - Admin Panel | Abra Web Portal":
            assert True
        else:
            assert False
        self.log.info("Test dashboard By Clicking Register Buildings Completed")

    def test_dashboard_using_register_homes(self):
        self.log.info("Test dashboard By Clicking Register Homes Started")
        time.sleep(5)
        self.driver.back()
        self.dashboard.click_on_register_homes()
        dashboard_url_by_home_owners = self.driver.title
        if dashboard_url_by_home_owners == "Homes - Admin Panel | Abra Web Portal":
            assert True
        else:
            assert False
        self.log.info("Test dashboard By Clicking Register Homes Completed")

