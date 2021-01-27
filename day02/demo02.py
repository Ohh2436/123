'''
UiAutomator定位
UiAutomator定位实际上是使用java代码定位的
注意区分单引号和双引号
'''
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

# 点击 同意并继续
# driver.find_element_by_android_uiautomator('new UiSelector().text("同意并继续")').click()
# driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.baidu.wenku:id/tv_agree")').click()
# 组合定位
# driver.find_element_by_android_uiautomator('className("android.widget.TextView).text("同意并继续")').click()
# sleep(3)
# 模糊文本定位
# driver.find_element_by_android_uiautomator('new UiSelector().textContains("继续")')
# 利用父子关系进行定位
# driver.find_element_by_android_uiautomator('className("android.widget.FrameLayout").childSelector(text("同意并继续"))').click()
# driver.find_element_by_android_uiautomator('className("android.widget.FrameLayout").childSelector(instance(3))').click()
# 兄弟关系
driver.find_element_by_android_uiautomator('text("温馨提示").fromParent(text("同意并继续"))').click()

driver.close_app()

# 打开美图秀秀
# driver.find_element_by_android_uiautomator('new UiSelector().description("美图秀秀")').click() 