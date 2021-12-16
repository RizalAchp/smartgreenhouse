import deps
import sys

mainfun = deps.mainFunctions
myboard = deps.board
calls = deps.callbacks
if __name__ == "__main__":
    try:
        mainfun(myboard,calls)
    except KeyboardInterrupt:
        myboard.shutdown()
        sys.exit()
