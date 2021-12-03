from src import utils
from collections import Counter


class Diagnose:
    def __init__(self):
        self.counters = [Counter() for _ in range(12)]

    def process_row(self, value):
        for x, bit in enumerate(value):
            self.counters[x].update(bit)

    def power_consumption(self):
        gamma_bin = "".join(
            c.most_common(1)[0][0] for c in self.counters
        )
        gamma = int(gamma_bin, 2)

        # e.g. '0b1111111111111'
        mask = (2 ** (len(gamma_bin) + 1) - 1)

        # XOR to get the inverse of gamma
        inverse_gamma = gamma ^ mask

        # e.g. remove the extra bit
        # 0b1001001000011 -> 001001000011
        epsilon_binary = bin(inverse_gamma)[3:]

        epsilon = int(epsilon_binary, 2)

        print(f"power consumption: {gamma * epsilon}")


def main():
    d = Diagnose()

    for row in utils.get_input("src/day_3/input.txt"):
        d.process_row(row)

    d.power_consumption()


if __name__ == "__main__":
    main()
