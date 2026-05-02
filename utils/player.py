class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.hand = []

    def play_hand(self):
        while True:
            try:
                for index,card in enumerate(self.hand,start=1):
                    print(f"{index}. {card}")

                response = int(input("Choose card : "))
                card = self.hand[response-1]
                self.hand.pop(response-1)
                return card

            except Exception as e :
                print("Player Class ",e)

