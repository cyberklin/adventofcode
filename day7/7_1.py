import sys
import collections

cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
cards_str_to_value_map = dict(zip(cards, [i for i in range(0,len(cards))]))

hand_types = ['1', '2','2+2','3','3+2','4','5']
hands_types_to_value_map = dict(zip(hand_types, [i for i in range(0,len(hand_types))]))

def encode_hand(hand): 
    max_same = 0
    hand_type = '1'
    cards = collections.defaultdict(int)
    hand_encoded = 0
    for i in range(0, 5):
        card = hand[i]
        cards[card] += 1

        if cards[card] == 2 and max_same == 2:
            hand_type = '2+2'
        elif cards[card] == 2 and max_same == 3:
            hand_type = '3+2'
        elif cards[card] == 3 and hand_type == '2+2':
            hand_type = '3+2'
            max_same = 3
        elif cards[card] > max_same:
            max_same = cards[card]
            hand_type = str(max_same)

        card_value = cards_str_to_value_map[card]
        hand_encoded = hand_encoded | (card_value << (4*(4-i)))

    hand_value = hands_types_to_value_map[hand_type]
    hand_encoded = hand_encoded | (hand_value << (4*5))


    return hand_encoded

def parse_file(fname):

    hands = [] # list of tuples (encoded_hand, bet)
    with open(fname) as f:

        for line in f:
            hand, bet = line.rstrip('\n').split()
            encoded = encode_hand(hand)
            hands.append((encoded,int(bet),hex(encoded)))

    return hands

def main():
    fname = sys.argv[1]
    total = 0

    hands = parse_file(fname)
    num = len(hands)

    sorted_hands = sorted(hands, key=lambda x: x[0])

    for i in range(1, num + 1):
        total += sorted_hands[i - 1][1]*i

    print("total = {}", total)

if __name__ == "__main__":
    main()
