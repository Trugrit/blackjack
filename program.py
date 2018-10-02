from variables import Player, Dealer, Deck


def main():
    intro()
    player = create_player()
    player.cards = [['spades', 'Ace'], ['hearts', 'Ace']]
    split_hand = None
    dealer = Dealer()
    deck = Deck()
    while True:
        while True:
            if player.money < 1:
                break
            bet = player.player_bet()
            # player.set_up(deck)
            player.cards = [['spades', 5], ['hearts', 5]]
            player.current_hand = [5, 5]
            if not player.check_blackjack(bet):
                break
            print('')
            dealer.set_up(deck)
            print()
            while True:  # Players turn
                if player.check_split():
                    answer = input("You have two {card}, would you like to split? (y/n)\n".
                                   format(card=player.current_hand[0]))
                    if answer == 'y':
                        player.current_hand = [player.current_hand[0]]
                        card = player.cards.pop(0)
                        split_hand = split(bet, player, deck, card=card)
                if not player.check_cards(deck, bet):
                    break
                if not player.hit(deck):
                    break
            player_amount = sum(player.current_hand)
            split_hand_amount = None
            if split_hand:
                if sum(split_hand.current_hand) == 21:
                    split_hand = None
                else:
                    split_hand_amount = sum(split_hand.current_hand)
            if player_amount > 21:
                if not split_hand_amount:
                    break
                else:
                    if split_hand_amount > 21:
                        break
            while True:  # Dealers turn
                if not dealer.check_cards():
                    break
                if not dealer.hit(deck):
                    break
            win_loss(player, dealer, bet, split_hand)
            break
        if not replay(player):
            break


def intro():
    print("------------------------------")
    print("          BlackJack")
    print("------------------------------")


def win_loss(player, dealer, bet, split_hand=None):
    player_total = sum(player.current_hand)
    dealer_total = sum(dealer.current_hand)
    if split_hand:
        split_hand_total = sum(split_hand.current_hand)
        print('----------------------------------------------')
        print('{name} has {points} '.format(name=split_hand.name, points=split_hand_total))
        print('{name} has {points} \n'.format(name=dealer.name, points=dealer_total))
        if dealer_total > 21:
            player.money += bet * 2
            player.win += 1
            player.high_score += 1
            print('You win {bet} '.format(bet=bet * 2))
            if player.win >= player.high_score:
                print('New win streak, {streak} games won in a row! '.format(streak=player.high_score))
                print('----------------------------------------------')
        elif split_hand_total == dealer_total:
            player.money += bet
            print('Draw\nBet returned ')
            player.win = 0
        elif split_hand_total > dealer_total:
            print('You win {bet} '.format(bet=bet * 2))
            player.win += 1
            player.high_score += 1
            player.money += bet * 2
            if player.win >= player.high_score:
                print('New win streak, {streak} games won in a row! '.format(streak=player.high_score))
                print('----------------------------------------------')

        else:
            print('{name} Loses '.format(name=split_hand.name))
            print('----------------------------------------------')

            player.win = 0
    print('----------------------------------------------')
    print('{name} has {points} '.format(name=player.name, points=player_total))
    print('{name} has {points} \n'.format(name=dealer.name, points=dealer_total))
    if dealer_total > 21:
        player.money += bet * 2
        player.win += 1
        player.high_score += 1
        print('You win {bet} '.format(bet=bet * 2))
        if player.win >= player.high_score:
            print('New win streak, {streak} games won in a row! '.format(streak=player.high_score))
            print('----------------------------------------------')
    elif player_total == dealer_total:
        player.money += bet
        print('Draw\nBet returned ')
        print('----------------------------------------------')
        player.win = 0
    elif player_total > dealer_total:
        print('You win {bet} '.format(bet=bet * 2))
        player.win += 1
        player.high_score += 1
        player.money += bet * 2
        if player.win >= player.high_score:
            print('New win streak, {streak} games won in a row! '.format(streak=player.high_score))
            print('----------------------------------------------')
    else:
        print('{name} Loses '.format(name=player.name))
        print('----------------------------------------------')
        player.win = 0


def create_player():
    name = input('What is your name: ')
    player = Player(name)
    return player


def replay(player):
    if player.money < 1:
        print('You have no money left to bet with\n')
        print('Thanks for playing!')
        return False
    answer = input('\nPlay again? (y/n) \n\n').lower()
    while answer != '' and answer != 'y' and answer != 'n':
        answer = input('Must enter (y) Yes or (n) No')
    if answer == '' or answer == 'y':
        return True
    print('Thanks for playing!')
    return False


def split(bet, player, deck, card):
    split_hand = Player('Second Hand')
    split_hand.cards = [card]
    while True:
        player.money -= bet
        split_hand.current_hand = [card[1]]
        split_hand.draw_card(deck, display=True)
        if not split_hand.check_blackjack(bet):
            player.money += bet * 2
            break
        while True:  # Players second hand
            print('\nSecond Hand\n')
            if not split_hand.check_cards(deck, bet):
                break
            if not split_hand.hit(deck):
                break
        break
    return split_hand


def check_split(player):
    if player.current_hand.count(player.current_hand[0]) == 2:
        return True
    return False


if __name__ == '__main__':
    main()
