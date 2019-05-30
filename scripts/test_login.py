import sys,os,pytest

sys.path.append(os.getcwd())

from Base.gitDriver import get_phone_driver
from Page.page import Page
from Base.getfiledata import GetFileData
from selenium.common.exceptions import TimeoutException

def get_login_data():
    # 预期成功列表
    suc_list = []
    # 预期失败列表
    fail_list = []
    # 读取 yaml 数据
    login_data = GetFileData().get_yaml_data("logindata.yml")
    for i in login_data:
        if login_data.get(i).get("toast"):
            # 预期失败测试用例
            fail_list.append((i,login_data.get(i).get("account"),login_data.get(i).get("passwd"),
                              login_data.get(i).get("toast"),login_data.get(i).get("expect_data")))
        else:
            # 预期成功测试用例
            suc_list.append((i,login_data.get(i).get("account"),login_data.get(i).get("passwd"),
                              login_data.get(i).get("expect_data")))
    return {"suc": suc_list,"fail": fail_list}

class TestLogin:
    def setup_class(self):
        # 初始化driver
        self.driver = get_phone_driver("com.yunmall.lc", "com.yunmall.ymctoc.ui.activity.MainActivity")
        # 初始化统一入口类
        self.page_obj = Page(self.driver)

    def teardown_class(self):
        # 退出driver对象
        self.driver.quit()

    @pytest.fixture(autouse=True)
    def auto_in_login(self):
        # 点击我
        self.page_obj.get_home().click_my_btn()
        # 点击已有账号
        self.page_obj.get_sign().click_exits_account()


    @pytest.mark.parametrize("case_num,account, passwd, expect_data",get_login_data().get("suc"))
    def test_login_suc(self,case_num,account, passwd, expect_data):
        """
        :param case_num: 用例编号
        :param account: 用户名
        :param passwd: 密码
        :param exp_data: 预期结果
        :return:
        """
        #登录操作 --个人中心
        self.page_obj.get_login().login(account, passwd)
        try:
            # 获取我的优惠
            shop_cart = self.page_obj.get_person().get_shop_cart()
            try:
                assert expect_data == shop_cart
            except AssertionError:
                """停留在个人中心，需要执行退出操作"""
                # 截图
                self.page_obj.get_login().screen_page()
                assert False
            finally:
                # 点击设置
                self.page_obj.get_person().click_setting_btn()
                # 退出操作
                self.page_obj.get_setting().logout()
        except TimeoutException:
            # 截图
            self.page_obj.get_login().screen_page()
            # 关闭页面
            self.page_obj.get_login().login_close_page()
            assert False

    @pytest.mark.parametrize("case_num, account, passwd, toast, expect_data",get_login_data().get("fail"))
    def test_login_fail(self, case_num, account, passwd, toast, expect_data):
        """
        :param case_num:用例编号
        :param account:用户名
        :param passwd:密码
        :param toast:获取toast消息
        :param exp_data:预期结果
        :return:
        """
        # 登录操作 --个人中心
        self.page_obj.get_login().login(account, passwd)
        try:
            #获取toast消息
            toast_data = self.page_obj.get_setting().get_toast(toast)
            try:
                # 登录页面
                # 判断登录按钮是否存在
                self.page_obj.get_login().if_login_btn()
                # 断言
                assert toast_data == expect_data
                # 关闭登录页面
                self.page_obj.get_login().login_close_page()
            except TimeoutException:
                # 获取toast错误信息,但登录成功
                # 截图
                self.page_obj.get_login().screen_page()
                # 点击设置
                self.page_obj.get_person().click_setting_btn()
                # 退出
                self.page_obj.get_setting().logout()
                assert False
            except AssertionError:
                # 登录页面
                # 截图操作
                self.page_obj.get_setting().screen_page(name="断言失败")
                # 关闭登录按钮
                self.page_obj.get_login().login_close_page()
                assert False

        except TimeoutException:
            # 找不到toast
            # 截图
            self.page_obj.get_setting().screen_page(name="未找到")
            try:
                # 登录页面
                # 登录按钮
                self.page_obj.get_login().if_login_btn()
                # 关闭登录页面
                self.page_obj.get_login().login_close_page()
            except TimeoutException:
                # 个人中心页面
                # 点击设置
                self.page_obj.get_person().click_setting_btn()
                # 退出操作
                self.page_obj.get_setting().logout()
            assert False

