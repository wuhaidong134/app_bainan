from Base.Base import Base
from Page.UIElement import UIElement

class SettingPage(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    def logout(self,tag=1):
        """
        退出操作
        :param tag: 1:退出
        :return:
        """
        # 滑动
        self.scroll_sreen()
        # 点击退出按钮
        self.click_element(UIElement.setting_logout_btn_id)
        if int(tag) == 1:
            # 点击确认退出按钮
            self.click_element(UIElement.setting_acc_quit_btn_id)
        else:
            # 取消 退出操作
            self.click_element(UIElement.setting_dis_quit_btn_id)