class ExceptionListOfNumbers(Exception):
    st_not_number: str

    def __init__(self, st_not_number: str) -> None:
        self.st_not_number = str(st_not_number)

    def __str__(self):
        return f"\tЗначение {self.st_not_number} не является целым числом! Будет проигнорировано"


class NumbersList(list):
    def __init__(self, income_list: list):
        filtered_inc_list = []
        for el in income_list:
            if str(el).isdecimal():
                filtered_inc_list.append(int(el))
            else:
                try:
                    raise ExceptionListOfNumbers(str(el))
                except ExceptionListOfNumbers as err:
                    print(err)

        super(NumbersList, self).__init__(filtered_inc_list)

    def append(self, __object) -> None:
        if str(__object).isnumeric():
            super().append(int(__object))
        else:
            raise ExceptionListOfNumbers(str(__object))

    def extend(self, __iterable) -> None:
        for el in __iterable:
            if str(el).isdecimal():
                super().append(int(el))
            else:
                raise ExceptionListOfNumbers(str(el))


my_list = NumbersList([12, 34, "'привет, я целое число'", 5656, 345.45])
while True:
    try:
        input_value = input("\tВведите целое число: ")
        if input_value == 'стоп':
            break
        my_list.append(input_value)
    except ExceptionListOfNumbers as error:
        print(error)

print(f"\t{my_list}\n")
