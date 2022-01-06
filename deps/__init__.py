from telemetrix import telemetrix
from .datasensor import TheCallback
from .dashboard import ui
from .fun import MainFunction
from .config import Config
# from deps.ardu_fun import main_functions
# from .database.query_sql import *


conf = Config()
my_function = MainFunction
my_ui = ui
my_time = Config.read_config_time(conf)
my_loop = Config.read_config_loop(conf)
my_kondisi = Config.read_config_kondisi(conf)
my_board = telemetrix.Telemetrix()
my_calls = TheCallback()
