#!/usr/bin/env python3
from deps import MainFunction, my_board, my_calls,\
    my_loop, my_time, my_kondisi, ui
import sys as s

if __name__ == "__main__":
    try:
        MainFunction(board=my_board, call=my_calls, ui=ui,
                     loops=my_loop, delay=my_time, konds=my_kondisi)
    except KeyboardInterrupt:
        my_board.shutdown()
        # end_database()
        s.exit()
