class Farm_Animals:
    def __init__(self, meat: int):
        self.meat = meat

    def __str__(self):
        return f'В результате смерти животного, мы получим {self.meat} грамм мяса'

    def __repr__(self):
        return f"{self.__class__.__name__}(meat={self.meat!r})"


class Mammals(Farm_Animals):
    def __init__(self, meat: int, pelt: str):
        super().__init__(meat)
        self.pelt = pelt
        if not isinstance(pelt, str):
            raise TypeError(f'{self.pelt} должен содержать в себе текст: "маленького", "среднего", "большого"')

    def __str__(self):
        super_str = super().__str__()
        return f'{super_str}. Шкура {self.pelt} размера'

    def __repr__(self):
        super_repr = super().__repr__()
        return f"{super_repr}, (pelt={self.pelt!r})"


class Cattle(Mammals):
    def __init__(self, meat: int, pelt: str):
        super().__init__(meat, pelt)

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return super().__repr__()


class SmallCattle(Mammals):
    def __init__(self, meat: int, pelt: str, wool: int):
        super().__init__(meat, pelt)
        if isinstance(wool, int):
            if wool > 0:
                self.wool = wool
            else:
                raise ValueError('Количество шерсти должно быть выражено в числовом формате')
        else:
            raise ValueError("Шерсть не собрана")

    def __str__(self):
        super_puper = super().__str__()
        return f'Шерсть: {self.wool} грамм. {super_puper}'

    def __repr__(self):
        repr_puper = super().__repr__()
        return f'{repr_puper}, (wool={self.wool!r})'


class Poultry(Farm_Animals):
    def __init__(self, meat: int, feathers, eggs: int):
        super().__init__(meat)
        self.feathers = feathers
        if isinstance(eggs, int):
            if eggs > 0:
                self.eggs = eggs
            else:
                raise ValueError('Яиц еще нет')
        else:
            raise ValueError("Количество яиц должно быть в виде числа")

    def __str__(self):
        return f'Количество яиц: {self.eggs}. Перья: {self.feathers}. В результате смерти животного, мы получим {self.meat} грамм мяса'

    def __repr__(self):
        return f'{self.__class__.__name__}(meat={self.meat!r}), (feathers={self.feathers!r}), (eggs={self.eggs!r})'


class Fish(Farm_Animals):
    def __init__(self, meat: int, caviar: int):
        super().__init__(meat)
        if isinstance(caviar, int):
            if caviar > 0:
                self.caviar = caviar
            else:
                raise ValueError('Количество икры не записано')
        else:
            raise ValueError('Количество собранной икры должно быть записано числом')

    def __str__(self):
        str_super = super().__str__()
        return f'Икры: {self.caviar} грамм. {str_super}'

    def __repr__(self):
        repr_super = super().__repr__()
        return f'{repr_super}, (caviar={self.caviar!r}).'


if __name__ == "__main__":
    cow = Cattle(550000, "большого")
    print(cow)
    ram = SmallCattle(35000, "маленького", 10000)
    print(ram)
    beluga = Fish(500, 100)
    print(beluga)
    chicken = Poultry(350, "нет", 7)
    print(chicken)
    pass
