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

# driver.find_element_by_accessibility_id('美图秀秀').click()
# 使用坐标定位 positions(参数): List[Tuple[int, int]]（参数的类型，只是说明，不强制）-> T（返回值）
# driver.tap([(400,700)])
# 用坐标定位百度文库
driver.tap([(200,700)])
sleep(9)
# 用坐标定位关闭升级
driver.tap([(350,950)])
sleep(5)
# 向上滑动
driver.swipe(360,950,360,600,500)
driver.close_app()