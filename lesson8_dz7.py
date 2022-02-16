class Complex:
    i_real: int
    i_imaginary: int

    def __init__(self, i_real: int, i_imaginary: int):
        self.i_real = i_real
        self.i_imaginary = i_imaginary

    def __add__(self, other):
        return Complex(self.i_real+other.i_real, self.i_imaginary+other.i_imaginary)

    def __mul__(self, other):
        return Complex(self.i_real*other.i_real - self.i_imaginary*other.i_imaginary,
                       self.i_real*other.i_imaginary + other.i_real*self.i_imaginary)

    def __str__(self):
        if self.i_imaginary >= 0:
            return f"{self.i_real} + {self.i_imaginary}i"
        else:
            return f"{self.i_real} - {abs(self.i_imaginary)}i"


cm_a = Complex(4, -7)
cm_b = Complex(2, 3)
cm_c = Complex(-2, -1)

print(f"\t({cm_a}) + ({cm_b}) = {cm_a+cm_b}")
print(f"\t({cm_a}) * ({cm_b}) = {cm_a*cm_b}")

print(f"\t({cm_b}) + ({cm_c}) = {cm_b+cm_c}")
print(f"\t({cm_b}) * ({cm_c}) = {cm_b*cm_c}")
