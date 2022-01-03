from pathlib import Path
import os

# file = Path('config.ini')

file = os.path.join(os.path.dirname(__name__))


print(file)
