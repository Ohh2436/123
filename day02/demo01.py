# appium独有的方式：
'''
定位方式
resource-id id
css css
xpath xpath

accessbility_id  content-desc属性
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
# 点击同意并继续
driver.find_element_by_xpath('//*[contains(@text,"同意并继续")]').click()
sleep(3)
driver.find_element_by_xpath('//*[contains(@resource-id,"")]').click()
sleep(3)')
# 关闭百度文库
driver.close_app()

# 打开美图秀秀
# driver.find_element_by_accessibility_id('美图秀秀').click()
# sleep(5)
# driver.quit()