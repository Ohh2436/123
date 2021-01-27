import os,sys
sys.path.append(os.getcwd()+r'\day01')

import unittest
from base.util import BoxDriver,GetCSV,GetLogger
from page.common_page import CommonPage
from page.search_page import SearchPage
from parameterized import parameterized


class SearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print(132)
        self.logger = GetLogger('day01/report/report.log')
        self.driver = BoxDriver('App')
        self.page = SearchPage(self.driver)
        self.page.common()
    @parameterized.expand(GetCSV().get(r'D:\workspace\appium\day01\data\data.csv'))
    def test_search_success(self,keyword,target):
        self.page.search(keyword)
        self.logger.info('输入搜索内容成功！')
        texts = self.page.get_texts()
        # assert target in texts
        self.assertIn(target,texts,'未找到指定内容！')
        self.logger.error('断言成功')
        # 点击取消
        self.page.cancel()
        self.logger.debug('取消成功！')

if __name__ == "__main__":
    unittest.main()
