from variables import *


def main():
    intro()
    player = create_player()
    dealer = Dealer()
    deck = Deck()
    while True:
        # game_on = True
        while True:
            if player.money < 1:
                break
            bet = player.player_bet()
            player.set_up(deck)
            if not player.check_blackjack(bet):
                break
            print('')
            dealer.set_up(deck)
            print()
            while True:  # Players turn
                if not player.check_cards():
                    break
                if not player.hit(deck):
                    break
            player_amount = sum(player.current_hand)
            if player_amount > 21:
                break
            while True:  # Dealers turn
                if not dealer.check_cards():
                    break
                if not dealer.hit(deck):
                    break
            win_loss(player, dealer, bet)
            break
        if not replay(player):
            break


def intro():
    print("------------------------------")
    print("          BlackJack")
    print("------------------------------")


def win_loss(player, dealer, bet):
    player_total = sum(player.current_hand)
    dealer_total = sum(dealer.current_hand)
    print('\n{name} has {points} '.format(name=player.name, points=player_total))
    print('{name} has {points} \n'.format(name=dealer.name, points=dealer_total))
    if dealer_total > 21:
        player.money += bet * 2
        player.win += 1
        player.high_score += 1
        print('You win {bet} '.format(bet=bet*2))
        if player.win >= player.high_score:
            print('New win streak, {streak} games won in a row! '.format(streak=player.high_score))
    elif player_total == dealer_total:
        player.money += bet
        print('Draw\nBet returned ')
        player.win = 0
    elif player_total > dealer_total:
        print('You win {bet} '.format(bet=bet*2))
        player.win += 1
        player.high_score += 1
        player.money += bet * 2
        if player.win >= player.high_score:
            print('New win streak, {streak} games won in a row! '.format(streak=player.high_score))
    else:
        print('You Lose ')
        player.win = 0


def create_player():
    name = input('What is your name: ')
    player = Player(name)
    return player


def replay(player):
    if player.money < 1:
        print('You have no money left to bet with\n')
        return False
    answer = input('Play again? (y/n) \n\n').lower()
    while answer != '' and answer != 'y' and answer != 'n':
        answer = input('Must enter (y) Yes or (n) No')
    if answer == '' or answer == 'y':
        return True
    return False


main()
