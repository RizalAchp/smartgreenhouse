from configparser import ConfigParser

class Config:
    _file       = 'config.ini'
    _time       = 'TIMING'
    _val_time   = 'timer'
    _loop       = 'LOOP'
    _val_loop   = 'banyak_loop'
    _kondisi    = 'PERKONDISIAN SENSOR'
    def __init__(self) -> None:
        self.parser = ConfigParser()
        self.parser.read(self._file)

    def read_config_time(self)->float:
        self._time = self.parser[self._time][self._val_time]

        return float(self._time)

    def read_config_loop(self)->int:
        self._loop = self.parser[self._loop][self._val_loop]

        return int(self._loop)

    def read_config_kondisi(self)->list:
        kond = self.parser[self._kondisi]

        return [
            kond['kond_temp_dht'], kond['kond_humadity_dht'],
            kond['kond_moisture_soil'], kond['kond_jarak_hcsr']
        ]

if __name__ == "__main__":
    conf = Config()
    time = Config.read_config_time(conf)
    loop = Config.read_config_loop(conf)
    kondisi = Config.read_config_kondisi(conf)

    print(f'time={time} loop={loop} kondisi= {kondisi}')
    print(f'tipe time={type(time)} tile loop={type(loop)} tipe kondisi= {type(kondisi)}')
