# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/


def sleep_in(weekday, vacation):
    if weekday is True and vacation is True:
        return True
    if weekday is not True or vacation is True:
        return True
    else:
        return False


# print(sleep_in(True, True))
# print(sleep_in(True, False))
# print(sleep_in(False, True))


def monkey_trouble(a_smile, b_smile):
    if a_smile == b_smile:
        return True
    else:
        return False
    # if not a_smile or not b_smile:
    #     return False
    # else:
    #     return True


# print(monkey_trouble(True, True))
# print(monkey_trouble(False, False))
# print(monkey_trouble(True, False))

a = 'kitten'
# print(len(a))
# print(a[1:len(a)-1])
middle = a[1:len(a) - 2]
start = a[0]
end = a[len(a) - 1]
print(end + middle + start)

print(''.join(reversed(a)))


def front_back(str):
    if len(str) == 0:
        return ''

    if len(str) == 1:
        return str
    elif len(str) == 2:
        return ''.join(reversed(str))
    else:
        middle = str[1:len(str) - 2]
        start = str[0]
        end = str[len(str) - 1]
        return end + middle + start


#
# print(front_back('code'))
# print(front_back('a'))
# print(front_back('ab'))

def array_front9(nums):
    if len(nums) < 4 and nums[:].count(9) > 0:
        return True
    elif len(nums) > 4 and nums[:3].count(9) > 0:
        return True
    else:
        return False


# print(array_front9([1,2,9]))
# print(array_front9([1, 2, 9, 3, 4]))
# print(array_front9([1, 2, 3, 4, 9]))
# print(array_front9([1, 2, 3, 4, 5]))

def array123(nums):
    for num in range(len(nums)):
        if nums[num:num + 3] == [1, 2, 3]:
            return True
    return False


# print(array123([1, 1, 2]))
# print(array123([1, 1, 2, 4, 1]))
# print(array123([1, 1, 2, 1, 2, 3]))

# print(sum([1,2,3]))

# print(max([2, 5, 7, 23, 23, 6, 2, 6, 125, 7, 8]))
# print(min([2, 5, 7, 23, 23, 6, 2, 6, 125, 7, 8]))

from operator import itemgetter, attrgetter

class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))

student_objects = [
    Student('john', 'A', 99),
    Student('gur', 'Z', 68),
    Student('jane', 'B', 23),
    Student('dave', 'B', 74),
    Student('asd', 'D', 17),
    Student('aty', 'E', 17),
]


# print(student_objects)
#
# print(sorted(student_objects, key = attrgetter('age')))
#
# student_tuple = tuple(student_objects)
# print(sorted(student_tuple), key=itemgetter(1))

a, b, c = (1, 2, 3, 4, 5, 6, 7, 8, 9)[1::3]

print(b)