#!/usr/bin/env python3.1
# This Python file uses the following encoding: utf-8

import curses

white = {
	'king':'♔',
	'queen':'♕',
	'rook':'♖',
	'bishop':'♗',
	'knight':'♘',
	'pawn':'♙'
}

black = {
	'king':'♚',
	'queen':'♛',
	'rook':'♜',
	'bishop':'♝',
	'knight':'♞',
	'pawn':'♟'
}

board1 = [
	[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
	[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
	[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
	[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
	[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
	[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
	[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
	[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
]
board2 = [[' '] * 8] * 8
board3 = [[' '] * 8 for i in range(8)]
board = board3

def setupBoard():
	backrow = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook']

	for col, piece in enumerate(backrow):
		board[0][col] = black[piece]
		board[1][col] = black['pawn']
		board[6][col] = white['pawn']
		board[7][col] = white[piece]

def displayBoard():
	frames = "┌└┐┘├┤┬┴│─╭╮╯╰┼"
	top     = "╭─┬─┬─┬─┬─┬─┬─┬─╮"
	between = "├─┼─┼─┼─┼─┼─┼─┼─┤"
	line = 8
	bottom  = "╰─┴─┴─┴─┴─┴─┴─┴─╯"
	print(top)
	for row in board:
		print("│", end = "")
		for col in row:
			print(col, end = "│")
		print(line)
		line = line - 1
		if line >= 1:
			print(between)
		else:
			print(bottom)
	print(" a b c d e f g h   \n")

def main():
	#stdscr = curses.initscr()
	#stdscr.keypad(1)

	setupBoard()
	displayBoard()

	#curses.nocbreak(); stdscr.keypad(0); curses.echo()
	#curses.endwin()

if __name__ == '__main__':
	main()
