import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as chrome_service
from selenium.webdriver.firefox.service import Service as firefox_service
from selenium.webdriver.edge.service import Service as edge_service


driver = None


@pytest.fixture(scope="class", autouse=True)
def setup(request, browser, url):
    global driver
    if browser == "chrome":
        driver = webdriver.Chrome(service=chrome_service(ChromeDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=firefox_service(GeckoDriverManager().install()))
    elif browser == "edge":
        driver = webdriver.Edge(service=edge_service(EdgeChromiumDriverManager().install()))

    # driver.get("https://dev.portal.abrahome.com/")

    # driver.maximize_window()
    driver.get(url)
    driver.find_element(By.ID, "email").send_keys("***********")
    driver.find_element(By.ID, "password").send_keys("**********")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    request.cls.driver = driver
    yield
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")


@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="class", autouse=True)
def url(request):
    return request.config.getoption("--url")


def pytest_html_report_title(report):
    report.title = "Abra Automation Report"
