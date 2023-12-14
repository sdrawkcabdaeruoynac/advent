import part
# any number adjacent or diagonal to a number will be a part number


def main():

    item_dictionary = part.ItemDictionary()

    with open("/Users/zen/desktop/adventText.txt") as text:
        lines = text.readlines() # get all the lines from text

    item_dictionary.set_row_and_columns(len(lines), len(lines[0]) - 1)
    item_dictionary.generate(lines)

    sum = 0
    for x in item_dictionary.numbers:
        value = x[0]
        items = x[1]
        for item in items:
            if item_dictionary.get_adjacent_and_diagonals(item.coordinate[0],item.coordinate[1]):
                sum += int(value)
                break

    print(sum)

if __name__ == "__main__":
    main()

