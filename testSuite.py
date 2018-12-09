import unittest

class MyFirstUnit(unittest.TestCase):

    def test_case_11(self):
        self.assertEqual(111, 111,"they are not equal")
        print("111111")

    def test_case_string(self):
        self.assertEqual("a", "a","they are not equal")
        print("ssssss")

    def test_case_list(self):
        lst=[1,2,3]
        self.assertListEqual(lst,[1,3,3],"they are not same list")
        print("LLLLLLL")

    def test_case_List(self):
        self.assertListEqual([1,2,3],[1,2,3],)
        print("TTTTTTT")

#测试套
def mysuite():
    suite=unittest.TestSuite()
    suite.addTest(MyFirstUnit("test_case_string"))
    # suite.addTest(MyFirstUnit("test_case_list"))
    # suite.addTest(MyFirstUnit("test_case_11"))
    suite.addTest(MyFirstUnit("test_case_List"))

    return suite


'''
若用右键 run+文件名，则所有的内容都会执行，不会执行下面的if
若有下面的if真正被调用，则用Run->Run...->选择当前文件
'''

if __name__ == "__main__":
    # unittest.main()
    runner=unittest.TextTestRunner()
    runner.run(mysuite())