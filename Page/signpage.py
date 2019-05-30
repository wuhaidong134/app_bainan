from Base.Base import Base
from Page.UIElement import UIElement

class SignPage(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    # 点击已有账号
    def click_exits_account(self):
        self.click_element(UIElement.sign_exits_account_btn_id)
