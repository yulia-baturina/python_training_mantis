# -*- coding: utf-8 -*-
from model.project import Project
from fixture.stringUtils import StringsHelper


def test_add_project(app):
    username = app.config['web']['username']
    password = app.config['web']['password']
    new_project = Project(name=StringsHelper.randomstring("name", 10), description=StringsHelper.randomstring("description", 20))
    app.session.ensure_login(username=username, password=password)
    old_projects = app.project.convert_projects_data_to_projects(app.soap.get_projects_list(username, password))
    app.project.create(new_project)
    new_projects = app.project.convert_projects_data_to_projects(app.soap.get_projects_list(username, password))
    old_projects.append(new_project)
    assert sorted(new_projects, key=Project.name) == sorted(old_projects, key=Project.name)