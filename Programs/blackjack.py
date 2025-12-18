import random

# Creates and returns a shuffled deck of 52 playing cards
def create_deck():
    suits = ['♠', '♥', '♦', '♣']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    deck = [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

# Calculates the total value of a hand, treating Aces as 1 or 11 optimally
def calculate_hand_value(hand):
    total = 0
    aces = 0
    
    for card in hand:
        if card['rank'] == 'A':
            aces += 1
            total += 11
        elif card['rank'] in ['J', 'Q', 'K']:
            total += 10
        else:
            total += int(card['rank'])
    
    # Adjust for aces if busted
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    
    return total

# Displays a hand of cards with decorative formatting
def display_hand(hand, name, hide_first=False):
    print(f"\n{'*' * 40}")
    print(f"  {name}'s Hand:")
    print('*' * 40)
    
    if hide_first:
        print(f"  [HIDDEN]  {hand[1]['rank']}{hand[1]['suit']}")
    else:
        for card in hand:
            print(f"  {card['rank']}{card['suit']}", end="  ")
        print(f"\n  Total: {calculate_hand_value(hand)}")
    print('*' * 40)

# Implements dealer strategy: hits on 16 or below, stands on 17 or above
def dealer_play(hand, deck):
    while calculate_hand_value(hand) < 17:
        hand.append(deck.pop())
    return hand

# Determines and displays the winner based on final hand values
def determine_winner(player_hand, dealer_hand):
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)
    
    print("\n" + "=" * 40)
    print("           FINAL RESULTS")
    print("=" * 40)
    
    display_hand(player_hand, "PLAYER", hide_first=False)
    display_hand(dealer_hand, "DEALER", hide_first=False)
    
    print("\n" + "*" * 40)
    if player_value > 21:
        print("  BUST! You went over 21. Dealer wins!")
    elif dealer_value > 21:
        print("  Dealer BUSTS! You win!")
    elif player_value > dealer_value:
        print("  You win with a higher hand!")
    elif dealer_value > player_value:
        print("  Dealer wins with a higher hand!")
    else:
        print("  It's a tie! Push!")
    print("*" * 40 + "\n")

# Main game loop that controls the flow of the blackjack game
def play_blackjack():
    print("\n" + "=" * 40)
    print("  PREPARE TO GAMBLE YOUR LIFE SAVINGS")
    print("         WELCOME TO BLACKJACK")
    print("=" * 40)
    
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    
    # Show initial hands
    display_hand(player_hand, "PLAYER")
    display_hand(dealer_hand, "DEALER", hide_first=True)
    
    # Check for natural blackjack
    if calculate_hand_value(player_hand) == 21:
        print("\nBLACKJACK!")
        dealer_hand = dealer_play(dealer_hand, deck)
        determine_winner(player_hand, dealer_hand)
        return
    
    # Player's turn
    while True:
        player_value = calculate_hand_value(player_hand)
        
        if player_value > 21:
            dealer_hand = dealer_play(dealer_hand, deck)
            determine_winner(player_hand, dealer_hand)
            return
        
        choice = input("\nWould you like to (H)it or (S)tand? ").strip().upper()
        
        if choice == 'H':
            player_hand.append(deck.pop())
            display_hand(player_hand, "PLAYER")
            
            if calculate_hand_value(player_hand) == 21:
                print("\nPerfect 21!")
                break
        elif choice == 'S':
            break
        else:
            print("Invalid choice. Please enter H or S.")
    
    # Dealer's turn
    print("\n" + "=" * 40)
    print("       DEALER'S TURN")
    print("=" * 40)
    dealer_hand = dealer_play(dealer_hand, deck)
    
    # Determine winner
    determine_winner(player_hand, dealer_hand)

# Entry point to start the game and handle replay
if __name__ == "__main__":
    while True:
        play_blackjack()
        
        play_again = input("Would you like to play again? (Y/N) ").strip().upper()
        if play_again != 'Y':
            print("\n" + "=" * 40)
            print("   Thanks for playing! Goodbye!")
            print("=" * 40 + "\n")
            break