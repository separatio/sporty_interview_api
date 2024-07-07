from seleniumbase import BaseCase
import time
BaseCase.main(__name__, __file__)


class TestSimpleLogin(BaseCase):
    def test_simple_login(self):
        self.open("https://twitch.tv")
        # self.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        # Accept cookies
        self.wait_for_element("button[data-a-target='consent-banner-accept']")
        self.click("button[data-a-target='consent-banner-accept']")

        self.click("[aria-label='Search']")

        search_input_locator = "[placeholder='Search...']"
        self.wait_for_element(search_input_locator)
        self.type(search_input_locator, "Starcraft II")

        self.click("[title='StarCraft II']")
        self.assert_text_visible("Follow")

        # Below this is still not working; need to fix
        self.scroll_to_bottom()
        self.scroll_to_bottom()

        streamer_elements = self.find_visible_elements("article")
        streamer_elements[2].click()
        # In case an alert is shown, dismiss it
        # Does not work for modals
        # self.dismiss_alert()

        # In case a modal pops up, close it
        # The locator is not correct most likely
        # Assuming that the close button has the same kind of locator
        # self.click("button[data-a-target='modal-close-button']")

        streamer_url = str(time.time())
        self.assert_element_visible("[data-a-target='follow-button']")
        self.save_screenshot(name=streamer_url, folder="./screenshots")
