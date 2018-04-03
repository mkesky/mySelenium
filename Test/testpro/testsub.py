from calculator import Count
import unittest

class TestSub(unittest.TestCase):
    def setUp(self):
        print("开始进行减法")

    def tearDown(self):
        print("减法测试结束")

    def test_sub(self):
        q = Count(9,3)
        self.assertEqual(q.sub(),6,msg = "9-3运算错误")

    # msg="",此处的字符串返回的是结果是：结果错误时，给出的提示
    def test_sub2(self):
        q = Count(88,22)
        self.assertEqual(q.sub(),55,msg = "88-22运算错误")


if __name__ == "__main__":
    unittest.main()