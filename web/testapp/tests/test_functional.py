# -*- coding: utf-8 -*-

#
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class SeleniumTest(TestCase):
    def setUp(self):
        self.chrome = webdriver.Remote(
            command_executor='http://selenium_hub:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME
        )
        self.firefox = webdriver.Remote(
            command_executor='http://selenium_hub:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.FIREFOX
        )

    def tearDown(self):
        # selenium webdrivers have to be quit()ed to free the associated resources.
        self.chrome.quit()
        self.firefox.quit()

    def test_visit_site_with_chrome(self):
        self.chrome.get('http://web:8000')
        self.assertIn('Django', self.chrome.title)

    def test_visit_site_with_firefox(self):
        self.firefox.get('http://web:8000')
        self.assertIn('Django', self.firefox.title)

    def test_visit_python_with_chrome(self):
        self.chrome.get('http://www.python.org/')
        self.assertIn('Python', self.chrome.title)

