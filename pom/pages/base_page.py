"""
This class stores locators that are common to many pages
"""


class BasePage:
    # Navigation bar
    AUTH_BUTTON = "//div[@data-popup-handler='auth']"
    CART_BUTTON = "//div[@class = 'header-right-row']/div[contains(@class, 'header-basket')]"

    LOGO = "//div[@class = 'header-center-row']/a[contains(@class, 'logo')]"

    CART_ITEMS_COUNT = CART_BUTTON + "/*/span[contains(@class, 'header-counter')]"

    # Search
    SEARCH_BUTTON = "//div[@class = 'search-button']"
    SEARCH_FIELD = "//input[@id = 'search-input']"
    SEARCH_DIALOG_CLOSE_ICON = "//div[contains(@class, 'close-icon']"

    # Login form
    LOGIN_FORM = "//form[@id = 'form-auth']"
    EMAIL_INPUT = "//input[@id= 'login']"
    PASSWORD_INPUT = "//input[@type= 'password']"
    SUBMIT_LOGIN_BUTTON = "//button[@type= 'submit' and text() = 'Log in']"
    FORGET_PASSWORD = "//div[@data-popup-handler='forget-password']"
    REGISTRATION_LINK = "//a[@class='auth-link']"
