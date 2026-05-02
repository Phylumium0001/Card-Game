import random
from utils.card import Card


class Deck:
    def __init__(self, hand_size=5):
        self.suites = ["Spade", "Heart", "Club", "Diamond"]
        self.ranks = [i for i in range(6, 15)]
        self.deck = []
        self.create_deck()
        self.hand_size = hand_size

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

    def choose_rand_card(self) -> list:
        player_cards = []
        for _ in range(self.hand_size):
            rand_index = random.randint(0,len(self.deck)-1)
            player_cards.append(self.deck[rand_index])

        return player_cards


    def serve(self,number_of_players) -> (list, list):
        cards = []
        for num in range(number_of_players):
            # Serve cards for each user
            player_cards = self.choose_rand_card()
            cards.append(player_cards)
        return cards


if __name__ == "__main__":
    d = Deck()
    # d.shuffle_cards()
    # for card in d.deck:
    #     print(card)
    print(d.deck)
