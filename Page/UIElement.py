from selenium.webdriver.common.by import By


class UIElement:
    """管理所有页面元素"""

    # 首页
    # 定位首页,我的按钮
    home_my_btn_id = (By.ID,"com.yunmall.lc:id/tab_me")


    # 注册页
    # 已有账号去登录
    sign_exits_account_btn_id = (By.ID,"com.yunmall.lc:id/textView1")


    # 登录页
    # 用户名
    login_account_id = (By.ID,"com.yunmall.lc:id/logon_account_textview")
    # 密码
    login_password_id = (By.ID,"com.yunmall.lc:id/logon_password_textview")
    # 登录按钮
    login_btn_id = (By.ID,"com.yunmall.lc:id/logon_button")
    # 关闭登录按钮
    login_close_page_btn_id = (By.ID,"com.yunmall.lc:id/ymtitlebar_left_btn_image")

    # 个人中心
    # 我的优惠券
    person_shop_cart_id = (By.ID,"com.yunmall.lc:id/txt_my_coupons")
    # 设置按钮
    person_setting_btn_id = (By.ID,"com.yunmall.lc:id/ymtitlebar_left_btn_image")


    # 设置页
    # 退出按钮
    setting_logout_btn_id = (By.ID,"com.yunmall.lc:id/setting_logout")
    # 弹窗 确认退出按钮
    setting_acc_quit_btn_id = (By.ID,"com.yunmall.lc:id/ymdialog_right_button")
    # 弹窗 取消退出按钮
    setting_dis_quit_btn_id = (By.ID,"com.yunmall.lc:id/ymdialog_left_button")
