from selenium.webdriver.common.by import By
from utilities.logger import get_logger
from utilities.config_reader import get_config

logger = get_logger(__name__)
config = get_config()

def test_valid_login(setup):
    logger.info("Valid login test started")

    # siteye git
    setup.get("https://the-internet.herokuapp.com/login")

    # kullanıcı adı gir
    setup.find_element(By.ID, "username").send_keys("tomsmith")

    # şifre gir
    setup.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

    # giriş butonuna tıkla
    setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # başarı mesajı doğrulaması
    success_msg = setup.find_element(By.ID, "flash").text
    assert "You logged into a secure area!" in success_msg

    logger.info("Valid login test passed")
