class Page(object):
    accept_cookies_button = "button[data-a-target='consent-banner-accept']"

    def get_locator_by_title(topic):
        return f"[title='{topic}']"
