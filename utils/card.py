class Card:
    def __init__(self,suite,rank):
        self.suites = ["Spade","Heart", "Club", "Diamond"]
        self.suite = suite
        self.rank = rank
        self.img = ""
        # self.update_card_details()

    # def update_card_details(self) -> None:
    #     if self.suite == "S":
    #         self.suite = "Spade"
    #
    #     elif self.suite == "D":
    #         self.suite = "Diamond"
    #
    #     elif self.suite == "C":
    #         self.suite = "Club"
    #
    #     elif self.suite == "H":
    #         self.suite = "Heart"
    #
    def __repr__(self) -> str:
        return f"({self.suite} : {self.rank})"

    def rank_repr(self) -> str:
        if self.rank == 11:
            self.rank = "J"
        elif self.rank == 12:
            self.rank = "Q"
        elif self.rank == 13:
            self.rank = "K"
        elif self.rank == 14:
            self.rank = "A"
