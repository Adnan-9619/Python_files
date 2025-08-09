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