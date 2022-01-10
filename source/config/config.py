from configparser import ConfigParser

class Config(ConfigParser):
    _time           = 'TIMING'
    _val_time       = 'timer'
    _loop           = 'LOOP'
    _val_loop       = 'banyak_loop'
    _kondisi        = 'PERKONDISIAN_SENSOR'
    kondisi_float   = ['on_temp_dht', 'off_temp_dht',
                       'on_humadity_dht', 'off_humadity_dht'
                       ]
    kondisi_int     = ['on_moisture_soil','off_moisture_soil',
                       'jarak_hcsr1','jarak_hcsr2',
                       'jarak_hcsr3','jarak_hcsr4'
                       ]

    kondisi = []
    # def __init__(self) -> None:
    #     self.parser = ConfigParser()
    #     self.parser.read(self._file)
    def __init__(self,file, *args, **kwargs):
        ConfigParser.__init__(self, *args, **kwargs)
        self.read(file)

    def read_config_time(self)->float:
        self._time = self[self._time][self._val_time]

        return float(self._time)

    def read_config_loop(self)->int:
        self._loop = self[self._loop][self._val_loop]

        return int(self._loop)

    def read_config_kondisi(self):
        kond = self[self._kondisi]
        self.kondisi.append(0)
        for dht in self.kondisi_float:
            self.kondisi.append(kond.getfloat(dht))

        for ints in self.kondisi_int:
            self.kondisi.append(kond.getint(ints))

        return self.kondisi


# testing saja.
if __name__ == "__main__":
    conf = Config('config.ini')
    time = Config.read_config_time(conf)
    loop = Config.read_config_loop(conf)
    kondisi = Config.read_config_kondisi(conf)

    print(f'time={time} loop={loop} kondisi= {kondisi}')
    print(f'tipe time={type(time)} tile loop={type(loop)} tipe kondisi= {type(kondisi)}')
    if kondisi[1] == 32.0:
        print(True)
