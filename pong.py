#!/usr/bin/env python
# This Python file uses the following encoding: utf-8

from time import sleep

'''
unicode pong - by yossi
demo to see what this looks like
䷩䷉䷀䷀䷁䷀䷀䷀䷨
'''

puck = '䷀䷌䷉䷈䷍'
negpuck = '䷁䷆䷎䷏䷇'
paddle = ' ䷋䷩䷨䷊'
board = [0,0,0,0,0,0,0]

path =  [1,1,2,2,3,3,4]
p1 = 1
p2 = 4

def draw():
        game = ''
        for i in range(7):
                if i!=3:
                        game += puck[board[i]]
                else:
                        game += negpuck[board[i]]
        return paddle[p1] + game + paddle[p2]

position = -1
for i in range(19):
        sleep(.5)
        board[position] = 0
        if i >= 7 and i < 13:
                position -= 1
        else:
                position += 1

        board[position] = path[position]
        p2 = path[position]
        print(draw())
