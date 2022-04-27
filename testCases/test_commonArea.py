import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.CommonArea import CommonAreas
from ddt import ddt, data, file_data, unpack
from utilities.utils import Utils
import pytest
import softest


@pytest.mark.usefixtures("setup")
@ddt
class TestCommonArea(softest.TestCase):
    log = Utils.custom_logger()

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.common_area = CommonAreas(self.driver)

    @data(*Utils.read_data_from_csv("/media/user/New Volume/abra_testing_practise/testData/add_common_area.csv"))
    @unpack
    def test_add_common_area(self, building_name, area_name):
        self.log.info("Add Common Area Started")
        self.common_area.click_on_buildings_menu()
        time.sleep(10)
        self.common_area.click_common_areas_submenu()
        self.common_area.click_common_areas_button()
        list_of_all_buildings = self.common_area.get_all_buildings()

        for building in list_of_all_buildings:
            if building_name in building:
                self.common_area.selectBuildingType(building_name)
                self.common_area.set_area_name(area_name)
                time.sleep(2)
                self.common_area.click_save_area_btn()
                time.sleep(2)
                self.common_area.search_common_area(area_name)
                # expected_area_name = self.driver.find_element(By.XPATH, "//td[normalize-space()='"+area_name+"']").text
                expected_area_name = self.common_area.return_area_name(area_name)
                assert area_name == expected_area_name
            else:
                continue
        self.log.info("Add Common Area Completed")

    @data(*Utils.read_data_from_csv("/media/user/New Volume/abra_testing_practise/testData/building_name.csv"))
    @unpack
    def test_commonArea_by_clicking_buildings_all(self, building_name):
        self.log.info("Testing CommonArea By Clicking Buildings All Started")
        self.driver.refresh()
        time.sleep(5)
        self.common_area.click_buildings_all_Box()
        # expected_building_name = self.driver.find_element(By.XPATH, "//span[normalize-space()='"+building_name+"']").text
        expected_building_name = self.common_area.return_building_name(building_name)
        if building_name == expected_building_name:
            # self.driver.find_element(By.XPATH, "//li[@aria-label='"+building_name+"']//div[@class='p-checkbox p-component']").click()
            self.common_area.click_building_name(building_name)
            self.log.info("Testing CommonArea By Clicking Buildings All Completes")
        else:
            self.log.info("Building ta paoa jai nai")





