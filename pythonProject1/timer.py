import time

clock_start = 0


# Печатаем продолжительность работы программы.
def time_print():

    clock_end = time.time()
    runtime_duration = clock_end - clock_start

    print("The program has worked for {:.9f} seconds".format(runtime_duration))
