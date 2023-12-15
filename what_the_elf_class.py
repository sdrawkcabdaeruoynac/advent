class Item:
    def __init__(self,value,row,col):
        self.value = str(value)
        self.coordinate = tuple((row,col))

    def __str__(self):
        return f'({self.value}\t{self.coordinate})'

class ItemDictionary:

    def __init__(self):
        self.coordinates = dict()
        self.symbols = set()
        self.numbers = list()
        self.MAX_ROWS = 0
        self.MAX_COL = 0

    def set_row_and_columns(self, row, col):
        self.MAX_ROWS = row
        self.MAX_COL = col

    def generate(self,lines):
        self.set_row_and_columns(len(lines), len(lines[0]) - 1)
        self.generate_coordinates(lines)
        self.generate_numbers()

    def generate_coordinates(self, lines):
        for row in range(self.MAX_ROWS):
            for col in range(self.MAX_COL):
                item = Item(lines[row][col], row, col)
                self.coordinates[item.coordinate] = item.value

    def generate_numbers(self):
        number_queue = []
        row = column = 0

        while row < self.MAX_ROWS:
            while column < self.MAX_COL:
                str_number = str()

                while column < self.MAX_COL \
                        and str(self.coordinates[(row, column)]).isdigit():

                    item = Item(self.coordinates[(row, column)],row,column)
                    number_queue.append(item)
                    str_number += item.value
                    column += 1

                if number_queue:
                    self.numbers.append((str_number, number_queue))
                    number_queue = []

                column += 1
            row += 1
            column = 0

    def get_adjacent_and_diagonals(self,x,y) -> bool:

        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if 0 <= i < self.MAX_ROWS and 0 <= j < self.MAX_COL and (i, j) != (x, y):
                    if not str(self.coordinates[(i, j)]).isalnum() and self.coordinates[(i, j)] != '.':
                        return True
        return False
