from util import BoxDriver
from time import sleep
# from common import CommonPage

class SearchPage():

    def search(self):
        '''搜索功能'''
        # driver = self.driver
        # 打开app
        driver = BoxDriver('App')
        sleep(3)
        # 点击同意并继续
        driver.click('id com.baidu.wenku:id/tv_agree')
        sleep(10)
        # 关闭升级
        driver.click('id com.baidu.wenku:id/dialog_pic_close')
        sleep(10)
        # 点击搜索栏
        driver.click('id com.baidu.wenku:id/h5_search_edit_text')
        sleep(2)

        assertion = ['软件测试工程师面试宝典','嫦娥五号卫星 - 百度文库']
        for i,key in enumerate(['软件测试面试宝典','嫦娥五号']):
            # 输入搜索内容
            driver.input('id com.baidu.wenku:id/h5_search_edit_text_inside',key)
            sleep(3)
            # 点击搜索
            driver.click('id com.baidu.wenku:id/h5_search_operate_text')
            sleep(9)
            # 选第三个
            # driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[3]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.view.View[1]').click()
            # 断言 查看搜索结果是否包含“软件测试面试宝典”
            # rname = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[3]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.view.View[1]').text
            # assert rname == '软件测试工程师面试宝典','搜索失败！'
            target = assertion[i]
            elements = driver.find_elements('c android.view.View')
            texts = [element.text for element in elements]
            assert target in texts

if __name__ == "__main__":
    SearchPage().search()
    # pass