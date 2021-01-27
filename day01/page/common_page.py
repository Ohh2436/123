from util import BoxDriver,BasePage
from time import sleep

class CommonPage(BasePage): 

    def common(self):

        driver = self.driver
        # 打开app
        # driver = BoxDriver('APP')
        sleep(3)
        # 点击同意并继续
        driver.click('id com.baidu.wenku:id/tv_agree')
        sleep(10)
        # 关闭升级
        driver.click('id com.baidu.wenku:id/dialog_pic_close')
if __name__ == "__main__":
    CommonPage(BasePage).common()
