#128x48y

# mostly created by chatgpt with prompting from me to nudge it in the right direction
# that chat is here: https://chat.openai.com/share/e185637d-414a-4d07-86b4-26e6dc33bfca

import curses
import datetime
import time

def draw_digit(stdscr, row, col, digit):
    # Define ASCII art for each digit
    digits = [
        [
            " 000 ",
            "0   0",
            "0   0",
            "0   0",
            "0   0",
            "0   0",
            " 000 "
        ],
        [
            "  1  ",
            "111  ",
            "  1  ",
            "  1  ",
            "  1  ",
            "  1  ",
            "11111"
        ],
        [
            " 222 ",
            "2   2",
            "    2",
            "   2 ",
            "  2  ",
            " 2   ",
            "22222"
        ],
        [
            "3333 ",
            "    3",
            "    3",
            "  33 ",
            "    3",
            "    3",
            "3333 "
        ],
        [
            "   4 ",
            "  44 ",
            " 4 4 ",
            "4  4 ",
            "44444",
            "   4 ",
            "   4 "
        ],
        [
            "55555",
            "5    ",
            "5555 ",
            "    5",
            "    5",
            "5   5",
            " 555 "
        ],
        [
            " 666 ",
            "6   6",
            "6    ",
            "6666 ",
            "6   6",
            "6   6",
            " 666 "
        ],
        [
            "77777",
            "7   7",
            "    7",
            "   7 ",
            "  7  ",
            " 7   ",
            " 7   "
        ],
        [
            " 888 ",
            "8   8",
            "8   8",
            " 888 ",
            "8   8",
            "8   8",
            " 888 "
        ],
        [
            " 999 ",
            "9   9",
            "9   9",
            " 9999",
            "    9",
            "   9 ",
            " 99  "
        ],
        [
            "    ",
            "    ",
            " :  ",
            "    ",
            " :  ",
            "    ",
            "    "
        ],
    ]


    # Define color pairs for background and foreground
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)  # Background: White, Foreground: Black

    # Set the color pair for the digit's background and foreground
    stdscr.attron(curses.color_pair(1))

    # Draw the digit at the specified row and column
    for i, line in enumerate(digits[digit]):
        for j, char in enumerate(line):
            if char != " ":
                stdscr.addch(row + i, col + j, char)

    # Reset the color pair
    stdscr.attroff(curses.color_pair(1))



def main(stdscr):
    # Make the cursor invisible
    curses.curs_set(0)

    # Initialize color mode
    curses.start_color()

    # Clear the screen
    stdscr.clear()

    # Get the dimensions of the terminal
    rows, cols = stdscr.getmaxyx()

    # Calculate the center coordinates
    center_row = rows // 2 -4
    center_col = cols // 2 -(5*5//2)

    previous_time = datetime.datetime.now()
    delay = 1
    while True:
        # Get the current time
        current_time = datetime.datetime.now()
        hour = current_time.hour
        minute = current_time.minute

        if delay == 1 and previous_time.minute != minute:
            delay = 60
        previous_time = current_time

        # Calculate the starting position to draw the digits
        start_col = center_col - (9 // 2)  # Assuming each digit is 5 characters wide

        # Clear the screen
        stdscr.clear()

        # Draw the hour digit
        draw_digit(stdscr, center_row, start_col, hour // 10)
        draw_digit(stdscr, center_row, start_col + 6, hour % 10)

        # Draw the separator (colon)
        draw_digit(stdscr, center_row, start_col + 12, 10)

        # Draw the minute digit
        draw_digit(stdscr, center_row, start_col + 18, minute // 10)
        draw_digit(stdscr, center_row, start_col + 24, minute % 10)

        # Refresh the screen
        stdscr.refresh()

        time.sleep(delay)


# Run the program
curses.wrapper(main)
