# Задание в Python:
# 1. Написать функцию, которая принимает на вход список целых чисел и возвращает новый список, содержащий только уникальные элементы из исходного списка.
def unique_numbers(l: list[int]) -> list[int]:
    list_with_unique_values = list(set(l))
    return list_with_unique_values

def unique_numbers_save_subsequence(l: list[int]) -> list[int]:
    list_with_unique_values = []

    # Solution 1
    for i in l:
        if i not in list_with_unique_values:
            list_with_unique_values.append(i)

    # Solution 2
    # [list_with_unique_values.append(i) for i in l if i not in list_with_unique_values]

    return list_with_unique_values


def unique_numbers_using_dict(l: list[int]) -> list[int]:
    return [*dict.fromkeys(l).keys()]

assert unique_numbers([6,7,9, 1,1,2,3,4,5,5,3,12,2,3]) == [1, 2, 3, 4, 5, 6, 7, 9, 12], "error unique_numbers"
assert unique_numbers_save_subsequence([6,7,9, 1,1,2,3,4,5,5,3,12,2,3]) == [6, 7, 9, 1, 2, 3, 4, 5, 12], "error unique_numbers_save_subsequence"
assert unique_numbers_using_dict([6,7,9, 1,1,2,3,4,5,5,3,12,2,3]) == [6, 7, 9, 1, 2, 3, 4, 5, 12], "error unique_numbers_using_dict"
###############################################################################################################################################################

# 2. Написать функцию, которая принимает на вход два целых числа (минимум и максимум) и возвращает список всех простых чисел в заданном диапазоне.
from typing import Union

def isPrime(number:int)->bool:
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def select_prime_numbers_in_range(min:int, max:int)-> list[int]:
    return [x for x in range(min, max) if isPrime(x)]

assert select_prime_numbers_in_range(3,50) == [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47], "Error"
################################################################################################################################################################


# 3. Создать класс Point, который представляет собой точку в двумерном пространстве. 
# Класс должен иметь методы для инициализации координат точки, 
# вычисления расстояния до другой точки, а также для получения и изменения координат.

from dataclasses import dataclass
from typing import Tuple

@dataclass
class Point:
    x: int = 0
    y: int = 0

    @property
    def coord(self)-> Tuple[int,int]:
        return (self.x, self.y)
    
    @coord.setter
    def new_coord(self, x:int, y:int):
        self.x = x
        self.y = y

    def distance_to(self, x:int, y:int) -> float:
        return ((self.x - x)**2 + (self.y - y)**2)**0.5
    
point = Point(5,5)
print("get coord: ", point)
point = Point(15,15)
print("updated: ", point)
print(f"distance_to (20,20): %.2f" % point.distance_to(20,20))
################################################################################################################################################################

# 4. Написать программу, которая сортирует список строк по длине, сначала по возрастанию, а затем по убыванию.
from enum import Enum

class DirectionClass(Enum):
    RISING = 0
    DESCENDING = 1

test_string = ['Написать', 'программу,', 'которая', 'сортирует', 'список', 'строк', 'по', 'длине,', 'сначала', 'по', 'возрастанию,', 'а', 'затем', 'по', 'убыванию.']

@dataclass
class Sorted_To_Direction:
    data: list[str]
    direction: Union[DirectionClass] = Union[ DirectionClass ]

    def sort(self):
        if self.direction == DirectionClass.RISING:
            self.direction = DirectionClass.DESCENDING
            return list(sorted(self.data, key=len, reverse=True))

        self.direction = DirectionClass.RISING
        return list(sorted(self.data, key=len))


l = Sorted_To_Direction(test_string)

print(l.sort())
print(l.sort())
