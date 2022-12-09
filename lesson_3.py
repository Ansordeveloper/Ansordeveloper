# Инкапсуляция
# git clone


# инкапсуляция заключение в одно место (класс) для работа с ними
# 

# публичные  без никаких подчеркивание
# защищенный
# скрытый
class Human:
    head = 1
    def __init__(self,name,age):
        self.__name = name
        self._age = age

    def run(self):
        print(f'{self.__name} is running')

h = Human('Aziret', 20)
h.name = 'dfvdfvdf'
h._name = 'daniel'
h.run()
# h._name = 'beka'            
# print(h._name)
# h._name = 'daniel'
# print(h._name)



# def run(a):
#     print((f'{a} is running'))