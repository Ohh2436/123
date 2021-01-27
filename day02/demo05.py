from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
from time import sleep


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

# 启动app
driver.start_activity("com.baidu.wenku","com.baidu.wenku.splash.view.activity.WelcomeActivity")
sleep(5)
# 点击home键回到主页面,在百度搜索andior keycode
driver.press_keycode(3)
sleep(5)
# 放大音量
driver.press_keycode(24)
driver.press_keycode(24)
driver.press_keycode(24)
driver.press_keycode(24)
sleep(2)
# 缩小音量
driver.press_keycode(25)
driver.press_keycode(25)
driver.press_keycode(25)
sleep(2)

# 安装app
driver.install_app('D:\com.mt.mtxx.mtxx.apk')
sleep(5)
# 卸载app
driver.remove_app('com.mt.mtxx.mtxx.apk')