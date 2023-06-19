# there can be located global tests fixtures
import allure
from playwright.sync_api import Playwright
from pytest import fixture

from pom.steps.base_page_steps import BasePageSteps


@fixture(scope='module')
def browser_fixture(playwright: Playwright):
    with playwright.chromium.launch(headless=False) as browser:
        with browser.new_context() as context:
            with context.new_page() as page:
                page.goto('https://makeupstore.com/')
                page.wait_for_load_state("load")
                yield page


@fixture(scope='module')
def homepage_fixture(browser_fixture):
    base_page = BasePageSteps(browser_fixture)
    yield base_page