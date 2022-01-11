from configparser import ConfigParser

class Config(ConfigParser):
    _config         = {'time':'TIMING', 'val_time':'timer',
                       'loop':'LOOP', 'val_loop':'banyak_loop'}
    _kondisi        = 'PERKONDISIAN_SENSOR'
    kondisi_float   = {'temp_hi': 0.0, 'temp_lo': 0.0,
                       'humadity_hi': 0.0, 'humadity_lo': 0.0
                       }
    kondisi_int     = {'moisture_hi': 0.0, 'moisture_lo': 0.0,
                       'water_low': 0.0, 'water_lowmed': 0.0,
                       'water_med': 0.0, 'water_hi': 0.0
                       }
    # def __init__(self) -> None:
    #     self.parser = ConfigParser()
    #     self.parser.read(self._file)
    def __init__(self, file, *args, **kwargs):
        ConfigParser.__init__(self, *args, **kwargs)
        self.read(file)

    def read_config_time(self)->float:
        return float(self[self._config['time']][self._config['val_time']])

    def read_config_loop(self)->int:
        return int(self[self._config['loop']][self._config['val_loop']])

    def read_config_kondisi(self):
        kond = self[self._kondisi]
        for dht in self.kondisi_float:
            self.kondisi_float[dht] = (kond.getfloat(dht))

        for ints in self.kondisi_int:
            self.kondisi_int[ints] = (kond.getint(ints))

        return self.kondisi_float | self.kondisi_int



# testing saja.
if __name__ == "__main__":
    conf = Config('config.ini')
    time = Config.read_config_time(conf)
    loop = Config.read_config_loop(conf)
    kondisi = Config.read_config_kondisi(conf)

    print(f'time={time} loop={loop} kondisi= {kondisi}')
    print(f'tipe time={type(time)} tile loop={type(loop)} tipe kondisi= {type(kondisi)}')
    for i in kondisi:
        print(f'value in list = {kondisi[i]}, type in list = {type(kondisi[i])}')
    print(kondisi['temp_hi'] == 32.0)
