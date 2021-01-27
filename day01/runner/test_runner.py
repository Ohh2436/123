import os,sys
sys.path.append(os.getcwd()+r'/day01')

from base.HTMLTestRunner import HTMLTestRunner
import unittest,time
from base.util import Email

class TestRunner:

    def runner(self):
        '''挑选用例'''
        # 创建测试套件
        suite = unittest.TestSuite()
        # 添加测试用例
        suite.addTests(unittest.TestLoader().discover('day01/test',pattern='search_test.py'))
        # 生成一个时间戳
        timestamp = time.strftime('%Y-%m-%d_%H_%M_%S')
        # 创建报告路径
        path = 'day01/report/report_%s.html'%timestamp
        # 创建html报告文件
        report = open(path,'wb')
        # 创建用例运行器，用于运行用例并生成报告
        test_runner = HTMLTestRunner(stream=report,title='appium自动化生成报告',description='报告的详细描述......')
        # 运行
        test_runner.run(suite)
        # 发送报告
        receivers = 'ohh_2045@163.com'
        subject = 'appium自动化报告'
        content = '''
        <p>Dear Anna</p>
        <p>&nbsp;这是appium的项目报告，请查收！</p>
        <p>此致</p>
        <p>lucy</p>
        '''
        Email().send(receivers,subject,content,path)
if __name__ == "__main__":
    TestRunner().runner()
