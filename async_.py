from decor import time_function
import concurrent.futures


def dividers(num):
    i = 2
    result = [1]
    while i <= num / 2:
        if num % i == 0:
            result.append(i)
        i += 1
    result.append(num)
    return result


@time_function
def factorize(*number):
    list_div_num = []
    with concurrent.futures.ProcessPoolExecutor(4) as executor:
        for num, divider in zip(number, executor.map(dividers, number)):
            list_div_num.append(divider)
    return list_div_num


def async_():
    print(f'\nRealization with ProcessPoolExecutor')
    a, b, c, d = factorize(128, 255, 99999, 10651060)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
                 1521580, 2130212, 2662765, 5325530, 10651060]

    if __name__ == '__main__':
        async_()
