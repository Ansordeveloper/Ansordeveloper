# oop - Обьект орентированное программирование
# Наследование полиморфизм - это изменения повидения методов в дочерных классах
# # Git
# #
# class H:
#     atribyt = 1
#     def __init__(self,name,age): 
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f'name is {self.name} \n'\
#              f'age is {self.age}'

#     def run(self):
#         print(f'{self.name} is running')

# g = H('asror', 19)
# print(g)
# g.run()

# # Супер класс = Главный класс который не от кого не наследуеться и не зависимо не от кого
# class Human:
#     head = 1
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f'name is {self.name}\n' \
#             f'age is {self.age}'

# hum = Human('sadir',34)
# print(hum)

# # Класс который от чего то наследуеться - называеться дочерний класс
# class Student(Human):
#     head = 2
#     def __init__(self, name, age, lastname):
#         super().__init__(name, age,)
#         Human.__init__(self,name,age,)
#         self.lastname = lastname
#     def __str__(self):
#         return f'name is {self.name}\n' \
#             f'age is {self.age}\n' \
#             f'lastname is {self.lastname}'
#     def run(self):
#         print(f'{self.name} is running')

#     def fly(self):
#         print(self.name, 'is fly in True')


# student = Student('Daniyl', 60, 'kab')

# print(student)
# student.run()
# student.fly()

# # дочерний класс
# class Teacher(Student):

# tech =Teacher('Beka', 55, 'dju')
# print(tech)
# tech.fly()




# class Robot:
#     def noSleep(a):
#         print(f'{a} funkchun no Sleep True')


# class Robot2(Robot):...

# Robot.noSleep(student.name)

