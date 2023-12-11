# Note: rename the csv files so that they are in the order of the homeworks (hw0, hw1, hw2, hw3) to output in order

import glob

UNIT_TEST_W = .3
INT_TEST_W = .5
BENCH_TEST_W = .2


def count_results(file):
    lines: list[str]
    with open(file) as f:
        # read lines of f into list
        lines = f.readlines()
    counters: dict[str, int] = {
        "linter": 0,
        "lintertotal": 0,
        "hw0unit": 0,
        "hw0unittotal": 0,
        "hw0int": 0,
        "hw0inttotal": 0,
        "hw0bench": 0,
        "hw0benchtotal": 0,
        "hw1unit": 0,
        "hw1unittotal": 0,
        "hw1int": 0,
        "hw1inttotal": 0,
        "hw1bench": 0,
        "hw1benchtotal": 0,
        "hw2unit": 0,
        "hw2unittotal": 0,
        "hw2int": 0,
        "hw2inttotal": 0,
        "hw2bench": 0,
        "hw2benchtotal": 0,
        "hw3unit": 0,
        "hw3unittotal": 0,
        "hw3int": 0,
        "hw3inttotal": 0,
        "hw3bench": 0,
        "hw3benchtotal": 0,
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
        if "Integration" in tokens[0]:
            key += "int"
        elif "Benchmark" in tokens[0]:
            key += "bench"
        elif "linter" not in tokens[0]:
            key += "unit"
        # add to counters
        counters[key + "total"] += 1
        if "success" in tokens[1]:
            counters[key] += 1
    # compute ratios
    counters["linter%"] = counters["lintertotal"] and round(counters["linter"] / counters["lintertotal"] * 100)

    for hw in ["hw0", "hw1", "hw2", "hw3"]:
        counters[hw + "unit%"] = counters[hw + "unittotal"] and round(
            counters[hw + "unit"] / counters[hw + "unittotal"] * 100)
        counters[hw + "int%"] = counters[hw + "inttotal"] and round(
            counters[hw + "int"] / counters[hw + "inttotal"] * 100)
        counters[hw + "bench%"] = counters[hw + "benchtotal"] and round(
            counters[hw + "bench"] / counters[hw + "benchtotal"] * 100)
        if hw == "hw0":
            counters[hw + "TOTAL%"] = round((
                    counters[hw + "unit%"] * UNIT_TEST_W + counters[hw + "int%"] * INT_TEST_W)/(UNIT_TEST_W + INT_TEST_W))
        else:
            counters[hw + "TOTAL%"] = round(
                counters[hw + "unit%"] * UNIT_TEST_W + counters[hw + "int%"] * INT_TEST_W +
                counters[
                    hw + "bench%"] * BENCH_TEST_W)

    s = " | "
    # print unit, integration and benchmark test results
    for test in ["TOTAL", "unit", "int", "bench"]:
        if test == "TOTAL":
            print(f"{file:>25}", end=s)
            print(f"{counters['linter']:2}/{counters['lintertotal']:2}({counters['linter%']:3}%)", end=s)
            print(f"{counters['hw0TOTAL%']:10}%", end=s)
            print(f"{counters['hw1TOTAL%']:10}%", end=s)
            print(f"{counters['hw2TOTAL%']:10}%", end=s)
            print(f"{counters['hw3TOTAL%']:10}%")
        else:
            print(f"{test:>25}", end=s)
            print(' ' * 11, end=s)
            print(f"{counters['hw0' + test]:2}/{counters['hw0' + test + 'total']:2}({counters['hw0' + test + '%']:3}%)",
                  end=s)
            print(f"{counters['hw1' + test]:2}/{counters['hw1' + test + 'total']:2}({counters['hw1' + test + '%']:3}%)",
                  end=s)
            print(f"{counters['hw2' + test]:2}/{counters['hw2' + test + 'total']:2}({counters['hw2' + test + '%']:3}%)",
                  end=s)
            print(f"{counters['hw3' + test]:2}/{counters['hw3' + test + 'total']:2}({counters['hw3' + test + '%']:3}%)")


def main():
    # print header
    header_elements = ["file", "linter", "hw0", "hw1", "hw2", "hw3"]
    # pad with spaces
    header_elements = [x.ljust(12) for x in header_elements]
    header_elements[0] = header_elements[0].ljust(26)
    print("| ".join(header_elements))
    # for all files like *.csv in folder count the different results
    for file in glob.glob("*.csv"):
        count_results(file)


if __name__ == '__main__':
    main()
