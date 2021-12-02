from src import utils


class Submarine2D:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.aim = 0

    def forward(self, x):
        #  It increases your horizontal position by X units.
        self.x += x
        #  It increases your depth by your aim multiplied by X.
        self.y += (self.aim * x)

    def up(self, y):
        # up X decreases your aim by X units.
        self.aim -= y

    def down(self, y):
        # down X increases your aim by X units.
        self.aim += y

    def navigate(self, instruction):
        method, amount = instruction.split(" ")
        func = getattr(self, method)
        func(int(amount))

    def summary(self):
        print(self.x * self.y)


def main():
    sub = Submarine2D()

    for instruction in utils.get_input("src/day_2/input.txt"):
        sub.navigate(instruction)

    sub.summary()


if __name__ == "__main__":
    main()
