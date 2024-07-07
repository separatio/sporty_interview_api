from seleniumbase import BaseCase


class BaseTestCase(BaseCase):
    def setUp(self):
        super().setUp()

    def tearDown(self):
        self.save_teardown_screenshot()  # If test fails, or if "--screenshot"

        super().tearDown()
