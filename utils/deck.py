import random
from card import Card


class Deck:
    def __init__(self):
        self.suites = ["Spade", "Heart", "Club", "Diamond"]
        self.ranks = [i for i in range(6, 15)]
        self.deck = []
        self.create_deck()

    def create_deck(self):
        for suite in self.suites:
            for rank in self.ranks:
                self.deck.append(Card(suite, rank))
            if suite == "Spade":
                self.deck.pop()

    def shuffle_cards(self):
        dummy = self.deck

        self.deck = []
        while True:
            if len(dummy) == 1:
                self.deck.append(dummy[0])
                break

            else:
                rand_index = random.randint(0, len(dummy)-1)
                self.deck.append(dummy[rand_index])
                dummy.pop(rand_index)


if __name__ == "__main__":
    d = Deck()
    # d.shuffle_cards()
    # for card in d.deck:
    #     print(card)
    print(d.deck)
