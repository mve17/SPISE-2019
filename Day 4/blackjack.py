import cards

def compute_value(hand): #hand is a list of Card objects. returns the blackjack value of the hand (returning the better value in the case of aces).
    values=[]
    for card in hand:
        values.append(card.get_value())
    value_to_count={'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}
    total_count=0
    for value in values:
        total_count+=value_to_count[value]
    if ('A' in values) and total_count<=11:
        total_count+=10
    return total_count

def deal_hand(num_cards,deck): #returns a list of num_cards cards dealt from deck useing the deal_card method
    hand=[]
    for i in range(num_cards):
        hand.append(deck.deal_card())
    return hand

def hit_hand(hand,deck): #adds a card to list of cards 'hand' using the deal_card method from given deck
    hand.append(deck.deal_card())

def card_to_string(card): #for example, if the card is the 4 of hearts, returns '4 of Hearts'
    return card.get_value()+' of '+card.get_suit()

def place_bet(player_money):
    valid_bet=False
    bet=None
    while not valid_bet:
        bet_string=input('Place your bet: ')
        try:
            bet=int(bet_string)
            if bet>0 and bet<=player_money:
                return bet
            else:
                print('bet must be >0 and at most your current holdings')
        except:
            print('Invalid bet')

deck=cards.Deck() #create deck
player_money=100

playing=True
while playing:
    print('\nYou have','$'+str(player_money))
    bet=place_bet(player_money)
    deck.shuffle()
    #create dealer and player hands
    dealer_hand=deal_hand(2,deck)
    player_hand=deal_hand(2,deck)
    print('\nYour Hand:')
    for card in player_hand:
        print(card_to_string(card))
    print('Dealer shows:')
    print(card_to_string(dealer_hand[0]))
    hitting=True
    player_busted=False
    while hitting:
        hit=input('\nWould you like to hit?[y/n]: ')
        if hit=='y':
            hit_hand(player_hand,deck)
            print('You got the '+card_to_string(player_hand[-1]))
            player_count=compute_value(player_hand)
            print('Your count is',player_count)
            if player_count>21:
                print('you lose')
                player_money-=bet
                player_busted=True
                hitting=False
        else:
            hitting=False
    if not player_busted:
        print("\nDealer's hand:")
        for card in dealer_hand:
            print(card_to_string(card))
        dealer_count=compute_value(dealer_hand)
        while compute_value(dealer_hand)<17:
            hit_hand(dealer_hand,deck)
            print('Dealer got the',card_to_string(dealer_hand[-1]))
        if compute_value(dealer_hand)>21:
            print('Dealer busts. You win!')
            player_money+=bet
        else:
            if compute_value(player_hand)>compute_value(dealer_hand):
                print('You win!')
                player_money+=bet
            else:
                print('You lose')
                player_money-=bet
    if player_money==0:
        print("\nYou're out of money. Better luck next time...")
        playing=False
    else:
        play_again=input('\nWould you like to play again?[y/n]: ')
        if not play_again=='y':
            playing=False
            
