from Base.Base import Base
from Page.UIElement import UIElement

class LoginPage(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    # 登录页
    def login(self,name,password):
        # 输入账号
        self.send_element(UIElement.login_account_id,name)
        # 输入密码
        self.send_element(UIElement.login_password_id,password)
        # 点击登录按钮
        self.click_element(UIElement.login_btn_id)

    def login_close_page(self):
        """关闭登录页面"""
        # 点击关闭按钮
        self.click_element(UIElement.login_close_page_btn_id)

    def if_login_btn(self):
        """判断登录按钮是否存在"""
        self.get_element(UIElement.login_btn_id)