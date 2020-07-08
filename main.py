from collections import OrderedDict

# print('hello world')

# day1 = ('monday', 'tuesday', 'wednesday')
# day2 = ('thursday', 'friday', 'saturday' , 'sunday')
# day3 = ('thursday', 'friday', 'saturday' , 'sunday', day1)

# day = day1 + day2
# print('Day: ', end="")
# print(day)
# print(day3)
# print(day3[1][0][0])
# a = 7 // 4.0
# print(type(a))

# from decimal import Decimal

# print(Decimal(0.1 + 0.2))
# print(Decimal(0.3))

# myString = 'abcdefgh'

# print(len(myString))

# print(myString[1:])
# print(myString[1:-1])
# print(myString[:])

# print(myString.split('h'))

# my_list = ['g', 'i','a', 'h','b', 'e', 'c', 'd', 'e', 'f']
# print(my_list)

# my_list.sort()
# my_sorted_list = my_list
# print(my_sorted_list)
# print(my_list)

# my_dict = {}
# my_dict['key6'] = 600
# my_dict['key1'] = 100
# my_dict['key7'] = 700
# my_dict['key9'] = 900
# my_dict['key5'] = 500
# my_dict['key2'] = 200
# my_dict['key8'] = 800
# my_dict['key3'] = 300
# my_dict['key4'] = 400


# print(my_dict)
# print(my_dict.items())
# print(my_dict.keys())
# print(my_dict.values())

# my_dict['key8'] = 800
# print(my_dict)
# my_dict['key1'] = 1000
# print(my_dict)

# for key, value in my_dict.items():
#     print(key, value)

# print("This is a Dict:\n") 
# d = {} 
# d['a'] = 1
# d['b'] = 2
# d['c'] = 3
# d['d'] = 4
  
# for key, value in d.items(): 
#     print(key, value) 

# print("\nThis is an Ordered Dict:\n") 
# od = OrderedDict() 
# od['a'] = 1
# od['b'] = 2
# od['c'] = 3
# od['d'] = 4
  
# for key, value in od.items(): 
#     print(key, value) 


# my_od = OrderedDict()
# my_od['a'] = 100
# my_od['e'] = 500
# my_od['c'] = 300
# my_od['d'] = 400
# my_od['b'] = 200

# for key, value in my_od.items():
#     print(key, value)

# print("\nAfter:\n") 
# my_od['e'] = 5000

# for key, value in my_od.items():
#     print(key, value)

# print(my_od)


# BOOLEAN
# print(1 > 2)
# print(0.1 == 0.1)
# print((0.4 - 0.3) == 0.1)
# b = None
# print(None == b)
# print(type(b))
# print(-False)
# print(-True)


# lap lai 3 ki tu trong chuoi 
def front3(str):
    front_end = 3
    if len(str) < front_end:
        front = str * 3
        return front
    else:
        front = str[0:front_end]
        return front * 3

# print(front3('as'))

# dao 2 ki tu dau tien va cuoi cung 
def front_back(str):
    if len(str) < 2:
        return str
    else:
        firstChar = str[0]
        lastChar = str[-1]
        middleText = str[1:-1]
        result = lastChar + middleText + firstChar
        return result

# print(front_back('asdasdasdasdqwettt'))

# week is false or vacation is true thi return true, unless return false
def sleep_in(week, vacation):
    if not week or vacation:
        return True
    else:
        return False

# print(sleep_in(True, True))
# print(sleep_in(True, False))
# print(sleep_in(False, False))
# print(sleep_in(False, True))

# Co 2 con khi, cung cuoi hoac cung ko cuoi thi tra ve true, con ko thi tra ve false
def monkey_trouble(a_smile, b_smile):
    if a_smile and b_smile:
        return True
    elif not a_smile and not b_smile:
        return True
    else: 
        return False
    
# print(monkey_trouble(True, True))
# print(monkey_trouble(True, False))
# print(monkey_trouble(False, False))
# print(monkey_trouble(False, True))

# cho 2 so nguyen, tinh tong cua chung, neu 2 so do giong y chang nhau thi tra ve x2 lan tong cua no
def sum_double(a, b):
    result = 0
    if a == b:
        result = (a + b) * 2
        return result
    else:
        result = a + b
        return result

# print(sum_double(5, 10))
# print(sum_double(100, 100))

# nhan zo 1 so nguyen n, tinh khoang cach tuyet doi giua n va so 21, neu n > 21 thi ra ve gap doi
def diff21(n):
    result = 0
    if n > 21:
        result = (n - 21) * 2
        return result
    else:
        result = 21 - n
        return result

# print(diff21(1))
# print(diff21(19))
# print(diff21(21))
# print(diff21(121))
# print(diff21(-1))

# co 1 con vet, tra ve true neu con vet dang noi va thoi gian no noi o khoang truoc 7h va sau 20h
def parrot_trouble(talking, hour):
    if talking and (hour < 7 or hour > 20):
        return True
    else:
        return False

print(parrot_trouble(True, 5))
print(parrot_trouble(False, 15))
print(parrot_trouble(True, 15))
print(parrot_trouble(False, 21))
print(parrot_trouble(True, 20))