import time
import sys
from typing import Optional
from rich.console import Console
from telemetrix.telemetrix import Telemetrix
from .datasensor import TheCallback
from .dashboard import ui

class MainFunction:
    """MainFunction.

    type: `class` function sebagai fungsi utama dari jalannya program
    """
    SOIL = 0
    LDR = 1
    DHT = DHTTIPE = 11
    HCSRTRIG, HCSRECHO = 9, 10
    REL1, REL2, REL3, REL4 = 2, 3, 4, 5
    LED = [13, 12, 8, 7, 6]
    list_rel_led = [2, 3, 4, 5, 6, 7, 8, 12, 13]

    def __init__(self, delay= float, kondisi= dict):
        """__init__.

        :param board:
        :type board: `telemetrix.Telemetrix` sebagai API board arduino
        :param call:
        :type call: `TheCallback` class dari bacaan sensor
        :param ui:
        :type ui: tupple items dari `dashing` sebagai visualisasi data
        :param loo1s:
        :type loops: jumlah banyaknya loop yang berjalan
        :param delay:
        :type delay: delay yang dibutuhkan setiap loop data
        :param konds:
        :type konds: list kondisi dari configparser file `config.ini`
            pada parrent directory
        """
        self.console = Console()
        self.call = TheCallback()
        self.ui = ui
        self.delay = delay
        self.kond = kondisi

    def start(self):
        """start.

        start semua proses pada program
        """
        try:
            self.board = Telemetrix()

            self.board.set_pin_mode_analog_input(self.SOIL,
                                                 differential=5,
                                                 callback=self.call.soil_callback)

            self.board.set_pin_mode_analog_input(self.LDR,
                                                 differential=5,
                                                 callback=self.call.ldr_callback)

            self.board.set_pin_mode_sonar(self.HCSRTRIG,
                                          self.HCSRECHO,
                                          callback=self.call.hcsr_callback)

            self.board.set_pin_mode_dht(self.DHT,
                                        self.call.dht_callback,
                                        self.DHTTIPE)

            for pin in self.list_rel_led:
                self.board.set_pin_mode_digital_output(pin)
            self.call.rel1_callback([0])
            self.call.rel2_callback([0])
            self.call.rel3_callback([0])
            self.call.rel4_callback([0])

            time.sleep(0.5)
            self.start_time = time.time()

            while self.board.shutdown_flag is False:
                try:
                    self.update_ui()
                    if ((time.time() - self.start_time) >= self.delay):
                        # perkondisian relay pada ketentuan suhu
                        # maupun kelembapan udara dari dht sensor
                        if self.call.data['humid'] > self.kond['humadity_hi']:  # humadity
                            self.board.digital_write(self.REL1, 0)
                            self.call.rel1_callback([0])

                        elif self.call.data['humid'] < self.kond['humadity_lo']:
                            self.board.digital_write(self.REL1, 1)
                            self.call.rel1_callback([1])
                        else: # print(f'rel1 and rel2 mati')
                            pass
                            # self.board.digital_write(self.REL1, 0)
                            # self.call.rel1_callback([0])

                        if self.call.data['temp'] >= self.kond['temp_lo']:  # suhu
                            # print(f'rel1 and rel2 hidup')
                            self.board.digital_write(self.REL2, 1)
                            self.call.rel2_callback([1])

                        elif self.call.data['temp'] <= self.kond['temp_hi']:
                            self.board.digital_write(self.REL2, 0)
                            self.call.rel2_callback([0])
                        else:
                            pass

                        # perkondisian relay pada pada tingkat kebasahan tanah
                        # dari bacaan `soilmoisturesensor`
                        if self.call.data['soil'] >= self.kond['moisture_lo']:
                            # print(f'rel4 hidup')
                            self.board.digital_write(self.REL4, 1)
                            self.call.rel4_callback([1])

                        elif self.call.data['soil'] <= self.kond['moisture_hi']:
                            # print(f'rel4 hidup')
                            self.board.digital_write(self.REL4, 0)
                            self.call.rel4_callback([0])
                        else: # print(f'rel4 mati')
                            pass

                        # perkondisian relay dan led sebagai
                        # indikator ketinggian air pada tanki
                        if self.call.data['hcsr'] >= self.kond['water_low']:
                            self.board.digital_write(self.REL3, 1)
                            self.led_fun(1,0,0,0,0)
                            self.call.rel3_callback([1])

                        elif self.call.data['hcsr'] >= self.kond['water_lowmed']:
                            self.board.digital_write(self.REL3, 1)
                            self.led_fun(1,1,0,0,0)
                            self.call.rel3_callback([1])

                        elif self.call.data['hcsr'] >= self.kond['water_med']:
                            self.led_fun(1,1,1,0,0)

                        elif self.call.data['hcsr'] >= self.kond['water_hi']:
                            self.led_fun(1,1,1,1,0)

                        elif self.call.data['hcsr'] <= self.kond['water_hi']:
                            self.board.digital_write(self.REL3, 0)
                            self.led_fun(1,1,1,1,1)
                            self.call.rel3_callback([0])
                        else:
                            pass
                        # log ui update lambat
                        self.start_time = time.time()
                    # UI update cepat
                    time.sleep(.1)
                except IndexError:
                    continue
        # jika error exit
        except (KeyboardInterrupt, RuntimeError, KeyError):
            self.exit(True)

    def led_fun(self, led1=None, led2=None, led3=None, led4=None, led5=None):
        """[led_fun]

        function untuk mengganti sesuai kondisi yang di berikan
        """
        _led_state = {'led1': led1, 'led2': led2, 'led3': led3,
                      'led4': led4, 'led5': led5 }
        for p, i in zip(self.LED , _led_state):
            if _led_state[i] == 1:
                self.board.digital_write(p, 1)
            else:
                self.board.digital_write(p, 0)

    def update_ui(self):
        self.ui.items[0].items[1].items[-1].items[0].value = self.call.data['relay1']
        self.ui.items[0].items[1].items[-1].items[1].value = self.call.data['relay2']
        self.ui.items[0].items[1].items[-1].items[2].value = self.call.data['relay3']
        self.ui.items[0].items[1].items[-1].items[3].value = self.call.data['relay4']
        self.ui.items[1].items[2].items[0].value = float(self.call.data['soil']/10)
        self.ui.items[1].items[2].items[1].value = float(self.call.data['ldr']/10)
        self.ui.items[0].items[2].value = self.call.data['hcsr']/1.5
        self.ui.items[1].items[0].append(self.call.data['humid'])
        self.ui.items[1].items[1].append(self.call.data['temp']/0.5)

        self.ui.items[0].items[0].append(f'=====================')
        self.ui.items[0].items[0].append(f'humidity = {str(self.call.data["humid"])} %')
        self.ui.items[0].items[0].append(f'Suhu = {str(self.call.data["temp"])}\u2103')
        self.ui.items[0].items[0].append(f'SOILsensor = {str(self.call.data["soil"]/10)}')
        self.ui.items[0].items[0].append(f'LDR = {str(self.call.data["ldr"]/10)}')
        self.ui.items[0].items[0].append(f'hcsr = {str(self.call.data["hcsr"])} cm')
        self.ui.display()
        self.ui

    def exit(self, errors: bool = None):
        if errors:
            self.board.shutdown()
            self.console.print_exception()
            return self.console.log('\nPROGRAM GAGAL UNTUK MENYAMUNGKAN PADA ARDUINO atau ARDUINO TIDAK TERHUBUNG!\
                                    \nPERIkSA SAMBUNGAN SERIAL/USB, dan JALANKAN ULANG PROGRAM',log_locals=True)
        else:
            self.board.shutdown()
            sys.exit('PROGRAM DITUTUP')
