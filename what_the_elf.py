import part
# any number adjacent or diagonal to a number will be a part number


def main():

    item_dictionary = part.ItemDictionary()

    with open("/Users/zen/desktop/adventText.txt") as text:
        lines = text.readlines() # get all the lines from text

    item_dictionary.set_row_and_columns(len(lines), len(lines[0]) - 1)
    item_dictionary.generate(lines)

    x = 0
    sum = 0
    while x < len(item_dictionary.numbers) :
        value = item_dictionary.numbers[x][0]
        items = item_dictionary.numbers[x][1]

        for item in items:
            if item_dictionary.get_adjacent_and_diagonals(item.coordinate[0],item.coordinate[1]):
                #print(value)
                sum += int(value)
                break

        x += 1

    print(sum)




if __name__ == "__main__":
    main()
