from appium import webdriver
from time import sleep

# 系统基础配置
desired_capabilities = {
  "platformName": "Android",
  "platformVersion": "5.1.1",
  "appPackage": "com.baidu.wenku",
  "appActivity": "com.baidu.wenku.splash.view.activity.WelcomeActivity",
  "deviceName": "127.0.0.1:62002"
}

# 打开app
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=desired_capabilities)
sleep(3)
# 点击同意并继续
driver.find_element_by_id('com.baidu.wenku:id/tv_agree').click()
sleep(10)
# 关闭升级
driver.find_element_by_id('com.baidu.wenku:id/dialog_pic_close').click()
sleep(10)
# 点击搜索栏
driver.find_element_by_id('com.baidu.wenku:id/h5_search_edit_text').click()
sleep(2)

assertion = ['软件测试工程师面试宝典','嫦娥五号卫星 - 百度文库']
for i,key in enumerate(['软件测试面试宝典','嫦娥五号']):
    # 输入搜索内容
    driver.find_element_by_id('com.baidu.wenku:id/h5_search_edit_text_inside').send_keys('软件测试面试宝典')
    sleep(3)
    # 点击搜索
    driver.find_element_by_id('com.baidu.wenku:id/h5_search_operate_text').click()
    sleep(9)
    # 选第三个
    # driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[3]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.view.View[1]').click()
    # 断言 查看搜索结果是否包含“软件测试面试宝典”
    # rname = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[3]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.view.View[1]').text
    # assert rname == '软件测试工程师面试宝典','搜索失败！'
    target = assertion[i]
    elements = driver.find_elements_by_class_name('android.view.View')
    texts = [element.text for element in elements]
    print(texts)
    assert target in texts