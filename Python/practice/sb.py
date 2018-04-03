# def discounts(price,rate):
#     final_price = price * rate
#     print("打印出old_price的值：", old_price)
#     return final_price
#
#
# old_price = float(input("请输入原价："))
# rate = float(input("请输入折扣率："))
# new_price = discounts(old_price,rate)
# print("打折后的价格是：",new_price)



# def recursion(n):
#     result = n
#     for i in range(1,n):
#         result *= i
#     return result
#
# number = int(input("请输入一个整数："))
# result = recursion(number)
# print("%d的阶乘是：%d" % (number,result))


#
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return  n * factorial(n-1)
#
# number = int(input("输入一个整数："))
# result = factorial(number)
# print("%d的阶乘是：%d" % (number,result))




# def fab(n):
#     if n < 1:
#         print("输入有误")
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fab(n-1) + fab(n-2)
#
# result = fab(20)
# if result != -1:
#     print("总共有%d对小兔崽子诞生" % result)




def c2f(cel):
	fah = cel*1.8 + 32
	return fah

def f2c(fah):
    cel = (fah-32)/1.8
    return cel

def test():
    print("0摄氏度=%.2f华氏度" % c2f(0))
    print("0华氏度=%.2f摄氏度" % f2c(0))

if __name__ == '__main__':
    test()




















