class Scratcher:
    def __init__(self):
        self.scratcher = {
            "game": int(),
            "numbers": list(),
            "winning_numbers": list(),
            "matches": int(),
            "copies": list()
        }

    def __str__(self):
        return f'{self.scratcher}'

    def calculate_matches(self):
        if self.scratcher == {}:
            raise BaseException("EMPTY")
        for win_num in self.scratcher["winning_numbers"]:
            for num in  self.scratcher["numbers"]:
                if win_num == num:
                    self.scratcher["matches"] += 1

    def calculate_copies(self):
        scratcher_num = self.scratcher["game"] + 1
        matches = self.scratcher["matches"]
        self.scratcher['copies'] = [x for x in range(scratcher_num, matches + scratcher_num)]
