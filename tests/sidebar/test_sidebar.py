import pytest


from framework.search.locators import Locator


parameters = [
    ('settings', Locator.SETTINGS_BUTTON),
    ('help', Locator.HELP_BUTTON),
    ('logs', Locator.LOGS_BUTTON),
    ('camera', Locator.CAMERA_BUTTON),
    ('add_space', Locator.ADD_BUTTON),
]


def configure_mocks(sidebar_fixture, mocker):
    mock_find_element = mocker.patch.object(sidebar_fixture, 'find_element')
    mock_click_element = mocker.patch.object(sidebar_fixture, 'click_element')
    return mock_find_element, mock_click_element


@pytest.mark.parametrize('button_name, locator', parameters)
def test_button_find_and_click(
        sidebar_fixture,
        mocker,
        button_name,
        locator,
        test_logger
):
    test_logger.info(f'Starting test for method "{button_name}"...')
    mock_find_element, mock_click_element = configure_mocks(sidebar_fixture, mocker)
    sidebar_method = getattr(sidebar_fixture, button_name)

    sidebar_method()
    mock_find_element.assert_called_with(locator)
    mock_click_element.assert_called()
    test_logger.info('Test passed.\n')


@pytest.mark.parametrize('button_name, locator', parameters)
def test_not_button_find_and_click(
        sidebar_fixture,
        mocker,
        button_name,
        locator,
        test_logger
):
    test_logger.info(f'Starting test for method "{button_name}" with invalid arguments...')
    mock_find_element, mock_click_element = configure_mocks(sidebar_fixture, mocker)
    mock_find_element.return_value = None
    sidebar_method = getattr(sidebar_fixture, button_name)

    sidebar_method()
    mock_find_element.assert_called_with(locator)
    mock_click_element.assert_not_called()
    test_logger.info('Test passed.\n')


@pytest.mark.parametrize('button_name, locator', parameters)
def test_exists_element_in_sidebar(
        sidebar_fixture_logged,
        sidebar_fixture,
        button_name,
        locator,
        test_logger
):
    test_logger.info(f'Starting test for SideBar Button {button_name}...')

    test_logger.info('Opening SideBar...')
    sidebar_fixture.sidebar()

    test_logger.info(f'Checking visible for {locator} element "{button_name}"')
    assert sidebar_fixture.check_displayed_element(locator)

    sidebar_method = getattr(sidebar_fixture, button_name)
    test_logger.info(f'Clicking {button_name} method...with argument: {locator}')
    sidebar_method()
    sidebar_fixture.get_back()
    test_logger.info(f'Test for button {button_name} passed!\n')
