# 打印一个字符串，使其是10个a
# a=''
# for i in range(10):
#     a=a+'a'
# print(a)

# 20以内的所有奇数，偶数，和素数
# a,b,c=[],[],[]
# for i in range(1,21):
#     flag=True
#     if i%2==0:
#         a.append(i)
#     else:
#         b.append(i)
#     if i>1:
#         for j in range(2,int(i/2)+1):
#             if i%j==0:
#                 flag=False
#                 break
#         if flag:
#             c.append(i)
# print(a,b,c)

#创建一个类Dog，有两个成员变量name,age,构造方法写入默认参数，创建5个对象写进一个列表,然后用列表生成式打印5个对象的属性
# 打印结果：[('小何0', 0), ('小何1', 1), ('小何2', 2), ('小何3', 3), ('小何4', 4)]
# class Dog:
#     def __init__(self,name='dog',age=20):
#         self.name = name
#         self.age = age
# a = []
# for i in range(1,6):
#     dogname = 'dog%d'%i
#     a.append(Dog(dogname,age=i))
# o = [(i.name,i.age) for i in a ]
# print(o)

#创建一个Teacher类，成员变量（编号、科目类别）一个Student，成员变量（名字）成员方法（上课（打印：名字上哪个老师的课）、
# 下课（哪个老师的课结束了）、玩耍（名字去玩耍了））
#举个例子：老师：编号：1 科目：语文     学生：小何  上课方法打印结果：小何开始上1号语文老师的课啦！ 
# 下课方法打印：1号语文老师的课结束啦，玩耍方法打印：小何去玩啦
# from selenium import webdriver
# class Teacher:
#     def __init__(self,bianhao=1,subject='语文'):
#         self.bianhao = bianhao
#         self.subject = subject
#     # for i in range(1,5):
#         # bianhao = 1
#         # subject = '语文'
   
# class Student:
#     def __init__(self,name='小明'):
#         self.name = name
#         # self.aclass = aclass
#         # self.play = play
        
#         # play = 
#     def student(self,aclass='上课',uclass='下课',play=url):
#         driver = webdriver.Chrome()
#         url = ('http://www.4399.com/')
#     print(name )

        