from sys import maxsize, setrecursionlimit

from src import utils


def count_higher(items: list[int], previous: int = maxsize, total_bigger: int = 0):
    try:
        next_item = items.pop(0)
        if next_item > previous:
            total_bigger += 1

        count_higher(items, next_item, total_bigger)

    except IndexError:
        print(f"Total measurements are larger than the previous measurement: {total_bigger}")


def main():
    measurements = list(map(int, utils.get_input("src/day_1/input.txt")))

    # 2000 measurements exceeds the default recursion limit.
    setrecursionlimit(len(measurements) + 7)

    count_higher(measurements)


if __name__ == "__main__":
    main()
