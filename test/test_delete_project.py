# -*- coding: utf-8 -*-
from model.project import Project
import random


def test_delete_project(app):
    if len(app.project.get_project_list()) == 0:
        app.project.create(Project(name="new project", description="some description"))
    old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project_by_name(project.name)
    new_projects = app.project.get_project_list()
    old_projects.remove(project)
    assert old_projects == new_projects