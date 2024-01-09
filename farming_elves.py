import re, file_cleanser as fc , table as tb


def main():

    grouped_lines = []
    names_and_numbers = ()
    names = []
    numbers = []
    almanac = {}

    with open("/Users/zen/desktop/adventText.txt") as text:
        lines = text.readlines()

    # cleaning lines from text
    grouped_lines = fc.group_lines(lines)
    names_and_numbers = fc.clean_line_1(grouped_lines)
    names = names_and_numbers[0]
    numbers = names_and_numbers[1]

    #building almanac
    almanac = fc.build_almanac(names,numbers)
    fc.add_lists( almanac["seeds"],almanac["seeds"].pop())

    print(almanac)

    tb.generate_table(almanac["seed-to-soil map"])


if __name__ == "__main__":
    main()
