from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def test_navigate_to_carta_com():
    driver = webdriver.Chrome(
                    service=ChromeService(ChromeDriverManager().install())
                )
    driver.get("https://carta.com")
    assert driver.title == "Carta | Equity Management Solutions"
    assert "Carta" in driver.title