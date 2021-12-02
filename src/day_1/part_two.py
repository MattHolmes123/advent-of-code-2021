from sys import maxsize, setrecursionlimit
from typing import Generator

from src import utils


def get_chunks(values):
    return (
        sum(chunk)
        for chunk in zip(values[0:], values[1:], values[2:])
    )


def count_higher(items: "Generator[int]", previous: int = maxsize, total_bigger: int = 0):
    try:
        next_item = next(items)
        total_bigger += 1 if next_item > previous else 0
        count_higher(items, next_item, total_bigger)

    except StopIteration:
        print(f"Total measurements are larger than the previous measurement: {total_bigger}")


def main():
    measurements = list(map(int, utils.get_input("src/day_1/input.txt")))
    chunks = get_chunks(measurements)

    # 2000 measurements exceeds the default recursion limit.
    setrecursionlimit(len(measurements) + 7)
    count_higher(chunks)


if __name__ == "__main__":
    main()
