__author__ = 'IEUser'

from model.project import Project
import re

class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def fill_in_fields(self, project):
        wd = self.app.wd
        self.fill_in_field("name", project.name)
        self.fill_in_field("description", project.description)

    def fill_in_field(self, fieldName, fieldValue):
        wd = self.app.wd
        if fieldValue is not None:
            wd.find_element_by_name(fieldName).click()
            wd.find_element_by_name(fieldName).clear()
            wd.find_element_by_name(fieldName).send_keys(fieldValue)

    project_cache = None

    def create(self, project):
        wd = self.app.wd
        # init project creation
        self.open_create_project_page()
        # fill in project fields
        self.fill_in_fields(project)
        # submit project creation
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.return_to_manage_projects_page()
        self.project_cache = None

    def is_manage_projects_page_opened(self):
        wd = self.app.wd
        return wd.current_url.endswith("manage_proj_page.php")

    def is_create_project_page_opened(self):
        wd = self.app.wd
        return wd.current_url.endswith("manage_proj_create_page.php")

    def open_manage_projects_page(self):
        wd = self.app.wd
        if not self.is_manage_projects_page_opened():
            wd.get(self.app.baseUrl+"manage_proj_page.php")

    def return_to_manage_projects_page(self):
        wd = self.app.wd
        if not self.is_manage_projects_page_opened():
            wd.find_element_by_link_text("Proceed").click()

    def open_create_project_page(self):
        wd = self.app.wd
        self.open_manage_projects_page()
        if not self.is_create_project_page_opened():
            wd.find_element_by_xpath("//input[@value='Create New Project']").click()

    def get_project_list(self):
        if self.project_cache is None:
           wd = self.app.wd
           self.open_manage_projects_page()
           self.project_cache = []
           for element in wd.find_elements_by_xpath("//a[contains(@href,'manage_proj_edit_page')]/../.."):
               name = element.find_element_by_tag_name("a").text
               description = element.find_elements_by_tag_name("td")[4].text
               self.project_cache.append(Project(name=name, description=description))
        return list(self.project_cache)

    def delete_project_by_name(self, name):
        wd = self.app.wd
        # select project by name
        wd.find_element_by_xpath("//a[contains(text(),'%s')]" % name).click()
        # submit deletion
        wd.find_element_by_xpath("//*[@value='Delete Project']").click()
        wd.find_element_by_xpath("//*[@value='Delete Project']").click()
        self.project_cache=None

