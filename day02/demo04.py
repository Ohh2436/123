from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction


# 系统基础配置
desired_capabilities = {
  "platformName": "Android",
  "platformVersion": "5.1.1",
#   "appPackage": "com.baidu.wenku",
#   "appActivity": "com.baidu.wenku.splash.view.activity.WelcomeActivity",
  "deviceName": "127.0.0.1:62002"
}
# 打开app
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=desired_capabilities)
sleep(3)

# 删除美图秀秀
mtxx = driver.find_element_by_accessibility_id('美图秀秀')
TouchAction(driver).long_press(mtxx).move_to(x=114,y=93).release().perform()
sleep(5)
# 点击确定或取消
driver.tap([(500,730)])