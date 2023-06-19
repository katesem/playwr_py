import allure

@allure.feature("Homepage")
@allure.description("Test case 1: Click on the button")
def test_auth_button_click(homepage_fixture):
    homepage_fixture.click_on_the_element("AUTH_BUTTON")
