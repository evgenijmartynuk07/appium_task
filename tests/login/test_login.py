
import pytest


@pytest.mark.parametrize(
    'username, password, expected',
    [
        ('qa.ajax.app.automation@gmail.com', 'qa_automation_password', True),
        ('qa.ajax.app.automation@gmail.com', 'qa_automation_password', True),
    ]
)
def test_valid_user_login_and_logout(
        user_login_fixture,
        username,
        password,
        expected,
        test_logger
):
    test_logger.info(f'Attempting login for user: {username}')
    user_login_fixture.login(username, password)
    assert user_login_fixture.is_logged_in() == expected
    test_logger.info('Login successful.')

    test_logger.info(f'Attempting logout for user: {username}')
    user_login_fixture.logout()
    assert not user_login_fixture.is_logged_in()
    test_logger.info('Logout successful.')
    test_logger.info('Test passed\n')


@pytest.mark.parametrize(
    'username, password, expected',
    [
        ('example@gmail.com', 'qa_automation_password', False),
        ('a', 's', False),
        ('python@gmail.com', 'python1234', False),
    ]
)
def test_invalid_user_login(
        user_login_fixture,
        username,
        password,
        expected,
        test_logger
):
    test_logger.info(f'Attempting login for user: {username}')
    user_login_fixture.login(username, password)
    assert user_login_fixture.is_logged_in() == expected
    test_logger.info('Login failed as expected.')

    user_login_fixture.get_back()
    test_logger.info('Test passed.\n')
