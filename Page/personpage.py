from Base.Base import Base
from Page.UIElement import UIElement

class PersonPage(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    def get_shop_cart(self):
        """获取优惠券的文本内容"""
        # 降低等待的时间
        return self.get_element(UIElement.person_shop_cart_id,timeout=10).text

    def click_setting_btn(self):
        """点击设置按钮"""
        self.click_element(UIElement.person_setting_btn_id)