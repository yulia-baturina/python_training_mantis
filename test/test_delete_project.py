# -*- coding: utf-8 -*-
from model.project import Project
import random


def test_delete_project(app):
    username = app.config['web']['username']
    password = app.config['web']['password']
    app.session.ensure_login(username=username, password=password)
    if len(app.project.convert_projects_data_to_projects(app.soap.get_projects_list(username, password))) == 0:
        app.project.create(Project(name="new project", description="some description"))
    old_projects = app.project.convert_projects_data_to_projects(app.soap.get_projects_list(username, password))
    project = random.choice(old_projects)
    app.project.delete_project_by_name(project.name)
    new_projects = app.project.convert_projects_data_to_projects(app.soap.get_projects_list(username, password))
    old_projects.remove(project)
    assert old_projects == new_projects