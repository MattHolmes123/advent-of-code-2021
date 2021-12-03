from src import utils


def life_support_rating(diagnostic_data):
    oxygen_rating = process_rows(diagnostic_data, filter_oxygen)
    co2_rating = process_rows(diagnostic_data, filter_co2)

    print(f"Oxygen Rating: {oxygen_rating}")
    print(f"CO2 Rating: {co2_rating}")
    print(f"Life support rating: {oxygen_rating * co2_rating}")


def process_rows(diagnostic_data, filter_func):
    idx = 0

    while len(diagnostic_data) > 1:
        diagnostic_data = filter_rows(diagnostic_data, idx, filter_func)
        idx += 1

    return int(diagnostic_data[0], 2)


def filter_rows(rows, idx, filter_func):
    low = []
    high = []

    for row in rows:
        value = row[idx]
        high.append(row) if int(value) else low.append(row)

    return filter_func(low, high)


def filter_oxygen(low, high):
    total_low = len(low)
    total_high = len(high)

    if total_low == total_high:
        return high

    if total_high > total_low:
        return high
    else:
        return low


def filter_co2(low, high):
    total_low = len(low)
    total_high = len(high)

    if total_low == total_high:
        return low

    if total_high > total_low:
        return low
    else:
        return high


def main():
    diagnostic_data = list(utils.get_input("src/day_3/input.txt"))
    life_support_rating(diagnostic_data)


if __name__ == "__main__":
    main()
