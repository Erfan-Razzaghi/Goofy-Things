from goofy_base64.base64 import Base64ToolKit as b64
import base64
import timeit


if __name__ == "__main__":    

    test_string = "Hello World33" * 10
    timer = timeit.Timer(lambda: b64.encode(test_string))
    for i in range(10):
        t = timer.timeit(number=10000)
        print(f"Iteration {i+1}: {t:.6f} seconds")
    

    timer_builtin = timeit.Timer(lambda: base64.b64encode(test_string.encode()))
    for i in range(10):
        t = timer_builtin.timeit(number=10000)
        print(f"Iteration {i+1}: {t:.6f} seconds")