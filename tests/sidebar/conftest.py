import pytest


from framework.sidebar_page import SideBar


@pytest.fixture(scope='session')
def sidebar_fixture(driver):
    yield SideBar(driver)


@pytest.fixture(scope='session')
def sidebar_fixture_logged(sidebar_fixture):
    username = 'qa.ajax.app.automation@gmail.com'
    password = 'qa_automation_password'

    sidebar_fixture.login(username=username, password=password)
