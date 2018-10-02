from random import choice
from time import sleep


class Player:

    def __init__(self, name, money=200):
        self.name = name
        self.money = money
        self.cards = []  # [suit, number]
        self.current_hand = []  # number only
        self.win = 0
        self.high_score = 0

    def set_up(self, deck):
        self.current_hand = []
        self.cards = []
        self.draw_card(deck)
        self.draw_card(deck)
        self.current_hand = [card[1] for card in self.cards]
        # self.display_cards()

    def draw_card(self, deck, display=False):
        deck.check_deck()
        random_suit = choice(list(deck.cards))
        random_number = choice(deck.cards[random_suit])
        deck.cards[random_suit].remove(random_number)
        self.cards.append([random_suit, random_number])
        self.current_hand.append(random_number)
        if display:
            print('{name} draws {number} of {suit}'.format(name=self.name, number=random_number, suit=random_suit))
        return random_suit, random_number

    def display_cards(self):
        print("{name}'s cards are".format(name=self.name))
        for card in self.cards:
            print('{number} of {suit}'.format(number=card[1], suit=card[0]))

    def player_bet(self):
        print('You have {money} to bet'.format(money=self.money))
        while True:
            try:
                bet = int(input('what is your bet: '))
            except ValueError:
                print('Bet must be a number!')
            else:
                while bet > self.money:
                    try:
                        bet = int(input('Must bet {} or less: '.format(self.money)))
                    except ValueError:
                        print('Bet must be a number!')
                self.money -= bet
                break
        return bet

    def check_blackjack(self, bet=0, display=True):
        if len(self.current_hand) == 2:
            if 'Ace' in self.current_hand and 10 in self.current_hand:
                print('BlackJack!\nYou win {bet}'.format(bet=bet*2))
                self.win += 1
                self.high_score += 1
                if display:
                    if self.win >= self.high_score:
                        print('New win streak, {streak} games won in a row! '.format(streak=self.high_score))
                self.money += bet * 2
                return False
            elif 'Ace' in self.current_hand and 'Queen' in self.current_hand:
                print('BlackJack!\nYou win {bet}'.format(bet=bet*2))
                self.win += 1
                self.high_score += 1
                if display:
                    if self.win >= self.high_score:
                        print('New win streak, {streak} games won in a row! '.format(streak=self.high_score))
                self.money += bet * 2
                return False
            elif 'Ace' in self.current_hand and 'King' in self.current_hand:
                print('BlackJack!\nYou win {bet}'.format(bet=bet*2))
                self.win += 1
                self.high_score += 1
                if display:
                    if self.win >= self.high_score:
                        print('New win streak, {streak} games won in a row! '.format(streak=self.high_score))
                self.money += bet * 2
                return False
            elif 'Ace' in self.current_hand and 'Jack' in self.current_hand:
                print('BlackJack!\nYou win {bet}'.format(bet=bet*2))
                self.win += 1
                self.high_score += 1
                if display:
                    if self.win >= self.high_score:
                        print('New win streak, {streak} games won in a row! '.format(streak=self.high_score))
                self.money += bet * 2
                return False
        return True

    def check_cards(self, deck=None, bet=None):  # TODO if two aces come out FIX
        if len(self.current_hand) == 1:
            self.draw_card(deck, display=True)
            if not self.check_blackjack(bet, display=True):
                return False
        for number in self.current_hand:
            index = self.current_hand.index(number)
            if number == "Ace":
                self.display_cards()
                answer = ""
                while answer != 11 and answer != 1:
                    try:
                        answer = int(input('Choose a value of 11 or 1 for your Ace'))
                    except ValueError:
                        print('Must chose 1 or 11')
                self.current_hand.remove(number)
                self.current_hand.insert(index, answer)
            if number == 'Queen' or number == 'Jack' or number == 'King':
                self.current_hand.remove(number)
                self.current_hand.insert(index, 10)
        total = sum(self.current_hand)
        if total == 21:
            self.display_cards()
            print('\nYou have 21\n')
            sleep(2)
            return False
        elif total > 21:
            print('Bust!\nYou had {total}'.format(total=total))
            return False
        else:
            self.display_cards()
            print('Totaling {total}\n'.format(total=total))
            return True

    def hit(self, deck):
        answer = input('Hit or Stand  (h/s) \n')
        while answer != 'h' and answer != 's':
            answer = input('Must choose (h) for Hit and (s) for Stand ')
        if answer == 'h':
            card_suit, card_number = self.draw_card(deck)
            print('{number} of {suit}\n'.format(suit=card_suit, number=card_number))
            return True
        return False


class Dealer:

    def __init__(self):
        self.name = 'Dealer'
        self.cards = []
        self.current_hand = []

    def draw_card(self, deck, display=False):
        deck.check_deck()
        random_suit = choice(list(deck.cards))
        random_number = choice(deck.cards[random_suit])
        deck.cards[random_suit].remove(random_number)
        self.cards.append([random_suit, random_number])
        self.current_hand.append(random_number)
        if display:
            print('{name} draws {number} of {suit}'.format(name=self.name, number=random_number, suit=random_suit))
        return random_suit, random_number

    def set_up(self, deck):
        self.current_hand = []
        self.cards = []
        self.draw_card(deck)
        self.draw_card(deck)
        self.current_hand = [card[1] for card in self.cards]
        self.display_cards()

    def display_cards(self):  # Dealer can only show one card at first
        print('The Dealer is showing')
        print('{number} of {suit}'.format(number=self.cards[1][1], suit=self.cards[1][0]))

    def display_all_cards(self):
        print('The Dealer cards are:')
        for card in self.cards:
            print('{number} of {suit}'.format(number=card[1], suit=card[0]))

    def check_blackjack(self):
        if len(self.cards) == 2:
            temp = [card[1] for card in self.cards]
            if 'Ace' in temp and 10 in temp:
                print('Dealer BlackJack!')
                return True
            elif 'Ace' in temp and 'Queen' in temp:
                print('Dealer BlackJack!')
                return True
            elif 'Ace' in temp and 'King' in temp:
                print('Dealer BlackJack!')
                return True
            elif 'Ace' in temp and 'Jack' in temp:
                print('Dealer BlackJack!')
                return True

    def check_cards(self):  # Dealer's Ace will be 11 if sum of cards is less than 11. Else 1
        temp = []
        for number in self.current_hand:
            index = self.current_hand.index(number)
            if number == "Ace":
                continue
            if number == 'Queen' or number == 'Jack' or number == 'King':
                self.current_hand.remove(number)
                self.current_hand.insert(index, 10)
                temp.append(10)
            else:
                temp.append(number)
        for number in self.current_hand:  # Deciding what to do with the Ace
            total = sum(temp)
            index = self.current_hand.index(number)
            if number == 'Ace':
                self.current_hand.remove(number)
                if total < 11:
                    self.current_hand.insert(index, 11)
                    temp.append(11)
                else:
                    self.current_hand.insert(index, 1)
                    temp.append(1)
        total = sum(self.current_hand)
        # Evaluate hand
        if total == 21:
            self.display_all_cards()
            print('Dealer has 21')
            return False
        elif total > 21:
            self.display_all_cards()
            print('\nBust!')
            # player.money = bet ** 2
            return False
        else:
            self.display_all_cards()
            print('Totaling {total}\n'.format(total=total))
            sleep(2)
            return True

    def hit(self, deck):
        dealer_total = sum(self.current_hand)
        if dealer_total < 17:
            card_suit, card_number = self.draw_card(deck)
            print('{name} draws {number} of {suit}\n'.format(name=self.name, suit=card_suit, number=card_number))
            sleep(2)
            return True
        return False


class Deck:

    def __init__(self):
        self.cards = {'clubs': [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace'],
                      'spades': [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace'],
                      'hearts': [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace'],
                      'diamonds': [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']}

    def check_deck(self):
        for number, suit in self.cards.items():
            if not suit:
                print('\n---New deck added---\n')
                self.cards = {'clubs': [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace'],
                              'spades': [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace'],
                              'hearts': [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace'],
                              'diamonds': [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']}
