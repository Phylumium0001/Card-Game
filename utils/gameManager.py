from utils.deck import Deck
from utils.player import Player


class GameManager:
    def __init__(self, hand_size=5, p1='p1', p2='p2'):
        self.hand_size = hand_size
        self.sessions = 5
        self.scores = {p1: 0, p2: 0}
        self.p1 = Player(p1)
        self.p2 = Player(p2)
        self.players = [self.p1, self.p2]
        self.deck = Deck()

    def start_game(self):
        # The game will run during duration of rounds
        session_winner = self.players[0]
        session_num = 1

        while (self.scores['p1'] + self.scores['p2']) <= self.sessions:
            print(f"Session : {session_num}")
            self.p1.hand, self.p2.hand = self.deck.serve(number_of_players=2)
            session_winner = self.play_session()
            # round_winner = self.deck.compare_cards(played_cards)

            # Increment score
            self.scores[session_winner.name] += 1
            session_num += 1

    def play_session(self):
        # A session will run until all served cards are played
        while True:
            if len(self.players[0].hand) != 0:
                session_winner = self.play_round()
                continue
            print(f"Player {session_winner.name} won session")
            return session_winner




    def play_round(self):
        # Make current user play hand
        # Allow second user to play
        # Compare hands
        # return winner
        played_cards = {}
        for player in self.players:
            player_card = player.play_hand()
            played_cards[player] = player_card

        winner = self.compare_cards(played_cards)
        return winner

    def compare_cards(self,played_cards):
        winner = ''
        count = 0
        for player in played_cards:
            # Compare suite then rank
            # Set first player card as leading card
            if count == 0:
                count+=1
                winner = player
                continue

            elif played_cards[winner].suite != played_cards[player].suite:
                continue

            elif played_cards[player].rank > played_cards[winner].rank:
                winner = player
        print(f"Round Winner : {winner.name}")
        return winner


