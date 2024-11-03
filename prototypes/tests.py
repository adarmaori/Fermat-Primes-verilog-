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


def sub(a: list[int], b: list[int]) -> list[int]:
    res = []
    borrow = 0
    index = 0
    len_a = len(a)
    len_b = len(b)
    while index < len_a:
        a_byte = a[index]
        b_byte = b[index] if index < len_b else 0
        temp = a_byte - b_byte - borrow
        if temp < 0:
            temp += 256
            borrow = 1
        else:
            borrow = 0
        res.append(temp)
        index += 1
        if borrow == 0 and index >= len_b:
            res.extend(a[index:])
            break
    if borrow != 0 or index < len_b:
        raise ValueError("Result is negative")
    while len(res) > 1 and res[-1] == 0:
        res.pop()
    return res

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


def test_sub():
    print("Testing SUB:")

    num1 = randint(1, 100000000)
    num2 = randint(1, num1)
    
    print(f"{num1=}")
    print(f"{num2=}")
    
    expected = num1 - num2
    print(f"{expected=}")
    
    arr1 = num_to_array(num1)
    arr2 = num_to_array(num2)
    
    print(f"{arr1=}")
    print(f"{arr2=}")


    result = sub(arr1, arr2)
    print(f"{result=}")

    result_num = array_to_num(result)
    print(f"{result_num=}")

    assert result_num == expected


if __name__ == "__main__":
    for i in range(10):
        test_sub
