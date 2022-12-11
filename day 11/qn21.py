from abc import ABC, abstractmethod
file = open("inputs.txt", "r")
values = file.read()
inputvalues = values.splitlines()
inputs = []


class MonkeyInterface(ABC):
    def __init__(self, initialValues, monkeyfail, monkeysucceed) -> None:
        self.initialValues = initialValues
        self.failMonkey = monkeyfail
        self.succeedMonkey = monkeysucceed
        self.total = 0

    def inspect(self, worry):
        newworry = self.operation(worry)
        newworry = newworry//3
        return newworry

    @abstractmethod
    def operation(self, item):
        pass

    def testdivisibility(self, worry):
        remainder = self.findremainder(worry)
        if remainder == 0:
            return True
        else:
            return False

    @abstractmethod
    def findremainder(self, worry):
        pass


class Monkey0(MonkeyInterface):

    def __init__(self, initialValues, monkeyfail, monkeysucceed) -> None:
        super(Monkey0, self).__init__(initialValues, monkeyfail, monkeysucceed)

    def operation(self, item):
        return item*17

    def findremainder(self, worry):
        return worry % 3


class Monkey1(MonkeyInterface):

    def __init__(self, initialValues, monkeyfail, monkeysucceed) -> None:
        super(Monkey1, self).__init__(initialValues, monkeyfail, monkeysucceed)

    def operation(self, item):
        return item*11

    def findremainder(self, worry):
        return worry % 5


class Monkey2(MonkeyInterface):

    def __init__(self, initialValues, monkeyfail, monkeysucceed) -> None:
        super(Monkey2, self).__init__(initialValues, monkeyfail, monkeysucceed)

    def operation(self, item):
        return item+4

    def findremainder(self, worry):
        return worry % 2


class Monkey3(MonkeyInterface):

    def __init__(self, initialValues, monkeyfail, monkeysucceed) -> None:
        super(Monkey3, self).__init__(initialValues, monkeyfail, monkeysucceed)

    def operation(self, item):
        return item*item

    def findremainder(self, worry):
        return worry % 13


class Monkey4(MonkeyInterface):

    def __init__(self, initialValues: list, monkeyfail: int, monkeysucceed: int) -> None:
        super(Monkey4, self).__init__(initialValues, monkeyfail, monkeysucceed)

    def operation(self, item):
        return item+7

    def findremainder(self, worry):
        return worry % 11


class Monkey5(MonkeyInterface):

    def __init__(self, initialValues, monkeyfail, monkeysucceed) -> None:
        super(Monkey5, self).__init__(initialValues, monkeyfail, monkeysucceed)

    def operation(self, item):
        return item+8

    def findremainder(self, worry):
        return worry % 17


class Monkey6(MonkeyInterface):

    def __init__(self, initialValues, monkeyfail, monkeysucceed) -> None:
        super(Monkey6, self).__init__(initialValues, monkeyfail, monkeysucceed)

    def operation(self, item):
        return item+5

    def findremainder(self, worry):
        return worry % 19


class Monkey7(MonkeyInterface):

    def __init__(self, initialValues, monkeyfail, monkeysucceed) -> None:
        super(Monkey7, self).__init__(initialValues, monkeyfail, monkeysucceed)

    def operation(self, item):

        return item+3

    def findremainder(self, worry):
        return worry % 7


monkeys = {
    0: Monkey0([99, 67, 92, 61, 83, 64, 98], 2, 4),
    1: Monkey1([78, 74, 88, 89, 50], 5, 3),
    2: Monkey2([98, 91], 4, 6),
    3: Monkey3([59, 72, 94, 91, 79, 88, 94, 51], 5, 0),
    4: Monkey4([95, 72, 78], 6, 7),
    5: Monkey5([76], 2, 0),
    6: Monkey6([69, 60, 53, 89, 71, 88], 1, 7),
    7: Monkey7([72, 54, 63, 80], 3, 1)
}

for _ in range(20):
    for i in range(8):
        length = len(monkeys[i].initialValues)
        for _ in range(length):
            x = monkeys[i].initialValues.pop(0)
            monkeys[i].total += 1
            inspectedvalue = monkeys[i].inspect(x)
            if monkeys[i].findremainder(inspectedvalue) == 0:
                monkeys[monkeys[i].succeedMonkey].initialValues.append(
                    inspectedvalue)
            else:
                monkeys[monkeys[i].failMonkey].initialValues.append(
                    inspectedvalue)

for i in range(8):
    print(monkeys[i].total)
