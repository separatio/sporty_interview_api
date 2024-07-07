from support.base_test_case import BaseTestCase
from support.pages.home_page import HomePage
from support.pages.page import Page
from support.pages.search_results_page import SearchResultsPage
from support.pages.streamer_page import StreamerPage
import time


BaseTestCase.main(__name__, __file__)


class TestSimpleLogin(BaseTestCase):
    def test_simple_login(self):
        self.open("https://twitch.tv")

        # Accept cookies
        self.wait_for_element_visible(Page.accept_cookies_button)
        self.click(Page.accept_cookies_button)

        self.click(HomePage.search_button)
        self.wait_for_element_visible(HomePage.search_input)
        self.type(HomePage.search_input, "Starcraft II")

        self.click(Page.get_locator_by_title(topic="StarCraft II"))
        self.assert_text_visible("Follow")

        # Scroll down twice
        self.scroll_to_bottom()
        self.wait_for_ready_state_complete()

        self.scroll_to_bottom()
        self.wait_for_ready_state_complete()

        streamer_elements = self.find_visible_elements(SearchResultsPage.results)
        streamer_elements[2].click()
        # In case an alert is shown, dismiss it
        # Does not work for modals
        # self.dismiss_alert()

        # In case a modal pops up, close it
        # The locator is not correct most likely
        # Assuming that the close button has the same kind of locator
        # self.click("button[data-a-target='modal-close-button']")

        streamer_url = str(time.time())
        self.assert_element_visible(StreamerPage.follow_button)
        self.save_screenshot(name=streamer_url, folder="./screenshots")
