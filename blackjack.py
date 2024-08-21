
value  = 0
card_values_ten = ["J", "K", "Q"]
hand_1 = ['K',"J","A"]
hand_2 = ['3', '4']

def blackjack_hand_greater_than(hand_1, hand_2):
    """
    Return True if hand_1 beats hand_2, and False otherwise.
    
    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21
    
    Hands are represented as a list of cards. Each card is represented by a string.
    
    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.
    
    When determining a hand's total, you should try to count aces in the way that 
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.
    
    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """
    total_hand_1 = 0
    total_hand_2 = 0
    for card_item in hand_1:
        if card_item in card_values_ten:
            total_hand_1 += 10
        elif card_item == "A":
            if total_hand_1 >= 21 or total_hand_1 + 11 >= 21:
                total_hand_1 += 1
            else:
                total_hand_1 += 11
    for card_item in hand_2:
        total_hand_2 += int(card_item)
    print(total_hand_1)
    print(total_hand_2)

    if total_hand_1 > total_hand_2 and total_hand_1 <= 21:
        return True
    else:
        return False

answer = blackjack_hand_greater_than(hand_1, hand_2)
print(f"The answer is {answer}")