class ExceptionZeroDiv(ZeroDivisionError):
    f_divisible: float
    f_divisor: float

    def __init__(self, f_divisible: float, f_divisor: float) -> None:
        self.f_divisible = f_divisible
        self.f_divisor = f_divisor

    def __str__(self):
        return f"\tДелимиое {self.f_divisible} делитель {self.f_divisor}. Делить на ноль нельзя"


class MyFloat(float):
    my_float: float

    def __init__(self, inc_float: float) -> None:
        self.my_float = float(inc_float)

    def __truediv__(self, other):
        if other == 0:
            raise ExceptionZeroDiv(self.my_float, other)
        else:
            return MyFloat(self.my_float / other)

    def __floordiv__(self, other):
        if other == 0:
            raise ExceptionZeroDiv(self.my_float, other)
        else:
            return MyFloat(self.my_float // other)

    def __mod__(self, other):
        if other == 0:
            raise ExceptionZeroDiv(self.my_float, other)
        else:
            return MyFloat(self.my_float % other)

    def __divmod__(self, other) -> tuple:
        if other == 0:
            raise ExceptionZeroDiv(self.my_float, other)
        else:
            return divmod(self.my_float, other)

    def __itruediv__(self, other):
        if other == 0:
            raise ExceptionZeroDiv(self.my_float, other)
        else:
            self.my_float /= other
            return MyFloat(self.my_float)

    def __ifloordiv__(self, other):
        if other == 0:
            raise ExceptionZeroDiv(self.my_float, other)
        else:
            self.my_float //= other
            return MyFloat(self.my_float)

    def __imod__(self, other):
        if other == 0:
            raise ExceptionZeroDiv(self.my_float, other)
        else:
            self.my_float %= other
            return MyFloat(self.my_float)


a = MyFloat(11)
b = MyFloat(2)
c = MyFloat(0)

a /= b
print(f"\t{a}")
try:
    print(f"\t{a/b}")
    print(f"\t{a/0}")
    print(f"\t{a/c}")
    print(f"\t{c/0}")
    print(f"\t{c/a}")
except ExceptionZeroDiv as error:
    print(error)
print()
