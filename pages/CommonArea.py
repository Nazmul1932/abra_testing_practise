import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CommonAreas:
    buildings_menu_by_xpath = "(//a[@href='/buildings'])[1]"
    click_common_areas_submenu_by_xpath = "//span[normalize-space()='Common Areas']"
    click_common_areas_button_by_css_selector = ".ml-3"
    select_building_type_id = 'buildingType'
    building_name_xpath = "//li[@aria-label='"
    area_name_by_xpath = "//input[@id='areaName']"
    save_area_button_by_xpath = "//button[normalize-space()='Save Area']"
    all_buildings_xpath = "//ul[@role='listbox']//li"
    search_field_by_xpath = "//input[@placeholder='Search']"
    click_building_all_by_xpath = "//div[@class='p-multiselect-label p-placeholder'][normalize-space()='Buildings (All)']"
    return_area_name_by_xpath = "//td[normalize-space()='"
    return_building_name_by_xpath = "//span[normalize-space()='"
    aria_level_xpath = "//li[@aria-label='"
    checkbox_component_xpath = "']//div[@class='p-checkbox p-component']"


    def __init__(self, driver):
        self.driver = driver

    def click_on_buildings_menu(self):
        bldngs_menu = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.buildings_menu_by_xpath)))
        self.driver.execute_script("arguments[0].click();", bldngs_menu)

    def click_common_areas_submenu(self):
        cmn_area_sb_menu = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.click_common_areas_submenu_by_xpath)))
        self.driver.execute_script("arguments[0].click();", cmn_area_sb_menu)

    def click_common_areas_button(self):
        cmn_area_btn = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.click_common_areas_button_by_css_selector)))
        self.driver.execute_script("arguments[0].click();", cmn_area_btn)

    def get_all_buildings(self):
        slct_bldng_type = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, self.select_building_type_id)))
        self.driver.execute_script("arguments[0].click();", slct_bldng_type)
        time.sleep(5)
        all_buildings = self.driver.find_elements(By.XPATH, self.all_buildings_xpath)
        buildings = []
        for building in all_buildings:
            buildings.append(building.text)
        return buildings

    def selectBuildingType(self, buildingName):
        self.driver.implicitly_wait(20)
        buildingType = self.building_name_xpath + buildingName + "']"
        self.driver.find_element(By.XPATH, buildingType).click()

    def set_area_name(self, area_name):
        self.driver.find_element(By.XPATH, self.area_name_by_xpath).send_keys(area_name)

    def click_save_area_btn(self):
        save_btn = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.save_area_button_by_xpath)))
        self.driver.execute_script("arguments[0].click();", save_btn)

    def search_common_area(self, name_k):
        self.driver.find_element(By.XPATH, self.search_field_by_xpath).send_keys(name_k)
        self.driver.implicitly_wait(20)

    def click_buildings_all_Box(self):
        self.driver.find_element(By.XPATH, self.click_building_all_by_xpath).click()

    def return_area_name(self, area_name):
        time.sleep(5)
        element = self.driver.find_element(By.XPATH, self.return_area_name_by_xpath+area_name+"']")
        return element.text

    def return_building_name(self, building_name):
        time.sleep(5)
        element = self.driver.find_element(By.XPATH, self.return_building_name_by_xpath+building_name+"']")
        return element.text

    def click_building_name(self, building_name):
        time.sleep(5)
        element = self.driver.find_element(By.XPATH, self.aria_level_xpath+building_name+self.checkbox_component_xpath)
        return element.click()
