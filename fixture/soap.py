from suds.client import Client
from suds import WebFault

class SoapHelper:
    def __init__(self, app):
        self.app = app
        self.client = Client("http://localhost:8080/mantisbt/api/soap/mantisconnect.php?wsdl")

    def can_login(self, username, password):
        try:
            self.client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_projects_list(self, username, password):
        try:
            return list(self.client.service.mc_projects_get_user_accessible(username, password))
        except WebFault:
            return None

