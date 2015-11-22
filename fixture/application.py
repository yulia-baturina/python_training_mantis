__author__ = 'IEUser'

from selenium import webdriver
from fixture.session import SessionHelper
from fixture.navigation import NavigationHelper
from fixture.project import ProjectHelper
from fixture.james import JamesHelper
from fixture.signup import SignupHelper
from fixture.mail import MailHelper
from fixture.soap import SoapHelper


class Application:
    def __init__(self, browser, config):
        if browser=="firefox":
            self.wd = webdriver.Firefox()
        elif browser=="chrome":
            self.wd = webdriver.Chrome()
        elif browser=="ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s " % browser)
        self.james = JamesHelper(self)
        self.config = config
        self.baseUrl = config['web']['baseUrl']
        self.session = SessionHelper(self)
        self.navigation = NavigationHelper(self)
        self.project = ProjectHelper(self)
        self.signup = SignupHelper(self)
        self.mail = MailHelper(self)
        self.soap = SoapHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def accept_alert(self):
        wd = self.wd
        try:
            wd.switch_to_alert().accept()
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()