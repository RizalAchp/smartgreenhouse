#!/usr/bin/env python3
import sys
sys.path.append(r"../")
from source import MainFunction


#TODO!! buat Cronjob pada program ini
# conf = Config(file_config)
# my_loop = conf.read_config_loop()
# my_time = conf.read_config_time()
# my_kondisi = conf.read_config_kondisi()
print(__name__)
print(sys.path)

if __name__ == "__main__":
    fun = MainFunction(100, 10, [12,12,12,12])
    try:
        fun.start()
        # print('testing')
        # fun.start()
    except Exception:
        fun.exit()
        sys.exit('Program Ditutup Menggunakan CTRL+C / Ctrl+Z')
        # end_database()
