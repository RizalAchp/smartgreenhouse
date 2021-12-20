import deps
import sys

# end_database = deps.end_query
main_fun = deps.mainFunctions
my_board = deps.board
calls = deps.callbacks

if __name__ == "__main__":
    try:
        main_fun(my_board,calls)
    except KeyboardInterrupt:
        my_board.shutdown()
        # end_database()
        sys.exit()
