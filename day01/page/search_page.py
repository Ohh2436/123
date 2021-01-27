from base.util import BoxDriver
from time import sleep
from page.common_page import CommonPage


class SearchPage(CommonPage):

    def search(self,keyword):
        '''搜索功能'''
        # 打开app,点击同意并继续，关闭升级
        driver = self.driver
        sleep(10)
        # 点击搜索栏
        driver.click('id com.baidu.wenku:id/h5_search_edit_text')
        sleep(2)

        # 输入搜索内容
        driver.input('id com.baidu.wenku:id/h5_search_edit_text_inside',keyword)
        sleep(3)
        # 点击搜索
        driver.click('id com.baidu.wenku:id/h5_search_operate_text')
        sleep(9)

    def get_text(self):
            # 选第三个
            # driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[3]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.view.View[1]').click()
            # 断言 查看搜索结果是否包含“软件测试面试宝典”
            # rname = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[3]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.view.View[1]').text
            # assert rname == '软件测试工程师面试宝典','搜索失败！'
        # 获取断言信息
        elements = self.driver.find_elements('c android.view.View')
        return [element.text for element in elements]

    def cancel(self):
        '''点击取消按钮'''
        self.driver.click('id com.baidu.wenku:id/h5_search_operate_text')

        

if __name__ == "__main__":
    # SearchPage().search()
    pass