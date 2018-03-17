#!/usr/bin/python3


"""
基础教程：http://www.runoob.com/python3/python3-tutorial.html




"""


tup1 = (12, 34.56);
tup2 = ('abc', 'xyz')

# 以下修改元组元素操作是非法的。
# tup1[0] = 100

# 创建一个新的元组
tup3 = tup1 + tup2;
print (tup3)
print(len(tup3))
# print(max(tup3))


tup = ('Google', 'Runoob', 1997, 2000)

print (tup)
del tup;
# print ("删除后的元组 tup : ")
# print (tup)



dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])

dict['Age'] = 8;               # 更新 Age
dict['School'] = "菜鸟教程"  # 添加信息

print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])
print(len(dict))
print(str(dict))
print(type(dict))


dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

del dict1['Name'] # 删除键 'Name'
dict1.clear()     # 清空字典
del dict1         # 删除字典

# print ("dict1['Age']: ", dict1['Age'])
# print ("dict1['School']: ", dict1['School'])



a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a+b


# 关键字end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符

# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b


a=10;b=388;c=98
print(a,b,c,sep='@')

# Python 中用 elif 代替了 else if，所以if语句的关键字为：if – elif – else。
"""
1、每个条件后面要使用冒号（:），表示接下来是满足条件后要执行的语句块。
2、使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
3、在Python中没有switch – case语句。
"""
'''
<	小于
<=	小于或等于
>	大于
>=	大于或等于
==	等于，比较对象是否相等
!=	不等于


var1 = 100
if var1:
    print("1 - if 表达式条件为 true")
    print(var1)

var2 = 0
if var2:
    print("2 - if 表达式条件为 true")
    print(var2)
print("Good bye!")

age = int(input("请输入你家狗狗的年龄: "))
print("")
if age < 0:
    print("你是在逗我吧!")
elif age == 1:
    print("相当于 14 岁的人。")
elif age == 2:
    print("相当于 22 岁的人。")
elif age > 2:
    human = 22 + (age - 2) * 5
    print("对应人类年龄: ", human)

### 退出提示
input("点击 enter 键退出")


# 该实例演示了数字猜谜游戏
number = 7
guess = -1
print("数字猜谜游戏!")
while guess != number:
    guess = int(input("请输入你猜的数字："))

    if guess == number:
        print("恭喜，你猜对了！")
    elif guess < number:
        print("猜的数字小了...")
    elif guess > number:
        print("猜的数字大了...")


num=int(input("输入一个数字："))
if num%2==0:
    if num%3==0:
        print ("你输入的数字可以整除 2 和 3")
    else:
        print ("你输入的数字可以整除 2，但不能整除 3")
else:
    if num%3==0:
        print ("你输入的数字可以整除 3，但不能整除 2")
    else:
        print  ("你输入的数字不能整除 2 和 3")
'''


"""
Python中while语句的一般形式：

while 判断条件：
    语句
同样需要注意冒号和缩进。另外，在Python中没有do..while循环。
"""
n = 100

sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1

print("1 到 %d 之和为: %d" % (n, sum))


"""
我们可以通过设置条件表达式永远不为 false 来实现无限循环

你可以使用 CTRL+C 来退出当前的无限循环。

无限循环在服务器上客户端的实时请求非常有用。

var = 1
while var == 1:  # 表达式永远为 true
    num = int(input("输入一个数字  :"))
    print("你输入的数字是: ", num)

print("Good bye!")
"""


"""
Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。

for循环的一般格式如下：
for <variable> in <sequence>:
    <statements>
else:
    <statements>

"""

sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")


## range()函数
for i in range(5): print(i,end=',')
for i in range(5,9) : print(i)

## 遍历序列
a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)): print(i, a[i])
## 创建列表
list = list(range(5))
for s in list : print(s,list[s])



"""
循环语句可以有 else 子句，它在穷尽列表(以for循环)或条件变为 false (以while循环)导致循环终止时被执行,但循环被break终止时不执行。
"""
for n in range(2, 20):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')



"""
Python pass是空语句，是为了保持程序结构的完整性。

pass 不做任何事情，一般用做占位语句
"""
for letter in 'Runoob':
    if letter == 'o':
        pass
        print('执行 pass 块')
    print('当前字母 :', letter)

print("Good bye!")


"""
冒泡排序，python 版本
"""
print("冒泡排序：")
def paixu(li) :
    max = 0
    for ad in range(len(li) - 1):
        for x in range(len(li) - 1 - ad):
            if li[x] > li[x + 1]:
                max = li[x]
                li[x] = li[x + 1]
                li[x + 1] = max
            else:
                max = li[x + 1]
    print(li)
paixu([41,23344,9353,5554,44,7557,6434,500,2000])



'''
迭代器
迭代是Python最强大的功能之一，是访问集合元素的一种方式。

迭代器是一个可以记住遍历的位置的对象。

迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。

迭代器有两个基本的方法：iter() 和 next()。
'''
print()
print("迭代器：")
list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
for x in it:
    print (x, end=" ")

print()

# import sys  # 引入 sys 模块
# list = [1, 2, 3, 4]
# it = iter(list)  # 创建迭代器对象
#
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()


'''
生成器
在 Python 中，使用了 yield 的函数被称为生成器（generator）。

跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。

在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。

调用一个生成器函数，返回的是一个迭代器对象。
'''
print()
print("生成器：")

# import sys  # 引入 sys 模块
# def fibonacci(n):  # 生成器函数 - 斐波那契
#     a, b, counter = 0, 1, 0
#     while True:
#         if (counter > n):
#             return
#         yield a
#         a, b = b, a + b
#         counter += 1
#
#
# f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成
#
# while True:
#     try:
#         print(next(f), end=" ")
#     except StopIteration:
#         sys.exit()




# import sys  # 引入 sys 模块
# def fibonacci(n,w=0): # 生成器函数 - 斐波那契
#     a, b, counter = 0, 1, 0
#     while True:
#         if (counter > n):
#             return
#         yield a
#         a, b = b, a + b
#         print('%d,%d' % (a,b))
#         counter += 1
# f = fibonacci(10,0) # f 是一个迭代器，由生成器返回生成
#
# while True:
#     try:
#         print (next(f), end=" ")
#     except :
#         sys.exit()


"""
函数：
函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()。
任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。
函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
函数内容以冒号起始，并且缩进。
return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
"""
print()
print("函数")

# 定义函数
def printme( str ):
   # "打印任何传入的字符串"
   print(str)
   return


# 调用函数
printme("我要调用用户自定义函数!")
printme("再次调用同一函数")


"""
可更改(mutable)与不可更改(immutable)对象
在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。

不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。

可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。

不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。

可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响

"""

print()

# 可写函数说明
def printinfo(name, age):
    "打印任何传入的字符串"
    print("Name: ", name);
    print("Age ", age);
    return;


# 调用printinfo函数
printinfo(age=50, name="miki");


# 可写函数说明
def printinfo(name, age=35):
    "打印任何传入的字符串"
    print("Name: ", name);
    print("Age ", age);
    return;


# 调用printinfo函数
printinfo(age=50, name="miki");
printinfo(name="miki");


"""
你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述2种参数不同，声明时不会命名。

def functionname([formal_args,] *var_args_tuple ):
   "函数_文档字符串"
   function_suite
   return [expression]

"""
print()
print("不定参数")

# 可写函数说明
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return;


# 调用printinfo 函数
printinfo(10);
printinfo(70, 60, 50);



"""
python 使用 lambda 来创建匿名函数。

lambda只是一个表达式，函数体比def简单很多。
lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。
虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。

lambda函数的语法只包含一个语句
lambda [arg1 [,arg2,.....argn]]:expression

"""

# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2;

# 调用sum函数
print("相加后的值为 : ", sum(10, 20))
print("相加后的值为 : ", sum(20, 20))


"""
return 语句
return语句[表达式]退出函数，选择性地向调用方返回一个表达式。不带参数值的return语句返回None。

"""


# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2
    print("函数内 : ", total)
    return total;


# 调用sum函数
total = sum(10, 20);


"""
变量作用域
全局变量/局部变量

定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。
局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。调用函数时，所有在函数内声明的变量名称都将被加入到作用域中
"""

print()
print("变量作用域")

total = 0;  # 这是一个全局变量

# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2;  # total在这里是局部变量.
    print("函数内是局部变量 : ", total)
    return total;


# 调用sum函数
sum(10, 20);
print("函数外是全局变量 : ", total)


#全局变量想作用于函数内，需加 global
globvar = 0

def set_globvar_to_one():
    global globvar    # 使用 global 声明全局变量
    globvar = 1

def print_globvar():
    print(globvar)     # 没有使用 global

print_globvar()         ##输出0，未调用
set_globvar_to_one()
print(globvar)        # 输出 1
print_globvar()       # 输出 1，函数内的 globvar 已经是全局变量



##列表反转函数
# def reverse(li):
#     for i in range(0, len(li)/2):
#         li[i], li[-i - 1] = li[-i - 1], li[i]
#     return
# l = [1, 2, 3, 4, 5]
# reverse(l)
# print(l)



## 数据结构
"""
http://www.runoob.com/python3/python3-data-structure.html
列表

list.append(x)	把一个元素添加到列表的结尾，相当于 a[len(a):] = [x]。
list.extend(L)	通过添加指定列表的所有元素来扩充列表，相当于 a[len(a):] = L。
list.insert(i, x)	在指定位置插入一个元素。第一个参数是准备插入到其前面的那个元素的索引，例如 a.insert(0, x) 会插入到整个列表之前，而 a.insert(len(a), x) 相当于 a.append(x) 。
list.remove(x)	删除列表中值为 x 的第一个元素。如果没有这样的元素，就会返回一个错误。
list.pop([i])	从列表的指定位置删除元素，并将其返回。如果没有指定索引，a.pop()返回最后一个元素。元素随即从列表中被删除。（方法中 i 两边的方括号表示这个参数是可选的，而不是要求你输入一对方括号，你会经常在 Python 库参考手册中遇到这样的标记。）
list.clear()	移除列表中的所有项，等于del a[:]。
list.index(x)	返回列表中第一个值为 x 的元素的索引。如果没有匹配的元素就会返回一个错误。
list.count(x)	返回 x 在列表中出现的次数。
list.sort()	对列表中的元素进行排序。
list.reverse()	倒排列表中的元素。
list.copy()	返回列表的浅复制，等于a[:]。
"""

##将列表当做堆栈使用

stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
print(stack.pop())      ##出栈
print(stack)


##将列表当作队列使用
##也可以把列表当做队列用，只是在队列里第一加入的元素，第一个取出来；但是拿列表用作这样的目的效率不高。在列表的最后添加或者弹出元素速度快，然而在列表里插入或者从头部弹出速度却不快（因为所有其他的元素都得一个一个地移动）。
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue)
print(queue.popleft())
print(queue)
print(queue.popleft())
print(queue)


"""
列表推导式

列表推导式提供了从序列创建列表的简单途径。通常应用程序将一些操作应用于某个序列的每个元素，用其获得的结果作为生成新列表的元素，或者根据确定的判定条件创建子序列。

每个列表推导式都在 for 之后跟一个表达式，然后有零到多个 for 或 if 子句。返回结果是一个根据表达从其后的 for 和 if 上下文环境中生成出来的列表。如果希望表达式推导出一个元组，就必须使用括号。

"""
print()
print("列表推导式")
vec = [2, 4, 6]
print(vec)
print([3*x for x in vec])
print(vec)
print([[x, x**2] for x in vec])

##对序列里每一个元素逐个调用某方法
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruit])


print([3*x for x in vec if x > 3])
print([3*x for x in vec if x < 2])

##关于循环和其它技巧的演示
vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
print([x*y for x in vec1 for y in vec2])    ## vec1[1]*vec2[1], vec1[1]*vec2[2],vec1[1]*vec2[3],vec1[2]*vec2[1]...
print([x+y for x in vec1 for y in vec2])
print([vec1[i]*vec2[i] for i in range(len(vec1))])

##使用复杂表达式或嵌套函数
print([str(round(355/113, i)) for i in range(1, 6)])

"""
嵌套列表解析

"""

matrix = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
]
print(matrix)
##将3X4的矩阵列表转换为4X3列表 1
print([[row[i] for row in matrix] for i in range(4)])
##将3X4的矩阵列表转换为4X3列表 2
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)
##将3X4的矩阵列表转换为4X3列表 3
transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)



"""
del 语句

用 del 语句可以从一个列表中依索引而不是值来删除一个元素。这与使用 pop() 返回一个值不同。可以用 del 语句从列表中删除一个切割，或清空整个列表

"""
print()
print("del:")
a = [-1, 1, 66.25, 333, 333, 1234.5]
print(a)
del a[0]
print(a)
del a[2:4]
print(a)
del a[:]
print(a)

#del 删除实体变量
del a
# print(a)


"""
元组和序列

"""
print()
print("元组和序列：")
t = 12345, 54321, 'hello!'
print(t)
print(t[0])




"""
集合
集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素。
可以用大括号({})创建集合。注意：如果要创建一个空集合，你必须用 set() 而不是 {} ；后者创建一个空的字典
"""

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('orange' in basket)
print('crabgrass' in basket)

a = set('abracadabra')
b = set('alacazam')
print(a)
print(a-b)
print(a|b)
print(a&b)
print(a^b)
print(~a)




