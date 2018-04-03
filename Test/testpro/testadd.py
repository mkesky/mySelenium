from calculator import Count
import unittest

class TestAdd(unittest.TestCase):
    def setUp(self):
        print("开始加法测试")

    def tearDown(self):
        print("加法测试结束")

#msg="",此处的字符串返回的是结果是：结果错误时，给出的提示
    def test_add(self):
        j = Count(5,6)
        self.assertEqual(j.add(),11,msg = "5+6运算错误")

    def test_add2(self):
        j = Count(55,66)
        self.assertEqual(j.add(),111,msg = "55+66运算错误")

if __name__ == "__main__":
    unittest.main()
