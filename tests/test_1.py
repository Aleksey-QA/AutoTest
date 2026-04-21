from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

BASE_URL = "http://localhost:3000"
SUBSCRIPTION = f"{BASE_URL}/automation-lab/cards"


def test_load_cards():
    opts = Options()

    opts.add_argument("--window-size=1280,900")
    driver = webdriver.Chrome(options=opts)

    driver.get(SUBSCRIPTION)

    button = driver.find_element(By.CSS_SELECTOR, "button.trigger-btn")
    assert button.is_displayed()