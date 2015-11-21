__author__ = 'IEUser'
import pytest
import json
import os.path
import ftputil
from fixture.application import Application

fixture = None
target = None

def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target

@pytest.fixture(scope="session")
def config(request):
    return load_config(request.config.getoption("--target"))

@pytest.fixture
def app(request, config):
    global fixture
    browser = request.config.getoption("--browser")

    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, config=config)
    fixture.session.ensure_login(username=config['web']['username'], password=config['web']['password'])

    return fixture

@pytest.fixture(scope="session", autouse=True)
def configure_server(request, config):
    install_server_configuration(config['ftp']['host'],config['ftp']['username'],config['ftp']['password'])
    def fin():
        restore_server_configuration(config['ftp']['host'],config['ftp']['username'],config['ftp']['password'])
    request.addfinalizer(fin)

def install_server_configuration(host,username,password):
    with ftputil.FTPHost(host,username,password) as remote:
        if remote.path.isfile("config.inc.php.back"):
            remote.remove("config.inc.php.back")
        if remote.path.isfile("config.inc.php"):
            remote.rename("config.inc.php","config.inc.php.back")
        remote.upload(os.path.join(os.path.dirname(__file__), "resources/config.inc.php"), "config.inc.php")

def restore_server_configuration(host,username,password):
    with ftputil.FTPHost(host,username,password) as remote:
        if remote.path.isfile("config.inc.php.back"):
            if remote.path.isfile("config.inc.php"):
                remote.remove("config.inc.php")
            remote.rename("config.inc.php.back","config.inc.php")

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()

    # using request.addfinalizer(fixture.destroy()) causes method destroy()
    # to be invoked right in the set up, so additional function fin() was added to avoid that
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
