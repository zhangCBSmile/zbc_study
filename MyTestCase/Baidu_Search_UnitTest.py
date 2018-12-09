from selenium import webdriver
import unittest
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class Search_Baidu(unittest.TestCase):

    def setUp(self):
        self.url = "https://www.baidu.com"
        self.driver = webdriver.Firefox()

    def test_search(self):
       self.driver.get(self.url)
       self.driver.find_element_by_id("kw").send_keys("JAVA")
       self.driver.find_element_by_id("su").click()
       sleep(2)

    def test_setting(self):
        self.driver.get(self.url)
        hover=self.driver.find_element_by_link_text("设置")
        ActionChains(self.driver).move_to_element(hover).perform()
        self.driver.find_element_by_link_text("搜索设置").click()
        sleep(2)
        self.driver.find_element_by_xpath("//select[@id='nr']/option[1]").click()
        self.driver.find_element_by_link_text("保存设置").click()
        self.driver.switch_to.alert.accept()
        sleep(2)

    def tearDown(self):
        self.driver.quit()

def MySuite():
    pass

if __name__=="__main__":
    unittest.main()
