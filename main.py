def decompose(num: int):
    """generate all digits from number"""
    while num:
        yield num % 10
        num = num // 10


def sum_digits(number: int) -> int:
    """get sum of all digits in number"""
    if number == 0:
        return 0
    else:
        return int(number % 10) + sum_digits(int(number / 10))


class Probability:

    def __init__(self, sum_: int, dice_amount: int):
        self.sum_ = sum_
        self.dice_amount = dice_amount
        if not isinstance(self.sum_, int):
            print(f"Expected type 'int', got {type(sum_)} instead in sum_")
            raise TypeError
        elif not isinstance(self.dice_amount, int):
            print(f"Expected type 'int', got {type(dice_amount)} instead in sum_")
            raise TypeError

    def rolldice_sum_probability(self) -> float:
        """find probability that the result of sum from throwing {dice_amount} dice, will equal {sum_}"""

        sum_ = self.sum_
        dice_amount = self.dice_amount

        if sum_ > 6 * dice_amount:  # sum of results from throwing dice can't be larger than {6 * dice_amount}
            return 0

        # generate list of digits from 111.. to 666...
        lst = []
        start_num = int('1' * dice_amount)  # 111...
        end_num = 6 * int('1' * dice_amount)  # 666...
        for i in range(start_num, end_num + 1):
            lst.append(i)

        lst2 = []
        for i in lst:
            if all(6 >= x > 0 for x in decompose(i)):  # check if all digits in number are > 0 and <= 6
                lst2.append(i)

        count = 0
        for i in lst2:
            if sum_digits(i) == sum_:
                count += 1  # increment {count} if sum of digits in number equals to {sum_}

        probability = count / 6 ** dice_amount

        return probability


ex = Probability(, )
print(ex.rolldice_sum_probability())
