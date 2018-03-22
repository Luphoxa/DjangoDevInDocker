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
        # self.firefox = webdriver.Remote(
            # command_executor='http://selenium_hub:4444/wd/hub',
            # desired_capabilities=DesiredCapabilities.FIREFOX
        # )

    def test_visit_extern_site_with_chrome(self):
        self.chrome.get('https://www.google.com')
        self.assertIn(self.chrome.title, 'Google')

    def test_visit_own_site_with_chrome(self):
        self.chrome.get('http://web:8000')
        self.assertIn(self.chrome.title, 'Google')

    # def test_visit_site_with_firefox(self):
        # self.firefox.get('http://web:8000')
        # self.assertIn(self.firefox.title, 'Django: the Web framework for perfectionists with deadlines.')
