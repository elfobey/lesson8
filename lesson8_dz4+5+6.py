class OfficeEqStorage:
    _unit_counter: int
    _unit_names_list: list

    def __init__(self):
        self._unit_counter = 0
        self._unit_names_list = []

    def __str__(self):
        return f"\tНа складе: {self._unit_counter} единиц хранения\n\t\t{self._unit_names_list}"

    def store_unit(self, name: str):
        self._unit_counter += 1
        self._unit_names_list.append(name)
        print(f"\tПолучен на склад: {name}")

    def get_from_store_unit(self) -> str:
        if self._unit_counter:
            self._unit_counter -= 1
            unit_name = self._unit_names_list.pop()
            print(f"\tВыдан со склада: {unit_name}")
            return unit_name
        else:
            print(f"\tСклад пуст!")
            return "Пусто"


class OfficeEquipment:
    _name: str
    _type_unit: str

    def __init__(self, name: str, type_unit: str):
        self._name = name
        self._type_unit = type_unit

    def __str__(self):
        return f"\t{self._type_unit} {self._name}\n"

    def get_name(self):
        return self._name

    def get_type(self):
        return self._type_unit


class Printer(OfficeEquipment):
    __print_counter: int

    def __init__(self, name: str):
        super(Printer, self).__init__(name, "Принтер")
        self.__print_counter = 0

    def __str__(self):
        return super(Printer, self).__str__() + f"\t\t{self.get_type()} {self.get_name()} - " \
                                                f"счётчик печати: {self.__print_counter}"

    def make_print(self):
        self.__print_counter += 1

    def get_print_counter(self):
        return self.__print_counter


class Scanner(OfficeEquipment):
    __scan_counter: int

    def __init__(self, name: str):
        super(Scanner, self).__init__(name, "Сканер")
        self.__scan_counter = 0

    def __str__(self):
        return super(Scanner, self).__str__() + f"\t\t{self.get_type()} {self.get_name()} - " \
                                                f"счётчик сканирования: {self.__scan_counter}"

    def make_scan(self):
        self.__scan_counter += 1

    def get_scan_counter(self):
        return self.__scan_counter


class Copier(OfficeEquipment):
    __copy_counter: int

    def __init__(self, name: str):
        super(Copier, self).__init__(name, "Копир")
        self.__copy_counter = 0

    def __str__(self):
        return super(Copier, self).__str__() + f"\t\t{self.get_type()} {self.get_name()} - " \
                                               f"счётчик копирования: {self.__copy_counter}"

    def make_copy(self):
        self.__copy_counter += 1

    def get_copy_counter(self):
        return self.__copy_counter


printer_1 = Printer("HP 1536")
printer_1.make_print()
print(printer_1)

scanner_1 = Scanner("Epson 310")
scanner_1.make_scan()
scanner_1.make_scan()
print(scanner_1)

copier_1 = Copier("Xerox 1000")
copier_1.make_copy()
copier_1.make_copy()
copier_1.make_copy()
print(copier_1)

store = OfficeEqStorage()
store.get_from_store_unit()
store.store_unit(printer_1.get_name())
store.store_unit(scanner_1.get_name())
store.store_unit(copier_1.get_name())
print(store)
unit_1 = store.get_from_store_unit()
unit_2 = store.get_from_store_unit()
print(store)
print()
