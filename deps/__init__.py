from telemetrix import telemetrix
from deps.data import *
from deps.dash import *
from deps.fun import *
from config import *
# from deps.ardu_fun import main_functions
# from deps.query_sql import *


conf = Config()
my_time = Config.read_config_time(conf)
my_loop = Config.read_config_loop(conf)
my_kondisi = Config.read_config_kondisi(conf)

my_board = telemetrix.Telemetrix()
my_calls = TheCallback()
