#!/usr/bin/env python3
from source import Config, MainFunction, file_config

conf = Config(file_config)
my_time = conf.read_config_time()
my_loop = conf.read_config_loop()
my_kondisi = conf.read_config_kondisi()

if __name__ == "__main__":
    fun = MainFunction(my_loop, my_time, my_kondisi)
    try:
        fun.start()
    except:
        fun.exit(None)


