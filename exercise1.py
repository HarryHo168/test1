str1 = input("请输入一个人的名字：")
str2 = input("请输入一个国家名字：")
print("世界这么大，{}想去{}看看。".format(str1,str2))

n = input("请输入整数 N:")
sum = 0
for i in range(int(n)):
    sum += i + 1
print("1到N求和结果： ", sum)
