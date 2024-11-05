from copy import copy
from random import randint


class Bignum:
    def __init__(self, value: int) -> None:
        self.value = num_to_array(value)
        self.length = len(self.value)


    def __add__(self, other):
        res = []
        result = 0
        carry = 0
        index = 0
        final = Bignum(0)
        while True:
            if index < self.length and index < other.length:
                temp = self.value[index] + other.value[index] + carry
                result = temp & 0xFF
                carry = (temp - result) // 256
                res.append(result)
            elif index < self.length:
                res.append(self.value[index] + carry)
                res += self.value[index+1:]
                final.value = res
                return final
            elif index < other.length:
                res.append(other.value[index] + carry)
                res += other.value[index+1:]
                final.value = res
                return final
            else:
                res.append(carry)
                final.value = res
                return final
            index += 1


    def __sub__(self, other):
        res = []
        result = Bignum(0)
        borrow = 0
        index = 0
        len_a = self.length
        len_b = other.length
        while index < len_a:
            a_byte = self.value[index]
            b_byte = other.value[index] if index < len_b else 0
            temp = a_byte - b_byte - borrow
            if temp < 0:
                temp += 256
                borrow = 1
            else:
                borrow = 0
            res.append(temp)
            index += 1
            if borrow == 0 and index >= len_b:
                res.extend(self.value[index:])
                break
        if borrow != 0 or index < len_b:
            raise ValueError("Result is negative")
        while len(res) > 1 and res[-1] == 0:
            res.pop()
        result.value = res
        return result
    
    
    def __le__(self, other) :
        return self.length < other.length or (self.length == other.length and self.value[-1] < other.value[-1])



    def __mod__(self, other):
        res = []
        result = Bignum(0)
        return result # TODO: implement this
        



def num_to_array(num: int) -> list[int]:
    res = []
    n = copy(num) # TODO: probably unnecessary
    while n > 0:
        res.append(n & 0xFF)
        n >>= 8

    return res


def array_to_num(arr: list[int]) -> int:
    n = 0
    for ind, value in enumerate(arr):
        n += value << (8 * ind)
    return n


def test_add():
    print("Testing ADD:")

    num1 = randint(1, 100000000)
    num2 = randint(1, 100000000)

    big1 = Bignum(num1)
    big2 = Bignum(num2)
    
    print(f"{num1=}")
    print(f"{num2=}")
    
    expected = num1 + num2
    print(f"{expected=}")
    
    result = big1 + big2
    print(f"{result=}")

    result_num = array_to_num(result.value)
    assert result_num == expected


def test_sub():
    print("Testing SUB:")
    num1 = randint(1, 100000000)
    num2 = randint(1, num1)

    big1 = Bignum(num1)
    big2 = Bignum(num2)
    
    print(f"{num1=}")
    print(f"{num2=}")
    
    expected = num1 - num2
    print(f"{expected=}")
    
    result = big1 - big2
    print(f"{result=}")

    result_num = array_to_num(result.value)
    assert result_num == expected



if __name__ == "__main__":
    for i in range(10):
        test_sub()
