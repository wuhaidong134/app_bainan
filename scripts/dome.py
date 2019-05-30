from selenium.webdriver.common.by import By

from Base.gitDriver import get_phone_driver
from Page.page import Page

# 实例化driver
driver = get_phone_driver("com.yunmall.lc", "com.yunmall.ymctoc.ui.activity.MainActivity")
# 实例化统一入口类
page_obj = Page(driver)

# 点击首页我
page_obj.get_home().click_my_btn()
# 点击注册页面已有账号去登录
page_obj.get_sign().click_exits_account()
# 执行登录操作
page_obj.get_login().login("13429975950", "wu1234567")

# 获取提示消息
# 获取错误提示
error_message = (By.XPATH, '//*[contains(@text,"错误")]')
message = page_obj.get_setting().get_element(error_message, timeout=5, poll_frequency=0.5).text

print(message)

# # 获取我的优惠券
# print("获取结果:{}".format(page_obj.get_person().get_shop_cart()))
# # 点击设置按钮
# page_obj.get_person().click_setting_btn()
# # 退出操作
# page_obj.get_setting().logout()