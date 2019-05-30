from Page.homepage import HomePage
from Page.signpage import SignPage
from Page.loginpage import LoginPage
from Page.personpage import PersonPage
from Page.settingpage import SettingPage


class Page:
    def __init__(self,driver):
        self.driver = driver

    def get_home(self):
        """返回首页"""
        return HomePage(self.driver)

    def get_sign(self):
        """返回注册页"""
        return SignPage(self.driver)

    def get_login(self):
        """返回登录页"""
        return LoginPage(self.driver)

    def get_person(self):
        """返回个人中心页"""
        return PersonPage(self.driver)

    def get_setting(self):
        """返回设置页"""
        return SettingPage(self.driver)