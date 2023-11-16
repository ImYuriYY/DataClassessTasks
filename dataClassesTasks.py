from dataclasses import dataclass, field, InitVar, make_dataclass
from random import randint
from typing import Any






# Задание "Воздушный замок"

# @dataclass(order=True)
# class AirCastle:
#     height: int
#     clouds: int
#     color: str

#     def change_height(self, value):
#         self.height = value if value > -1 else 0


#     def visible(self, vis):
#         return f'Видимость замка: {self.height // vis * self.clouds}'


#     def __add__(self, other):
#         if not isinstance(other, int):
#             raise TypeError("ERROR!ERROR!ERROR!")
#         self.clouds += other
#         self.height += other // 5

#         return AirCastle(self.height, self.clouds, self.color)

#     def __str__(self):
#         return f'The AirCastle at an altitude of {self.height}, meters is {self.color}, with {self.clouds}'



# c = AirCastle(22,33,"red")
# c2 = AirCastle(22,33,"red")

# print(c == c2)
# print(c != c2)
# print(c >= c2)
# print(c <= c2)









# Задание "Добрый ифрит"

# @dataclass(order=True)
# class GoodIfrit:
#     height: int
#     name: str
#     goodness: int

#     def change_goodness(self, value):
#         if(self.goodness + value > 0):
#             self.goodness += value
#         else:
#             self.goodness = 0

#     def __add__(self, other):
#         if not isinstance(other, int):
#             raise TypeError("ERROR!ERROR!ERROR!")
#         self.height += other
#         return GoodIfrit(self.height, self.name,  self.goodness)
    
#     def __str__(self):
#         return f'Good Ifrit {self.name}, height: {self.height}, goodness: {self.goodness}'
    
#     def __call__(self, arg):
#         return arg * self.goodness // self.height

# print("____________ПЕРВЫЙ ВЫВОД____________")
# gi = GoodIfrit(80, "Harzul", 3)
# gi.change_goodness(4)
# print(gi)
# gi1 = gi + 15
# print(gi1)
# print(gi(31))


# print("____________ВТОРОЙ ВЫВОД____________")
# gi = GoodIfrit(80, "Harzul", 3)
# gi1 = GoodIfrit(80, "Dalziel", 1)
# print(gi < gi1)
# gi1.change_goodness(2)
# print(gi > gi1)
# print(gi, gi1, sep='\n')







# Задание "Волшебник"

# @dataclass(order=True)
# class Wizard:
#     name: str
#     rating: int
#     looksAge: int

#     def check_age(self, age):
#         if age < 18:
#             age = 18
#             return age
#         else:
#             return age

#     def change_rating(self, value):
#         if(self.rating + value > 100):
#             self.rating = 100
#             self.looksAge -= value // 10
#             self.looksAge = self.check_age(self.looksAge)
#         elif(self.rating + value < 0):
#             self.rating = 0
#             self.looksAge += value // 10
#             self.looksAge = self.check_age(self.looksAge)
#         else:
#             self.rating += value
#             self.looksAge -= value // 10
#             self.looksAge = self.check_age(self.looksAge)
    
#     def __add__(self, other):
#         if not isinstance(other, str):
#             raise TypeError("ERROR!ERROR!ERROR!")
#         return Wizard(self.name, self.rating + len(other), self.looksAge - (len(other) // 10))
    
#     def __call__(self, arg):
#         if not isinstance(arg, int):
#             raise TypeError("ERROR!ERROR!ERROR!")
#         return (arg - self.looksAge) * self.rating

#     def __str__(self):
#         return f'Wizard {self.name} with {self.rating} rating looks {self.looksAge} years old'


# wiz = Wizard("Badili", 50, 23)
# wiz.change_rating(25)
# print(wiz.rating)
# print(wiz.looksAge)
# wiz += "aboba"
# print(wiz)
# print(wiz(31))

# wiz2 = Wizard("Caesar", 40, 28)
# print(wiz.rating > wiz2.rating)
# print(wiz.looksAge != wiz2.looksAge)
# print(wiz.name == wiz2.name)


























# РАБОТА НА ЗАНЯТИИ

# class Thing:
#     def __init__(self, name, weight, price, dims = []):
#         self.name = name
#         self.weight = weight
#         self.price = price
#         self.dims = dims
#
#     def __repr__(self):
#         return(f'{self.__dict__}')
#
#
# @dataclass
# class ThingData:
#     name: str
#     weight: int
#     price: float
#     dims: list = field(default_factory=list)
#
#     def __eq__(self, other):
#         return self.price == other.price
#
# th = Thing("name", 15, 1500)
# print(th)
# td = ThingData('name2', 10, 299.99)
# td.dims.append(10)
# print(td)

#
# @dataclass
# class VectorData:
#     x: int
#     y: int = field(compare=False)
#     z: int = field(default=0)
#     calc_len: InitVar[bool] = True
#     length: float = field(init=False, default=0)
#
#
#     def __post_init__(self, calc_len):
#         if calc_len:
#             self.length = (self.x**2 + self.y**2 + self.z**2)**0.5
#
#
#
# class Vector3D:
#     def __init__(self, x, y, z, calc_len):
#         self.x = x
#         self.y = y
#         self.z = z
#         self.length = (self.x**2 + self.y**2 + self.z**2)**0.5 if calc_len else 0
#
#
#
#
#
# # v = Vector3D(1,2,3)
# # print(v.__dict__)
#
# vd = VectorData(1,2)
# print(vd)
# vd2 = VectorData(1,4)
# print(vd2)
# print(vd2 == vd)

#
# @dataclass
# class Goods:
#     current_uid = 0
#
#     uid: int = field(init=False)
#     price: Any = None
#     weight: Any = None
#
#     def __post_init__(self):
#         print('Goods')
#         Goods.current_uid += 1
#         self.uid = Goods.current_uid
#
#
#
#
# class GoodMeassureFactory:
#     @staticmethod
#     def get_init_meassure():
#         return [0,0,0]
#
#
#
#
#
#
# @dataclass
# class Book(Goods):
#     title: str = ""
#     author: str = ""
#     price: int = 0
#     weight: float
#     meassure: list = field(default_factory=GoodMeassureFactory.get_init_meassure)
#
#     def __post_init__(self):
#         print("Book")
#         super().__post_init__()
#
#
# g = Goods(12)
# print(g)
#
# g2 = Goods(124)
# print(g2)
#
#
# b = Book(200,2.5, "Rammov's Earth", "Badili")
# for i in range(len(b.meassure)):
#     b.meassure[i] = randint(1,5)
# print(b)


# class Car:
#     def __init__(self, model, max_speed, price):
#         self.model = model
#         self.max_speed = max_speed
#         self.price = price
#
#     def get_max_speed(self):
#         return self.max_speed
#
#
# CarData = make_dataclass("CarData", [('model', str), 'max_speed', ('price', int, field(default=0))],
#                          namespace={'get_max_speed': lambda self: self.max_speed,
#                                     "get_price": lambda self: self.price})
#
#
# cd = CarData('Lada Granta', 120, 952952)
# print(cd)
# print(cd.get_max_speed())
# print(cd.get_price())








