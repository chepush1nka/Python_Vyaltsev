import time
from container import *
import timer


# Метод для сортировки элементов контейнера слиянием (Merge Sort).
def straight_merge(i, j, container, help_container):
    if j == -1:
        j = len(container.data) - 1
    if j <= i:
        return
    mid = (i + j) // 2
    straight_merge(i, mid, container, help_container)
    straight_merge(mid + 1, j, container, help_container)
    pointer_left = i
    pointer_right = mid + 1
    for k in range(i, j + 1):
        if pointer_left == mid + 1:
            help_container.data[k] = container.data[pointer_right]
            pointer_right += 1
        elif pointer_right == j + 1:
            help_container.data[k] = container.data[pointer_left]
            pointer_left += 1
        elif container.data[pointer_left].road_time() > container.data[pointer_right].road_time():
            help_container.data[k] = container.data[pointer_left]
            pointer_left += 1
        else:
            help_container.data[k] = container.data[pointer_right]
            pointer_right += 1
    for k in range(i, j + 1):
        container.data[k] = help_container.data[k]


if __name__ == '__main__':
    timer.clock_start = time.time()
    if len(sys.argv) != 4:
        print("The program expects 4 arguments\n"
              "Example:\n"
              "command -f input.txt output.txt\n")
        timer.time_print()
        sys.exit(1)

    container = Container()
    help_container = Container()

    # Заполнение контейнера из файла.
    if sys.argv[1] == '-f':
        try:
            input_stream = open(sys.argv[2])
        except IOError:
            print("invalid input file")
            timer.time_print()
            sys.exit(1)

        flag = container.fill_container(input_stream)
        if not flag:
            timer.time_print()
            sys.exit(1)
        input_stream.close()
        input_stream = open(sys.argv[2])
        flag = help_container.fill_container(input_stream)
        if not flag:
            timer.time_print()
            sys.exit(1)
        input_stream.close()

    # Заполнение контейнера рандомными значениями.
    elif sys.argv[1] == '-n':
        if not sys.argv[2].isdigit():
            print("Container size should be a digit")
            timer.time_print()
            sys.exit(1)
        size = int(sys.argv[2])

        if size <= 0 or size > 10000:
            print("Container size should be from 1 to 10000")
            timer.time_print()
            sys.exit(1)
        container.random_fill(size)
        help_container.random_fill(size)
    else:
        print("invalid mod specified\n"
              "Expected:\n"
              "1) command -f input.txt output.txt\n"
              "2) command -n number output.txt\n")
        timer.time_print()
        sys.exit(1)

    try:
        output_stream = open(sys.argv[3], "w")
    except IOError:
        print("invalid output file")
        timer.time_print()
        sys.exit(1)

    container.out_container(output_stream)

    straight_merge(0, -1, container, help_container)
    print('\n\nBest time:')
    output_stream.write('\n\nBest time:\n')
    container.out_container(output_stream)
    output_stream.close()

    print('==> Finish')

    timer.time_print()
