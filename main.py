#!/usr/bin/env python3
from source import my_function, my_board, my_calls,\
    my_loop, my_time, my_kondisi, my_ui #, database 

import sys

#TODO!! buat Cronjob pada program ini

if __name__ == "__main__":
    try:
        my_function(board=my_board, call=my_calls, ui=my_ui,
                     loops=my_loop, delay=my_time, konds=my_kondisi)
    except KeyboardInterrupt:
        my_board.shutdown()
        # end_database()
        sys.exit('Program Ditutup Menggunakan CTRL+C / Ctrl+Z')
