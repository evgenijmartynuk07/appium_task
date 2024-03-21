import subprocess
import time
import logging

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

from utils.android_utils import android_get_desired_capabilities


@pytest.fixture(scope='session')
def run_appium_server():
    subprocess.Popen(
        ['appium', '-a', '0.0.0.0', '-p', '4723', '--allow-insecure', 'adb_shell'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        shell=True
    )
    time.sleep(5)


@pytest.fixture(scope='session')
def driver(run_appium_server, test_logger, get_udid):

    test_logger.info(f'Phone UDID: {get_udid}. Starting tests!')

    driver = webdriver.Remote(
        'http://localhost:4723/wd/hub',
        options=UiAutomator2Options().load_capabilities(
            android_get_desired_capabilities()
        )
    )
    yield driver


@pytest.fixture(scope='session')
def test_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    handler_stream = logging.StreamHandler()
    handler_stream.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler_stream.setFormatter(formatter)
    logger.addHandler(handler_stream)

    handler_file = logging.FileHandler('test_logs.log')
    handler_file.setLevel(logging.DEBUG)
    handler_file.setFormatter(formatter)
    logger.addHandler(handler_file)

    return logger


@pytest.fixture(scope='session')
def get_udid():
    result = subprocess.run(
        ['adb', 'devices'],
        capture_output=True,
        text=True
    )
    return result.stdout.split()[-2]
