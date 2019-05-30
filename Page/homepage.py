from Base.Base import Base
from Page.UIElement import UIElement

class HomePage(Base):

    def __init__(self,driver):
        Base.__init__(self,driver)

    # 点击我的
    def click_my_btn(self):
        self.click_element(UIElement.home_my_btn_id)