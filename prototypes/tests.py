from copy import copy
from random import randint


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



def add(a: list[int], b: list[int]) -> list[int]:
    """
    This function adds two numbers, represented as byte-arrays, without going back to number representation to allow for arbitrary-sized ints
    """
    res = []
    result = 0
    carry = 0
    index = 0
    while True:
        print(f"{carry=}")
        if index < len(a) and index < len(b):
            temp = a[index] + b[index] + carry
            result = temp & 0xFF
            carry = (temp - result) // 256
            res.append(result)
        elif index < len(a):
            res.append(a[index] + carry)
            res += a[index+1:]
            return res
        elif index < len(b):
            res.append(b[index] + carry)
            res += b[index+1:]
            return res
        else:
            res.append(carry)
            return res
        index += 1


def test_add():
    print("Testing ADD:")

    num1 = randint(1, 100000000)
    num2 = randint(1, 100000000)
    
    print(f"{num1=}")
    print(f"{num2=}")
    
    expected = num1 + num2
    print(f"{expected=}")
    
    arr1 = num_to_array(num1)
    arr2 = num_to_array(num2)
    
    print(f"{arr1=}")
    print(f"{arr2=}")


    result = add(arr1, arr2)
    print(f"{result=}")

    result_num = array_to_num(result)
    print(f"{result_num=}")

    assert result_num == expected


if __name__ == "__main__":
    for i in range(10):
        test_add()
