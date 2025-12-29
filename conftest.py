import pytest
import allure
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Выбор браузера: chrome или firefox"
    )


@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("--browser")
    
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
    
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    
    else:
        raise ValueError(f"Неподдерживаемый браузер: {browser_name}")
    
    driver.implicitly_wait(10)
    driver.maximize_window()
    
    yield driver
    
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
