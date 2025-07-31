#single inheritance
# Parent class
"""class Animal:
    def speak(self):
        print("Animal speaks")


class Dog(Animal):
    def bark(self):
        print("Dog barks")


d = Dog()
d.speak()
d.bark()


#multiple inheritance


class Father:
    def skill(self):
        print("father knows everything")


class Mother:
    def work(self):
        print("mother knows cooking")


class child(Father, Mother):
    def hobby(self):
        print("child love both")


a = child()
a.skill()
a.work()
a.hobby()


#Hierarchical inheritance
class Animal:
    def speak(self):
        print("animal speaks")


class Dog(Animal):
    def bark(self):
        print("dog barks")


d = Dog()
d.speak()
d.bark()


class Cat(Animal):
    def meaow(self):
        print("cat meaow")


c = Cat()
c.speak()
c.meaow()

#bubble sort

a = [10, 8, 6, 2]


def bubble_sort(a):
    endindex = len(a)
    for i in range(0, endindex):
        #print(a[i])
        for j in range(0, endindex - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


d = bubble_sort(a)
print(d)
#time complexity = O(n)*2
#space complexity = O(1)

#Reverse Bubble Sort
a = [10, 8, 6, 2]


def bubble_sort(a):
    endindex = len(a)
    for i in range(0, endindex):
        #print(a[i])
        for j in range(0, endindex - i - 1):
            if a[j] < a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


d = bubble_sort(a)
print(d)


#time complexity = O(n)*2
#space complexity = O(1)


#Star Pattern
def pattern(n):
    for i in range(n, 0, -1):
        for j in range(0, i):
            print("*" * i)


num = int(input("Enter a number: "))
pattern(num)

#merge sort
l1 = [23, 23, 4, 54, 3, 2, 4, 5, 455, 34, 534, 53, 4, 34, 34, 53, ]


def merge_Sort(l1):
    if len(l1) <= 1:
        return l1
    midpoint = len(l1)//2
    #print(midpoint)
    leftside = l1[:midpoint]
    rightside = l1[midpoint:]
    #print(leftside)
    #print(rightside)
    left1 = merge_Sort(leftside)
    right1 = merge_Sort(rightside)
    return merging(left1,right1)


def merging(l1,l2):
    result = []
    i = j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            result.append(l1[i])
            i += 1
        else:
            result.append(l2[j])
            j += 1

    result.extend(l1[i:])
    result.extend((l2[j:]))

    return result


a = merge_Sort(l1)
print(a)

#Reverse Merge Sort
l1 = [3, 4, 55, 3, 2, 4, 5, 9, 43]


def merge_sort(l1):
    if len(l1) <= 1:
        return l1
    midpoint = len(l1)//2
    leftside = l1[:midpoint]
    #print(leftside)
    rightside = l1[midpoint:]
    #print(rightside)
    #print(midpoint)
    left1 = merge_sort(leftside)
    right1 = merge_sort(rightside)
    return merging(left1,right1)


def merging(l1,l2):
    result = []
    i = j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] > l2[j]:
            result.append(l1[i])
            i += 1
        else:
            result.append(l2[j])
            j += 1

    result.extend(l1[i:])
    result.extend(l2[j:])

    return result


a = merge_sort(l1)
print(a)

#merge sort with for loop
l1 = [3, 4, 55, 3, 2, 4, 5, 45, 21, 89, 9, 43]


def merge_Sort(l1):
    if len(l1) <= 1:
        return l1
    midpoint = len(l1)// 2
    #print(midpoint)
    leftside = l1[:midpoint]
    rightside = l1[midpoint:]
    #print(leftside)
    #print(rightside)
    left1 = merge_Sort(leftside)
    right1 = merge_Sort(rightside)
    return merging(left1, right1)


def merging(l1, l2):
    result = []
    i = j = 0
    total_length = len(l1) + len(l2)
    for xyz in range(total_length):
        if i < len(l1) and (j >= len(l2) or l1[i] < l2[j]):
            result.append(l1[i])
            i += 1
        else:
            result.append(l2[j])
            j += 1

    return result


a = merge_Sort(l1)
print(a)


#Star Pattern


def print_pattern():
    for i in range(4):
        if i == 0:
            print("*   *    *")
        elif i == 1:
            print("  * *    *")
        elif i == 2:
            print("*   *  *")
        elif i == 3:
            print("  * *    *")


print_pattern()



class Airport:
    def __init__(self,name,age):
        self.name = name
        self.age = age


p1 = Airport("John", 36)
print(p1.name)
print(p1.age)

p1 = Airport("adsnan", 36)
print(p1.name)
print(p1.age)

p1 = Airport("hasnain", 36)
print(p1.name)
print(p1.age)

class MyClass:
    def __init__(self,name,terminal):
        self.name = name
        self.terminal = terminal

    def get_details(self):
        return self.name+'@##@@@#'+self.terminal

p1 = MyClass("adnan", "ssdsdf")
print(p1.get_details())


class A:
    def __init__(self,name):
        self.name = name

    def display(self):
        print("this is A")
        return self.name


p1 = A("adnan")
print(p1.display())


class B:
    def __init__(self,name):
        self.name = name

    def display(self):
        print("this is B")
        return self.name


p1 = B("Zaid")
print(p1.display())


class C(A, B):
    def __init__(self,name):
        super().__init__(name)


p2 = C.__mro__
#print(p2.display())
print(p2)


class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age
        if age <= 10:
            self.age = age
        else:
            self.age = None


c = A("adnan", 26)
print(c.get_name())
print(c.get_age())

c.set_name("zaid")
c.set_age(13)
print(c.get_name())
print(c.get_age())"""

def my_decorater(function):
    def wrapper():
        print("this is my decorator")
        function()
    return wrapper


@my_decorater
def world():
    print("hello world")


world()


def myDecorator(function):
    def call():
        b = 5 + function()
        return b
    return call


@myDecorator
def word():
    a = 5
    return a


a = word()
print(a)


class A:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


c = A("adnan", 34)
print(c.name)
c.name = "hasnain"
print(c.name)


















