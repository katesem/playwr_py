#import logging

import allure
from playwright.sync_api import Page

from pom.pages.base_page import BasePage


class BasePageSteps:
    def __init__(self, page: Page):
        self.page = page
        self.locators = BasePage()
    #  self.logger = logging.getLogger(__name__)

    def _get_element(self, locator_name):
        locator = getattr(BasePage, locator_name)
        return self.page.locator(locator)

    def _verify_element_is_visible(self, locator_name):
        assert self._get_element(locator_name).is_visible(), f'Element {locator_name} is not displayed'

    @allure.step
    def click_on_the_element(self, element_name: str):
        self._verify_element_is_visible(element_name)
        self._get_element(element_name).click()
        self._verify_element_is_visible(element_name)
        return self