#!/usr/bin/env python
# This Python file uses the following encoding: utf-8

# http://en.wikipedia.org/wiki/Domino

# While this will work fine on most terminals (provided they support unicode), the prefered
# font for this game is NOT a monospaced font. In Ubuntu I used Aegean.

# You will also want to increase the font size so the pips can be seen more easily. I used size 17.
# There are other fonts that work well, I just happened to pick Aegean.

from random import shuffle, randint
import string

def domino_horiz(a,b):
    return '🀱🀲🀳🀴🀵🀶🀷🀸🀹🀺🀻🀼🀽🀾🀿🁀🁁🁂🁃🁄🁅🁆🁇🁈🁉🁊🁋🁌🁍🁎🁏🁐🁑🁒🁓🁔🁕🁖🁗🁘🁙🁚🁛🁜🁝🁞🁟🁠🁡🀰'[(7*a)+b]

def domino_vert(a,b):
    return '🁣🁤🁥🁦🁧🁨🁩🁪🁫🁬🁭🁮🁯🁰🁱🁲🁳🁴🁵🁶🁷🁸🁹🁺🁻🁼🁽🁾🁿🂀🂁🂂🂃🂄🂅🂆🂇🂈🂉🂊🂋🂌🂍🂎🂏🂐🂑🂒🂓🁢'[(7*a)+b]

def get_new_set():
    set = []
    for a in range(7):
        for b in range(a+1):
            set.append((b,a))
    return set

def deal(set):
    return [set.pop() for piece in range(7)], [set.pop() for piece in range(7)], set

def display_hand(hand):
    for piece in hand:
        print(domino_vert(*piece), end=' ')

def display_backs(hand):
    for piece in hand:
        print(domino_vert(0, -1), end=' ')

def display_line(line):
    for piece in line:
        print(domino_horiz(*piece), end=' ')

def pip_count(hand):
    return sum(sum(hand, ()))

def place_piece(line, piece):
    if line == []:
        line.append(piece)
        return True

    left, right = line[0][0], line[-1][-1]
    a, b = piece
    state = [(a == left or b == left), (a == right or b == right)]

    if not (state[0] or state[1]):
        return False
    elif (state[0] and state[1]):
        picked = (left == right)
        while not picked:
            picked = True
            side = input('╰> ')[0]
            if side in '.>lL':
                state[0] = False
            elif side in ',<rR':
                state[1] = False
            else:
                picked = False

    if state[0]:
        if left == a:
            a, b = b, a
        line.insert(0, (a, b))
        return True
    else:
        if right == b:
            a, b = b, a
        line.append((a, b))
        return True

def no_moves(line, hand):
    if line == []:
        return False
    left, right = line[0][0], line[-1][-1]
    sides = sum(hand, ())
    return not(left in sides or right in sides)

def ai_go(line, hand):
    if line == []: # never happens, unless you give the ai first turn
        line.append(hand.pop(randint(0,6)))
        return

    shuffle(hand)
    for p, piece in enumerate(hand):
        left, right = line[0][0], line[-1][-1]
        a, b = piece
        state = [(a == left or b == left), (a == right or b == right)]
        if not (state[0] or state[1]):
            continue
        elif (state[0] and state[1]):
            state[randint(0, 1)] = False

        if state[0]:
            if left == a:
                a, b = b, a
            line.insert(0, (a, b))
            hand.pop(p)
            return
        else:
            if right == b:
                a, b = b, a
            line.append((a, b))
            hand.pop(p)
            return

def main():
    set = get_new_set()
    shuffle(set)
    player_hand, ai_hand, stock = deal(set)
    line = []
    gameover = False
    while (not gameover):
        print('--')
        display_backs(ai_hand)
        print('')
        display_line(line)
        print('')
        display_hand(player_hand)
        print('')
                                                    # this bit here needs to be modified for games with a stock
        if len(ai_hand) == 0 or len(player_hand) == 0 or (no_moves(line, player_hand) and no_moves(line, ai_hand)):
            gameover = True
            break

        if not no_moves(line, player_hand):
            placed = False
            while not placed:
                choice = None
                while choice not in list(range(1, 1+len(player_hand))):
                    choice = input('> ')
                    if choice not in string.digits:
                        continue
                    choice = int(choice)
                placed = place_piece(line, player_hand[choice-1])
            player_hand.pop(choice-1)

        ai_go(line, ai_hand)

    print(pip_count(ai_hand) - pip_count(player_hand), end=' ')
    display_hand(ai_hand)
    print()

if __name__ == '__main__':
    main()
