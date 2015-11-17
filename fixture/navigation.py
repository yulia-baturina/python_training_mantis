__author__ = 'IEUser'


class NavigationHelper:

    def __init__(self, app):
        self.app = app
        self.baseUrl = app.baseUrl

    def is_login_page_opened(self):
        wd = self.app.wd
        return wd.current_url.endswith("mantisbt/login_page.php")

    def open_login_page(self):
        wd = self.app.wd
        if not self.is_login_page_opened():
            wd.get(self.baseUrl)