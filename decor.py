import time


def time_function(function):
    def wrapped(*args):
        start_time = time.perf_counter()
        result = function(*args)
        print(f'Time execution: {time.perf_counter() - start_time}')
        return result
    return wrapped
