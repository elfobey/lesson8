class Date:
    @classmethod
    def parse_date(cls, inc_date: str) -> tuple:
        year: int = -1
        month: int = -1
        day: int = -1

        separators_list: list = [' ', '.', '/', '-', '_', '\\']
        split_list: list = [inc_date]

        for sp in separators_list:
            internal_list: list = []
            for el in split_list:
                internal_list.extend(el.split(sp))
            split_list = internal_list

        numbers_list: list = []
        for el in split_list:
            if str(el).isdecimal() and len(el) < 5:
                numbers_list.append(int(el))

        len_four: int = 0
        for ind in reversed(range(len(numbers_list))):
            if len(str(numbers_list[ind])) == 4:
                len_four = ind

        if len(numbers_list) > 2:
            if len_four:
                day = numbers_list[0]
                month = numbers_list[1]
                year = numbers_list[2]
            else:
                year = numbers_list[0]
                month = numbers_list[1]
                day = numbers_list[2]

        return year, month, day

    @staticmethod
    def check_date(check_str: str) -> bool:
        date_corr: bool = True
        year, month, day = Date.parse_date(check_str)
        if not 0 <= year <= 3000:
            date_corr = False
        if not 1 <= month <= 12:
            date_corr = False
        if month in [1, 3, 5, 7, 8, 10, 12]:
            if not 1 <= day <= 31:
                date_corr = False
        elif month in [4, 6, 9, 11]:
            if not 1 <= day <= 30:
                date_corr = False
        elif month == 2:
            if not 1 <= day <= 29:
                date_corr = False
        return date_corr


my_date = Date()
date_1 = " ллапоо щащпщдддв ыв _2022/02\\16-ачарыр==="
print(f"\t{my_date.parse_date(date_1)}")
if my_date.check_date(date_1):
    print("\t\tДата корректна")
else:
    print("\t\tДата некорректна")

date_2 = "влвллплв паищлыщал пыпалвып_1922_07_19 ог врыапгшаыпр"
print(f"\t{my_date.parse_date(date_2)}")
if my_date.check_date(date_2):
    print("\t\tДата корректна")
else:
    print("\t\tДата некорректна")

date_3 = "влвалдвдад 31/2/1175 выапаавпр"
print(f"\t{my_date.parse_date(date_3)}")
if my_date.check_date(date_3):
    print("\t\tДата корректна")
else:
    print("\t\tДата некорректна")
print()
