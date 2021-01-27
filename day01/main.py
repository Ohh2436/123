'''程序入口'''
from runner.test_runner import TestRunner

class Main:
    def start(self):
        TestRunner().runner()

if __name__ == "__main__":
    '''代码自动化入口'''
    Main().start()