# -*- coding: utf-8 -*-
from model.project import Project
from fixture.stringUtils import StringsHelper


def test_add_project(app):
    new_project = Project(name=StringsHelper.randomstring("name", 10), description=StringsHelper.randomstring("description", 20))
    old_projects = app.project.get_project_list()
    app.project.create(new_project)
    new_projects = app.project.get_project_list()
    old_projects.append(new_project)
    assert sorted(new_projects, key=Project.name) == sorted(old_projects, key=Project.name)