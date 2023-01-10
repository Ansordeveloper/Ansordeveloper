# линейный поиск
#
name = ['бука','beka','erf','нурислам','adahan']

search_for = 'нурислам' # что мы ищем


def linear_search(where,what):
    for v in enumerate(where):
        if v[1] == what :
            return  v[0] # возвращаем индекс

        return  None
print('искомый элемент',search_for,'найден под индексом',
      linear_search(name,search_for))

# сортировка выборка
nums=[2,3,1,3,1,5,7,85,5,3,44,9,9]
print('было',nums)

for i in range(len(nums)):
    lowest = i


    for j in range(i + 1, len(nums)):
        if nums[j] < nums[lowest]:
            lowest = j

    nums[i],nums[lowest]=nums[lowest],nums[i]
print('стало',nums)

num = [2,1,5,7,30,54,67,23,0,98,100,21]
print('было', num)

for i in range(len(num)):
    lowest=i


    for h in range(i + 1, len(num)):
        if num[h] < num[lowest]:
            lowest = h
    num[i],num[lowest] = num[lowest],num[i]
print('стало',num)

# o(log n)
# бинарный поиск
m = sorted(nums)
print(m)

nu= 6

lowest=0
highest=len(m)-1
index=None

while(lowest<=highest) and (index is None):
    # повторять пока не найдем
    mid = (lowest+highest)//2
    if m[mid] ==nu:
        index=mid
    else:
        if nu < m[mid]:
            # ищем по девой части списка
            highest=mid -1
        else:
            # по правой
            lowest=mid + 1
print('искомый элемент', nu, 'находиться под индексом', index)


# алгоритм Евклида - нахождение нод

# def nod(a, b):
#     while a != 0 and b != 0:
#         if a > b:
#             a = a % b
#         else:
#             b = b % a
#     return b + a


# print('НОД чисел 70 120=', nod(70, 120))

# from math import gcd

# print(gcd(70, 120))

# # поворот строки

# some_string = 'я не сегодня заболел!'


# def reversee(s):
#     chars = list(s)

#     for i in range(len(s) // 2):
#         #         до середины
#         temp = chars[i]
#         chars[i] = chars[len(s) - i - 1]
#         chars[len(s) - i - 1] = temp

#     return ''.join(chars)

# print(some_string)
# print(reversee(some_string))
# print(some_string[::-1])





