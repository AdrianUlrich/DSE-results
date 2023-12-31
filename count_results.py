# Note: rename the csv files so that they are in the order of the homeworks (hw0, hw1, hw2, hw3) to output in order

import glob


def count_results(file):
    lines: list[str]
    with open(file) as f:
        # read lines of f into list
        lines = f.readlines()
    counters: dict[str, int] = {
        "linter": 0,
        "lintertotal": 0,
        "hw0": 0,
        "hw0total": 0,
        "hw1": 0,
        "hw1total": 0,
        "hw2": 0,
        "hw2total": 0,
        "hw3": 0,
        "hw3total": 0,
    }
    for line in lines:
        # split line into list of strings
        tokens: list[str] = line.split(",")
        # check if line has correct length
        if len(tokens) != 2:
            print("Error in line: " + line)
            continue
        # check if line contains correct data
        key = None
        if "HW0" in tokens[0]:
            key = "hw0"
        elif "HW1" in tokens[0]:
            key = "hw1"
        elif "HW2" in tokens[0]:
            key = "hw2"
        elif "HW3" in tokens[0]:
            key = "hw3"
        elif "linter" in tokens[0]:
            key = "linter"

        if key is None:
            print("Error in line: " + line)
            continue
        # add to counters
        counters[key + "total"] += 1
        if "success" in tokens[1]:
            counters[key] += 1
    # compute ratios
    counters["linter%"] = counters["lintertotal"] and round(counters["linter"] / counters["lintertotal"] * 100)
    counters["hw0%"] = counters["hw0total"] and round(counters["hw0"] / counters["hw0total"] * 100)
    counters["hw1%"] = counters["hw1total"] and round(counters["hw1"] / counters["hw1total"] * 100)
    counters["hw2%"] = counters["hw2total"] and round(counters["hw2"] / counters["hw2total"] * 100)
    counters["hw3%"] = counters["hw3total"] and round(counters["hw3"] / counters["hw3total"] * 100)

    # print results
    s = " | "
    print(f"{counters['linter']:2}/{counters['lintertotal']:2}({counters['linter%']:3}%)", end=s)
    print(f"{counters['hw0']:2}/{counters['hw0total']:2}({counters['hw0%']:3}%)", end=s)
    print(f"{counters['hw1']:2}/{counters['hw1total']:2}({counters['hw1%']:3}%)", end=s)
    print(f"{counters['hw2']:2}/{counters['hw2total']:2}({counters['hw2%']:3}%)", end=s)
    print(f"{counters['hw3']:2}/{counters['hw3total']:2}({counters['hw3%']:3}%)")


def main():
    # print header
    header_elements = ["linter", "hw0", "hw1", "hw2", "hw3"]
    # pad with spaces
    header_elements = [x.ljust(12) for x in header_elements]
    print("| ".join(header_elements))
    # for all files like *.csv in folder count the different results
    for file in glob.glob("*.csv"):
        count_results(file)


if __name__ == '__main__':
    main()
